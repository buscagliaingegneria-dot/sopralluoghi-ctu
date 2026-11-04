---
name: soleil
description: Les ombres portées du quartier, calculées heure par heure avec les vraies hauteurs.
argument-hint: "[adresse en France]"
disable-model-invocation: true
---

Fais l'étude des ombres portées du quartier autour de cette adresse le 21 mars (équinoxe), de 8 h à 18 h en heure solaire, à la latitude et la longitude de `site.json`. Calcule vraiment la hauteur et l'azimut du soleil heure par heure avec les formules astronomiques, et projette au sol l'ombre de chaque bâtiment avec sa hauteur BD TOPO (union de l'emprise et de ses arêtes translatées ; les bâtiments sans hauteur ne portent pas d'ombre, et dis-le). Garde un disque d'environ 300 m de rayon autour de l'adresse. PNG : le bâti en blanc avec un contour noir fin, l'ombre de 10 h en aplat bleu-gris translucide, l'heure et la hauteur du soleil écrites dans le cartouche. Vidéo : l'ombre tourne autour des îlots de 8 h à 18 h et l'heure défile en grand. Le relief n'est pas pris en compte : dis-le.

Adresse donnée : $ARGUMENTS

Commence toujours comme ça :
1. Si `site/site.json` n'existe pas, lance `python outils/donnees_site.py "<l'adresse>"`. Il télécharge les données ouvertes de l'IGN (BD TOPO, Base Adresse Nationale, isochrones piétons) dans `site/`, en mètres, origine à l'adresse, nord en haut. S'il existe, réutilise-le.
2. Lis `site/site.json` : vérifie que l'adresse trouvée est bien celle demandée (sinon arrête-toi et dis-le), note le cadre et le nombre d'objets.
3. Ouvre les GeoJSON dont tu as besoin et regarde ce qu'ils contiennent vraiment (champs, valeurs vides) avant de dessiner.

Dessine ensuite en code, avec un script Python (matplotlib, numpy, shapely, Pillow ; installe ce qui manque avec pip, et ffmpeg sert à la vidéo). Aucun générateur d'images : tout se calcule depuis `site/`.

Ce que tu rends, dans le dossier courant :
- `soleil.png` : le dessin final, 1080 × 1920 en portrait, à fond perdu, sans marge blanche autour. Le dessin remplit le cadre portrait. Trait net, niveau d'un rendu d'école d'architecture ou d'agence, jamais un graphique de tableur. Pas de titre géant : un petit cartouche discret dans un coin (nom du dessin, adresse en petit, échelle graphique, nord, « © IGN BD TOPO »).
- `soleil.mp4` : 3 s, 1080 × 1920, 30 i/s, H.264, yuv420p, où le dessin se construit sous les yeux et se termine sur l'image finale tenue les 20 dernières images. La première image n'est jamais vide.

Ouvre le PNG pour le regarder, et corrige s'il y a du texte coupé ou qui se chevauche, ou un dessin trop petit pour se lire sur un téléphone. Termine en disant en quelques lignes ce que le dessin montre, ce que disent les données et ce que tu as supposé. N'invente rien sans le dire.
