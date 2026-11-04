"""Données ouvertes d'un site autour d'une adresse française : Géoplateforme IGN (géocodage BAN, BD TOPO, isochrones piétons).

Usage : python outils/donnees_site.py "Place des Terreaux, Lyon" [--largeur 1000]
Écrit dans ./site/ (réutilisé s'il existe déjà, --refaire pour tout recharger) :
  site.json             adresse trouvée, centre, cadre, projection, sources et date
  batiments.geojson     emprises, hauteur (m), étages, usage
  voies.geojson         tronçons de route : nature, importance (1 = grand axe … 6 = chemin), nom, largeur
  eau.geojson           surfaces en eau
  vegetation.geojson    bois, haies, forêts (BD TOPO)
  lieux.geojson         places, parcs, squares, équipements (zones d'activité ou d'intérêt)
  isochrones.geojson    zones atteignables à pied en 5, 10 et 15 min depuis l'adresse (moteur Valhalla de l'IGN)
Coordonnées en mètres, repère local : origine à l'adresse, x vers l'est, y vers le nord (le nord est donc en haut).
Cadre en portrait 9:16 : largeur choisie, hauteur = largeur × 16/9.
Aucune clé, aucune bibliothèque à installer (urllib, json).
"""
import argparse, datetime as dt, json, math, sys, time, urllib.parse, urllib.request
from pathlib import Path

R = 6371008.8
WFS = "https://data.geopf.fr/wfs/ows"
COUCHES = {
    "batiments": "BDTOPO_V3:batiment",
    "voies": "BDTOPO_V3:troncon_de_route",
    "eau": "BDTOPO_V3:surface_hydrographique",
    "vegetation": "BDTOPO_V3:zone_de_vegetation",
    "lieux": "BDTOPO_V3:zone_d_activite_ou_d_interet",
}
GARDER = {
    "batiments": ["hauteur", "nombre_d_etages", "usage_1", "nature", "altitude_maximale_toit", "altitude_minimale_sol"],
    "voies": ["nature", "importance", "nom_voie_ban_gauche", "nom_collaboratif_gauche", "largeur_de_chaussee", "nombre_de_voies", "position_par_rapport_au_sol", "acces_vehicule_leger"],
    "eau": ["nature", "cpx_toponyme_de_cours_d_eau"],
    "vegetation": ["nature"],
    "lieux": ["nature", "nature_detaillee", "toponyme", "categorie"],
}


def lire(url: str, essais: int = 4) -> dict:
    for i in range(essais):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "analyse-de-site/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # service saturé : on attend et on réessaie
            if i == essais - 1:
                raise
            print(f"  nouvel essai dans {2 ** (i + 1)} s ({e})", file=sys.stderr)
            time.sleep(2 ** (i + 1))


def geocoder(adresse: str) -> dict:
    d = lire("https://data.geopf.fr/geocodage/search?" + urllib.parse.urlencode({"q": adresse, "limit": 1}))
    if not d.get("features"):
        sys.exit(f"Adresse introuvable dans la Base Adresse Nationale : {adresse}")
    f = d["features"][0]
    lon, lat = f["geometry"]["coordinates"]
    return {"label": f["properties"].get("label"), "score": f["properties"].get("score"), "lon": lon, "lat": lat}


class Repere:
    def __init__(self, lon0, lat0):
        self.lon0, self.lat0, self.k = lon0, lat0, math.cos(math.radians(lat0))

    def xy(self, lon, lat):
        return (round(math.radians(lon - self.lon0) * self.k * R, 2), round(math.radians(lat - self.lat0) * R, 2))

    def lonlat(self, x, y):
        return (self.lon0 + math.degrees(x / (R * self.k)), self.lat0 + math.degrees(y / R))

    def geom(self, g):
        def conv(c):
            if isinstance(c[0], (int, float)):
                return list(self.xy(c[0], c[1]))
            return [conv(x) for x in c]
        return {"type": g["type"], "coordinates": conv(g["coordinates"])}


