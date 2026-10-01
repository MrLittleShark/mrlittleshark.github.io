"""Build the pinned v2512 reference from official sources and captured guest help.

Requires the locally retained official source tarball and commands-runtime.json.
Does not execute OpenFOAM commands or modify tutorial cases. Existing teaching
text is backed up once and retained; generated additions are repeatable.
"""
from __future__ import annotations
import hashlib
import html
import json
import pathlib
import re
import tarfile
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / 'source-openfoam'
WORK = ROOT / '.openfoam-work/replan'
BACKUP = WORK / 'reference-originals'
BACKUP.mkdir(exist_ok=True)
TAG = 'OpenFOAM-v2512'
GIT = 'https://gitlab.com/openfoam/core/openfoam/-/blob/' + TAG + '/'
TREE = 'https://gitlab.com/openfoam/core/openfoam/-/tree/' + TAG + '/'

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def original(path):
    backup = BACKUP / path.relative_to(SRC)
    if not backup.exists():
        backup.parent.mkdir(parents=True, exist_ok=True)
        backup.write_bytes(path.read_bytes())
    return backup.read_text(encoding='utf-8')

def esc(s):
    # Dollar signs in source descriptions are shell syntax, never inline TeX.
    # Character references bypass the Markdown math recognizer and are restored
    # by the HTML parser, including within highlighted code blocks.
    return html.escape(str(s), quote=True).replace('$','&#36;')

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def code(s, lang='openfoam'):
    return '<pre><code class="language-' + lang + '">' + esc(s.rstrip()) + '</code></pre>'

def classify_retained_code(match):
    raw=match.group(1)
    plain=html.unescape(raw)
    if re.search(r'(?m)^(?:foam\w+|\w+Foam|postProcess|blockMesh|checkMesh|source|cd|cp|mpirun|wmake|printf)\b',plain):
        lang='bash'
    elif re.search(r'\b(?:fvm::|fvc::|fvCFD.H|forAll\()',plain):
        lang='cpp'
    elif re.search(r'\b(?:EXE_INC|EXE_LIBS|LIB_LIBS)\b',plain):
        lang='makefile'
    else:
        lang='openfoam'
    return '<pre><code class="language-'+lang+'">'+raw+'</code></pre>'

def link(url, text):
    return '<a href="' + esc(url) + '">' + esc(text) + '</a>'

def paragraph(text):
    return '<p>' + esc(text) + '</p>'

def table(headers, rows):
    return '<div class="table-scroll"><table><thead><tr>' + ''.join('<th>'+esc(x)+'</th>' for x in headers) + '</tr></thead><tbody>' + ''.join('<tr>'+''.join('<td>'+esc(x)+'</td>' for x in row)+'</tr>' for row in rows) + '</tbody></table></div>'

