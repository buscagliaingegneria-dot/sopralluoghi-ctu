// Archivio locale (IndexedDB). Tutto il lavoro di campo passa da qui, mai dalla rete.
import { siglaDa } from './util.js';
const DB_NAME = 'sopralluoghi-ctu';
const DB_VER = 3;
let dbp = null;

export function db() {
  if (!dbp) {
    dbp = new Promise((resolve, reject) => {
      if (!globalThis.indexedDB) return reject(new Error('IndexedDB non disponibile in questo browser.'));
      const r = indexedDB.open(DB_NAME, DB_VER);
      let motivo = null; // motivo di un abort() della migrazione, mostrato al posto dell'errore generico
      r.onupgradeneeded = e => {
        const d = r.result;
        // Migrazioni: aggiungere nuovi "if (e.oldVersion < N)" senza toccare i blocchi esistenti.
        // Ogni blocco deve essere sincrono (niente await: la transazione di upgrade si chiuderebbe) e, se non può
        // completarsi, chiamare r.transaction.abort(): il database resta alla versione precedente e i dati intatti.
        if (e.oldVersion < 1) {
          d.createObjectStore('meta', { keyPath: 'k' });
          d.createObjectStore('immobili', { keyPath: 'id' });
          d.createObjectStore('ambienti', { keyPath: 'id' }).createIndex('imm', 'imm');
          const f = d.createObjectStore('foto', { keyPath: 'id' });
          f.createIndex('imm', 'imm'); f.createIndex('amb', 'amb');
          d.createObjectStore('docs', { keyPath: 'id' }).createIndex('imm', 'imm');
        }
        if (e.oldVersion < 2) d.createObjectStore('edifici', { keyPath: 'id' });
        if (e.oldVersion < 3) {
          // v3: sigla stabile (U1, U2…) aggiunta ai soli immobili che non l'hanno; nessun altro campo cambia (updatedAt e bk inclusi).
          // Idempotente. Codice senza cifra finale o sigla duplicata: abort, il database resta alla v2.
          const tx = r.transaction; const viste = new Set();
          tx.objectStore('immobili').openCursor().onsuccess = ev => {
            const c = ev.target.result; if (!c) return;
            const rec = c.value; const sigla = rec.sigla || siglaDa(rec.codice);
            if (!sigla || viste.has(sigla)) {
              motivo = !sigla ? `Migrazione alla versione 3 annullata: il codice «${rec.codice}» non termina con un numero. I dati non sono stati modificati.`
                : `Migrazione alla versione 3 annullata: la sigla ${sigla} risulterebbe duplicata (codice «${rec.codice}»). I dati non sono stati modificati.`;
              tx.abort(); return;
            }
            viste.add(sigla);
            if (!rec.sigla) c.update({ ...rec, sigla });
            c.continue();
          };
        }
      };
      r.onsuccess = () => {
        r.result.onversionchange = () => r.result.close();
        resolve(r.result);
      };
      r.onerror = () => reject(motivo ? new Error(motivo) : r.error);
      r.onblocked = () => reject(new Error('Archivio bloccato da un\'altra scheda dell\'app: chiuderla e riaprire.'));
    });
  }
  return dbp;
}

const req = r => new Promise((res, rej) => { r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error); });
const done = t => new Promise((res, rej) => {
  t.oncomplete = () => res(); t.onerror = () => rej(t.error); t.onabort = () => rej(t.error || new Error('Transazione annullata'));
});
function txw(d, stores) {
  try { return d.transaction(stores, 'readwrite', { durability: 'strict' }); }
  catch { return d.transaction(stores, 'readwrite'); }
}

export async function get(store, key) { const d = await db(); return req(d.transaction(store).objectStore(store).get(key)); }
export async function all(store) { const d = await db(); return req(d.transaction(store).objectStore(store).getAll()); }
export async function byIndex(store, index, key) { const d = await db(); return req(d.transaction(store).objectStore(store).index(index).getAll(key)); }
export async function count(store) { const d = await db(); return req(d.transaction(store).objectStore(store).count()); }
export async function put(store, val) {
  const d = await db(); const t = txw(d, store); t.objectStore(store).put(val); return done(t);
}
export async function putMany(store, vals) {
  const d = await db(); const t = txw(d, store); const os = t.objectStore(store); vals.forEach(v => os.put(v)); return done(t);
}
export async function del(store, key) {
  const d = await db(); const t = txw(d, store); t.objectStore(store).delete(key); return done(t);
}
export async function clearStores(stores) {
  const d = await db(); const t = txw(d, stores); stores.forEach(s => t.objectStore(s).clear()); return done(t);
}

export async function getMeta(k, def = null) { const r = await get('meta', k); return r ? r.v : def; }
export async function setMeta(k, v) { return put('meta', { k, v }); }