def wfs(couche: str, bbox: tuple) -> list:
    lat_min, lon_min, lat_max, lon_max = bbox
    tout, debut, pas = [], 0, 2000
    while True:
        q = {"SERVICE": "WFS", "VERSION": "2.0.0", "REQUEST": "GetFeature", "TYPENAMES": couche, "COUNT": pas, "STARTINDEX": debut,
             "SORTBY": "cleabs", "BBOX": f"{lat_min},{lon_min},{lat_max},{lon_max},urn:ogc:def:crs:EPSG::4326", "outputFormat": "application/json"}
        d = lire(WFS + "?" + urllib.parse.urlencode(q))
        f = d.get("features", [])
        tout += f
        if len(f) < pas:
            return tout
        debut += pas


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("adresse")
    ap.add_argument("--largeur", type=float, default=1000, help="largeur du cadre en mètres (hauteur = × 16/9)")
    ap.add_argument("--refaire", action="store_true")
    a = ap.parse_args()
    dossier = Path("site")
    if (dossier / "site.json").exists() and not a.refaire:
        print("site/ existe déjà : réutilisé (--refaire pour recharger)")
        return
    dossier.mkdir(exist_ok=True)
    g = geocoder(a.adresse)
    rep = Repere(g["lon"], g["lat"])
    w, h = a.largeur, a.largeur * 16 / 9
    lon_min, lat_min = rep.lonlat(-w / 2, -h / 2)
    lon_max, lat_max = rep.lonlat(w / 2, h / 2)
    bbox = (lat_min, lon_min, lat_max, lon_max)
    comptes = {}
    for nom, couche in COUCHES.items():
        brut = wfs(couche, bbox)
        feats = []
        for f in brut:
            if not f.get("geometry"):
                continue
            p = {k: f["properties"].get(k) for k in GARDER[nom]}
            feats.append({"type": "Feature", "properties": p, "geometry": rep.geom(f["geometry"])})
        (dossier / f"{nom}.geojson").write_text(json.dumps({"type": "FeatureCollection", "features": feats}, ensure_ascii=False), encoding="utf-8")
        comptes[nom] = len(feats)
        print(f"{nom} : {len(feats)} objets")
    iso = []
    for minutes in (5, 10, 15):
        q = {"point": f"{g['lon']},{g['lat']}", "resource": "bdtopo-valhalla", "costValue": minutes * 60, "costType": "time",
             "profile": "pedestrian", "geometryFormat": "geojson"}
        d = lire("https://data.geopf.fr/navigation/isochrone?" + urllib.parse.urlencode(q))
        iso.append({"type": "Feature", "properties": {"minutes": minutes}, "geometry": rep.geom(d["geometry"])})
    (dossier / "isochrones.geojson").write_text(json.dumps({"type": "FeatureCollection", "features": iso}), encoding="utf-8")
    print("isochrones : 5, 10 et 15 min à pied")
    hauteurs = [f["properties"]["hauteur"] for f in json.loads((dossier / "batiments.geojson").read_text(encoding="utf-8"))["features"]]
    sans = sum(1 for x in hauteurs if not x)
    (dossier / "site.json").write_text(json.dumps({
        "adresse_demandee": a.adresse, "adresse_trouvee": g["label"], "score_geocodage": g["score"],
        "centre": {"lon": g["lon"], "lat": g["lat"]}, "cadre_m": {"xmin": -w / 2, "xmax": w / 2, "ymin": -h / 2, "ymax": h / 2},
        "repere": "mètres, origine à l'adresse, x vers l'est, y vers le nord (projection locale équirectangulaire, écart < 0,1 % sur le cadre)",
        "objets": comptes, "batiments_sans_hauteur": sans,
        "sources": "IGN, Géoplateforme : BD TOPO (Licence Ouverte Etalab 2.0), Base Adresse Nationale, isochrones Valhalla sur BD TOPO",
        "credit": "© IGN BD TOPO · BAN · Licence Ouverte 2.0",
        "telecharge_le": dt.datetime.now().isoformat(timespec="minutes"),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Adresse trouvée : {g['label']} (score {g['score']:.2f}). Bâtiments sans hauteur : {sans}.")


if __name__ == "__main__":
    main()
