"""Import the supplied references and student handouts into the Hexo learning site.
Only content is imported; document prose is never executed as instructions.
"""
from pathlib import Path
import html, json, re, shutil, zipfile, hashlib, sys
import xml.etree.ElementTree as ET
from tex_content import mathify

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'source-openfoam'
DOCS = Path(r'E:\PKU\2024\MyPHD\LearningMaterials\OpenFoam\大纲')
COURSE = Path(r'F:\UbuntuShareFolder\OpenFOAM学习课程_28讲')
NS = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
      'm':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
W = '{'+NS['w']+'}'
esc = html.escape
def technical_text(t):
    replacements={
        'CFD 工作流全景':'CFD 工作流程', '盲跑':'运行',
        '把每一段落到实处':'说明各阶段的输入、输出及检查方法',
        '现场装一条':'选择一种方式完成安装与验证',
        '不解释参数先跑通':'先执行基准算例并记录输出，再分析参数含义',
        'ParaView 速成':'ParaView 基础操作',
        '算例目录解剖':'算例目录结构',
        '跑通':'成功执行', '重跑':'重新计算',
        '实战':'操作与验证', '避坑':'常见问题分析',
        '典型算例与物理分析':'典型算例与物理分析',
        '把它们当成':'将其视为', '多区域算例的救命工具':'适用于多区域算例',
        '一个查边界条件的万能方法':'边界条件查询方法',
        '“不报错但结果不对”（最危险的一类）':'无运行报错情况下的结果偏差',
        '第 1 章　先搞清楚：你装的是哪个 OpenFOAM':'第 1 章　OpenFOAM 分支与版本识别',
        '集群上最常见的两个坑':'集群运行中常见的两类环境问题',
        '它们占自定义编译错误的九成。':'应结合完整错误信息进一步检查头文件、链接配置与版本匹配。',
        '所以加密等级要精打细算，从低往高试。':'因此应逐级增加加密等级，并记录单元数与计算成本。',
        '跑 OpenFOAM 必备的 Linux 命令':'OpenFOAM 运行所需的 Linux 命令',
        '把某个单元的压力钉死在某个值':'指定参考单元的压力值',
        '保护神':'检查机制','救命':'排查', '万能':'通用',
    }
    for a,b in replacements.items():t=t.replace(a,b)
    paragraphs=[
      ('初学者踩的第一个坑','使用其他发行分支的教程可能产生配置不兼容。应先确认分支、版本及配套教程。常用发行分支可按下表区分。'),
      ('为什么 FOAM_SIGFPE 值得记住','FOAM_SIGFPE 用于启用浮点异常捕获。在运行环境支持的情况下，它可帮助定位除零、无效浮点运算等异常。异常位置仍需结合调用栈、初始场、边界条件及离散设置分析。'),
      ('几乎必踩的坑','STL 文件本身不保存统一的长度单位约定。若几何按毫米导出，而算例采用米，需要进行相应缩放。应使用 surfaceCheck 核对包围盒尺寸，确认几何尺度与物性及边界条件的单位体系一致。'),
      ('一个初学者必踩的坑','使用 ParaView 过滤器前，应检查输入数组是单元数据还是点数据。对需要点数据的操作，可根据过滤器要求使用 Cell Data to Point Data，或检查 OpenFOAM 读取器的相关转换选项。转换会引入插值，分析结果时应明确其数据位置。'),
      ('locationInMesh 是 snappy','locationInMesh 指定待保留流体区域内部的一个点。该点应位于目标连通区域内，并避开几何表面和网格面。坐标选择应依据几何尺寸和区域拓扑，不宜使用与模型尺度无关的固定偏移。'),
      ('Tab 补全是终端里','Tab 补全可减少命令和路径的拼写错误。输入名称前缀后按 Tab，查看当前 shell 提供的候选项；补全结果也可用于检查路径是否存在。'),
      ('三部分：错误类型','错误日志通常包含错误类型、具体说明以及相关文件或源码位置。FATAL IO ERROR 通常与文件读取或字典解析有关；FATAL ERROR 的原因范围更广。应保留完整错误上下文，依据具体说明定位，不能仅凭错误类别确定原因。'),
      ('为什么 default none','在相应格式字典中使用 default none，可要求相关项显式指定离散格式。缺失项会在运行时报告。应先确认方程项、变量及适用格式，再补充配置，避免仅根据名称机械复制。'),
      ('为什么用它而不是在 ParaView 里切','在求解或后处理阶段直接输出所需截面，可减少保存的场数据量。实际节省程度取决于网格规模、输出变量和时间采样频率；仍应保存满足后续验证需要的数据。'),
      ('为什么每一步都要 > log.xxx','重定向可保存标准输出与标准错误，便于记录运行过程和排查异常。2>&1 将标准错误合并到标准输出。foamLog 可从求解器日志提取残差数据；foamMonitor 可用于监视相应的数据文件。'),
    ]
    for prefix,value in paragraphs:
        if t.startswith(prefix):return value
    return t
