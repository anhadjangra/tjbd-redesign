# TJBD website redesign prototype

A static prototype of a redesigned site for Tarun Jangra Building Designers (tjbuildingdesigners.com.au). It uses the studio's real projects, photos and films, taken from the current site's backup.

It is a single page with no build step: `index.html` plus `img/` and `media/`. To run it locally, serve the folder with any static server, for example `python3 -m http.server`.

## Hallmark concept (`hallmark/`)

A second, separate concept built with the [Hallmark](https://github.com/nutlope/hallmark) design skill: theme Brutal (Libre Franklin 900 capitals, 3px ink rules, one yellow fill), Catalogue shape. The work leads as a boxed grid of all 27 projects printed in ink; opening one shows it in full colour with its specs and, where there is one, its film.

Open `hallmark/index.html` through a static server from the repo root (it reuses `../img` and `../media`). `hallmark/build.py` regenerates the page from `template.html` and `projects.json`.
