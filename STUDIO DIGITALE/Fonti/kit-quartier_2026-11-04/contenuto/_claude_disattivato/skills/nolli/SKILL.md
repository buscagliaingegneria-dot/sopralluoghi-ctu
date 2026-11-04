---
name: nolli
description: Plan figure-fond façon Nolli autour d'une adresse : le bâti en noir, le vide en blanc.
argument-hint: "[adresse en France]"
disable-model-invocation: true
---

Fais le plan figure-fond du quartier autour de cette adresse, façon plan de Rome de Nolli (1748) : tous les bâtiments en noir plein, le vide (rues, places, cours) en blanc cassé papier, l'eau en gris très clair avec de fines hachures horizontales, aucun nom de rue, aucune écriture sur la carte. L'adresse est marquée par un petit cercle vermillon. Il doit tenir du dessin d'architecte qu'on accroche au mur, pas d'une carte routière. Vidéo : le bâti apparaît du centre vers l'extérieur, en cercles qui s'élargissent depuis l'adresse.

Adresse donnée : $ARGUMENTS

Commence toujours comme ça :
1. Si `site/site.json` n'existe pas, lance `python outils/donnees_site.py "<l'adresse>"`. Il télécharge les données ouvertes de l'IGN (BD TOPO, Base Adresse Nationale, isochrones piétons) dans `site/`, en mètres, origine à l'adresse, nord en haut. S'il existe, réutilise-le.
2. Lis `site/site.json` : vérifie que l'adresse trouvée est bien celle demandée (sinon arrête-toi et dis-le), note le cadre et le nombre d'objets.
3. Ouvre les GeoJSON dont tu as besoin et regarde ce qu'ils contiennent vraiment (champs, valeurs vides) avant de dessiner.

Dessine ensuite en code, avec un script Python (matplotlib, numpy, shapely, Pillow ; installe ce qui manque avec pip, et ffmpeg sert à la vidéo). Aucun générateur d'images : tout se calcule depuis `site/`.

Ce que tu rends, dans le dossier courant :
- `nolli.png` : le dessin final, 1080 × 1920 en portrait, à fond perdu, sans marge blanche autour. La carte couvre tout le cadre de `site.json`. Trait net, niveau d'un rendu d'école d'architecture ou d'agence, jamais un graphique de tableur. Pas de titre géant : un petit cartouche discret dans un coin (nom du dessin, adresse en petit, échelle graphique, nord, « © IGN BD TOPO »).
- `nolli.mp4` : 3 s, 1080 × 1920, 30 i/s, H.264, yuv420p, où le dessin se construit sous les yeux et se termine sur l'image finale tenue les 20 dernières images. La première image n'est jamais vide.

Ouvre le PNG pour le regarder, et corrige s'il y a du texte coupé ou qui se chevauche, ou un dessin trop petit pour se lire sur un téléphone. Termine en disant en quelques lignes ce que le dessin montre, ce que disent les données et ce que tu as supposé. N'invente rien sans le dire.
