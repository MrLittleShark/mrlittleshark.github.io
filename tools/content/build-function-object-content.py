"""Assemble functionObject lessons, navigation and guarded CMS drafts."""
from pathlib import Path
import re,json,uuid,runpy,html

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).parent/'function-objects'
OUT=ROOT/'.openfoam-work/function-objects'
CASES=Path('F:/UbuntuShareFolder/.foamlab-build/function-objects/source/foamLabFunctionObjects')
TOPICS='1f14bf4e-a678-459c-9bea-413184204c5b'
HREF='/topics/function-objects/'
UID=str(uuid.uuid5(uuid.NAMESPACE_URL,'https://foamlabshark.github.io'+HREF))
LESSONS=[
 ('第一个后处理对象：配置、运行与结果','在方腔中计算速度大小，练习五种 postProcess 调用，认识场文件与采样文件。','01-cavity','sampling'),
 ('通用参数：什么时候计算，什么时候保存','逐项设置库、区域、执行频率、写出频率、统计起点和文本精度。','01-cavity','schedule'),
 ('probes：记录速度、压力与壁面测点','布置域内与壁面探针，选择插值和采样间隔，读取向量时间序列。','01-cavity','statistics'),
 ('sets：提取中心线剖面与离散点数据','设置直线、坐标轴、点数和文件格式，解释采样位置与网格分辨率。','01-cavity','sampling'),
 ('surfaces 与 streamLine：截面、界面和流线','设置切平面、相分数等值面和流线种子，导出可直接打开的 VTK 文件。','01-cavity','sampling'),
 ('空间统计：极值、体积平均与直方图','比较平均与体积平均，掌握 fieldStatistics、volFieldValue 和分箱参数。','01-cavity','statistics'),
 ('流量与压降：选面、积分和组合运算','用 phi 求流量、用压力求面积平均，再自动计算进出口压降。','02-pitzDaily','forces'),
 ('场运算：梯度、涡量、Q 与表达式','从速度大小开始，逐步生成导数、涡结构指标和自定义动能场。','01-cavity','vortex'),
 ('时间统计：平均场、脉动与统计窗口','区分时间与空间平均，解释 UPrime2Mean、窗口和重启设置。','01-cavity','statistics'),
 ('forces 与 forceCoeffs：力、力矩和参考量','设置受力壁面、密度、参考中心、面积、方向，读懂系数曲线。','02-pitzDaily','forces'),
 ('壁面与湍流：yPlus、剪切应力和模型场','输出近壁指标、剪切方向与湍流量，使用求解器加载模型做后处理。','02-pitzDaily','wall'),
 ('传热：壁面热流、热流传感器与换热系数','解释 v2512 wall/gauge 两种模型，设置热流积分与参考温差。','03-hotRoom','heat'),
 ('两相流：水量、液位和自由表面','运行溃坝算例，用相分数积分检查水量，沿重力方向测量液位。','04-damBreak','multiphase'),
 ('结果导出：读取场、VTK 与 EnSight','选择字段和网格部分，输出单元坐标与体积，整理可分享的结果。','01-cavity','workflow'),
 ('计算监测：残差、守恒和 Courant 数','组合 solverInfo、continuityError 与 Co 场，定位数值和物理变化。','01-cavity','monitor'),
 ('runTimeControl：按条件结束或切换阶段','运行自动停止算例，解释条件、持续时间、组合逻辑和触发器。','05-autoStop','schedule'),
 ('工具分类与选用索引','按采样、统计、场运算、载荷、传热、声学、颗粒和流程管理查工具。','01-cavity','workflow'),
]

def block(s,key):
 m=re.search(r'(?m)^'+re.escape(key)+r'\s*\{',s);assert m,key
 i=s.index('{',m.start());depth=1;j=i+1
 while depth:
  depth+=(s[j]=='{')-(s[j]=='}');j+=1
 return s[m.start():j]
def resolve(m):
 kind,arg=m[1].split(':',1)
 if kind=='fo':
  case,key=arg.split(':');s=block((CASES/case/'system/functions').read_text(encoding='utf-8'),key)
 elif kind=='file':s=(CASES/arg).read_text(encoding='utf-8').strip()
 else:raise ValueError(kind)
 return '```foam\n'+s+'\n```'