def write(path, content):
    p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding='utf-8')
def text_of(el):
    out=[]
    for n in el.iter():
        if n.tag in [W+'t','{'+NS['m']+'}t']: out.append(n.text or '')
        elif n.tag==W+'br':out.append('\n')
        elif n.tag==W+'tab':out.append('    ')
    return ''.join(out)
def load_doc(path, image_prefix=None):
    blocks=[]
    with zipfile.ZipFile(path) as z:
        styles={}
        for s in ET.fromstring(z.read('word/styles.xml')).findall('w:style',NS):
            nm=s.find('w:name',NS)
            styles[s.get(W+'styleId')]=nm.get(W+'val','') if nm is not None else ''
        rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('word/_rels/document.xml.rels'))}
        body=ET.fromstring(z.read('word/document.xml')).find('w:body',NS)
        for el in body:
            if el.tag==W+'p':
                t=text_of(el); st=el.find('w:pPr/w:pStyle',NS)
                style=styles.get(st.get(W+'val'),'') if st is not None else ''
                fonts=[f.get(W+'ascii','') for f in el.findall('.//w:rFonts',NS)]
                code=style.lower() in ['code','source code'] or bool(fonts and sum(f in ['Consolas','Courier New'] for f in fonts)>len(fonts)*.45)
                # Mixed Word runs may mark a scientific paragraph as monospace.
                # Keep prose readable while preserving shell lines and code comments.
                if code and '\n' not in t and (len(re.findall(r'[\u4e00-\u9fff]',t))>=18 or t.startswith(('该式与mixed','Vexpected='))) and not re.match(r'^\s*(#|//|/\*|\*|\$|>)',t) and not re.search(r'[{};]|\s//',t):
                    code=False
                if t.strip():blocks.append({'type':'code' if code else 'p','style':style,'text':t})
                if image_prefix:
                    for b in el.findall('.//a:blip',NS):
                        target=rels.get(b.get('{'+NS['r']+'}embed'),'')
                        if target.startswith('media/') and Path(target).suffix.lower() in ['.png','.jpg','.jpeg','.gif']:
                            dest=SRC/'assets'/'lessons'/image_prefix/Path(target).name
                            dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read('word/'+target))
                            blocks.append({'type':'image','src':'/assets/lessons/'+image_prefix+'/'+Path(target).name})
            elif el.tag==W+'tbl':
                blocks.append({'type':'table','rows':[[text_of(c) for c in row.findall('w:tc',NS)] for row in el.findall('w:tr',NS)]})
    return blocks
def render(blocks, title_skip=False):
    out=[]; code=[]
    def flush():
        if code:out.append('<pre><code>'+esc('\n'.join(code))+'</code></pre>');code.clear()
    for b in blocks:
        if b['type']=='code':code.append(b['text']);continue
        flush()
        if b['type']=='p':
            if title_skip and (b['style'].lower()=='title' or re.match(r'^第\s*\d+\s*讲',b['text'])):continue
            heading=re.search(r'heading\s*(\d+)',b['style'],re.I)
            tag='h'+str(min(4,int(heading[1])+1)) if heading else 'p'
            out.append(f'<{tag}>'+mathify(technical_text(b['text']))+f'</{tag}>')
        elif b['type']=='table':
            rows=b['rows']; out.append('<div class="table-scroll"><table>')
            for i,row in enumerate(rows):
                tag='th' if i==0 else 'td'
                out.append('<tr>'+''.join(f'<{tag}>'+mathify(technical_text(c))+f'</{tag}>' for c in row)+'</tr>')
            out.append('</table></div>')
        elif b['type']=='image':out.append(f'<figure><img loading="lazy" src="{b["src"]}" alt="本讲配套算例图"><figcaption>配套学生讲义中的算例图</figcaption></figure>')
    flush();return '\n'.join(out)
