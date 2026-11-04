---
name: planche-coupe
description: Tous les dessins de coupe sur une seule planche A3.
argument-hint: "[nom du projet]"
disable-model-invocation: true
---

Nom du projet : $ARGUMENTS

Assemble tous les dessins PNG du dossier en une seule planche verticale de rendu, au format A3 portrait (sauf l'image de la coupe de départ). Grille stricte, marges égales, un petit titre pour chaque dessin, un cartouche en bas avec le nom du projet et la date. Ne redessine rien : prends les images telles quelles et ne les déforme pas. Rends `planche.png` en 1080 × 1920, recadré si besoin sans couper de dessin, et `planche.pdf`. Termine en disant quels fichiers sont entrés dans la planche.
