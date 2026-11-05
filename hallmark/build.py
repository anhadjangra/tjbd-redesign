"""Builds hallmark/index.html from projects.json. Run: python3 hallmark/build.py"""
import json, html, pathlib

HERE = pathlib.Path(__file__).parent
P = json.loads((HERE / "projects.json").read_text())
CATS = {"res": "Residential", "com": "Commercial", "ind": "Industrial", "th": "Townhouses"}
FILMS = {
    "tesla-ern-harley-drive": ("tesla-drone", "tesla-poster.jpg", "tesla-drone-m"),
    "grout-street-macgregor": ("grout-reel", "grout-poster.jpg", "grout-reel-p"),
    "562-grassdale-road-gumdale": ("grassdale", "grassdale-poster.jpg", "grassdale-m"),
}
SHOWN = 9
e = html.escape


def card(i, p):
    f, w, h = p["imgs"][0]
    kind = CATS[p["cat"]] + (f", {p['loc']}" if p["loc"] else "")
    st = f'<span class="st">{e(p["status"])}</span>' if p["status"] else ""
    more = ' class="more"' if i >= SHOWN else ""
    return f'''      <li data-cat="{p["cat"]}"{more}>
        <button class="card" type="button" data-open="{i}" aria-haspopup="dialog">
          <span class="shot" data-slot="work-{p["slug"]}" data-alt="{e(p["name"])}, lead render">
            <img src="../img/m/{f}" srcset="../img/t/{f} 480w, ../img/m/{f} 900w" sizes="(max-width: 40rem) 100vw, (max-width: 60rem) 50vw, 440px" width="{w}" height="{h}" alt="" loading="lazy" decoding="async">
          </span>
          <span class="txt"><h3>{e(p["name"])}</h3><span class="kind">{e(kind)}</span>{st}</span>
        </button>
      </li>'''


counts = {k: sum(1 for p in P if p["cat"] == k) for k in CATS}
filters = [f'<input type="radio" name="cat" id="f-all" value="all" checked><label for="f-all">All <span class="n">{len(P)}</span></label>']
for k, v in CATS.items():
    filters.append(f'<input type="radio" name="cat" id="f-{k}" value="{k}"><label for="f-{k}">{v} <span class="n">{counts[k]}</span></label>')

page = (HERE / "template.html").read_text()
page = page.replace("{{FILTERS}}", "\n        ".join(filters))
page = page.replace("{{CARDS}}", "\n".join(card(i, p) for i, p in enumerate(P)))
page = page.replace("{{COUNT}}", str(len(P)))
data = [{"n": p["name"], "k": CATS[p["cat"]] + (f", {p['loc']}" if p["loc"] else ""), "d": p["desc"], "s": p["specs"], "i": p["imgs"], "f": FILMS.get(p["slug"])} for p in P]
page = page.replace("{{DATA}}", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
(HERE / "index.html").write_text(page)
print("wrote", HERE / "index.html")