def searchable(blocks):
    return ' '.join(technical_text(b.get('text','')) if b['type']!='table' else ' '.join(' '.join(row) for row in b['rows']) for b in blocks)
def page(slug,title,layout='page',content='',**meta):
    front={'title':title,'layout':layout,**meta}
    header='---\n'+'\n'.join(k+': '+json.dumps(v,ensure_ascii=False) for k,v in front.items())+'\n---\n'
    write('source-openfoam/'+slug+'/index.md' if slug else 'source-openfoam/index.md',header+('{% raw %}\n'+content+'\n{% endraw %}' if content else ''))

names=['OpenFOAM_v2512命令与配置参考手册（GPT整理）','OpenFOAM命令与文件大全_v2512（Claude整理）','OpenFOAM教学备课大纲_28讲_电极气泡','OpenFOAM教学课程大纲_电极气泡']
docs=[load_doc(DOCS/(n+'.docx')) for n in names]
outline=next(b['rows'] for b in docs[3] if b['type']=='table' and len(b['rows'])==36)
stages=[{'id':1,'name':'环境与首次上手','range':'01—04','description':'配置运行环境，执行算例并分析日志。','start':1,'end':4},
 {'id':2,'name':'典型算例与物理分析','range':'05—06','description':'比较两相流与绕流的模型设置和结果。','start':5,'end':6},
 {'id':3,'name':'网格生成与质量','range':'07—11','description':'学习结构网格、复杂几何与边界分区。','start':7,'end':11},
 {'id':4,'name':'数值方法与验证','range':'12—17','description':'理解离散、耦合与误差，验证静止气泡。','start':12,'end':17},
 {'id':5,'name':'并行与定量后处理','range':'18—19','description':'提高计算效率，提取可比较的气泡特征量。','start':18,'end':19},
 {'id':6,'name':'多相流与传质','range':'20—24','description':'理解 VOF、润湿、扩散与自定义边界。','start':20,'end':24},
 {'id':7,'name':'电极气泡与结课项目','range':'25—28','description':'建立守恒模型，研究生长与脱落。','start':25,'end':28}]
short=['环境与 Linux','方腔流动与 ParaView','算例目录与量纲','日志阅读与排错','溃坝与上升气泡','圆柱绕流','网格质量','blockMesh 与轴对称','snappyHexMesh 原理','snappyHexMesh 实战','网格转换与边界分区','有限体积与离散格式','时间步与线性求解器','压力速度耦合','残差与边界条件','格式误差实验','静止气泡与寄生流','并行计算','气泡特征量与后处理','VOF 与接触角','标量扩散与通量边界','稳态扩散与混合边界','源项与自适应加密','codeStream 与 coded 边界','自定义 myInterFoam','电极气泡的产气与生长','电势耦合与气泡脱落','结课项目与定量验证']
lessons=[];search=[];manifest=[]
for row in outline:
    if len(row)<6 or not row[0].isdigit():continue
    row=[technical_text(value) for value in row]
    n=int(row[0]);slug=f'lessons/{n:02d}';stage=next(s for s in stages if s['start']<=n<=s['end'])
    src=next((COURSE/'28课_学生版_Word讲义').glob(f'第{n:02d}*'))
    blocks=load_doc(src,f'{n:02d}')
    lesson={'id':n,'title':short[n-1],'fullTitle':row[1],'stage':stage['id'],'stageName':stage['name'],'url':'/'+slug+'/','summary':row[3].split('\n')[0].lstrip('①'),'topics':row[3],'homework':row[5],'duration':90}
    lessons.append(lesson)
    dest=SRC/'downloads'/f'lesson-{n:02d}.docx';dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
    course_dir=next(p for p in COURSE.iterdir() if p.is_dir() and p.name.startswith(f'{n:02d}_'))
    case_dir=course_dir/'代码'
    if case_dir.is_dir() and not ('--skip-cases' in sys.argv and (SRC/'downloads'/f'lesson-{n:02d}-cases.zip').exists()):
        with zipfile.ZipFile(SRC/'downloads'/f'lesson-{n:02d}-cases.zip','w',zipfile.ZIP_DEFLATED) as archive:
            for f in case_dir.rglob('*'):
                if not f.is_file():continue
                rel=f.relative_to(case_dir)
                if any(part in ['postProcessing','VTK','logs','.git','__pycache__','dynamicCode'] or part.startswith(('processor','linux64','platforms')) or (re.fullmatch(r'\d+(\.\d+)?',part) and part!='0') for part in rel.parts[:-1]):continue
                if f.name.startswith(('log.','core.')) or f.suffix in ['.foam','.o','.dep','.pyc','.so']:continue
                archive.write(f,'代码/'+rel.as_posix())
    content='<section class="lesson-intro"><h2>本讲学习任务</h2><p>'+mathify(technical_text(row[3]))+'</p></section>\n<p class="source-note">配套算例来自已有课程。下载解压后阅读其中的 README 与运行脚本，并在已加载 v2512 环境的 Linux 终端执行。本站未重新运行这些算例；原讲义中的本机路径需改为自己的实际路径。</p>\n'+render(blocks,True)
    content+='\n<section class="exercise"><h2>课后练习</h2><p>'+mathify(row[5])+'</p><a class="button secondary" href="/assignments/">前往作业区 →</a></section>'
    page(slug,short[n-1],'lesson',content,lesson_id=n,stage=stage['id'],description=lesson['summary'])
    search.append({'title':f'第 {n:02d} 讲 · '+short[n-1],'url':'/'+slug+'/','kind':'课程','text':searchable(blocks)})

