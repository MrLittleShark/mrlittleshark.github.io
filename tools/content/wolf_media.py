"""Shared attribution markup for figures extracted from the supplied Wolf training PDF."""
from pathlib import Path
import html,json
ROOT=Path(__file__).resolve().parents[2]
FIGURES={r['id']:r for r in json.loads((Path(__file__).parent/'wolf-figures.json').read_text(encoding='utf-8'))}
def figure_html(key):
    f=FIGURES[key];e=html.escape
    return ('<figure class="wolf-figure"><img src="'+e(f['file'])+'" alt="'+e(f['title'])+'" loading="lazy">'
      '<figcaption><strong>'+e(f['title'])+'。</strong>'+e(f['caption'])+' '
      +e(f.get('scientific_note') or '')+'<br><span>来源：Joel Guerrero / '
      '<a href="'+e(f['source_url'])+'">Wolf Dynamics，OpenFOAM Introductory Training</a>，'
      +e(f['source_module_pdf'])+' 第 '+str(f['source_module_page'])+' 页（合并讲义 PDF 第 '+str(f['page'])+' 页）。'
      '<a href="'+e(f['license_url'])+'">CC BY-SA 4.0</a>，裁剪提取；中文说明由本站编写。</span></figcaption></figure>')