def diagram(name,title,subtitle,boxes,footer):
 colors=['#2e7462','#327db0','#aa7830']
 contents=[]
 for i,(heading,lines) in enumerate(boxes):
  x=38+i*355;c=colors[i%3]
  contents.append(f'<rect x="{x}" y="140" width="314" height="216" rx="12" fill="white" stroke="#cbded5"/><rect x="{x}" y="140" width="314" height="49" rx="12" fill="{c}"/><text x="{x+20}" y="173" fill="white" font-size="21" font-weight="bold">{html.escape(heading)}</text>')
  for j,line in enumerate(lines):contents.append(f'<text x="{x+20}" y="{223+j*37}" font-size="18" fill="#29443d">{html.escape(line)}</text>')
  if i<2:contents.append(f'<path d="M {x+322},246 h 25 m -7,-6 7,6 -7,6" fill="none" stroke="#488776" stroke-width="2"/>')
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="445" viewBox="0 0 1120 445" role="img"><title>{html.escape(title)}</title><rect width="1120" height="445" fill="#f4f8f5"/><g font-family="Microsoft YaHei, PingFang SC, sans-serif"><text x="38" y="55" font-size="28" font-weight="bold" fill="#243d35">{html.escape(title)}</text><text x="38" y="92" font-size="18" fill="#527066">{html.escape(subtitle)}</text>{''.join(contents)}<text x="38" y="407" font-size="17" fill="#527066">{html.escape(footer)}</text></g></svg>'''
 (ROOT/'source-openfoam/assets/science'/f'functionobjects-{name}.svg').write_text(svg,encoding='utf-8')

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 diagram('workflow','从计算场到后处理结果','functionObject 的输入、处理与输出',[
  ('读取输入',['求解器内存中的 U、p、T','或时间目录中的已有场','readFields → 对象数据库']),
  ('选择处理',['点 / 线 / 面：采样','场运算 / 平均 / 积分','执行频率与输出频率分开']),
  ('保存结果',['OpenFOAM 派生场','postProcessing 文本曲线','VTK / EnSight 几何与数据'])], '配置位置：system/controlDict → functions；独立配置可由 postProcess -dict 调用。')
 diagram('schedule','执行与写出是两个时序','方腔：Δt = 0.005 s；fieldAverage 从 0.1 s 开始',[
  ('求解时间步',['0.005、0.010、0.015 …','更新速度与压力','一直推进到 0.5 s']),
  ('平均场更新',['timeStart 0.1','executeControl timeStep','executeInterval 1']),
  ('保存统计结果',['writeControl writeTime','随主场每 0.05 s 保存','UMean / UPrime2Mean'])], '自动停止示例：控制器在 0.005 s 首次执行，累计 0.2 s 后于 0.205 s 结束。')
 diagram('wall','把近壁网格与模型结果联系起来','壁面后处理使用求解器提供的动量和湍流模型',[
  ('网格位置：yPlus',['首层单元距壁距离 y','摩擦速度与运动黏度','得到壁面单位 y+']),
  ('摩擦：wallShearStress',['壁面应力向量','大小：局部摩擦强弱','方向：分离与再附着']),
  ('模型：turbulenceFields',['k / epsilon / omega','nut / R / 有效应力','对照湍流强度与输运'])], '先运行模型，再输出壁面量；离线处理可使用 simpleFoam -postProcess。')
 diagram('monitor','用三组数据观察计算过程','按研究问题选择监测量',[
  ('代数求解',['solverInfo','初始 / 最终残差','线性迭代次数']),
  ('离散与守恒',['continuityError','局部 / 全局 / 累计误差','Co 场定位时间步限制']),
  ('物理结果',['流量与压降','力、热功率或水相体积','随时间 / 迭代的变化'])], '把残差、守恒与目标物理量一起查看，判断继续迭代、延长统计或调整网格。')
 manifest=json.loads((ROOT/'source-openfoam/downloads/function-objects/manifest.json').read_text())
 node=dict(id=UID,key='topic-function-objects',name='functionObject',parent_id=TOPICS,href=HREF,description='采样、统计、场运算、载荷与传热后处理：参数、示例和结果。',nav_group='学习空间',visible=False,sort_order=180)
 rows=[dict(slug='topic-function-objects',kind='module',title='functionObject',summary=node['description'],body=(HERE/'introduction.md').read_text(encoding='utf-8'),track='functionObject',series='',sort_order=180,cover_url='/assets/science/functionobjects-sampling.png',metadata={'topic_key':'function-objects','version':'v2512','canonical_path':HREF},section_ids=[UID])]
 for i,(title,summary,case,figure) in enumerate(LESSONS):
  body=(HERE/'lessons'/f'{i:02d}.md').read_text(encoding='utf-8');body=re.sub(r'\{\{([^}\n]+)\}\}',resolve,body)
  assert '{{' not in body and body.count('```')%2==0
  suffix='svg' if figure in ('schedule','workflow','wall','monitor') else 'png'
  cover=f'/assets/science/functionobjects-{figure}.{suffix}'
  if '![' not in body:
   paragraphs=body.split('\n\n',1);body=paragraphs[0]+'\n\n!['+title+']('+cover+')\n\n'+paragraphs[1]
  files=[case]
  if i==4:files+=['04-damBreak']
  if i==0:files+=['02-pitzDaily']
  downloads=[dict(label={'01-cavity':'方腔','02-pitzDaily':'后台阶','03-hotRoom':'冷热壁面','04-damBreak':'溃坝','05-autoStop':'自动停止'}[c]+'：完整算例与参考数据',kind='case',description='解压后进入算例目录，运行 bash Allrun。',size_bytes=manifest[c]['bytes'],**manifest[c]) for c in files]
  rows.append(dict(slug=f'function-objects-{i:02d}',kind='lesson',title=f'{i:02d} · '+title,summary=summary,body=body,track='functionObject',series='functionObject 后处理',sort_order=400+i,cover_url=cover,section_ids=[UID],metadata={'version':'v2512','topics':['function-objects'],'duration':'30–60 分钟','downloads':downloads,'download':downloads[0]['url']}))
 for r in rows:r.update(status='published',author_name='FoamLab',comments_enabled=r['kind']=='lesson')
 (HERE.parent/'function-objects-content.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (HERE/'section.json').write_text(json.dumps(node,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 p=ROOT/'source-openfoam/topics/function-objects/index.md';p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text('---\ntitle: functionObject\nlayout: topics\nsection: topics\ntopic: function-objects\ndescription: 采样、统计、场运算、载荷与传热后处理的参数与示例。\n---\n',encoding='utf-8')
 payload=json.dumps([node],ensure_ascii=False)
 (OUT/'sections.sql').write_text("insert into foamlab_sections(id,key,name,parent_id,href,description,nav_group,visible,sort_order) select id,key,name,parent_id,href,description,nav_group,false,sort_order from jsonb_to_recordset($nodes$"+payload+"$nodes$::jsonb) as n(id uuid,key text,name text,parent_id uuid,href text,description text,nav_group text,sort_order integer) returning id,key,revision;",encoding='utf-8')
 for i,row in enumerate(rows):
  payload=json.dumps(row,ensure_ascii=False,separators=(',',':'))
  sql="""with data as(select $fo_content$"""+payload+"""$fo_content$::jsonb j), owner as(select author_id from foamlab_content where slug='development-boundary')
insert into foamlab_content(slug,kind,title,summary,body,track,series,sort_order,status,author_name,author_id,cover_url,comments_enabled,metadata,section_ids)
select j->>'slug',j->>'kind',j->>'title',j->>'summary',j->>'body',j->>'track',j->>'series',(j->>'sort_order')::integer,'draft','FoamLab',(select author_id from owner),j->>'cover_url',(j->>'comments_enabled')::boolean,j->'metadata',array(select jsonb_array_elements_text(j->'section_ids')::uuid) from data returning slug,status,revision;"""
  (OUT/f'draft-{i:02d}.sql').write_text(sql,encoding='utf-8')
 names=','.join("'"+r['slug']+"'" for r in rows)
 publish=f"""begin;
do $$ begin
 if (select count(*) from foamlab_content where slug in ({names}) and status='draft' and revision=1) <> {len(rows)} then raise exception 'functionObject drafts changed'; end if;
 if (select count(*) from foamlab_sections where id='{UID}' and visible=false and revision=1) <> 1 then raise exception 'functionObject directory changed'; end if;
end $$;
update foamlab_sections set visible=true where id='{UID}';
update foamlab_content set status='published',published_at=now() where slug in ({names});
commit;
select slug,status,length(body) as characters from foamlab_content where slug in ({names}) order by sort_order;
"""
 (OUT/'publish.sql').write_text(publish,encoding='utf-8')
 print(json.dumps({'rows':len(rows),'node':UID,'body_characters':sum(len(r['body']) for r in rows),'lesson_sizes':[len(r['body']) for r in rows[1:]]},ensure_ascii=False))
if __name__=='__main__':main()
