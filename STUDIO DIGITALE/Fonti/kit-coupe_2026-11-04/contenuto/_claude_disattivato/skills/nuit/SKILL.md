---
name: nuit
description: Coupe de nuit : la maison éclairée de l'intérieur, sous un ciel nocturne.
argument-hint: "[image de la coupe]"
disable-model-invocation: true
---

Fais une coupe de nuit, comme une image de couverture : ciel en dégradé bleu nuit avec quelques étoiles, terrain sombre, éléments coupés en noir profond, intérieur éclairé d'une lumière chaude (lampes calculées comme des halos dans chaque pièce, la lumière qui sort par les baies et se pose sur le terrain), silhouettes humaines à contre-jour dans les pièces. Les baies vitrées doivent briller. Vidéo : la coupe est sombre, puis les pièces s'allument une à une.

Coupe donnée : $ARGUMENTS (s'il n'y a rien, prends l'image de coupe du dossier courant).

Commence toujours comme ça :
1. Ouvre l'image de la coupe et lis-la vraiment : l'échelle ou les cotes, les niveaux, l'orientation, les pièces, les murs, les dalles, la toiture, les baies, le terrain.
2. Si `coupe.json` existe déjà, réutilise-le. Sinon écris-le : éléments coupés (murs, dalles, toiture, fondations : polygones en mètres), baies (position, hauteurs d'allège et de linteau), pièces (nom, contour, hauteur sous plafond), niveaux, terrain, orientation, profondeur du bâtiment si elle est donnée. Écris aussi ce que tu n'as pas pu lire.
3. Vérifie ta lecture avant de dessiner : les cotes et les niveaux recalculés depuis `coupe.json` doivent coller à ceux écrits sur la coupe (écart de 5 cm au plus), sinon corrige `coupe.json`.

Dessine ensuite en code, avec un script Python (matplotlib, numpy, Pillow ; installe ce qui manque avec pip, et ffmpeg sert à la vidéo). Aucun générateur d'images : tout se calcule depuis `coupe.json`.

Ce que tu rends, dans le dossier courant :
- `nuit.png` : le dessin final, 1080 × 1920 en portrait, sans marge perdue. La coupe étant plus large que haute, cadre-la pour qu'elle occupe au moins 85 % de la largeur et reste lisible sur un téléphone ; la place libre au-dessus et en dessous sert au ciel, au sol ou à la légende, jamais à du vide. Trait net, niveau d'un rendu d'école d'architecture ou d'agence, jamais un graphique de tableur. Pas de titre géant : un petit cartouche discret (nom du dessin, échelle graphique).
- `nuit.mp4` : 3 s, 1080 × 1920, 30 i/s, H.264, yuv420p, où le dessin se construit sous les yeux et se termine sur l'image finale tenue les 20 dernières images. La première image n'est jamais vide.

Ouvre le PNG pour le regarder, et corrige s'il y a du texte coupé ou qui se chevauche. Termine en disant en quelques lignes ce que le dessin montre, ce que tu as lu sur la coupe et ce que tu as supposé parce qu'elle ne le dit pas. N'invente rien sans le dire.
