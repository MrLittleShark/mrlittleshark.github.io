"""Apply reviewed prose and authored chapters, then refresh the static CMS fallback.

Run after the source-content generators. Course Markdown in authored-lessons is
the edited source; exact prose replacements preserve code and formula blocks.
"""
from pathlib import Path
import json, re, sys
from wolf_media import FIGURES, figure_html

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).parent
SRC = ROOT / 'source-openfoam'

def load(path, fallback=None):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else fallback

def short_figures(body):
    def replace(match):
        markup = match.group()
        for key, item in FIGURES.items():
            if item['file'] in markup:
                return figure_html(key)
        return markup
    return re.sub(r'<figure\b[^>]*class="wolf-figure"[^>]*>[\s\S]*?</figure>', replace, body)

def programming(body):
    body = re.sub(r'^适用版本：[^\n]*先修：([^\n]*)\n', r'先修：\1\n', body)
    body = re.sub(r'\n\*\*本页核验记录：\*\*[^\n]*', '', body)
    body = re.sub(r' · \[下载清单与 SHA-256\]\([^)]*\)', '', body)
    body = re.sub(r'源码应放在用户可写目录中；[^\n]*', '编译需要 v2512 开发环境。解压到个人工作目录后运行上述命令。', body)
    body = re.sub(r'本课依据用户提供的 \*\*Basic OpenFOAM Programming Tutorials\*\*[^\n]*',
                  '源码：Artur K. Lidtke 及贡献者，*Basic OpenFOAM Programming Tutorials*（2017–2021），GPL-3.0-or-later。下载包保留作者信息与许可证。', body)
    body = re.sub(r'下面摘取 `([^`]+)`[^\n]*', r'`\1` 核心代码：', body)
    for old, new in {'## 对照源码':'## 源码解析','## 编译与复现实验':'## 编译与运行',
                     '## 练习与验收':'## 练习','## 来源与延伸':'## 参考资料',
                     '## 怎样判断练习完成':'## 运行结果'}.items():
        body = body.replace(old, new)
    return body

def static_page(row):
    canonical = row.get('metadata', {}).get('canonical_path', '')
    if not canonical or row['kind'] == 'module':
        return
    path = (SRC / canonical.strip('/') / 'index.md').resolve()
    if not path.is_relative_to(SRC.resolve()) or not path.is_file():
        raise RuntimeError('Missing static content page: ' + str(path))
    original = path.read_text(encoding='utf-8')
    match = re.match(r'^(---\n[\s\S]*?\n---\n)', original)
    if not match:
        raise RuntimeError('Missing front matter: ' + str(path))
    header = match.group(1)
    for key, value in [('title', row['title']), ('description', row['summary']), ('cms_slug', row['slug'])]:
        line = key + ': ' + json.dumps(value, ensure_ascii=False)
        if re.search('^' + key + ':', header, re.M):
            header = re.sub('^' + key + ':.*$', lambda m: line, header, flags=re.M)
        else:
            header = header[:-4] + line + '\n---\n'
    path.write_text(header + '\n' + row['body'].strip() + '\n', encoding='utf-8')

