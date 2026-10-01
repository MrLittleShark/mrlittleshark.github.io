"""Apply selected Wolf figures after course prose refinements; safe to rerun."""
from pathlib import Path
import re,json
from wolf_media import FIGURES,figure_html
BASE=Path(__file__).parent
# The first figure replaces the course's earlier general-purpose SVG. Following
# figures are inserted near a relevant section, preserving prose and source code.
plans={
 'blockmesh-first-principles':['wolf-mesh-smooth-transition'],
 'checkmesh-and-quality':['wolf-mesh-nonorthogonality','wolf-mesh-skewness','wolf-diffusion-orthogonal-comparison'],
 'surface-geometry-preparation':['wolf-snappy-background'],
 'snappyhexmesh-workflow':['wolf-snappy-workflow','wolf-snappy-refinement-level','wolf-snappy-surface-refinement','wolf-snappy-surface-snapping','wolf-snappy-layer-stage','wolf-snappy-relative-layer-size','wolf-snappy-layer-coverage'],
 'finite-volume-conservation':['wolf-fvm-convective-face-flux'],
 'advection-schemes-boundedness':['wolf-advection-scheme-comparison','wolf-advection-profile-errors'],
 'diffusion-gradients-laplacian':['wolf-diffusion-nonorthogonal-correction','wolf-mesh-nonorthogonality'],
 'simple-piso-pimple':['wolf-simple-pressure-coupling','wolf-piso-pressure-coupling','wolf-pimple-pressure-coupling'],
 'physical-boundary-design':['wolf-multiphase-ship-boundaries'],
 'laminar-turbulence-model-choice':['wolf-turbulence-rans-les-fields','wolf-turbulence-averaging','wolf-turbulence-model-hierarchy'],
 'wall-resolution-yplus':['wolf-turbulence-wall-law','wolf-mesh-wall-alignment','wolf-turbulence-flatplate-profile'],
 'vof-interface-dambreak':['wolf-vof-volume-fraction','wolf-multiphase-dambreak-workflow'],
 'moving-mesh-and-ami':['wolf-dynamic-cylinder-deformation','wolf-dynamic-mesh-modes','wolf-dynamic-rotor-zones','wolf-dynamic-mrf-configuration','wolf-dynamic-ami-interface'],
 'sampling-functions-and-observables':['wolf-multiphase-ship-validation'],
 'verification-validation-uncertainty':['wolf-turbulence-flatplate-profile'],
 'programming-03':['wolf-mesh-nonorthogonality'],
 'programming-11':['wolf-mesh-smooth-transition'],
 'programming-14':['wolf-simple-pressure-coupling'],
 'programming-15':['wolf-advection-scheme-comparison'],
}
anchors={
 'wolf-snappy-refinement-level':'首先只生成 castellated 网格',
 'wolf-snappy-surface-refinement':'首先只生成 castellated 网格',
 'wolf-snappy-surface-snapping':'其次启用 snap',
 'wolf-snappy-layer-stage':'最后增加 layers',
 'wolf-snappy-relative-layer-size':'字典是否使用相对厚度',
 'wolf-snappy-layer-coverage':'总层数写成某个值',
 'wolf-mesh-skewness':'可以用两个动作区分它们',
 'wolf-diffusion-orthogonal-comparison':'**数值实验：**',
 'wolf-mesh-nonorthogonality':'单元中心值需要插值到面上',
 'wolf-piso-pressure-coupling':'方腔使用：',
 'wolf-pimple-pressure-coupling':'对于使用 PIMPLE 的具体求解器',
 'wolf-advection-profile-errors':'平滑高斯与方波应分别测试',
 'wolf-turbulence-averaging':'这里的“未闭合”指的是',
 'wolf-turbulence-model-hierarchy':'建立一张选择表',
 'wolf-mesh-wall-alignment':'对近似平直、均匀的第一层单元',
 'wolf-turbulence-flatplate-profile':'显示整个目标壁面上的',
 'wolf-multiphase-dambreak-workflow':'在这个案例里，0.orig 提供字段结构',
 'wolf-dynamic-mesh-modes':'描述旋转或移动问题时',
 'wolf-dynamic-rotor-zones':'网格运动后，对流相对于运动面发生',
 'wolf-dynamic-mrf-configuration':'网格运动后，对流相对于运动面发生',
 'wolf-dynamic-ami-interface':'AMI 用于连接两侧不必逐面匹配的接口',
 'wolf-multiphase-morphology':'多相流包含许多不同情形',
 'wolf-multiphase-model-families':'多相流包含许多不同情形',
 'wolf-dynamic-floating-body':'处理运动物体时，首先描述什么在运动',
}

