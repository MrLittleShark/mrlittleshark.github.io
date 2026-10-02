"""Reorganize reference pages around usage, explanation and worked examples.

The original v2512 example files and captured help are left byte-for-byte intact.
Authored Markdown guides replace the mixed excerpts on common dictionary pages.
"""
from pathlib import Path
import html, json, re, subprocess, sys
from bs4 import BeautifulSoup
from wolf_media import figure_html

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).parent
SRC = ROOT/'source-openfoam'
ASSETS = SRC/'assets'
GIT = 'https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/'
TREE = 'https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/'
e = html.escape
def load(path, fallback=None):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else fallback
def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def p(text): return '<p>'+e(text)+'</p>'
def code(text, lang='foam'): return '<pre><code class="language-'+lang+'">'+e(text.strip())+'</code></pre>'
def a(url, text): return '<a href="'+e(url,quote=True)+'">'+e(text)+'</a>'
def table(headers, rows):
    return '<table><thead><tr>'+''.join('<th>'+e(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+e(str(x))+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def clean_description(text):
    text = text.split('具体方程、物理假设和所需字段')[0].strip()
    text = re.sub(r'\s*\\(?:c|a|e|b)\s+', ' ', text)
    return text

OPTION_NOTES = {
 '-case':'指定算例目录；省略时使用当前目录。', '-dict':'改用指定字典文件。',
 '-region':'指定网格区域名称。', '-parallel':'启用并行运行；由 mpirun 启动相应进程数。',
 '-overwrite':'将修改后的网格写回原位置。操作前保存需要保留的网格。',
 '-latestTime':'选择最近的结果时刻。', '-time':'选择时刻或时间范围，如 0.1:0.5。',
 '-constant':'将 constant 目录加入选择。', '-noZero':'跳过 0 时刻。',
 '-allRegions':'处理 regionProperties 中列出的所有区域。', '-noFunctionObjects':'运行时停用函数对象。',
 '-decomposeParDict':'使用指定的并行分解字典。', '-fields':'按工具要求指定要处理的字段或仅处理字段。具体参数见完整帮助。',
 '-help':'显示常用参数。', '-help-full':'显示完整参数。',
 '-entry':'定位字典中的键或子字典路径。', '-value':'仅输出所选条目的值。',
 '-keywords':'列出当前字典层级的键名。', '-set':'设置条目值，会修改文件。',
 '-expand':'展开字典引用和函数条目；#codeStream 等条目可能执行代码。',
 '-sourceTime':'选择源算例的时间。', '-consistent':'按匹配的边界拓扑进行场映射。',
 '-allTopology':'执行更完整的网格拓扑检查。', '-allGeometry':'执行更完整的网格几何检查。',
 '-writeSets':'写出问题单元或面的集合，格式由参数指定。',
 '-func':'执行指定的预配置函数对象。', '-list':'列出可用的预配置函数。',
 '-cellDist':'写出单元所属子域，便于检查分区。', '-ifRequired':'按已有分区和当前配置判断是否需要重新分解。',
 '-no-clean':'保留已有 polyMesh 文件；默认行为见完整帮助。',
 '-write-vtk':'输出块拓扑的 VTK 文件。', '-sets':'同时将 cellZone 写成 cellSet。',
 '-builtin':'使用 ParaView 内置的 OpenFOAM Reader。',
}
NOISY = {'-debug-switch','-info-switch','-opt-switch','-lib','-fileHandler','-no-libs','-doc','-doc-source','-help-man','-help-notes','-help-compat','-hostRoots','-roots','-world','-mpi-no-comm-dup','-mpi-split-by-appnum','-mpi-threads','-listRegisteredSwitches','-listSwitches','-listUnsetSwitches'}
def help_text(item):
    file = SRC/item.get('helpUrl','').lstrip('/')
    if not item.get('helpUrl') or not file.is_file(): return ''
    raw = file.read_text(encoding='utf-8')
    match = re.search(r'(?m)^Usage:', raw)
    return raw[match.start():] if match else raw
def options(raw):
    entries = []
    for line in raw.splitlines():
        match = re.match(r'^\s{1,8}(-[\w-]+[^\n]*?)\s{2,}(\S.*)$', line)
        if match:
            entries.append([match.group(1).strip(), match.group(2).strip()])
        elif entries and re.match(r'^\s{12,}\S', line):
            entries[-1][1] += ' '+line.strip()
    return entries

def command_body(item, old, guide):
    name = item['name']; raw = help_text(item)
    body = p(item['description'])
    if guide:
        body += guide
    else:
        body += '<h2>用法</h2>'+code(item.get('example',''), 'bash')
        detail = item.get('details','').split('源码说明：')[0].split('核验范围：')[0].split('本条基于固定版本')[0].strip()
        detail = re.sub(r'用法：[\s\S]*', '', detail).strip()
        if detail and detail != item['description'] and len(detail)<900: body += p(detail)
        if item.get('scope')=='core-solver':
            body += '<h2>运行计算</h2>'+code(name+' > log.'+name+' 2>&1\ntail -n 20 log.'+name, 'bash')
            body += p('在已经准备好网格、物性和初始场的算例目录运行。第一行把终端输出保存到日志，计算结束后，第二行显示日志最后 20 行。计算结果按 controlDict 的设置写入时间目录。')
    opts = []
    for flag, desc in options(raw):
        key = flag.split()[0]
        if key in NOISY: continue
        opts.append([flag, OPTION_NOTES.get(key, desc)])
    if opts:
        parameter_table=table(['参数','作用'], opts[:14])
        parameter_table=re.sub(r'<tr><td>([\s\S]*?)</td>', r'<tr><td><code>\1</code></td>', parameter_table)
        body += '<h2>常用参数</h2>'+parameter_table
    if item.get('configs'):
        body += '<h2>相关配置</h2><p>'+' · '.join(a(x['url'],x['name']) for x in item['configs'])+'</p>'
    old_soup = BeautifulSoup(old, 'html.parser')
    cases = []
    for link in old_soup.select('a[href]'):
        if link['href'].startswith(TREE+'tutorials/'):
            cases.append((link['href'], link.get_text(' ',strip=True)))
    if cases:
        body += '<h2>配套算例</h2><ul>'+''.join('<li>'+a(u,t)+'</li>' for u,t in dict.fromkeys(cases))+'</ul>'
        if item.get('scope')=='core-solver':
            rel = cases[0][0].split('/tutorials/',1)[1]
            body += code('mkdir -p "$FOAM_RUN"\ncd "$FOAM_RUN"\ncp -r "$FOAM_TUTORIALS/'+rel+'" '+name+'-study\ncd '+name+'-study\nls', 'bash')
            body += p('使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。')
    if raw:
        body += '<details><summary>完整命令帮助</summary>'+code(raw,'text')+'</details>'
    body += '<h2>参考</h2><p>'+a(item['source'],'源码与说明')
    if item.get('helpUrl'): body += ' · '+a(item['helpUrl'],'帮助文本')
    body += '</p>'
    return body

def legacy_teaching(old):
    soup = BeautifulSoup(old,'html.parser')
    nodes = list(soup.children); start = None; end = None
    for i, node in enumerate(nodes):
        if getattr(node,'name',None)=='h2':
            title = node.get_text(' ',strip=True)
            if start is None and re.match(r'^\d',title): start = i
            if title in ['从真实配置理解关键条目','v2512 完整示例与对照'] and end is None: end=i
    if start is None: return ''
    kept=[]
    for node in nodes[start+1:end]:
        if getattr(node,'name',None)=='h2' and node.get_text(strip=True)=='补充说明': continue
        if getattr(node,'name',None)=='p' and node.get_text(strip=True).startswith('它管什么：'):continue
        kept.append(str(node))
    return ''.join(kept)

def dictionary_body(item, old, guide, examples, notes, example_notes):
    name=item['name']
    body=p(item['description'])+'<p>位置：<code>'+e(item['path'])+'</code></p>'
    figures={'blockMeshDict':'wolf-mesh-smooth-transition','snappyHexMeshDict':'wolf-snappy-workflow','meshQualityDict':'wolf-mesh-nonorthogonality','fvSchemes':'wolf-advection-profile-errors','fvSolution':'wolf-pimple-pressure-coupling','turbulenceProperties':'wolf-turbulence-model-hierarchy','dynamicMeshDict':'wolf-dynamic-mesh-modes','MRFProperties':'wolf-dynamic-mrf-configuration','alpha.water':'wolf-vof-volume-fraction','nut':'wolf-turbulence-wall-law'}
    if name in figures: body+=figure_html(figures[name])
    if guide: body += guide
    else:
        original=legacy_teaching(old)
        if original: body += '<h2>配置实例</h2>'+original
        elif examples:
            first=examples[0]; text=(SRC/first['download'].lstrip('/')).read_text(encoding='utf-8')
            text=re.sub(r'/\*[\s\S]*?\*/','',text,count=1).strip()
            text=re.sub(r'(?m)^// \*.*$', '', text)
            text=re.sub(r'\n{3,}','\n\n',text)
            # Very long configuration remains in the expandable full example.
            if len(text.splitlines())<=100:
                body += '<h2>配置实例</h2>'+p(first['case'].removeprefix('tutorials/')+' 中的 '+name+'：')+code(text)
        context=notes.get('configKeyNotes',{}).get(name,{})
        entries=[]
        for key in item.get('keys',[]):
            meaning=context.get(key) or notes.get('keyNotes',{}).get(key)
            if meaning: entries.append([key,meaning])
        if entries: body+='<h2>参数说明</h2>'+table(['条目','含义'],entries)
    if examples:
        body+='<h2>完整案例配置</h2>'+p('以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。')
        for i, example in enumerate(examples,1):
            text=(SRC/example['download'].lstrip('/')).read_text(encoding='utf-8')
            case=example['case'].removeprefix('tutorials/')
            explanation=example_notes.get(example['download'],'')
            body+='<details class="reference-example"'+(' open' if i==1 else '')+'><summary>示例 '+e(str(i)+' · '+case)+'</summary>'+explanation+'<p>'+a(example['download'],'下载配置')+' · '+a(GIT+example['path'],'源码')+' · '+a(TREE+example['case'],'案例目录')+'</p>'+code(text)+'</details>'
    if item.get('commands'):
        links=[]
        for command in item['commands']:
            url='/commands/'+re.sub(r'[^a-z0-9]+','-',command.lower()).strip('-')+'/'
            links.append(a(url,command) if (SRC/url.strip('/')/'index.md').is_file() else '<code>'+e(command)+'</code>（扩展工具）')
        body+='<h2>相关命令</h2><p>'+' · '.join(links)+'</p>'
    soup=BeautifulSoup(old,'html.parser')
    for tab in soup.select('table'):
        if '现象' in tab.get_text() and '检查方法' in tab.get_text():
            body+='<h2>常见问题</h2>'+str(tab).replace('残差小不能替代物理验证','同时比较流量、压降等目标量与参考数据').replace('不是无条件提高精度的办法','其作用随网格质量和解的光滑程度变化，可通过细化对比评估').replace('字典可解析不代表每个键被使用','检查当前求解器是否读取该参数')
    body+='<p class="figure-source">配置来源：'+a(TREE+'tutorials','OpenFOAM v2512 教程')+' · '+a(GIT+'COPYING','GPL-3.0-or-later')+'。</p>'
    return body

def render_guides(guides):
    if not guides: return {}
    # Reuse the site's math protection so Markdown cannot consume TeX escapes.
    script="const fs=require('fs'),{marked}=require('marked'),P=require('./lib/presentation.cjs');const x=JSON.parse(fs.readFileSync(0,'utf8'));for(const k in x)x[k]=marked.parse(P.protectMath(x[k]));process.stdout.write(JSON.stringify(x));"
    node=Path('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe')
    result=subprocess.run([str(node) if node.exists() else 'node','-e',script],input=json.dumps(guides,ensure_ascii=False),text=True,encoding='utf-8',capture_output=True,cwd=ROOT,check=True)
    # protectMath placeholders contain TeX in a data attribute; P.render resolves
    # them for static HTML. CMS markdown rendering also handles raw delimiters.
    rendered=json.loads(result.stdout)
    for key, value in rendered.items():
        # Store raw TeX delimiters in HTML, rather than server-rendered KaTeX.
        original=guides[key]
        # protectMath emits data-tex attributes; recover delimiters for CMS.
        soup=BeautifulSoup(value,'html.parser')
        for span in soup.select('[data-tex]'):
            tex=span.get('data-tex','');display=span.get('data-display')=='true'
            span.replace_with(('\\[' if display else '\\(')+tex+('\\]' if display else '\\)'))
        rendered[key]=str(soup)
    return rendered

def main():
    commands=load(ASSETS/'commands.json');dicts=load(ASSETS/'dictionaries.json')
    records=load(HERE/'reference-content.json');by_slug={r['slug']:r for r in records}
    definitions=load(HERE/'reference-definitions.json',{})
    command_edits=load(HERE/'command-guides.json',{})
    command_edits.update(load(HERE/'shell-command-guides.json',{}))
    # Explicit, reviewed progressions take precedence over the earlier short
    # guides and remain part of the normal rebuild pipeline.
    example_guides={}
    for file in sorted(HERE.glob('command-examples-*.json')):
        for name, guide in load(file,{}).items():
            assert name not in example_guides, ('Duplicate command guide', name)
            examples=guide['examples']
            assert len(examples)>=5, (name, 'At least five examples required')
            assert len({x['code'] for x in examples})==len(examples), (name, 'Duplicate code')
            body='## 开始前\n\n'+guide['prerequisites']+'\n\n'
            for i, example in enumerate(examples,1):
                body+='## 示例 '+str(i)+'：'+example['title']+'\n\n```bash\n'+example['code'].strip()+'\n```\n\n'
                if example.get('output'):
                    body+='输出示例：\n\n```text\n'+example['output'].strip()+'\n```\n\n'
                body+=example['explanation'].strip()+'\n\n'
            example_guides[name]=dict(command_edits.get(name,{}),body=body,examples=examples,example=examples[0]['code'])
            if guide.get('summary'):example_guides[name]['summary']=guide['summary']
    command_edits.update(example_guides)
    guides={}
    for filename in ['dictionary-guides.json','field-guides.json','mesh-guides.json']:
        guides.update(load(HERE/filename,{}))
    rendered=render_guides(guides)
    command_html=render_guides({k:v['body'] for k,v in command_edits.items() if v.get('body')})
    manifest=load(ASSETS/'reference-example-manifest.json')
    notes=load(ROOT/'tools/reference-notes.json')
    example_sources=load(HERE/'reference-example-notes.json',{})
    advanced_examples=load(HERE/'reference-example-notes-advanced.json',{})
    assert not set(example_sources)&set(advanced_examples), 'Duplicate example explanations'
    example_sources.update(advanced_examples)
    example_notes=render_guides(example_sources)
    missing={x['download'] for x in manifest}-set(example_notes)
    if missing:
        raise RuntimeError('Missing case explanations for '+str(len(missing))+' complete examples')
    # Keep raw templates as the rebuild input; never layer new output over itself.
    baseline=HERE/'reference-layout-baseline.json'
    if not baseline.exists():save(baseline,{r['slug']:r['body'] for r in records})
    originals=load(baseline)
    for item in commands:
        slug='command-'+re.sub(r'[^a-z0-9]+','-',item['name'].lower()).strip('-')
        row=by_slug[slug];edit=command_edits.get(item['name'],{})
        item['description']=edit.get('summary',clean_description(item['description']))
        if edit.get('example'):item['example']=edit['example']
        item['details']=edit.get('details',item['description'])
        item['examples']=edit.get('examples',[])
        if not item['examples']:
            item['examples']=[{'title':'基本用法','code':item['example'],'explanation':item['description']}]
            # Only add options listed by the actual program, preserving positional
            # arguments from the existing example (surface names, input paths...).
            if '-case' in item.get('options',[]) and '-case' not in item['example'] and '\n' not in item['example']:
                item['examples'].append({'title':'指定算例目录','code':item['example']+' -case ../myCase','explanation':'把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。'})
        if not command_html.get(item['name']) and len(item['examples'])>1:
            additional=item['examples'][1:]
            extra=''.join('<h2>'+e(x['title'])+'</h2>'+code(x['code'],'bash')+p(x['explanation']) for x in additional)
        else: extra=''
        item['title']=item['name']+' · '+item['description'].split('。')[0][:48]
        item.pop('display',None)
        body=command_body(item,originals[slug],command_html.get(item['name'],''))
        if extra:
            anchor='<h2>常用参数</h2>'
            body=body.replace(anchor,extra+anchor,1) if anchor in body else body+extra
        row.update(title=item['title'],summary=item['description'],body=body)
    for item in ([] if '--commands-only' in sys.argv else dicts):
        slug='dictionary-'+re.sub(r'[^a-z0-9]+','-',item['name'].lower()).strip('-')
        row=by_slug[slug]
        item['description']=definitions.get(item['name'],item['description'].split('。')[0]+'。')
        body=dictionary_body(item,originals[slug],rendered.get(item['name'],''),[x for x in manifest if x['dictionary']==item['name']],notes,example_notes)
        row.update(title=item['name'],summary=item['description'],body=body)
        item['searchText']=BeautifulSoup(body,'html.parser').get_text(' ',strip=True)
    save(ASSETS/'commands.json',commands);save(ASSETS/'dictionaries.json',dicts);save(HERE/'reference-content.json',records)
    print(json.dumps({'commands':len(commands),'dictionaries':len(dicts),'authored_guides':len(rendered),'command_guides':len(command_html),'complete_example_files':len(manifest)}))

if __name__=='__main__':main()
