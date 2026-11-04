---
name: pieton
description: Ce qu'on atteint à pied en 5, 10 et 15 minutes depuis une adresse.
argument-hint: "[adresse en France]"
disable-model-invocation: true
---

Fais la carte de ce qu'on atteint à pied depuis cette adresse, avec les isochrones de `site/isochrones.geojson` (calculées par l'IGN sur le réseau réel, profil piéton) : 5 min, 10 min et 15 min en trois aplats translucides d'une même teinte, du plus soutenu au plus clair, avec leur contour fin. Bâti en gris moyen par-dessus, l'eau en bleu-gris pâle. Compte, dans la zone des 10 minutes, les lieux de `lieux.geojson` par grande famille (enseignement, santé, culture et culte, sport, espaces publics et parcs) et écris ces chiffres dans une petite légende. Écris « 5 min », « 10 min », « 15 min » sur le bord de chaque zone. L'adresse en point noir. Vidéo : les trois zones s'étendent l'une après l'autre depuis l'adresse.

Adresse donnée : $ARGUMENTS

Commence toujours comme ça :
1. Si `site/site.json` n'existe pas, lance `python outils/donnees_site.py "<l'adresse>"`. Il télécharge les données ouvertes de l'IGN (BD TOPO, Base Adresse Nationale, isochrones piétons) dans `site/`, en mètres, origine à l'adresse, nord en haut. S'il existe, réutilise-le.
2. Lis `site/site.json` : vérifie que l'adresse trouvée est bien celle demandée (sinon arrête-toi et dis-le), note le cadre et le nombre d'objets.
3. Ouvre les GeoJSON dont tu as besoin et regarde ce qu'ils contiennent vraiment (champs, valeurs vides) avant de dessiner.

Dessine ensuite en code, avec un script Python (matplotlib, numpy, shapely, Pillow ; installe ce qui manque avec pip, et ffmpeg sert à la vidéo). Aucun générateur d'images : tout se calcule depuis `site/`.

Ce que tu rends, dans le dossier courant :
- `pieton.png` : le dessin final, 1080 × 1920 en portrait, à fond perdu, sans marge blanche autour. La carte couvre tout le cadre de `site.json`. Trait net, niveau d'un rendu d'école d'architecture ou d'agence, jamais un graphique de tableur. Pas de titre géant : un petit cartouche discret dans un coin (nom du dessin, adresse en petit, échelle graphique, nord, « © IGN BD TOPO »).
- `pieton.mp4` : 3 s, 1080 × 1920, 30 i/s, H.264, yuv420p, où le dessin se construit sous les yeux et se termine sur l'image finale tenue les 20 dernières images. La première image n'est jamais vide.

Ouvre le PNG pour le regarder, et corrige s'il y a du texte coupé ou qui se chevauche, ou un dessin trop petit pour se lire sur un téléphone. Termine en disant en quelques lignes ce que le dessin montre, ce que disent les données et ce que tu as supposé. N'invente rien sans le dire.