def main():
    revisions = load(HERE/'editorial-revisions.json', {})
    metadata = {}
    for file in (HERE/'authored-lessons').glob('*metadata.json'):
        metadata.update(load(file, {}))
    for file in (HERE/'authored-pages').glob('*metadata.json'):
        metadata.update(load(file, {}))
    additions = load(HERE/'programming-explanations.json', {})
    simple = load(HERE/'programming14-correction.json', {})
    cleanups = load(HERE/'programming-cleanup.json', {})
    titles = load(HERE/'programming-titles.json', {})
    walkthrough = load(HERE/'programming10-walkthrough.json', {})
    workflows = {}
    for file in sorted(HERE.glob('programming-workflow-*.json')):
        if not re.fullmatch(r'programming-workflow-\d{2}-\d{2}\.json', file.name):
            continue
        for slug, value in load(file, {}).items():
            assert slug not in workflows, ('Duplicate workflow', slug)
            workflows[slug] = value
    report = []
    for path in sorted(HERE.glob('*content.json')):
        rows = load(path)
        for row in rows:
            before = json.dumps(row, sort_keys=True, ensure_ascii=False)
            slug = row['slug']
            authored = next((p for p in [HERE/'authored-lessons'/f'{slug}.md', HERE/'authored-pages'/f'{slug}.md'] if p.exists()), None)
            if authored:
                row['body'] = authored.read_text(encoding='utf-8').strip()+'\n'
            elif slug in revisions:
                for edit in revisions[slug]['replacements']:
                    old, new = edit['before'], edit['after']
                    assert not old.startswith(('```','<figure','$$')), (slug, 'protected block')
                    new = new.replace(r'\n\n', '\n\n').replace(r'\n|', '\n|')
                    if old in row['body']:
                        row['body'] = row['body'].replace(old, new, 1)
                row['summary'] = revisions[slug]['summary']
            if slug in revisions and slug not in metadata:
                row['summary'] = revisions[slug]['summary']
            if slug in metadata:
                for key, value in metadata[slug].items():
                    if key == 'metadata': row.setdefault('metadata', {}).update(value)
                    elif key in ('title','summary','cover_url'): row[key] = value
            body = short_figures(row['body'])
            if slug.startswith('programming-') and row['kind']=='lesson':
                body = programming(body)
                if additions.get(slug):
                    start, end = '<!-- programming-explanation -->', '<!-- /programming-explanation -->'
                    body = re.sub(re.escape(start)+r'[\s\S]*?'+re.escape(end)+r'\s*', '', body)
                    insertion = start+'\n\n'+additions[slug].strip()+'\n\n'+end+'\n\n'
                    anchor = '## 编译与运行'
                    body = body.replace(anchor, insertion+anchor, 1) if anchor in body else body+'\n'+insertion
            if slug == simple.get('slug'):
                body = simple['body']
                row['summary'] = simple['summary']
                row.setdefault('metadata', {}).update(simple['metadata'])
            for edit in cleanups.get(slug, {}).get('replacements', []):
                body = body.replace(edit['before'], edit['after'])
            if slug == walkthrough.get('slug'):
                body = walkthrough['body']
                row['summary'] = walkthrough['summary']
            if slug in workflows:
                workflow = workflows[slug]
                marker = '<!-- workflow-' + slug + ' -->'
                endmarker = '<!-- /workflow-' + slug + ' -->'
                body = re.sub(re.escape(marker)+r'[\s\S]*?'+re.escape(endmarker)+r'\s*', '', body)
                for edit in workflow.get('replacements', []):
                    body = body.replace(edit['before'], edit['after'])
                if workflow.get('insertion'):
                    anchor = workflow['anchor']
                    assert body.count(anchor) == 1, (slug, 'Workflow anchor', anchor)
                    body = body.replace(anchor, marker+'\n\n'+workflow['insertion'].strip()+'\n\n'+endmarker+'\n\n'+anchor, 1)
            body = body.replace('OpenCFD OpenFOAM v2512', 'OpenFOAM v2512')
            row['body'] = re.sub(r'\n{4,}', '\n\n\n', body).strip()+'\n'
            if slug in titles:
                row['title'] = titles[slug]
            meta = row.setdefault('metadata', {})
            if 'wolf_figures' in meta or '/assets/wolf/' in row['body']:
                meta['wolf_figures'] = [key for key, figure in FIGURES.items() if figure['file'] in row['body']]
            if row.get('track') == 'C++ 入门':
                meta['topics'] = [key for key in meta.get('topics', []) if key != 'cpp']
            for download in row.get('metadata', {}).get('downloads', []):
                desc = download.get('description', '')
                desc = re.sub(r' 含原始归属、GPL 许可证及说明；不含编译产物与历史解。$', '', desc)
                download['description'] = desc
            static_page(row)
            if before != json.dumps(row, sort_keys=True, ensure_ascii=False): report.append(slug)
        path.write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'updated':len(report), 'authored_chapters':len(list((HERE/'authored-lessons').glob('*.md')))}, ensure_ascii=False))

if __name__ == '__main__':
    main()