def insertion_many(body,keys):
    # Resolve positions before inserting. Figures sharing one paragraph retain
    # their intended order, including when this script is run repeatedly.
    groups={}
    for key in keys:
        anchor=anchors.get(key);found=body.find(anchor) if anchor else -1
        if found>=0:
            assert body[:found].count(chr(96)*3)%2==0,(key,'anchor inside code')
            if key in ('wolf-piso-pressure-coupling','wolf-pimple-pressure-coupling'):
                pos=body.rfind('\n\n',0,found)+2
            else:
                end=body.find('\n\n',found);pos=end if end>=0 else len(body)
        else:
            matches=list(re.finditer(r'^#{2,4}\s+(.+)$',body,re.M))
            pos=next((m.start() for m in matches if re.search('练习|实践|验收|来源|延伸',m.group(1))),len(body))
        groups.setdefault(pos,[]).append(key)
    for pos,group in sorted(groups.items(),reverse=True):
        body=body[:pos].rstrip()+'\n\n'+'\n\n'.join(figure_html(key) for key in group)+'\n\n'+body[pos:].lstrip()
    return body

changes=[]
for name in ['core-content.json','programming-content.json']:
    path=BASE/name;rows=json.loads(path.read_text(encoding='utf-8'))
    for row in rows:
        selected=plans.get(row['slug'])
        if not selected:continue
        body=row['body']
        # Update existing blocks in place so repeated runs preserve reading order.
        first=figure_html(selected[0])
        existing=re.search(r'<figure class="wolf-figure"><img src="'+re.escape(FIGURES[selected[0]]['file'])+r'"[\s\S]*?</figure>',body)
        image=re.search(r'!\[[^\]]*\]\(/assets/diagrams/[^)]+\)',body)
        if existing:body=body[:existing.start()]+first+body[existing.end():]
        elif image:body=body[:image.start()]+first+body[image.end():]
        else:
            pos=body.find('\n\n');pos=pos if pos>=0 else len(body)
            body=body[:pos]+'\n\n'+first+body[pos:]
        for key in selected[1:]:
            body=re.sub(r'<figure class="wolf-figure"><img src="'+re.escape(FIGURES[key]['file'])+r'"[\s\S]*?</figure>\s*','',body)
        body=insertion_many(body,selected[1:])
        row['body']=body.strip();row['cover_url']=FIGURES[selected[0]]['file']
        row.setdefault('metadata',{})['wolf_figures']=selected
        changes.append({'slug':row['slug'],'figures':selected})
    path.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')

# Remaining overview figures belong to the introductions rather than the first
# exercises; this keeps the VOF lesson focused on a runnable dam-break case.
p=BASE/'topics-content.json';topics=json.loads(p.read_text(encoding='utf-8'))
extras={'topic-multiphase':['wolf-multiphase-morphology','wolf-multiphase-model-families'], 'topic-dynamic-mesh':['wolf-dynamic-floating-body']}
for row in topics:
    keys=extras.get(row['slug'],[])
    for key in keys:
        row['body']=re.sub(r'<figure class="wolf-figure"><img src="'+re.escape(FIGURES[key]['file'])+r'"[\s\S]*?</figure>\s*','',row['body'])
    row['body']=insertion_many(row['body'],keys)
p.write_text(json.dumps(topics,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'courses':len(changes),'course_figure_uses':sum(len(x['figures']) for x in changes),'changes':changes},ensure_ascii=False))
