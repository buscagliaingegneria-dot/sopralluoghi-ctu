---
name: hauteurs
description: Le quartier en 3D, chaque bâtiment à sa vraie hauteur.
argument-hint: "[adresse en France]"
disable-model-invocation: true
---

Fais une vue 3D axonométrique du quartier autour de cette adresse : chaque bâtiment extrudé à sa hauteur (`hauteur` de la BD TOPO ; s'il manque, compte-le et laisse-le à plat en gris), couleur en dégradé de la plus basse à la plus haute (du crème au bleu nuit), faces latérales plus sombres que les toits pour lire le volume, vue depuis le sud-ouest à environ 35° au-dessus de l'horizon. Garde un disque d'environ 350 m de rayon autour de l'adresse pour que les volumes se lisent sur un téléphone, et marque l'adresse d'une petite tige vermillon. Une légende des hauteurs en mètres, et la hauteur médiane et la plus haute écrites. Dessine-la en projection maison avec numpy et matplotlib (polygones triés de l'arrière vers l'avant), pas en nuage de points. Vidéo : les bâtiments montent du sol à leur hauteur, du centre vers l'extérieur.

Adresse donnée : $ARGUMENTS

Commence toujours comme ça :
1. Si `site/site.json` n'existe pas, lance `python outils/donnees_site.py "<l'adresse>"`. Il télécharge les données ouvertes de l'IGN (BD TOPO, Base Adresse Nationale, isochrones piétons) dans `site/`, en mètres, origine à l'adresse, nord en haut. S'il existe, réutilise-le.
2. Lis `site/site.json` : vérifie que l'adresse trouvée est bien celle demandée (sinon arrête-toi et dis-le), note le cadre et le nombre d'objets.
3. Ouvre les GeoJSON dont tu as besoin et regarde ce qu'ils contiennent vraiment (champs, valeurs vides) avant de dessiner.

Dessine ensuite en code, avec un script Python (matplotlib, numpy, shapely, Pillow ; installe ce qui manque avec pip, et ffmpeg sert à la vidéo). Aucun générateur d'images : tout se calcule depuis `site/`.

Ce que tu rends, dans le dossier courant :
- `hauteurs.png` : le dessin final, 1080 × 1920 en portrait, à fond perdu, sans marge blanche autour. La vue 3D remplit le cadre portrait. Trait net, niveau d'un rendu d'école d'architecture ou d'agence, jamais un graphique de tableur. Pas de titre géant : un petit cartouche discret dans un coin (nom du dessin, adresse en petit, échelle graphique, nord, « © IGN BD TOPO »).
- `hauteurs.mp4` : 3 s, 1080 × 1920, 30 i/s, H.264, yuv420p, où le dessin se construit sous les yeux et se termine sur l'image finale tenue les 20 dernières images. La première image n'est jamais vide.

Ouvre le PNG pour le regarder, et corrige s'il y a du texte coupé ou qui se chevauche, ou un dessin trop petit pour se lire sur un téléphone. Termine en disant en quelques lignes ce que le dessin montre, ce que disent les données et ce que tu as supposé. N'invente rien sans le dire.