commands=[]
for i,b in enumerate(docs[0]):
    if b['type']=='p' and b.get('style','').lower()=='heading 3':
        name=b['text'].split()[0]
        if not re.match(r'^[a-zA-Z][\w:+.-]*$',name):continue
        following=[]
        for nxt in docs[0][i+1:]:
            if nxt['type']=='p' and 'heading' in nxt.get('style','').lower():break
            following.append(nxt)
        text=searchable(following)
        example=next((x['text'].removeprefix('示例：') for x in following if x['type']=='code'),name+' -help')
        desc=next((x['text'] for x in following if x['type']=='p' and not x['text'].startswith('用法：')),'')
        category='前处理' if i<653 and i>=126 else '求解与并行' if i<925 and i>=653 else '后处理' if i<1088 and i>=925 else '系统工具'
        if i>=1088:continue
        commands.append({'name':name,'title':b['text'].removesuffix('源码').strip(),'description':desc,'example':example,'details':text,'category':category})

chapters=[]
for di,level in [(0,'heading 1'),(1,'heading 2')]:
    starts=[i for i,b in enumerate(docs[di]) if b['type']=='p' and b.get('style','').lower()==level and (re.match(r'^\d{2} ',b['text']) if di==0 else re.match(r'^第 \d+ 章',b['text']))]
    for j,start in enumerate(starts):
        end=starts[j+1] if j+1<len(starts) else len(docs[di])
        title=technical_text(docs[di][start]['text']);slug=f'reference/{"manual" if di==0 else "guide"}-{j+1:02d}'
        body=docs[di][start+1:end]
        notice='<p class="source-note">资料来源：'+esc(names[di])+'.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p>'
        page(slug,title,'reference',notice+render(body),description='OpenFOAM v2512 命令、文件与配置参考',manual=di+1)
        chapters.append({'title':title,'url':'/'+slug+'/','manual':di+1})
        search.append({'title':title,'url':'/'+slug+'/','kind':'参考手册','text':searchable(body)})

