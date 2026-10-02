"""Assemble tutorials from tested dictionaries and prepare guarded CMS drafts."""
from pathlib import Path
import json,re,uuid,runpy

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).parent
G=runpy.run_path(str(HERE/'build-advanced-mesh.py'))
OUT=ROOT/'.openfoam-work/advanced-mesh'
TOPICS='1f14bf4e-a678-459c-9bea-413184204c5b'
MESHING='4342316d-cb35-4abd-a0be-3af53c95254d'
DYNAMIC='098acc0d-1381-4ebe-91cd-59ce79a3ab74'
def uid(route):return str(uuid.uuid5(uuid.NAMESPACE_URL,'https://foamlabshark.github.io'+route))
PARENT=uid('/topics/meshes/')
sections=[
 ('topic-meshes','各类网格','meshes',TOPICS,'从基础划分到变形、重叠、动态加密和旋转流动。',170),
 ('topic-overset','重叠网格','overset',PARENT,'让物体附近网格独立运动，用重叠插值连接背景流场。',181),
 ('topic-adaptive-refinement','动态加密网格','adaptive-refinement',PARENT,'跟随水气界面分裂和合并单元，查看网格数量与水量变化。',182),
 ('topic-rotating-ami','旋转网格与 AMI','rotating-ami',PARENT,'转子网格实际旋转，跨 AMI 接口交换流动信息。',183),
 ('topic-rotating-frames','旋转参考系：MRF / SRF','rotating-frames',PARENT,'用固定网格处理旋转流动，读懂绝对速度与相对速度。',184),
]
lessons=[
 ('移动锥体：让边界带动网格变形','设置单方向网格速度和运动壁面，观察锥体移动 3 mm 后的网格与流场。','deforming',DYNAMIC,'60 分钟'),
 ('重叠网格：在背景流场中旋转一个物体','从区域编号、挖孔和运动设置开始，运行完整重叠插值算例。','overset',uid('/topics/overset/'),'90 分钟'),
 ('动态加密：让网格跟随水气界面','逐项设置加密范围与级别，比较粗细网格、单元数量及水量。','refinement',uid('/topics/adaptive-refinement/'),'90 分钟'),
 ('旋转网格与 AMI：计算搅拌槽中的真实转动','建立旋转区和静止区，设置接口、转速与时间步，查看半圈旋转结果。','ami',uid('/topics/rotating-ami/'),'90 分钟'),
 ('MRF：用固定网格计算旋转设备','指定旋转 cellZone、转速和壁面，阅读 SIMPLE 迭代与速度结果。','mrf',uid('/topics/rotating-frames/'),'60 分钟'),
 ('SRF：在旋转参考系中设置入口与壁面','运行三维旋转通道，理解 Urel、U、rpm 和 SRFVelocity 的关系。','srf',uid('/topics/rotating-frames/'),'60 分钟'),
]

def clean(text):
 text=re.sub(r'/\*.*?\*/','',text,flags=re.S)
 return '\n'.join(line for line in text.splitlines() if not re.match(r'\s*//\s*\*',line)).strip()
def block_at(text,key):
 m=re.search(r'(?m)^\s*'+re.escape(key)+r'\s*\{',text)
 if not m:raise ValueError(key)
 start=m.start();opening=text.index('{',m.start());level=1;i=opening+1
 while level:
  if text[i]=='{':level+=1
  if text[i]=='}':level-=1
  i+=1
 return text[start:i].strip(),text[opening+1:i-1]
