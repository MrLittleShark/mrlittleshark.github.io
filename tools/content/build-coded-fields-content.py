"""Assemble six tutorials from teaching prose and the exact tested case sources."""
from pathlib import Path
import re, json, runpy, uuid

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).parent
G=runpy.run_path(str(HERE/'build-coded-fields.py'))
CASES=G['CASES']
SECTION_ID=str(uuid.uuid5(uuid.NAMESPACE_URL,'https://foamlabshark.github.io/programming/coded-fields/'))
lessons=[
 ('用 codeStream 设置温度初值：均匀、线性与热斑','从完整 0/T 文件开始，逐行解释网格访问、字段创建和输出，运行三组热扩散算例。','temperature','60 分钟'),
 ('按几何区域设置初值：椭圆热区与平滑过渡','用单元坐标判断椭圆内外，计算初始热区体积，再扩展到圆形、多热区和体积分数。','ellipse','45 分钟'),
 ('用 codeStream 设置固定入口速度剖面','在二维通道中生成内部初始速度与入口抛物线，解释单元中心、面中心、平均速度与流量。','fixed','60 分钟'),
 ('用 codedFixedValue 编写边界公式','复现相同固定入口，逐行理解 patch、向量字段、operator== 与动态编译，衔接时变边界。','steady','45 分钟'),
 ('设置随时间变化的入口：启动、脉动与开关','完整运行线性启动和正弦入口，再改成延迟启动、半余弦启动和有限时长脉冲。','time','60 分钟'),
 ('设置时空变化入口：参数、流量、重启与并行','通过 codeContext 设置脉动抛物线，用面积归一化控制平均速度，完成重启和两进程计算。','pulsed','90 分钟'),
]

def block(text,language):return '```'+language+'\n'+text.strip()+'\n```'
def resolve(match):
    kind,arg=match.group(1).split(':',1)
    if kind=='file':return block((CASES/arg).read_text(encoding='utf-8'),'foam')
    if kind=='boundary':return block('inlet\n{\n'+G['textwrap'].indent(G['BCS'][arg],'    ')+'\n}','foam')
    if kind=='snippet':
        names=arg.split(':');v=G[names[0]]
        for name in names[1:]:v=v[name]
        return block(v,'cpp')
    raise ValueError(kind)

def main():
    manifest=json.loads((ROOT/'source-openfoam/downloads/programming/coded-fields-manifest.json').read_text())
    rows=[]
    for i,(title,summary,figure,duration) in enumerate(lessons,1):
        slug=f'coded-fields-{i:02d}'
        body=(HERE/'coded-fields/lessons'/f'{slug}.md').read_text(encoding='utf-8')
        body=re.sub(r'\{\{([^}\n]+)\}\}',resolve,body)
        assert '{{' not in body
        rows.append(dict(slug=slug,kind='lesson',title=f'{i:02d} · '+title,summary=summary,body=body,track='OpenFOAM 编程',series='用代码设置初始与边界条件',sort_order=240+i,status='published',author_name='FoamLab',cover_url=f'/assets/science/coded-fields-{figure}.png',comments_enabled=True,section_ids=[SECTION_ID],metadata={'version':'v2512','duration':duration,'source':'FoamLab；接口参考 OpenFOAM v2512 源码；几何初值教学参考 Wolf Dynamics','downloads':[dict(label='本课完整算例与参考数据',description='解压后进入对应算例目录，运行 bash Allrun。',kind='case',**manifest[f'{i:02d}'])], 'download':manifest[f'{i:02d}']['url']}))
    (HERE/'coded-fields-content.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    out=ROOT/'.openfoam-work/coded-fields';out.mkdir(parents=True,exist_ok=True)
    section=dict(id=SECTION_ID,key='coded-fields',name='用代码设置初始与边界条件',parent_key='programming',href='/programming/coded-fields/',description='codeStream 初始场、固定边界与 codedFixedValue 时变入口。六节教程，九个可运行算例。',nav_group='学习空间',sort_order=405)
    (HERE/'coded-fields/section.json').write_text(json.dumps(section,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    def quote(s):return "'"+s.replace("'","''")+"'"
    (out/'section.sql').write_text(f"insert into public.foamlab_sections(id,key,name,parent_id,href,description,nav_group,visible,sort_order) select '{SECTION_ID}', 'coded-fields', {quote(section['name'])}, id, '/programming/coded-fields/', {quote(section['description'])}, '学习空间', false, 405 from public.foamlab_sections where key='programming' returning id,key,name,visible;",encoding='utf-8')
    for i,row in enumerate(rows,1):
        draft={**row,'status':'draft'}
        payload=json.dumps(draft,ensure_ascii=False,separators=(',',':'))
        assert '$coded_lesson$' not in payload
        sql="""with data as (select $coded_lesson$"""+payload+"""$coded_lesson$::jsonb as j), owner as (select author_id from public.foamlab_content where slug='development-boundary')
insert into public.foamlab_content(slug,kind,title,summary,body,track,series,sort_order,status,author_name,author_id,cover_url,comments_enabled,metadata,section_ids)
select j->>'slug',j->>'kind',j->>'title',j->>'summary',j->>'body',j->>'track',j->>'series',(j->>'sort_order')::integer,'draft','FoamLab',(select author_id from owner),j->>'cover_url',true,j->'metadata',array(select jsonb_array_elements_text(j->'section_ids')::uuid)
from data returning slug,status,revision;"""
        (out/f'lesson-{i:02d}.sql').write_text(sql,encoding='utf-8')
    print(json.dumps({'section_id':SECTION_ID,'lessons':len(rows),'characters':[len(r['body']) for r in rows]},ensure_ascii=False))

if __name__=='__main__':main()