# Configuration records link file paths, keywords, consuming applications and source examples.
config_specs=[
 ('system/blockMeshDict','网格','blockMesh','vertices blocks edges boundary scale convertToMeters simpleGrading'),
 ('system/snappyHexMeshDict','网格','snappyHexMesh','castellatedMesh snap addLayers geometry refinementSurfaces refinementRegions locationInMesh nCellsBetweenLevels'),
 ('system/surfaceFeatureExtractDict','网格','surfaceFeatureExtract','extractionMethod extractFromSurfaceCoeffs includedAngle writeObj'),
 ('system/meshQualityDict','网格','checkMesh snappyHexMesh','maxNonOrtho maxBoundarySkewness maxInternalSkewness minVol minDeterminant'),
 ('system/setFieldsDict','初始化','setFields','defaultFieldValues regions boxToCell sphereToCell cylinderToCell fieldValues'),
 ('system/setExprFieldsDict','初始化','setExprFields','expressions field expression fieldMask dimensions create'),
 ('system/topoSetDict','网格','topoSet','actions name type action source sourceInfo cellSet faceSet cellZoneSet'),
 ('system/createPatchDict','网格','createPatch','pointSync patches name patchInfo constructFrom set'),
 ('system/createBafflesDict','网格','createBaffles','internalFacesOnly baffles faceZone zoneName master slave'),
 ('system/refineMeshDict','网格','refineMesh','set coordinateSystem globalCoeffs directions useHexTopology geometricCut'),
 ('system/extrudeMeshDict','网格','extrudeMesh','constructFrom sourceCase sourcePatches exposedPatchName extrudeModel nLayers expansionRatio thickness'),
 ('system/mapFieldsDict','初始化','mapFields mapFieldsPar','patchMap cuttingPatches'),
 ('system/changeDictionaryDict','初始化','changeDictionary','dictionaryReplacement boundaryField'),
 ('system/controlDict','计算控制','icoFoam interFoam simpleFoam','application startFrom startTime stopAt endTime deltaT writeControl writeInterval purgeWrite adjustTimeStep maxCo maxAlphaCo functions libs'),
 ('system/fvSchemes','数值方法','icoFoam interFoam simpleFoam','ddtSchemes gradSchemes divSchemes laplacianSchemes interpolationSchemes snGradSchemes fluxRequired wallDist'),
 ('system/fvSolution','数值方法','icoFoam interFoam simpleFoam','solvers solver tolerance relTol preconditioner smoother PISO PIMPLE SIMPLE nCorrectors nOuterCorrectors nNonOrthogonalCorrectors relaxationFactors residualControl pRefCell pRefValue'),
 ('system/decomposeParDict','并行计算','decomposePar redistributePar','numberOfSubdomains method scotch simpleCoeffs hierarchicalCoeffs regions constraints'),
 ('system/renumberMeshDict','网格','renumberMesh','renumberMethod CuthillMcKee'),
 ('constant/transportProperties','物理模型','icoFoam interFoam','transportModel nu rho phases sigma'),
 ('constant/turbulenceProperties','物理模型','simpleFoam pimpleFoam','simulationType laminar RAS LES RASModel turbulence printCoeffs'),
 ('constant/thermophysicalProperties','物理模型','rhoPimpleFoam chtMultiRegionFoam','thermoType type mixture transport thermo equationOfState specie energy'),
 ('constant/fvOptions','物理模型','simpleFoam pimpleFoam','type active selectionMode cellZone semiImplicitSource scalarSemiImplicitSource vectorSemiImplicitSource'),
 ('constant/MRFProperties','物理模型','simpleFoam pimpleFoam','cellZone active origin axis omega nonRotatingPatches'),
 ('constant/SRFProperties','物理模型','SRFSimpleFoam','SRFModel origin axis rpm'),
 ('constant/dynamicMeshDict','网格','interFoam pimpleFoam','dynamicFvMesh dynamicRefineFvMesh dynamicMotionSolverFvMesh motionSolver field lowerRefineLevel upperRefineLevel refineInterval maxRefinement maxCells'),
 ('constant/regionProperties','物理模型','chtMultiRegionFoam splitMeshRegions','regions fluid solid'),
 ('constant/radiationProperties','物理模型','buoyantSimpleFoam','radiation radiationModel absorptionEmissionModel scatterModel sootModel'),
 ('constant/g','物理模型','interFoam','dimensions value'),
 ('0/U','初始场','icoFoam interFoam','dimensions internalField boundaryField fixedValue noSlip movingWallVelocity flowRateInletVelocity'),
 ('0/p','初始场','icoFoam simpleFoam','dimensions internalField boundaryField fixedValue zeroGradient totalPressure'),
 ('0/p_rgh','初始场','interFoam','dimensions internalField boundaryField fixedFluxPressure prghPressure'),
 ('0/alpha.water','初始场','interFoam interIsoFoam setFields','dimensions internalField boundaryField inletOutlet constantAlphaContactAngle dynamicAlphaContactAngle theta0 limit'),
 ('0/T','初始场','laplacianFoam chtMultiRegionFoam','dimensions internalField boundaryField externalWallHeatFluxTemperature fixedValue zeroGradient'),
 ('0/k','初始场','simpleFoam pimpleFoam','dimensions internalField boundaryField kqRWallFunction turbulentIntensityKineticEnergyInlet'),
 ('0/epsilon','初始场','simpleFoam','dimensions internalField boundaryField epsilonWallFunction'),
 ('0/omega','初始场','simpleFoam','dimensions internalField boundaryField omegaWallFunction'),
 ('0/nut','初始场','simpleFoam','dimensions internalField boundaryField nutkWallFunction calculated'),
 ('0/alphat','初始场','buoyantSimpleFoam','dimensions internalField boundaryField compressible::alphatWallFunction'),
 ('Make/files','编译','wmake','EXE LIB FOAM_USER_APPBIN FOAM_USER_LIBBIN'),
 ('Make/options','编译','wmake','EXE_INC EXE_LIBS LIB_LIBS'),
 ('system/setAlphaFieldDict','初始化','setAlphaField','field surfaces plane sphere'),
 ('system/noiseDict','后处理','noise','noiseModel pointNoise surfaceNoise'),
 ('functions/probes','函数对象','postProcess','type probes libs fields probeLocations writeControl writeInterval'),
 ('functions/sets','函数对象','postProcess','type sets interpolationScheme setFormat fields sets axis start end nPoints'),
 ('functions/surfaces','函数对象','postProcess','type surfaces surfaceFormat fields surfaces cuttingPlane point normal'),
 ('functions/forces','函数对象','simpleFoam postProcess','type forces patches rho rhoInf CofR'),
 ('functions/forceCoeffs','函数对象','simpleFoam postProcess','type forceCoeffs patches liftDir dragDir pitchAxis magUInf lRef Aref'),
 ('functions/fieldAverage','函数对象','postProcess','type fieldAverage fields mean prime2Mean base'),
 ('functions/volFieldValue','函数对象','postProcess','type volFieldValue operation regionType fields'),
 ('functions/surfaceFieldValue','函数对象','postProcess','type surfaceFieldValue regionType name operation fields'),
 ('functions/residuals','函数对象','icoFoam simpleFoam','type residuals libs fields writeControl'),
 ('functions/yPlus','函数对象','simpleFoam postProcess','type yPlus libs executeControl writeControl'),
 ('functions/Q','函数对象','postProcess','type Q field result')
]
section_groups=[]
for di in range(2):
    sections=[i for i,b in enumerate(docs[di]) if b['type']=='p' and 'heading' in b.get('style','').lower()]
    for j,i in enumerate(sections):section_groups.append((di,docs[di][i]['text'],docs[di][i+1:sections[j+1] if j+1<len(sections) else len(docs[di])]))
