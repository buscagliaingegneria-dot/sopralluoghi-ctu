---
name: planche-site
description: Toutes les cartes d'analyse de site sur une seule planche A3.
argument-hint: "[nom du projet ou de l'adresse]"
disable-model-invocation: true
---

Nom du projet : $ARGUMENTS

Assemble toutes les cartes PNG du dossier courant (pas celles de `site/`) en une seule planche d'analyse de site, au format A3 portrait. Grille stricte, marges égales, un petit titre pour chaque carte, un cartouche en bas avec le nom du projet, l'adresse lue dans `site/site.json` s'il existe, la date et « Données © IGN BD TOPO, BAN · Licence Ouverte 2.0 ». Ne redessine rien : prends les images telles quelles et ne les déforme pas. Rends `planche.png` en 1080 × 1920, recadré si besoin sans couper de carte, et `planche.pdf`. Termine en disant quelles cartes sont entrées dans la planche.