def write_page(path, title, desc, body, dictionary=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    front = '---\ntitle: ' + json.dumps(title, ensure_ascii=False) + '\nlayout: reference\ndescription: ' + json.dumps(desc[:240], ensure_ascii=False) + '\n'
    if dictionary:
        front += 'dictionary: true\n'
    path.write_text(front + '---\n{% raw %}\n' + body + '\n{% endraw %}\n', encoding='utf-8')

notes = load(ROOT / 'tools/reference-notes.json')
inventory = load(WORK / 'v2512-source-inventory.json')
runtime_path = pathlib.Path(r'F:\UbuntuShareFolder\.foamlab-build\commands-runtime.json')
runtime = {x['name']: x for x in load(runtime_path)}
tools_runtime_path = runtime_path.with_name('commands-tools-runtime.json')
if tools_runtime_path.exists() and tools_runtime_path.stat().st_size:
    runtime.update({x['name']: x for x in load(tools_runtime_path)})
old_commands = json.loads(original(SRC / 'assets/commands.json'))
old_dicts = json.loads(original(SRC / 'assets/dictionaries.json'))
legacy_dictionary_names = {item['name'] for item in old_dicts}
tar = tarfile.open(WORK / 'openfoam-v2512.tar.gz')
members = tar.getmembers()
prefix = members[0].name.split('/')[0] + '/'
entries = {m.name[len(prefix):]: m for m in members if m.isfile()}
cache = {}

# Read selected text members in archive order. Repeated backward seeks in a
# gzip archive otherwise decompress the same source tree thousands of times.
for _path, _member in entries.items():
    if _member.size <= 300000 and _path.startswith(('tutorials/', 'applications/', 'bin/', 'etc/', 'wmake/')):
        try:
            _raw = tar.extractfile(_member).read()
            if b'\x00' not in _raw:
                cache[_path] = _raw.decode('utf-8')
        except UnicodeDecodeError:
            pass

def read(path):
    if path not in cache:
        try:
            cache[path] = tar.extractfile(entries[path]).read().decode('utf-8')
        except (KeyError, UnicodeDecodeError):
            cache[path] = ''
    return cache[path]

def desc_from_source(source):
    text = source
    if text.startswith('#!'):
        header=[]
        for line in text.splitlines()[1:]:
            if line.strip() and not line.startswith('#'):
                break
            header.append(re.sub(r'^# ?', '', line))
        text='\n'.join(header)
    match = re.search(r'\nDescription\s*\n(.*?)(?:\n(?:Environment|See also|Note|Notes|SourceFiles|Author|Usage)\b|\n\\\*|\n-{10}|\\heading)', text, re.S)
    if not match:
        return ''
    desc = match.group(1).strip()
    if desc.startswith('-----'):
        return ''
    # Keep the prose. Doxygen equations/macros are not silently converted to TeX.
    desc = re.split(r'\\(?:f\[|f\$|verbatim|vartable|plaintable)', desc)[0]
    return re.sub(r'\s+', ' ', desc).strip()

def primary_source(target):
    base = str(pathlib.PurePosixPath(target['source']).parent.parent)
    make = read(target['source'])
    files = re.findall(r'^([^/#\s][^\n]*\.C)\s*$', make, re.M)
    for f in files:
        path = base + '/' + f
        if read(path):
            return path
    same = base + '/' + target['name'] + '.C'
    return same if read(same) else target['source']

def source_help(path, name):
    source = read(path)
    chunks = []
    for m in re.finditer(r'<<-?\s*[\'\"]?((?:HELP|USAGE)[A-Z_0-9]*)[\'\"]?[^\n]*\n(.*?)\n\s*\1\b', source, re.S):
        chunks.append(m.group(2).replace('$Script', name).replace('${0##*/}', name))
    return '\n\n'.join(chunks).strip()

def tutorial_case(path):
    parts = path.split('/')
    for i, part in enumerate(parts):
        if part in ('system', 'constant', '0', '0.orig', '0.org'):
            return '/'.join(parts[:i])
    return str(pathlib.PurePosixPath(path).parent)

def application(case):
    text = read(case + '/system/controlDict')
    m = re.search(r'^\s*application\s+([^;\s]+)', text, re.M)
    return m.group(1) if m else ''

# A tutorial is evidence of input structure, not evidence that it was run here.
tutorial_files = defaultdict(list)
for path in entries:
    if path.startswith('tutorials/'):
        tutorial_files[path.rsplit('/', 1)[-1]].append(path)

solver_cases = defaultdict(list)
for path in tutorial_files['controlDict']:
    app = application(tutorial_case(path))
    if app:
        solver_cases[app].append(tutorial_case(path))

family_labels = {'DNS':'直接数值模拟', 'acoustic':'声学', 'basic':'基础方程', 'combustion':'燃烧与化学反应', 'compressible':'可压缩流动', 'discreteMethods':'离散分子方法', 'electromagnetics':'电磁场', 'financial':'金融 PDE', 'finiteArea':'有限面积方法', 'heatTransfer':'传热与浮力', 'incompressible':'不可压缩流动', 'lagrangian':'拉格朗日颗粒', 'multiphase':'多相流', 'stressAnalysis':'固体力学'}
commands = {c['name']: c for c in old_commands}
cms = []
core_names = set()
extra_targets = [{'name':name,'group':'tool','source':'applications/tools/'+name+'/Make/files'} for name in ['foamCalc','foamExprParserInfo']]
for target in inventory['source_targets'] + extra_targets:
    name = target['name']
    if target['group'] in ('solver','utility'):
        core_names.add(name)
    item = commands.get(name, {'name':name, 'configs':[]})
    primary = primary_source(target)
    description = desc_from_source(read(primary))
    group = target['source'].split('/')[2]
    if target['group'] == 'solver':
        cn = notes['solverTitles'].get(name, family_labels.get(group,group) + '求解器')
        item.update(title=name + ' · ' + cn, description=cn + '。具体方程、物理假设和所需字段见下方源码与教程。', category='求解与并行', example=name+' -help-full', configs=item.get('configs') or [{'name':'controlDict','url':'/dictionaries/system-controldict/'},{'name':'fvSchemes','url':'/dictionaries/system-fvschemes/'},{'name':'fvSolution','url':'/dictionaries/system-fvsolution/'}])
    item.update(source=GIT+primary, sourcePath=primary, buildSource=GIT+target['source'], scope='core-'+target['group'], family=family_labels.get(group, group), version='v2512')
    record = runtime.get(name, {})
    item['verification'] = record.get('status', 'not-checked')
    item['verificationText'] = 'v2512 帮助命令退出码 0' if item['verification']=='help-verified' else ('源码包含此目标；当前虚拟机未找到可执行文件' if record else '源码包含此目标；本次尚未采集运行时帮助')
    item['sourceDescription'] = description
    item['details'] = item.get('details', '') + '\n源码说明：' + description + '\n核验范围：'+item['verificationText']+'；未据此宣称完整算例通过。'
    captured = record.get('help') or ('未取得运行时帮助。\n\n源码路径：'+primary+'\n\n'+description)
    item['helpUrl'] = '/assets/command-help/' + slug(name) + '.txt'
    dest = SRC / item['helpUrl'].lstrip('/')
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text('OpenFOAM v2512 command reference\nCommand: '+name+'\nEvidence: '+item['verification']+'\nSource: '+item['source']+'\n\n'+captured,encoding='utf-8')
    # Exact option strings become searchable, rather than guessed command flags.
    item['options'] = sorted(set(re.findall(r'^\s{2,}(-[A-Za-z][A-Za-z0-9-]*)', captured, re.M)))
    item['details'] += '\n已记录的选项：'+' '.join(item['options'])
    commands[name] = item

top_level_scripts = [{'name':'Allwmake','source':'Allwmake'},{'name':'Allrun','source':'tutorials/Allrun'},{'name':'Allclean','source':'tutorials/Allclean'}]
for candidate in inventory['executable_scripts_candidates'] + top_level_scripts:
    name, path = candidate['name'], candidate['source']
    if name in core_names:
        continue
    helper = '/tools/' in path or '/scripts/' in path or '/src/' in path
    item = commands.get(name, {'name':name,'configs':[]})
    description = desc_from_source(read(path))
    helps = source_help(path,name)
    item.update(source=GIT+path, sourcePath=path, scope='build-helper' if helper else 'official-script', verification='source-reviewed', verificationText='v2512 脚本源码已收录；未执行脚本', version='v2512', sourceDescription=description)
    if not item.get('title'):
        item['title'] = name + (' · 构建或开发辅助脚本' if helper else ' · OpenFOAM 官方脚本')
        item['description'] = description or '该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码。'
        item['category'] = '环境与编译' if helper or path.startswith('wmake/') else '系统工具'
        item['example'] = '# 查看安装中的脚本；这条命令不会执行脚本\nsed -n \'1,180p\' "$WM_PROJECT_DIR/' + path + '"'
    item['details'] = item.get('details', '') + '\n'+description+'\n'+('辅助脚本不一定加入 PATH；不要把内部调用接口当作稳定的用户命令。' if helper else '本条基于固定版本脚本源码，运行前检查帮助与依赖。')
    item['helpUrl'] = '/assets/command-help/' + slug(name) + '.txt'
    (SRC / item['helpUrl'].lstrip('/')).write_text('OpenFOAM v2512 script source evidence\nCommand: '+name+'\nSource: '+item['source']+'\n\n以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。\n\n'+(helps or description or read(path)[:5000]),encoding='utf-8')
    item['options'] = sorted(set(re.findall(r'^\s*(-[A-Za-z][A-Za-z0-9-]*)',helps,re.M)))
    item['details'] += '\n源码帮助选项：'+' '.join(item['options'])
    commands[name] = item

# Sourceable shell functions are explicitly distinguished from executables.
shell_functions = []
for path in ['bin/tools/RunFunctions','bin/tools/CleanFunctions','etc/config.sh/aliases']:
    source = read(path)
    if not source:
        continue
    funcs = re.findall(r'^([A-Za-z][A-Za-z0-9_]*)\s*\(\)\s*\{?',source,re.M)
    if path.endswith('aliases'):
        funcs += re.findall(r'^alias\s+([A-Za-z][A-Za-z0-9_]*)=',source,re.M)
    for name in sorted(set(funcs)):
        if name.startswith('_') or (name in commands and commands[name].get('scope')):
            continue
        shell_functions.append(name)
        if name in commands:
            commands[name].update(source=GIT+path,sourcePath=path,scope='shell-function',verification='source-reviewed',verificationText='v2512 环境中的函数或别名；非独立可执行程序',version='v2512')
            continue
        commands[name] = dict(name=name,title=name+' · 已加载脚本中的 shell 函数',description='定义于 '+path+'；需要先 source 对应脚本。它不是独立的 OpenFOAM 可执行程序。',details='这是 v2512 源码中的函数入口。用途、位置参数和副作用应以函数定义及调用处为准。清理函数会删除指定算例的生成文件，应先保存需要保留的数据。' if 'Clean' in path or name.lower().startswith('clean') else '这是 v2512 源码中的函数或别名入口。使用前先检查 type 输出，参数应以源码定义与官方 Allrun 调用为准。',example='. "$WM_PROJECT_DIR/'+path+'"\ntype '+name,category='环境与编译',configs=[],source=GIT+path,sourcePath=path,scope='shell-function',verification='source-reviewed',verificationText='源码中定义；未执行函数',version='v2512')

# Existing environment/Linux entries remain, but are not counted as core apps.
for name,item in commands.items():
    if 'scope' not in item:
        external_docs={'less':'https://www.greenwoodsoftware.com/less/','tmux':'https://github.com/tmux/tmux/wiki','ssh':'https://www.openssh.com/manual.html','scp':'https://www.openssh.com/manual.html','tar':'https://www.gnu.org/software/tar/manual/','grep':'https://www.gnu.org/software/grep/manual/','find':'https://www.gnu.org/software/findutils/manual/','diff':'https://www.gnu.org/software/diffutils/manual/','ps':'https://gitlab.com/procps-ng/procps','top':'https://gitlab.com/procps-ng/procps'}
        doc=external_docs.get(name,'https://www.gnu.org/software/bash/manual/' if name in ('source','cd','command','type','echo','pwd') else 'https://www.gnu.org/software/coreutils/manual/')
        item.update(scope='companion-command',verification='inherited-reference',verificationText='配套命令说明；不计入 278 个核心编译目标',source=doc,version='shell / installed tools')
    item['url']='/commands/'+slug(name)+'/'
    if name=='foamVersion':
        item['example']='printf \'%s\\n\' "$WM_PROJECT_VERSION"\n# foamVersion 是环境函数，先确认当前 shell 是否加载\ntype foamVersion'
        item['description']='v2512 源码提供的环境函数，可查询或切换版本；部分打包环境或非交互 shell 未加载该函数时，直接检查 WM_PROJECT_VERSION。'
    if name=='foamMonitor':
        item['example']='foamLog log.simpleFoam\nfoamMonitor -l logs/p_0'
        item['details']=item['details'].replace('foamMonitor -l postProcessing/residuals/0/residuals.dat','foamLog log.simpleFoam；foamMonitor -l logs/p_0')

def command_body(item):
    name=item['name']
    body='<div class="source-note">'+esc(item['verificationText'])+'。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div>'
    body+=paragraph(item['description'])
    if item.get('sourceDescription'):
        body+='<h2>v2512 源码中的用途</h2>'+paragraph(item['sourceDescription'])
    body+='<h2>使用入口</h2>'+code(item.get('example',''),'bash')
    if item.get('scope')=='build-helper':
        body+=paragraph('该条属于内部构建或开发辅助入口，可能依赖调用方预先设置变量、工作目录和参数。正常使用应优先从 wmake、Allwmake 或相应公开脚本进入。')
    body+='<h2>使用条件与核对</h2>'+paragraph(item.get('details',''))
    if item.get('configs'):
        body+='<p>关联配置：'+' · '.join(link(x['url'],x['name']) for x in item['configs'])+'</p>'
    cases=sorted(set(solver_cases.get(name,[])),key=lambda x:('incompressible/icoFoam/cavity/cavity' not in x,len(x),x))[:5]
    if cases:
        body+='<h2>同版本官方教程</h2>'+paragraph('以下链接直接指向 OpenFOAM-v2512 标签中的教程目录。先阅读 Allrun 确定网格生成、初始化和依赖，再在自己的工作目录运行。列出教程不表示本网站已执行它的全部计算。')+'<ul>'
        for case in cases:
            body+='<li>'+link(TREE+case,case.removeprefix('tutorials/'))+'</li>'
        body+='</ul>'
        sample=cases[0].removeprefix('tutorials/')
        body+=code('mkdir -p "$FOAM_RUN"\ncd "$FOAM_RUN"\n# 先选择一个尚不存在的新目录；保留原教程\ncp -r "$FOAM_TUTORIALS/'+sample+'" ./'+name+'-study\ncd ./'+name+'-study\nls\n# 查看运行流程后，再决定执行哪些步骤\nsed -n \'1,200p\' Allrun','bash')
    if item.get('helpUrl'):
        body+='<h2>完整帮助与证据文件</h2><p>'+link(item['helpUrl'],'下载或打开帮助文本')+'</p>'
        helptext=(SRC/item['helpUrl'].lstrip('/')).read_text(encoding='utf-8')
        body+='<details><summary>展开完整帮助文本</summary>'+code(helptext,'plaintext')+'</details>'
    body+='<h2>来源与版本边界</h2><p>'+link(item['source'],'对应源码或配套工具文档')
    if item.get('buildSource'):
        body+=' · '+link(item['buildSource'],'Make/files 编译目标')
    body+='</p>'+paragraph('核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。')
    return body

for i,item in enumerate(commands.values()):
    body=command_body(item)
    write_page(SRC / item['url'].strip('/') / 'index.md',item['title'],item['description'],body)
    cms.append(dict(slug='command-'+slug(item['name']),kind='reference',title=item['title'],summary=item['description'],body=body,track='命令与配置',series='命令参考',status='published',sort_order=i,metadata={'format':'html','canonical_path':item['url'],'source_url':item['source'],'version':item['version'],'evidence':item['verification'],'scope':item['scope']}))

# Merge variant filenames into their actual dictionary family.
variant_names={n for n in tutorial_files if n.endswith('.topoSetDict')}
dictionary_names={x['name'] for x in inventory['dictionary_candidates']} - variant_names
dicts={x['name']:x for x in old_dicts}
# The old manuscript used the Foundation-style residuals type. The v2512
# registration and shipped templates use solverInfo. Preserve the old URL as
# a migration note instead of continuing to teach an unregistered type.
residuals = dicts.pop('residuals')
dicts['solverInfo'] = dict(name='solverInfo',path='system/controlDict → functions → solverInfo',group='函数对象',description='记录线性求解器类型、初始/最终残差、迭代次数与收敛标记。v2512 使用 solverInfo；旧资料中的 type residuals 不能作为本版本的默认配置照抄。',keys=['type','libs','fields','writeResidualFields','executeControl','writeControl'],commands=['icoFoam','simpleFoam'],url='/dictionaries/functions-solverinfo/',searchText='residuals residual solverInfo 残差')
for name in sorted(dictionary_names-set(dicts)):
    note=notes['configNotes'].get(name)
    if not note:
        raise RuntimeError('Add an individual explanatory note for dictionary: '+name)
    paths=tutorial_files[name]
    location=str(pathlib.PurePosixPath(paths[0]).relative_to(tutorial_case(paths[0])))
    d=dict(name=name,path=location,group=note[0],description=note[1],keys=[],commands=[note[2]],url='/dictionaries/'+slug(location)+'/',searchText='')
    dicts[name]=d

group_flow={
 '网格': [('几何与分辨率','表面 / 顶点 / 单元尺寸'),('网格字典','生成 · 选择 · 拓扑修改'),('polyMesh + checkMesh','检查几何、拓扑和边界')],
 '初始化': [('网格与物理区域','坐标 · 集合 · 场名称'),('初始化字典','选择区域并赋予数值'),('0/ 与初始状态','检查范围、量纲和守恒')],
 '初始场': [('polyMesh/boundary','patch 名称与网格类型'),('0/ 中的场文件','dimensions · 内部场 · 边界'),('方程与物理模型','检查边界相容性和场量纲')],
 '计算控制': [('求解器与初始时刻','模型 / 网格 / 初始条件'),('controlDict 与辅助配置','时间推进 · 写出 · 函数对象'),('时间目录与日志','检查时间步、输出与续算')],
 '数值方法': [('连续方程与网格','守恒式 · 面通量 · 非正交性'),('离散与求解控制','fvSchemes · fvSolution'),('线性系统与外循环','残差 · 守恒 · 目标量变化')],
 '物理模型': [('物理假设与材料','相态 · 热力学 · 闭合模型'),('物性与模型字典','模型选择 · 系数 · 作用区域'),('求解器所需字段','量纲 · 初边值 · 库与源项')],
 '并行计算': [('原始网格与 MPI 进程','单元数 · 分区方法'),('decomposeParDict','分区数与区域设置'),('processor* 与重构','并行求解 · 负载 · 一致性')],
 '函数对象': [('已存在的网格与场','类型 · 时刻 · 区域'),('functions 实例','type · libs · fields'),('采样与派生量','postProcessing / 时间目录')],
 '后处理': [('结果场与采样位置','时间范围 · 坐标 · 场名'),('采样或导出字典','插值 · 积分 · 格式'),('图表与物理检查','标明单位、采样位置和时刻')],
 '编译': [('C++ 源码与头文件','类定义 · 运行时注册'),('Make/files + options','目标 · include · 依赖库'),('wmake 与运行时加载','ABI · 库路径 · libs')]
}

def make_diagram(group):
    stages=group_flow.get(group,group_flow['物理模型'])
    filename='reference-'+slug(str(list(group_flow).index(group) if group in group_flow else 5))+'.svg'
    path=SRC/'assets/diagrams'/filename
    path.parent.mkdir(parents=True,exist_ok=True)
    svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 220" role="img" aria-labelledby="title desc"><title id="title">'+esc(group)+'配置关系</title><desc id="desc">'+esc(' → '.join(x[0] for x in stages))+'</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#3675ac"/></marker></defs><rect width="1080" height="220" rx="20" fill="#f0f6fc"/>'
    for i,(a,b) in enumerate(stages):
        x=24+i*358
        svg+=f'<rect x="{x}" y="48" width="316" height="123" rx="12" fill="white" stroke="#aac6df"/><text x="{x+19}" y="78" font-family="Arial,sans-serif" font-size="13" fill="#3675ac">0{i+1}</text><text x="{x+19}" y="109" font-family="Arial,Microsoft YaHei,sans-serif" font-size="18" font-weight="600" fill="#153950">{esc(a)}</text><text x="{x+19}" y="141" font-family="Arial,Microsoft YaHei,sans-serif" font-size="13" fill="#516c80">{esc(b)}</text>'
        if i<2:
            svg+=f'<path d="M{x+322} 109 L{x+352} 109" stroke="#3675ac" stroke-width="2" marker-end="url(#arrow)"/>'
    svg+='</svg>'
    path.write_text(svg,encoding='utf-8')
    return '/assets/diagrams/'+filename

diagrams={group:make_diagram(group) for group in group_flow}

preferred={
 'controlDict':['incompressible/icoFoam/cavity/cavity/','incompressible/simpleFoam/pitzDaily/','multiphase/interFoam/laminar/damBreak/damBreak/'],
 'fvSchemes':['incompressible/icoFoam/cavity/cavity/','incompressible/simpleFoam/pitzDaily/','multiphase/interFoam/laminar/damBreak/damBreak/'],
 'fvSolution':['incompressible/icoFoam/cavity/cavity/','incompressible/simpleFoam/pitzDaily/','multiphase/interFoam/laminar/damBreak/damBreak/'],
 'blockMeshDict':['incompressible/icoFoam/cavity/cavity/','incompressible/simpleFoam/pitzDaily/','basic/laplacianFoam/flange/'],
 'transportProperties':['incompressible/icoFoam/cavity/cavity/','incompressible/nonNewtonianIcoFoam/','multiphase/interFoam/laminar/damBreak/damBreak/'],
 'turbulenceProperties':['incompressible/simpleFoam/pitzDaily/','incompressible/icoFoam/cavity/cavity/','incompressible/pimpleFoam/LES/'],
 'snappyHexMeshDict':['incompressible/simpleFoam/motorBike/','mesh/snappyHexMesh/'],
 'U':['incompressible/icoFoam/cavity/cavity/','incompressible/simpleFoam/pitzDaily/','incompressible/pimpleFoam/laminar/'],
 'p':['incompressible/icoFoam/cavity/cavity/','incompressible/simpleFoam/pitzDaily/','compressible/rhoSimpleFoam/']
}

function_names={'probes','sets','surfaces','forces','forceCoeffs','fieldAverage','volFieldValue','surfaceFieldValue','solverInfo','yPlus','Q'}

def choose_examples(name):
    candidates=list(tutorial_files.get(name,[]))
    if name=='topoSetDict':
        candidates += [p for v in variant_names for p in tutorial_files[v]]
    if name in function_names:
        # Full dictionaries are retained, including the surrounding functions block.
        candidates += [p for p in tutorial_files['controlDict'] if re.search(r'\btype\s+'+re.escape(name)+r'\s*;',read(p))]
    if name in ('files','options'):
        candidates=[p for p in entries if p.startswith('applications/') and p.endswith('/Make/'+name)]
    # Include canonical shipped templates as a separate source kind when useful.
    candidates += [p for p in entries if p.startswith('etc/caseDicts/') and p.rsplit('/',1)[-1]==name]
    def score(p):
        pref=next((i for i,v in enumerate(preferred.get(name,[])) if v in p),99)
        size=len(read(p))
        return (pref,not p.startswith('tutorials/'),size>22000,'/IO/' in p,size,p)
    ranked=sorted(set(candidates),key=score)
    result=[]; hashes=set(); families=set()
    for path in ranked:
        text=read(path)
        if not text or len(text)>250000:
            continue
        h=hashlib.sha256(re.sub(r'/\*.*?\*/|//[^\n]*|\s','',text,flags=re.S).encode()).hexdigest()
        if h in hashes:
            continue
        family='/'.join(tutorial_case(path).split('/')[:4])
        if result and family in families and len(ranked)>6:
            continue
        result.append(path);hashes.add(h);families.add(family)
        if len(result)==3:
            break
    # Some properties appear only in one family: retain distinct configurations.
    if len(result)<3:
        for path in ranked:
            text=read(path)
            h=hashlib.sha256(re.sub(r'/\*.*?\*/|//[^\n]*|\s','',text,flags=re.S).encode()).hexdigest()
            if text and len(text)<250000 and h not in hashes:
                result.append(path);hashes.add(h)
                if len(result)==3:
                    break
    return result

def key_comments(text):
    lines=re.sub(r'/\*.*?\*/','',text,flags=re.S).splitlines()
    keys={}; comments=[]
    for line in lines:
        stripped=line.strip()
        if stripped.startswith('//'):
            s=stripped[2:].strip(' -')
            if s: comments.append(s)
            comments=comments[-3:]
            continue
        m=re.match(r'^([A-Za-z_][A-Za-z0-9_:.<>+-]*)(?=\s|[({\[]|$)',stripped)
        if m and not stripped.startswith(('#','FoamFile')) and m.group(1) not in ('version','format','class','location','object'):
            key=m.group(1)
            inline=stripped.split('//',1)[1].strip() if '//' in stripped else ''
            comment=inline or ' '.join(comments)
            if key not in keys: keys[key]=comment
        if stripped and stripped not in ('{','('): comments=[]
    return keys

def failure_notes(group):
    return {
      '网格': [('边界名称与字段不一致','修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。'),('单位或坐标方向错误','比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。'),('网格生成成功但质量不足','运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。')],
      '初始化':[('场没有发生预期变化','核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。'),('初始化破坏守恒','统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。'),('边界值与内部值冲突','初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。')],
      '物理模型':[('Unknown model / Unknown type','核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。'),('量纲不一致或压力基准错误','对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。'),('计算收敛但物理结果不合理','用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。')],
      '数值方法':[('找不到离散项或场求解器','把错误中的完整键名与 fvSchemes / fvSolution 对照，注意 div(phi,U) 等键的精确拼写。'),('残差下降但目标量漂移','同时监测守恒误差、力或流量，并分别检查时间步与网格敏感性。'),('非正交修正导致成本增加','优先改善网格；增加修正次数不是无条件提高精度的办法。')],
      '后处理':[('No field / No functionObject','确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。'),('结果坐标或单位错误','记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。'),('峰值随采样方式改变','比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。')],
      '函数对象':[('函数对象未执行','核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。'),('输出路径找不到','检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。'),('统计量定义不一致','明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。')],
      '初始场':[('Unknown patchField / patch type mismatch','同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。'),('速度与压力约束不相容','在入口、出口和封闭壁面共同考虑通量约束与压力参考。'),('湍流场出现非法值','检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。')],
      '编译':[('找不到头文件','核对 EXE_INC、库 lnInclude 是否生成以及当前 WM_PROJECT_DIR。'),('链接时 undefined reference','核对 EXE_LIBS / LIB_LIBS、库名与链接顺序，并确认实现文件参与编译。'),('加载共享库失败','检查编译使用的 v2512 环境与运行时 ABI、库搜索路径和 controlDict 的 libs。')],
      '并行计算':[('分区数与 MPI 进程数不同','核对 numberOfSubdomains 与 mpirun -np，修改分区数后重新分解。'),('串并行结果差异过大','保持网格、初值、时间步与收敛准则一致，并检查各进程日志与整体守恒。')],
      '计算控制':[('重启时刻不符合预期','核对 startFrom、startTime 与已存在的时间目录，避免旧结果影响首次运行。'),('时间目录增长过快','结合 writeControl、writeInterval、purgeWrite 与函数对象输出，先估计磁盘占用。'),('开启 adjustTimeStep 仍不生效','确认求解器确实实现对应时间步控制；字典可解析不代表每个键被使用。')]
    }.get(group,[])

example_manifest=[]
for order,(name,d) in enumerate(dicts.items()):
    existing_path=SRC/d['url'].strip('/')/'index.md'
    if name in legacy_dictionary_names and existing_path.exists():
        text=original(existing_path)
        match=re.search(r'{% raw %}\s*(.*?)\s*{% endraw %}',text,re.S)
        retained=match.group(1) if match else re.sub(r'^---.*?---\s*','',text,flags=re.S)
        retained=re.sub(r'<h2>第\s*\d+\s*章[^<]*</h2>', '<h2>补充说明</h2>',retained)
        retained=retained.replace('foamVersion\n','printf \'%s\\n\' &quot;$WM_PROJECT_VERSION&quot;\n')
        retained=re.sub(r'<pre><code>(.*?)</code></pre>',classify_retained_code,retained,flags=re.S)
        retained=retained.replace('<td>residuals</td>','<td>solverInfo</td>').replace('type residuals;', 'type solverInfo;')
    else:
        retained=''
    if name=='solverInfo':
        retained='<h3>残差记录属于求解过程</h3>'+paragraph('solverInfo 读取 mesh 中的 solverPerformance 数据，必须在实际方程求解时执行。对已经写出的 U 和 p 单独运行后处理，不能重建过去每一步的线性求解历史。初始残差、最终残差与连续性误差是不同指标，需要分别监测。')+code('functions\n{\n    linearSolverHistory\n    {\n        type solverInfo;\n        libs (utilityFunctionObjects);\n        fields (p U);\n        writeResidualFields false;\n        executeControl timeStep;\n        executeInterval 1;\n        writeControl timeStep;\n        writeInterval 1;\n    }\n}')+paragraph('上例为依据 v2512 solverInfo.H 整理的教学配置。writeResidualFields 控制是否额外写出初始残差场，会增加输出开销。向量各分量与总体守恒需要结合检查。')+'<p>'+link(GIT+'src/functionObjects/utilities/solverInfo/solverInfo.H','查看类型注册、必需参数与默认值')+'</p>'
    selected=choose_examples(name)
    allkeys={}
    for path in selected:
        for key,comment in key_comments(read(path)).items():
            if key not in allkeys or not allkeys[key]:allkeys[key]=comment
    local_notes=notes.get('configKeyNotes',{}).get(name,{})
    known=[(key,local_notes.get(key,notes['keyNotes'].get(key))) for key in allkeys if key in local_notes or key in notes['keyNotes']]
    if name in notes['configNotes']:
        d['description']=notes['configNotes'][name][1]
    body='<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div>'
    body+=paragraph(d['description'])
    diagram=diagrams.get(d['group'],diagrams['物理模型'])
    body+='<figure><img src="'+diagram+'" alt="'+esc(d['group'])+'配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure>'
    if retained:
        body+='<h2>配置原理与基础示例</h2>'+retained
    body+='<h2>从真实配置理解关键条目</h2>'
    if known:
        body+=table(['条目','含义与使用条件'],known[:24])
    source_comments=[(key,comment) for key,comment in allkeys.items() if comment and key not in notes['keyNotes'] and len(comment)>5]
    if source_comments:
        body+='<h3>教程保留的参数注释</h3>'+paragraph('下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。')+table(['条目','源码注释'],source_comments[:24])
    if not known and not source_comments:
        body+=paragraph('该专用配置的字段由对应程序决定。阅读下面完整文件时，应把同一层的大括号块作为一个模型实例，并从 Allrun 和 #include 追踪输入关系；本页不为缺少直接证据的键杜撰默认值。')
    body+='<h2>v2512 完整示例与对照</h2>'
    if selected:
        body+=paragraph('共选取 '+str(len(selected))+' 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。')
    else:
        body+=paragraph('本项属于编译接口或函数对象说明，固定版本教程没有检索到同名独立文件。保留上面的教学片段；不能据此构造不存在的“官方完整示例”。')
    if len(selected)==1:
        body+=paragraph('该文件族在本次固定版本源码中仅选到一份不同的完整配置；不重复同一个文件充当多个案例。')
    if name=='topoSetDict':
        body+=paragraph('同一语法也可保存在 *.topoSetDict 等自定义名称中，通过 topoSet -dict 指定。createInletOutletSets.topoSetDict、cRefine.topoSetDict、f.topoSetDict 与 fBurner.topoSetDict 归在此文件族，不虚增为四种独立配置格式。')
    for n,path in enumerate(selected,1):
        text=read(path)
        case=tutorial_case(path)
        app=application(case) if path.startswith('tutorials/') else ''
        local='/assets/examples/v2512/'+slug(name)+'/'+str(n)+'-'+path.rsplit('/',1)[-1]+'.txt'
        dest=SRC/local.lstrip('/');dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(text.encode('utf-8'))
        body+='<h3>示例 '+str(n)+' · '+esc(case.removeprefix('tutorials/'))+'</h3>'
        body+='<p>原始路径：<code>'+esc(path)+'</code>' + ('；求解器：<code>'+esc(app)+'</code>' if app else '')+'</p>'
        body+='<p>'+link(GIT+path,'查看固定版本源码')+' · '+link(local,'下载完整配置')+' · '+link(TREE+case,'查看配套目录')+'</p>'
        if len(text)>16000:
            body+='<details><summary>展开完整配置（'+str(len(text.splitlines()))+' 行）</summary>'+code(text,'makefile' if name in ('files','options') else 'openfoam')+'</details>'
        else:
            body+=code(text,'makefile' if name in ('files','options') else 'openfoam')
        includes=re.findall(r'^\s*#(?:include\w*)\s+([^\n]+)',text,re.M)
        if includes:
            body+=paragraph('本例包含外部引用：'+'；'.join(includes[:12])+'。下载单个文件不会自动取得这些依赖。')
        example_manifest.append(dict(dictionary=name,path=path,download=local,sha256=hashlib.sha256(text.encode()).hexdigest(),lines=len(text.splitlines()),case=case,application=app))
    body+='<h2>配套命令与验证次序</h2>'
    cmds=[x for x in d['commands'] if x in commands]
    if cmds: body+='<p>'+' · '.join(link(commands[c]['url'],c) for c in cmds)+'</p>'
    if selected and name not in ('files','options'):
        relative=selected[0].removeprefix(tutorial_case(selected[0])+'/')
        body+=code('# 在完整算例目录中检查；解析成功不等于模型和物理设置正确\nprintf \'%s\\n\' "$WM_PROJECT_VERSION"\nfoamDictionary "'+relative+'" -keywords\n# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容\n# foamDictionary "'+relative+'" -expand','bash')
    body+=table(['现象','检查方法'],failure_notes(d['group']))
    body+='<h2>来源与许可</h2><p>本页完整源码示例来自 '+link(TREE+'','OpenFOAM-v2512 官方标签')+'，保留原文件版权头，适用 '+link(GIT+'COPYING','GPL-3.0 或更新版本许可')+'。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>'
    d['keys']=list(dict.fromkeys(d.get('keys',[])+list(allkeys)))[:90]
    d['examples']=len(selected)
    d['source']='OpenFOAM-v2512'
    d['searchText']=re.sub(r'<[^>]+>',' ',body)
    # Keep searchable words without duplicating full examples inside the index.
    d['searchText']=html.unescape(re.sub(r'\s+',' ',d['searchText']))[:24000]
    write_page(existing_path,d['path']+' · '+name,d['description'],body,True)
    cms.append(dict(slug='dictionary-'+slug(name),kind='reference',title=d['path']+' · '+name,summary=d['description'],body=body,track='命令与配置',series='配置字典',status='published',sort_order=1000+order,metadata={'format':'html','canonical_path':d['url'],'version':'v2512','example_count':len(selected),'group':d['group'],'source_url':TREE+'tutorials'}))

write_page(SRC/'dictionaries/functions-residuals/index.md','残差记录：v2512 使用 solverInfo','旧 residuals 链接的版本迁移说明。','<p>本页保留旧参考链接。OpenCFD v2512 的残差与线性求解器信息记录使用 <code>solverInfo</code> 函数对象，加载 <code>utilityFunctionObjects</code>。</p><p>'+link('/dictionaries/functions-solverinfo/','阅读 solverInfo 的完整说明与 v2512 示例')+'</p><p>'+link(GIT+'src/functionObjects/utilities/solverInfo/solverInfo.C','检查 v2512 的运行时类型注册')+'</p>')

command_list=list(commands.values())
dictionary_list=list(dicts.values())
save(SRC/'assets/commands.json',command_list)
save(SRC/'assets/dictionaries.json',dictionary_list)
# Other learning.json fields are controlled by the main integration task.
learning_path=SRC/'_data/learning.json'
learning=load(learning_path)
learning['commands']=command_list
save(learning_path,learning)
save(ROOT/'tools/content/reference-content.json',cms)
save(SRC/'assets/reference-example-manifest.json',example_manifest)
counts=Counter(x['scope'] for x in command_list)
report=dict(version='v2512',core_targets=len(core_names),solver_targets=sum(x['group']=='solver' for x in inventory['source_targets']),utility_targets=sum(x['group']=='utility' for x in inventory['source_targets']),additional_compiled_tools=len(extra_targets),help_verified=sum(x.get('verification')=='help-verified' for x in command_list),not_installed=[x['name'] for x in command_list if x['name'] in core_names and x.get('verification')!='help-verified'],command_entries=len(command_list),scopes=dict(counts),dictionary_entries=len(dicts),tutorial_filename_candidates=len(inventory['dictionary_candidates']),merged_toposet_variant_filenames=sorted(variant_names),complete_examples=len(example_manifest),dictionary_examples=Counter(x['dictionary'] for x in example_manifest),dictionary_single_examples=[x['name'] for x in dictionary_list if x.get('examples')==1],dictionary_without_examples=[x['name'] for x in dictionary_list if not x.get('examples')],cms_entries=len(cms),source_archive_sha256=hashlib.sha256((WORK/'openfoam-v2512.tar.gz').read_bytes()).hexdigest())
report['additional_tools_not_installed']=[x['name'] for x in command_list if x['scope']=='core-tool' and x['verification']=='not-installed']
save(SRC/'assets/reference-audit.json',report)
save(WORK/'reference-audit.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='dictionary_examples'},ensure_ascii=False,indent=2))