dictionaries=[]
fallback={'0/U':'9.1','0/p':'9.1','0/p_rgh':'9.3','0/alpha.water':'9.3','0/T':'9.3','0/k':'9.4','0/epsilon':'9.4','0/omega':'9.4','0/nut':'9.4','0/alphat':'9.4','constant/g':'9.8','constant/regionProperties':'9.12','constant/radiationProperties':'9.12','Make/files':'9.14','Make/options':'9.14','functions/probes':'10.2','functions/sets':'10.3','functions/surfaces':'10.4','functions/forces':'10.5','functions/forceCoeffs':'10.5','functions/fieldAverage':'10.6','functions/volFieldValue':'10.6','functions/surfaceFieldValue':'10.6','functions/residuals':'10.6','functions/yPlus':'10.6','functions/Q':'10.6'}
for filepath,group,related,keys in config_specs:
    name=filepath.split('/')[-1]
    candidates=[(di,t,b) for di,t,b in section_groups if ((name in t and (len(name)>2 or filepath in t)) or (di==0 and filepath in fallback and t.startswith(fallback[filepath]+' ')))]
    if not candidates:
        candidates=[(di,t,b) for di,t,b in section_groups if di==0 and (t.startswith('9.12 ') if group=='物理模型' else t.startswith('10.6 '))]
    # Keep the detailed source section and a complementary section from the other manual.
    candidates=sorted(candidates,key=lambda x:x[0])[:3]
    chunks=[]
    for di,t,b in candidates:
        chunks.append('<h2>'+esc(technical_text(t))+'</h2>'+render(b))
    description=next((technical_text(b['text']) for _,_,blocks in candidates for b in blocks if b['type']=='p' and 'heading' not in b.get('style','').lower()),'按所用求解器和算例配置对应条目。')
    slug='dictionaries/'+re.sub(r'[^a-z0-9]+','-',filepath.lower()).strip('-')
    actualpath='system/controlDict → functions → '+name if filepath.startswith('functions/') else filepath
    record={'name':name,'path':actualpath,'group':group,'description':description,'keys':keys.split(),'commands':related.split(),'url':'/'+slug+'/','searchText':searchable([b for _,_,blocks in candidates for b in blocks])}
    dictionaries.append(record)
    intro='<p class="source-note">配置位置：<code>'+esc(actualpath)+'</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p>'
    keyhtml='<h2>关键条目索引</h2><p>'+ ' · '.join('<code>'+esc(k)+'</code>' for k in keys.split())+'</p>'
    cmdhtml='<h2>关联命令</h2><p>'+' · '.join('<a href="/commands/?q='+esc(c)+'">'+esc(c)+'</a>' for c in related.split())+'</p>'
    query='cat '+filepath if filepath.startswith('Make/') else ('foamDictionary system/controlDict -entry functions -value' if filepath.startswith('functions/') else 'foamDictionary '+filepath+' -keywords')
    cmdhtml+='<h2>本机核对</h2><pre><code>'+esc('foamVersion\n'+query+'\n'+related.split()[0]+' -help')+'</code></pre>'
    page(slug,actualpath,'reference',intro+keyhtml+cmdhtml+'\n'.join(chunks),description=description[:150],dictionary=True)
    search.append({'title':actualpath,'url':'/'+slug+'/','kind':'配置文件','text':keys+' '+related+' '+description+' '+searchable([b for _,_,blocks in candidates for b in blocks])})

