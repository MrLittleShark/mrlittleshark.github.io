"""Shared attribution markup for figures extracted from the supplied Wolf training PDF."""
from pathlib import Path
import html,json
ROOT=Path(__file__).resolve().parents[2]
FIGURES={r['id']:r for r in json.loads((Path(__file__).parent/'wolf-figures.json').read_text(encoding='utf-8'))}
def figure_html(key):
    f=FIGURES[key];e=html.escape
    return ('<figure class="wolf-figure"><img src="'+e(f['file'])+'" alt="'+e(f['title'])+'" loading="lazy">'
      '<figcaption><strong>'+e(f['title'])+'</strong>'
      '<small class="figure-source">来源：Joel Guerrero / '
      '<a href="'+e(f['source_url'])+'">Wolf Dynamics</a> · '
      +e(f['source_module_pdf'])+'，p. '+str(f['source_module_page'])+'</small></figcaption></figure>')