def resolve(m):
 kind,arg=m[1].split(':',1);path,*selector=arg.split(':',1)
 text=clean((G['CASES']/path).read_text(encoding='utf-8'))
 language='bash' if path.endswith('/Allrun') else 'foam'
 if kind=='block':
  for key in selector[0].split('/'):
   result,inner=block_at(text,key);text=inner
  text=result
 elif kind=='entry':
  name=selector[0];match=re.search(r'\b'+re.escape(name)+r'\s*\(.*?\)\s*;',text,re.S);assert match;text=match[0]
 elif kind!='file':raise ValueError(kind)
 return '```'+language+'\n'+text+'\n```'

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 manifest=json.loads((ROOT/'source-openfoam/downloads/meshes/advanced-mesh-manifest.json').read_text())
 rows=[];nodes=[]
 for key,name,route,parent,desc,sort in sections:
  href=f'/topics/{route}/';node=dict(id=uid(href),key=key,name=name,parent_id=parent,href=href,description=desc,nav_group='学习空间',visible=True,sort_order=sort,revision=1);nodes.append(node)
  source=ROOT/'source-openfoam'/href.strip('/')/'index.md';source.parent.mkdir(parents=True,exist_ok=True)
  source.write_text(f'---\ntitle: "{name}"\nlayout: topics\nsection: topics\ntopic: {route}\ndescription: "{desc}"\n---\n',encoding='utf-8')
  body=(HERE/'advanced-mesh/modules'/f'{route}.md').read_text(encoding='utf-8')
  cover={'meshes':'refinement','overset':'overset','adaptive-refinement':'refinement','rotating-ami':'ami','rotating-frames':'mrf'}[route]
  rows.append(dict(slug=key,kind='module',title=name,summary=desc,body=body,track='各类网格',series='',sort_order=sort,cover_url=f'/assets/science/advanced-mesh-{cover}.png',metadata={'topic_key':route,'version':'v2512','canonical_path':href},section_ids=[node['id']]))
 for i,(title,summary,figure,section,duration) in enumerate(lessons,1):
  slug=f'advanced-mesh-{i:02d}'
  body=(HERE/'advanced-mesh/lessons'/f'{slug}.md').read_text(encoding='utf-8')
  body=re.sub(r'\{\{([^}\n]+)\}\}',resolve,body);assert '{{' not in body
  rows.append(dict(slug=slug,kind='lesson',title=f'{i:02d} · '+title,summary=summary,body=body,track='各类网格',series='高级网格与旋转流动',sort_order=300+i,section_ids=[section],cover_url=f'/assets/science/advanced-mesh-{figure}.png',metadata={'version':'v2512','duration':duration,'download':manifest[f'{i:02d}']['url'],'downloads':[dict(label='本课完整算例与参考数据',description='解压后进入算例目录，运行 bash Allrun。',kind='case',**manifest[f'{i:02d}'])]}))
 for r in rows:r.update(status='published',author_name='FoamLab',comments_enabled=r['kind']=='lesson')
 (HERE/'advanced-mesh-content.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (HERE/'advanced-mesh/sections.json').write_text(json.dumps(nodes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 payload=json.dumps([{**n,'visible':False} for n in nodes],ensure_ascii=False)
 (OUT/'sections.sql').write_text("""insert into public.foamlab_sections(id,key,name,parent_id,href,description,nav_group,visible,sort_order)
select id,key,name,parent_id,href,description,nav_group,false,sort_order from jsonb_to_recordset($nodes$"""+payload+"""$nodes$::jsonb) as n(id uuid,key text,name text,parent_id uuid,href text,description text,nav_group text,sort_order integer) returning id,key,visible;""",encoding='utf-8')
 for i,row in enumerate(rows):
  payload=json.dumps({**row,'status':'draft'},ensure_ascii=False,separators=(',',':'))
  sql="""with data as(select $mesh_lesson$"""+payload+"""$mesh_lesson$::jsonb j), owner as(select author_id from public.foamlab_content where slug='development-boundary')
insert into public.foamlab_content(slug,kind,title,summary,body,track,series,sort_order,status,author_name,author_id,cover_url,comments_enabled,metadata,section_ids)
select j->>'slug',j->>'kind',j->>'title',j->>'summary',j->>'body',j->>'track',j->>'series',(j->>'sort_order')::integer,'draft','FoamLab',(select author_id from owner),j->>'cover_url',(j->>'comments_enabled')::boolean,j->'metadata',array(select jsonb_array_elements_text(j->'section_ids')::uuid)
from data returning slug,status,revision;"""
  (OUT/f'draft-{i:02d}.sql').write_text(sql,encoding='utf-8')
 # Existing URLs and all content placements remain valid when their parents change.
 names=','.join("'"+r['slug']+"'" for r in rows)
 nodeids=','.join("'"+n['id']+"'" for n in nodes)
 dynamic_body=(HERE/'advanced-mesh/modules/dynamic-mesh.md').read_text(encoding='utf-8')
 publish=f"""begin;
do $$ begin
 if (select count(*) from foamlab_sections where id in ('{MESHING}','{DYNAMIC}') and parent_id='{TOPICS}' and revision=1) <> 2 then raise exception 'Original mesh directories changed'; end if;
 if (select count(*) from foamlab_content where slug in ({names}) and status='draft' and revision=1) <> 11 then raise exception 'Drafts changed'; end if;
 if (select count(*) from foamlab_sections where id in ({nodeids}) and visible=false and revision=1) <> 5 then raise exception 'New directories changed'; end if;
 if (select count(*) from foamlab_content where slug='topic-dynamic-mesh' and revision=3) <> 1 then raise exception 'Dynamic mesh introduction changed'; end if;
end $$;
update foamlab_sections set parent_id='{PARENT}' where id in ('{MESHING}','{DYNAMIC}');
update foamlab_sections set visible=true where id in ({nodeids});
update foamlab_content set status='published',published_at=now() where slug in ({names});
update foamlab_content set body=$dynamic${dynamic_body}$dynamic$, summary='从移动锥体开始，设置网格运动、壁面速度和时间步，观察变形后的网格与流动。',cover_url='/assets/science/advanced-mesh-deforming.png' where slug='topic-dynamic-mesh';
commit;
select key,name,parent_id,visible from foamlab_sections where id in ({nodeids},'{MESHING}','{DYNAMIC}');
"""
 (OUT/'publish.sql').write_text(publish,encoding='utf-8')
 print(json.dumps({'new_nodes':len(nodes),'new_rows':len(rows),'lesson_characters':[len(r['body']) for r in rows if r['kind']=='lesson']},ensure_ascii=False))

if __name__=='__main__':main()