# Environment helpers, compiler tools and shell operations complement the application index.
extras=[
 ('foamVersion','环境与编译','显示当前 OpenFOAM 环境版本。','foamVersion'),
 ('wmake','环境与编译','编译应用程序或用户库，读取 Make/files 与 Make/options。','wmake'),
 ('wclean','环境与编译','清理当前应用的构建产物；执行前确认工作目录。','wclean'),
 ('Allwmake','环境与编译','项目提供的批量编译脚本；需先阅读脚本和构建说明。','./Allwmake'),
 ('Allrun','环境与编译','算例提供的运行脚本，具体执行步骤由该文件定义。','./Allrun'),
 ('Allclean','环境与编译','算例提供的清理脚本，执行前检查其删除范围。','less Allclean'),
 ('tut','环境与编译','加载环境后可用的教程目录别名。','tut'),
 ('run','环境与编译','加载环境后切换到用户运行目录的别名。','run'),
 ('sol','环境与编译','加载环境后切换到求解器源码目录的别名。','sol'),
 ('foam','环境与编译','加载环境后切换到 OpenFOAM 安装根目录。','foam'),
 ('src','环境与编译','加载环境后切换到库源码目录的别名。','src'),
 ('foamExec','环境与编译','使用安装目录中提供的环境包装脚本运行应用。','"$WM_PROJECT_DIR/bin/tools/foamExec" icoFoam -help'),
 ('source','Linux','在当前 Bash 进程中执行环境脚本。','source /usr/lib/openfoam/openfoam2512/etc/bashrc'),
 ('pwd','Linux','显示当前工作目录。','pwd'),('ls','Linux','列出文件与目录。','ls -lh 0 constant system'),
 ('cd','Linux','切换工作目录；含空格的路径使用引号。','cd "$FOAM_RUN"'),
 ('mkdir','Linux','创建工作目录。','mkdir -p "$FOAM_RUN"'),('cp','Linux','复制算例与配置文件。','cp -r cavity cavity-copy'),
 ('mv','Linux','移动或重命名文件；检查目标是否已存在。','mv log.icoFoam log.icoFoam.previous'),
 ('rm','Linux','删除文件；删除前逐项核对路径，删除通常无法撤销。','rm -i ./unneeded.txt'),
 ('cat','Linux','查看短文本文件。','cat system/controlDict'),('less','Linux','分页阅读配置与日志。','less log.interFoam'),
 ('head','Linux','查看文件开头。','head -n 20 log.interFoam'),('tail','Linux','查看或持续监视日志末尾。','tail -f log.interFoam'),
 ('grep','Linux','按文本模式检索文件。','grep -n "Courant Number" log.interFoam'),
 ('find','Linux','按路径和文件名查找文件。','find "$FOAM_TUTORIALS" -name controlDict'),
 ('diff','Linux','对比两份字典或日志。','diff -u system/fvSchemes ../caseB/system/fvSchemes'),
 ('du','Linux','检查算例或结果目录的存储占用。','du -sh .'),('df','Linux','检查文件系统可用空间。','df -h .'),
 ('ps','Linux','查看当前用户的进程。','ps -u "$USER"'),('top','Linux','交互查看计算资源占用。','top'),
 ('nohup','Linux','使程序忽略挂断信号并重定向日志。','nohup interFoam > log.interFoam 2>&1 &'),
 ('tmux','Linux','创建可分离终端会话；需安装 tmux。','tmux new -s openfoam'),
 ('ssh','Linux','连接计算服务器。','ssh username@hostname'),('scp','Linux','通过 SSH 复制文件，替换账号与主机名后使用。','scp report.pdf username@hostname:~/'),
 ('tar','Linux','打包算例目录。','tar -czf case.tar.gz case/'),('chmod','Linux','设置脚本执行权限。','chmod u+x Allrun'),
 ('command','Linux','查询外部程序的实际位置。','command -v interFoam'),('type','Linux','识别命令是别名、函数还是程序文件。','type foamVersion'),
 ('echo','Linux','显示环境变量或简单文本。','echo "$WM_PROJECT_VERSION"')
]
for name,category,desc,example in extras:
    if any(c['name']==name for c in commands):continue
    commands.append({'name':name,'title':name,'description':desc,'example':example,'details':desc+' 示例中的算例名、路径与主机名须按实际环境替换。','category':category})
