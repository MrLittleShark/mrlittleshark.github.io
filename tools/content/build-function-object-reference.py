"""Build independent, per-type reference articles from reviewed v2512 data."""
from pathlib import Path
import html,json,re,textwrap,urllib.parse
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).parent/'function-object-reference'
SRC=ROOT/'source-openfoam'
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
profiles=load(HERE/'profiles.json');docs=load(HERE/'source-reference.json')
notes=dict(line.split('|',1) for line in (HERE/'parameter-notes.txt').read_text(encoding='utf-8').splitlines() if '|' in line)
sections=load(HERE/'categories.json')
section_ids={x['name']:x['id'] for x in sections}
def esc(s):return html.escape(str(s),quote=True)
def p(s):return '<p>'+esc(s)+'</p>'
def code(s,lang='foam'):return '<pre><code class="language-'+lang+'">'+esc(s.strip())+'</code></pre>'
def table(head,rows):return '<div class="table-scroll"><table><thead><tr>'+''.join('<th>'+esc(x)+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>'
def ident(s):return '<code>'+esc(s)+'</code>'
def link(url,title):return '<a href="'+esc(url)+'">'+esc(title)+'</a>'
def parse_top(text):
    # Token positions avoid matching a similarly named key inside a child dict.
    tokens=list(re.finditer(r'"(?:\\.|[^"\\])*"|\#\{[\s\S]*?\#\}|[{}();]|[^\s{}();]+',text));depth=0;items={};i=0
    while i<len(tokens):
        t=tokens[i].group()
        if t=='{':depth+=1
        elif t=='}':depth-=1
        elif depth==1 and t not in (';',')','('):
            key=t;start=tokens[i].start();j=i+1;sub=0
            while j<len(tokens):
                v=tokens[j].group()
                if v in ('{','('):sub+=1
                elif v in ('}',')'):
                    sub-=1
                    if sub==0 and v=='}':
                        j+=1
                        if j<len(tokens) and tokens[j].group()==';':j+=1
                        break
                elif v==';' and sub==0:j+=1;break
                j+=1
            if j>i+1:items[key]=(start,tokens[j-1].end());i=j-1
        i+=1
    return items
def modify(text,updates):
    for k,v in updates.items():
        spans=parse_top(text)
        replacement=k+' '+v+('' if v.strip().startswith('{') else ';')
        if k in spans:
            a,b=spans[k];text=text[:a]+replacement+text[b:]
        else:text=text.rstrip()[:-1].rstrip()+'\n    '+replacement+'\n}'
    return text
def clean_defaults(text):
    # Tutorial examples sometimes disable a schedule with -1. Use one active
    # write per selected event in these introductory reference configurations.
    return re.sub(r'\b(writeInterval|executeInterval)\s+-1;',r'\1 1;',text)
COMMON=[
 ('enabled','true / false','true','是否启用当前对象。'),
 ('executeControl','timeStep、writeTime、runTime、onEnd、none','timeStep','计算或更新数据的时机。'),
 ('executeInterval','正数','1','执行间隔；timeStep 按步数，runTime 按模拟时间。'),
 ('writeControl','timeStep、writeTime、runTime、onEnd、none','timeStep','保存结果的时机，与执行阶段分别控制。'),
 ('writeInterval','正数','1','写出间隔；writeTime 下表示每几次主输出保存一次。'),
 ('timeStart','模拟时间','0','开始执行当前对象的时间。'),
 ('timeEnd','模拟时间','运行结束','结束执行当前对象的时间。'),
]
OVERRIDE={
 ('norm','p'):'Lp 范数的指数，仅在 norm Lp 时填写。',
 ('stabilityBlendingFactor','D'):'PID 控制中的微分系数。',
 ('stabilityBlendingFactor','tolerance'):'判断混合单元数量变化的容差。',
 ('thermoCoupleProbes','rho'):'热电偶材料密度，单位 kg/m³。',
 ('thermoCoupleProbes','epsilon'):'热电偶表面的发射率。',
 ('bladeForces','n'):'旋转速度，单位转/秒；rpm 使用转/分钟。',
 ('propellerInfo','n'):'旋转速度，单位转/秒。',
 ('setFlow','omega'):'角速度的 Function1 函数，通常以 rad/s 设置。',
 ('graphFunctionObject','width'):'SVG 图像宽度，单位像素。',
 ('fieldAverage','fields'):'每个字段的平均设置列表；内部填写 mean、prime2Mean 和 base。',
 ('surfaceInterpolate','fields'):'输入、输出字段名称对，例如 ((U Uf) (p pf))。',
 ('nearWallFields','fields'):'输入、输出字段名称对，例如 ((U UNear))。',
 ('volFieldValue','regionType'):'all 选择全域，cellZone 选择命名单元区。',
 ('surfaceFieldValue','regionType'):'patch、faceZone、sampledSurface 等表面选择方式。',
 ('volFieldValue','name'):'regionType cellZone 时的单元区域名称。',
 ('surfaceFieldValue','name'):'所选 patch 或 faceZone 的名称。',
 ('fieldStatistics','mean'):'volumetric 采用单元体积权重；arithmetic 采用算术平均。',
 ('fieldStatistics','mode'):'component 逐分量统计，magnitude 按向量或张量的模统计。',
 ('fieldStatistics','internal'):'true 仅统计内部单元；false 同时处理边界场。',
 ('fieldMinMax','mode'):'magnitude 按模比较，component 按分量比较。',
 ('streamLine','direction'):'forward 向下游，backward 向上游，bidirectional 双向追踪。',
 ('wallBoundedStreamLine','direction'):'forward 向下游，backward 向上游，bidirectional 双向追踪。',
 ('interfaceHeight','direction'):'积分方向向量，结合重力方向和所定义的液相选择。',
 ('wallHeatFlux','model'):'wall 计算壁面热流；gauge 模拟指定温度的热流计。',
 ('wallHeatFlux','writeFields'):'gauge 模式下是否保存 qConv 和 qRad。',
 ('writeObjects','writeOption'):'anyWrite、autoWrite、noWrite 控制写出筛选；log 用于列出匹配对象。',
 ('writeDictionary','libs'):'加载 utilityFunctionObjects 库。',
 ('fieldExtents','internalField'):'是否把内部单元纳入范围统计。',
 ('comfort','tolerance'):'衣服表面温度迭代的收敛容差。',
 ('externalCoupled','regions'):'区域与耦合边界组子字典，内部指定交换的字段。',
}
EXTRA={
 'fieldCoordinateSystemTransform':[('fields','输入场列表','必填','—'),('coordinateSystem','坐标系子字典','必填','—')],
 'fieldAverage':[('fields.<场名>.mean','是否计算平均场','必填','true / false'),('fields.<场名>.prime2Mean','是否计算二阶脉动矩','必填','true / false'),('fields.<场名>.base','time 按时间加权，iteration 按样本数统计','必填','time / iteration'),('fields.<场名>.window','该字段的平均窗口长度','可选','累计整个统计时段')],
 'thermoCoupleProbes':[('probeLocations','热电偶测点坐标列表','必填','—'),('fields','采样字段，通常为 (T)','必填','—'),('solver','温度响应所用的常微分方程求解器','必填','如 rodas23'),('absTol','常微分方程绝对容差','可选','由求解设置决定'),('relTol','常微分方程相对容差','可选','由求解设置决定')],
 'heatTransferCoeff':[('TRef','fixedReferenceTemperature 模型的参考温度，单位 K','条件必填','—')],
 'reactingEulerHtcModel':[('TRef','fixedReferenceTemperature 模型的参考温度，单位 K','条件必填','—')],
 'multiphaseInterHtcModel':[('TRef','fixedReferenceTemperature 模型的参考温度，单位 K','条件必填','—')],
 'binField':[('binData.nBin','分箱数量','必填','—'),('binData.direction','singleDirectionUniformBin 的分箱方向','必填','—'),('binData.cumulative','是否输出累计和','可选','false')],
 'reference':[('position','refValue sample 模式的空间采样位置','条件必填','—')],
 'volFieldValue':[('name','cellZone 的区域名称','条件必填','—'),('writeFields','是否写出所选原始场','必填','true / false')],
 'surfaceFieldValue':[('writeFields','是否保存表面采样原始值','必填','true / false'),('direction','sumDirection 等操作的参考方向','条件必填','—')],
 'electricPotential':[('phases','多相电导率和介电常数子字典，按相分数场命名','多相时使用','—')],
 'resolutionIndex':[('result','解析指标的输出场名','可选','模型名称'),('U','PopeIndex 使用的瞬时速度','可选','U'),('UMean','PopeIndex 使用的平均速度','可选','UMean'),('k','亚网格湍动能场','可选','k'),('delta','LES 滤波尺度场','可选','delta'),('nu','Celik 模型使用的运动黏度','可选','nu'),('nut','Celik 模型使用的亚网格黏度','可选','nut')],
}
def param_rows(name,profile):
    spec=list(docs[name]['parameters'])
    if name=='forceCoeffs':spec+=docs['forces']['parameters'][2:]
    if name in ('streamLine','wallBoundedStreamLine'):
        spec=[(['lifeTime']+r[1:]) if r[0]=='lifetime' else r for r in spec]
        notes['lifeTime']=notes['lifetime']
    if name=='viewFactorHeatFlux':spec=[r for r in spec if r[0] not in ('F','globalFaceFaces')]
    rows=[];seen=set();lib=re.search(r'\blibs\s+\(([^)]+)\)',profile['code']).group(1)
    for r in spec:
        key=r[0]
        if key in seen:continue
        seen.add(key)
        default=r[-1] if len(r)>=4 else '—'
        req=r[-2] if len(r)>=4 else 'no'
        condition='必填' if req in ('yes','expected') else '条件必填' if req not in ('no','-','recommended') else '可选'
        default={'-':'—','':'—','none':'none','all wall patches':'所有 wall 类型边界','calculated':'自动计算','dict name':'子字典名称','same as IOstream':'采用全局写出精度','empty dict':'空字典','empty-dict':'空字典','postProcessing/NAME':'postProcessing/对象名'}.get(default,default)
        meaning=OVERRIDE.get((name,key),notes.get(key))
        assert meaning,(name,key)
        if key=='type':default=name;condition='必填'
        if key=='libs':default='('+lib+')';condition='必填'
        if name=='cloudInfo' and key=='clouds':condition='必填';default='—'
        if name=='wallHeatFlux' and key in ('patch','Tgauge','absorptivity','emissivity','T','qin','alphat','convective','radiative','writeFields'):
            meaning='gauge 模型：'+meaning;condition='gauge 中必填' if key in ('patch','Tgauge') else 'gauge 中可选'
        if name=='wallHeatFlux' and key in ('patches','qr'):meaning='wall 模型：'+meaning
        if name=='graphFunctionObject' and key in ('object','entry','colour','dashes','title'):key='functions.<曲线名>.'+key
        if name=='regionSizeDistribution' and key in ('origin','direction','maxD','nDownstreamBins','maxDownstream'):condition='isoPlanes 为 true 时'
        rows.append([ident(key),esc(meaning),esc(condition),ident(default)])
    if 'fieldExpression.H' in docs[name]['doc']:
        for key,default in [('field','U' if name in ('vorticity','Q','Lambda2','enstrophy','LambVector','flowType','MachNo') else '按输入填写'),('result','工具默认名称'),('cellZones','全域')]:
            if key not in seen:rows.append([ident(key),esc(notes[key]),'可选' if key!='field' or default=='U' else '必填',ident(default)]);seen.add(key)
    if 'writeFile.H' in docs[name]['doc'] or name=='forceCoeffs':
        for key,meaning,default in [('writeToFile','是否保存统计文本文件','true'),('writePrecision','文本数值的有效位数','全局写出精度'),('useUserTime','是否采用用户时间单位','true')]:
            if key not in seen:rows.append([ident(key),esc(meaning),'可选',ident(default)])
    for key,meaning,condition,default in EXTRA.get(name,[]):
        if key not in seen:rows.append([ident(key),esc(meaning),esc(condition),ident(default)])
    return rows
records=[];manifest=[]
for order,(name,profile) in enumerate(profiles.items()):
    slug=name.lower();url='/function-objects/'+slug+'/'
    base=clean_defaults(profile['code'])
    assert base and profile['explanation'],name
    variants=list(profile['variants'])
    if not variants:
        variants=[dict(title='每个时间步保存结果',patch={'writeControl':'timeStep','writeInterval':'1'},explanation='将该诊断量与每一步的求解状态对应，适合观察启动过程或快速变化。'),dict(title='随主结果保存',patch={'writeControl':'writeTime','writeInterval':'1'},explanation='与 controlDict 中的完整场输出使用相同时刻，便于在 ParaView 中组合查看。')]
    variants=variants[:2]
    variants+=[dict(title='每十步保存一次',patch={'writeControl':'timeStep','writeInterval':'10'},explanation='执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。'),dict(title='只处理指定时间段',patch={'timeStart':'0.1','timeEnd':'0.5'},explanation='本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。')]
    # Avoid repeated configurations for parameterless diagnostic tools.
    if not profile['variants']:
        variants[2]=dict(title='每二十步保存一次',patch={'writeControl':'timeStep','writeInterval':'20'},explanation='较低的保存频率适合变化缓慢的诊断量，可减少结果目录数量。')
    variants+=[dict(title='每五步保存一次',patch={'writeControl':'timeStep','writeInterval':'5'},explanation='采用五步间隔，在时间分辨率与数据量之间选择适合当前计算的输出频率。'),dict(title='限制到后半段时间',patch={'timeStart':'0.2','timeEnd':'0.5'},explanation='把对象工作区间设为模拟时间 0.2 到 0.5，集中记录这一阶段的数据。')]
    selected=[dict(title='基本配置',code=base,explanation=profile['explanation'])]
    for v in variants:
        v=dict(v,code=modify(base,v['patch']))
        if v['code'] not in {x['code'] for x in selected}:selected.append(v)
        if len(selected)==5:break
    variants=selected
    assert len(variants)==5,(name,'insufficient variants')
    body=p(profile['description'])
    body+='<h2 id="usage">配置方法</h2>'
    body+=p('将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。')
    body+=code('functions\n{\n'+textwrap.indent(base,'    ')+'\n}')
    body+=p(profile['explanation'])
    origin=str(profile['origin'])
    if origin.startswith(('01-','02-','03-','04-','05-')):
        labels={'01-cavity':'顶盖驱动方腔','02-pitzDaily':'后台阶湍流','03-hotRoom':'浮力传热房间','04-damBreak':'溃坝两相流','05-autoStop':'按条件停止的方腔'}
        body+=p('示例算例：'+labels[origin]+'。')
    elif '/' in origin:
        body+='<p>配套教程配置：'+ident(origin)+'。</p>'
    body+='<p>完整的配置放置与运行方法见 '+link('/function-objects/usage/','functionObject 配置说明')+'。</p>'
    body+='<h2 id="parameters">参数说明</h2>'+table(['参数','含义与设置','填写条件','默认值 / 示例'],param_rows(name,profile))
    body+='<h3 id="scheduling">执行与保存</h3>'+table(['参数','可设置的值','默认','作用'],[[ident(a),esc(b),ident(c),esc(e)] for a,b,c,e in COMMON])
    if name=='surfaceFieldValue':
        body+='<h3 id="operations">常用统计操作</h3>'+table(['operation','计算内容'],[[ident(a),esc(b)] for a,b in [('sum','求和；用于 phi 时得到面通量总和'),('average','各面值的算术平均'),('areaAverage','按面面积加权平均'),('areaIntegrate','将场值乘面积后求和'),('areaNormalAverage','向法向投影后进行面积平均'),('areaNormalIntegrate','向法向投影后进行面积积分'),('weightedAreaAverage','同时采用面积和 weightField 加权'),('min / max','所选面上的最小值 / 最大值'),('CoV','变异系数'),('uniformity','均匀性指标')]])
    if name=='volFieldValue':body+='<h3 id="operations">常用统计操作</h3>'+table(['operation','计算内容'],[[ident(a),esc(b)] for a,b in [('sum','单元值之和'),('average','单元值的算术平均'),('volAverage','按单元体积加权平均'),('volIntegrate','单元值与体积相乘后求和'),('weightedVolAverage','体积与 weightField 共同加权'),('min / max','最小值 / 最大值'),('CoV','变异系数')]])
    body+='<h2 id="examples">配置示例</h2>'+p('以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。')
    for i,v in enumerate(variants,1):
        body+='<h3 id="example-'+str(i)+'">示例 '+str(i)+' · '+esc(v['title'])+'</h3>'+p(v['explanation'])
        if i==1:body+=code(v['code'])
        else:
            patch='\n'.join(k+' '+value+('' if value.strip().startswith('{') else ';') for k,value in v['patch'].items())
            body+=p('在该对象内修改以下条目：')+code(patch)
            body+='<details><summary>完整配置</summary>'+code(v['code'])+'</details>'
        manifest.append(dict(name=name,example=i,code=v['code'],origin=origin,tested_base=profile['tested']))
    body+='<h2 id="related">相关工具</h2><p>'+link('/function-objects/?category='+urllib.parse.quote(profile['category']),profile['category']+'速查')+' · '+link('/function-objects/','全部 functionObject')+'</p>'
    body+='<p>延伸阅读：'+link(profile['lesson'],'专题课程')+'。</p>'
    source='https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/'+profile['source']
    body+='<p class="source-note">参考：'+link(source,'OpenFOAM v2512 · '+name+' 接口')+'。</p>'
    page=SRC/url.strip('/')/'index.md';page.parent.mkdir(parents=True,exist_ok=True)
    front={'title':name,'layout':'reference','section':'function-objects','cms_slug':'function-object-'+slug,'description':profile['description']}
    page_text='---\n'+''.join(k+': '+json.dumps(v,ensure_ascii=False)+'\n' for k,v in front.items())+'---\n{% raw %}\n'+body+'\n{% endraw %}\n'
    page.write_text(re.sub(r'[ \t]+\n','\n',page_text),encoding='utf-8')
    records.append(dict(slug='function-object-'+slug,kind='reference',title=name,summary=profile['description'],body=body,track='functionObject 速查',series=profile['category'],status='published',sort_order=order,section_ids=[section_ids[profile['category']]],metadata=dict(format='html',canonical_path=url,version='v2512',source_url=source,reference_type='functionObject',group=profile['category'])))
(Path(__file__).parent/'function-object-reference-content.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=ROOT/'.openfoam-work/function-object-reference';out.mkdir(exist_ok=True)
(out/'examples.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Independent reference pages:',len(records),'configuration examples:',len(manifest))
