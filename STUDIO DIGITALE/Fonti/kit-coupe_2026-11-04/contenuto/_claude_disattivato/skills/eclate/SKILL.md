---
name: eclate
description: Éclaté par niveau : la coupe ouverte en tranches, niveau par niveau.
argument-hint: "[image de la coupe]"
disable-model-invocation: true
---

Fais un éclaté vertical de la coupe : sépare la maison en tranches par niveau (fondations et sous-sol, rez-de-chaussée, étage, toiture), écartées verticalement d'environ 1,5 m chacune, avec de fines lignes pointillées qui relient les arêtes d'une tranche à l'autre. Chaque tranche garde ses éléments coupés en noir et ses pièces nommées, avec sa cote de niveau. Une couleur pâle différente par niveau dans les pièces. Vidéo : la maison est entière, puis les tranches s'écartent en douceur jusqu'à l'éclaté final.

Coupe donnée : $ARGUMENTS (s'il n'y a rien, prends l'image de coupe du dossier courant).

Commence toujours comme ça :
1. Ouvre l'image de la coupe et lis-la vraiment : l'échelle ou les cotes, les niveaux, l'orientation, les pièces, les murs, les dalles, la toiture, les baies, le terrain.
2. Si `coupe.json` existe déjà, réutilise-le. Sinon écris-le : éléments coupés (murs, dalles, toiture, fondations : polygones en mètres), baies (position, hauteurs d'allège et de linteau), pièces (nom, contour, hauteur sous plafond), niveaux, terrain, orientation, profondeur du bâtiment si elle est donnée. Écris aussi ce que tu n'as pas pu lire.
3. Vérifie ta lecture avant de dessiner : les cotes et les niveaux recalculés depuis `coupe.json` doivent coller à ceux écrits sur la coupe (écart de 5 cm au plus), sinon corrige `coupe.json`.

Dessine ensuite en code, avec un script Python (matplotlib, numpy, Pillow ; installe ce qui manque avec pip, et ffmpeg sert à la vidéo). Aucun générateur d'images : tout se calcule depuis `coupe.json`.

Ce que tu rends, dans le dossier courant :
- `eclate.png` : le dessin final, 1080 × 1920 en portrait, sans marge perdue. La coupe étant plus large que haute, cadre-la pour qu'elle occupe au moins 85 % de la largeur et reste lisible sur un téléphone ; la place libre au-dessus et en dessous sert au ciel, au sol ou à la légende, jamais à du vide. Trait net, niveau d'un rendu d'école d'architecture ou d'agence, jamais un graphique de tableur. Pas de titre géant : un petit cartouche discret (nom du dessin, échelle graphique).
- `eclate.mp4` : 3 s, 1080 × 1920, 30 i/s, H.264, yuv420p, où le dessin se construit sous les yeux et se termine sur l'image finale tenue les 20 dernières images. La première image n'est jamais vide.

Ouvre le PNG pour le regarder, et corrige s'il y a du texte coupé ou qui se chevauche. Termine en disant en quelques lignes ce que le dessin montre, ce que tu as lu sur la coupe et ce que tu as supposé parce qu'elle ne le dit pas. N'invente rien sans le dire.