from urllib.parse import quote
for c in commands:
    c['configs']=[{'name':d['name'],'url':d['url']} for d in dictionaries if c['name'] in d['commands']]
    search.append({'title':c['name'],'url':'/commands/?q='+quote(c['name']),'kind':'命令','text':c['title']+' '+c['description']+' '+c['details']+' '+c['example']})

for i,name in enumerate(names):
    src=DOCS/(name+'.docx');dest=SRC/'downloads'/f'reference-{i+1}.docx';shutil.copy2(src,dest)
    manifest.append({'name':name,'url':f'/downloads/reference-{i+1}.docx','bytes':src.stat().st_size,'sha256':hashlib.sha256(src.read_bytes()).hexdigest()})

site={'lessons':lessons,'stages':stages,'commands':commands,'chapters':chapters,'documents':manifest,'dictionaries':dictionaries}
write('source-openfoam/_data/learning.json',json.dumps(site,ensure_ascii=False,indent=2))
write('source-openfoam/assets/search.json',json.dumps(search,ensure_ascii=False))
write('source-openfoam/assets/commands.json',json.dumps(commands,ensure_ascii=False))
write('source-openfoam/assets/dictionaries.json',json.dumps(dictionaries,ensure_ascii=False))
write('source-openfoam/assets/assignment-templates.json',json.dumps([{'lesson':l['id'],'title':f'第 {l["id"]:02d} 讲 · '+l['title'],'body':l['homework']} for l in lessons],ensure_ascii=False,indent=2))
for slug,title,layout in [('', '学习概览','home'),('courses','28 讲学习路径','courses'),('commands','命令速查','commands'),('dictionaries','配置文件与 Dict 索引','dictionaries'),('reference','配置与参考手册','library'),('resources','学习资料','resources'),('assignments','作业中心','workspace'),('announcements','课程公告','workspace'),('community','提问与答疑','workspace')]:page(slug,title,layout,section=slug)
print(json.dumps({'lessons':len(lessons),'commands':len(commands),'dictionaries':len(dictionaries),'reference_chapters':len(chapters),'original_documents':len(manifest)},ensure_ascii=False))
