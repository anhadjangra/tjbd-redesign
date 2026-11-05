# TJBD website redesign prototype

A static prototype of a redesigned site for Tarun Jangra Building Designers (tjbuildingdesigners.com.au). It uses the studio's real projects, photos and films, taken from the current site's backup.

It is a single page with no build step: `index.html` plus `img/` and `media/`. To run it locally, serve the folder with any static server, for example `python3 -m http.server`.

## Concepts

- `/` — the first prototype (blueprint "drafting film" look).
- `sunstudy/` — **Sun Study**, a scroll-driven 3D concept built with three.js. A model house assembles on load, then scrolling runs a sun study across a December day in Brisbane and walks the model through the six design stages (wireframe, massing, plan cut, exploded, plan view, as built at dusk). The portfolio is a 3D fly-through of all 27 projects, with a list view for people who prefer a grid. It reuses the shared `img/` and `media/` folders.
- `deck/` — **Project Deck**, a project-first 3D concept. It opens on a turning drum made of every project photo (hover to see the project, click to open it), then a scroll-driven deck deals the 27 projects one at a time with their specs, photos and an index beside them. Films, studio, process, NDIS, team and contact follow in short sections.
