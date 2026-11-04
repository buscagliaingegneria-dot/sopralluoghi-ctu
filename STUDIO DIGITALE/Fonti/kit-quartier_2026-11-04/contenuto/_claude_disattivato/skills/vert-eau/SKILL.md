---
name: vert-eau
description: Espaces verts et eau autour d'une adresse, avec la distance du plus proche.
argument-hint: "[adresse en France]"
disable-model-invocation: true
---

Fais la carte des espaces verts et de l'eau autour de cette adresse. Végétation (`vegetation.geojson`) et lieux de nature parc, jardin, square (`lieux.geojson`, champs `nature` et `nature_detaillee`) en vert sauge, nuancés selon le type ; l'eau en bleu profond ; le bâti en gris très pâle ; le reste en blanc cassé. Calcule la distance à vol d'oiseau de l'adresse au bord du plus proche espace vert et au bord de l'eau, trace ces deux segments en fin trait noir et écris les deux distances en mètres, en grand, près des segments. Nomme seulement les 3 plus grands espaces verts et le cours d'eau s'il a un nom, en petit. Vidéo : l'eau se remplit d'abord, puis les verts apparaissent, puis les deux segments se tracent.

Adresse donnée : $ARGUMENTS

Commence toujours comme ça :
1. Si `site/site.json` n'existe pas, lance `python outils/donnees_site.py "<l'adresse>"`. Il télécharge les données ouvertes de l'IGN (BD TOPO, Base Adresse Nationale, isochrones piétons) dans `site/`, en mètres, origine à l'adresse, nord en haut. S'il existe, réutilise-le.
2. Lis `site/site.json` : vérifie que l'adresse trouvée est bien celle demandée (sinon arrête-toi et dis-le), note le cadre et le nombre d'objets.
3. Ouvre les GeoJSON dont tu as besoin et regarde ce qu'ils contiennent vraiment (champs, valeurs vides) avant de dessiner.

Dessine ensuite en code, avec un script Python (matplotlib, numpy, shapely, Pillow ; installe ce qui manque avec pip, et ffmpeg sert à la vidéo). Aucun générateur d'images : tout se calcule depuis `site/`.

Ce que tu rends, dans le dossier courant :
- `vert-eau.png` : le dessin final, 1080 × 1920 en portrait, à fond perdu, sans marge blanche autour. La carte couvre tout le cadre de `site.json`. Trait net, niveau d'un rendu d'école d'architecture ou d'agence, jamais un graphique de tableur. Pas de titre géant : un petit cartouche discret dans un coin (nom du dessin, adresse en petit, échelle graphique, nord, « © IGN BD TOPO »).
- `vert-eau.mp4` : 3 s, 1080 × 1920, 30 i/s, H.264, yuv420p, où le dessin se construit sous les yeux et se termine sur l'image finale tenue les 20 dernières images. La première image n'est jamais vide.

Ouvre le PNG pour le regarder, et corrige s'il y a du texte coupé ou qui se chevauche, ou un dessin trop petit pour se lire sur un téléphone. Termine en disant en quelques lignes ce que le dessin montre, ce que disent les données et ce que tu as supposé. N'invente rien sans le dire.
