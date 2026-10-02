from pathlib import Path
import json,re
from wolf_media import FIGURES,figure_html
HERE=Path(__file__).parent
body=(HERE/'authored-pages/topic-finite-volume.md').read_text(encoding='utf-8')
body=re.sub(r'\{\{figure:([^}]+)\}\}',lambda m:figure_html(m.group(1)),body)
(HERE/'authored-pages/topic-finite-volume.md').write_text(body,encoding='utf-8')
row={'slug':'topic-finite-volume','kind':'module','title':'有限体积法','summary':'控制体、面通量、离散格式、矩阵装配与压力速度耦合。','body':body,'track':'专题学习','series':'OpenFOAM v2512 专题','sort_order':0,'status':'published','author_name':'FoamLab','cover_url':FIGURES['wolf-fvm-convective-face-flux']['file'],'comments_enabled':True,'metadata':{'topic_key':'finite-volume','version':'v2512','canonical_path':'/topics/finite-volume/'}}
(HERE/'finite-volume-content.json').write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
core={'finite-volume-conservation','advection-schemes-boundedness','diffusion-gradients-laplacian','time-discretisation-courant','simple-piso-pimple','linear-solvers-residuals','relaxation-stability-diagnosis','grid-time-verification'}
for filename in ['core-content.json','programming-content.json','algorithm-theory-content.json']:
    file=HERE/filename;rows=json.loads(file.read_text(encoding='utf-8'))
    for item in rows:
        if item['slug'] in core or item['slug'].startswith('algorithm-theory-') or item['slug'] in ['programming-10','programming-14','programming-15']:
            topics=item.setdefault('metadata',{}).setdefault('topics',[])
            if 'finite-volume' not in topics:topics.append('finite-volume')
    file.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
