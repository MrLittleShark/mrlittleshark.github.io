"""Apply Chinese reference explanations without changing examples or authored prose."""
from pathlib import Path
import html
import json
import re
import runpy
from command_options import parameter_sections

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'source-openfoam'
COMMON = re.compile(r'<h2\b[^>]*>常用参数</h2>\s*(?:<div[^>]*>)?\s*<table\b[\s\S]*?</table>(?:\s*</div>)?')
HELP = re.compile(r'<details\b[^>]*>\s*<summary>完整命令帮助</summary>[\s\S]*?</details>')
MORE = re.compile(r'<details class="command-more-options">[\s\S]*?</details>')
PROSE = json.loads(Path(__file__).with_name('reference-prose-zh.json').read_text(encoding='utf-8'))


def localize_prose(body):
    edits = []
    for before, after in PROSE.items():
        if before in body:
            body = body.replace(before, after)
            edits.append({'before': before, 'after': after})
    return body, edits


def localize_command(body, raw):
    common, more = parameter_sections(raw)
    replacements = []
    for pattern, replacement in [(COMMON, common), (HELP, more), (MORE, more)]:
        match = pattern.search(body)
        if match and match.group() != replacement:
            replacements.append({'before': match.group(), 'after': replacement})
            body = body[:match.start()] + replacement + body[match.end():]
    if common and not COMMON.search(body):
        anchor = '<h2>参考</h2>'
        if anchor not in body:
            raise ValueError('Missing insertion point for parameter table')
        replacement = common + more + anchor
        replacements.append({'before': anchor, 'after': replacement})
        body = body.replace(anchor, replacement, 1)
    return body, replacements


def main():
    static_page = runpy.run_path(str(Path(__file__).with_name('apply-editorial.py')))['static_page']
    commands = json.loads((SOURCE/'assets/commands.json').read_text(encoding='utf-8'))
    commands = {'command-' + re.sub('[^a-z0-9]+', '-', x['name'].lower()).strip('-'): x for x in commands}
    report = []
    for path in sorted(Path(__file__).parent.glob('*content.json')):
        rows = json.loads(path.read_text(encoding='utf-8'))
        changed = False
        for row in rows:
            command = commands.get(row['slug'])
            body, edits = localize_prose(row['body'])
            if command:
                file = SOURCE / command.get('helpUrl', '').lstrip('/')
                raw = file.read_text(encoding='utf-8') if file.is_file() else ''
                body, option_edits = localize_command(body, raw)
                edits += option_edits
            if edits:
                row['body'] = body
                static_page(row)
                report.append({'slug': row['slug'], 'replacements': edits})
                changed = True
        if changed:
            path.write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    output = ROOT/'.openfoam-work/chinese-reference'
    output.mkdir(exist_ok=True)
    # Keep the original patch for the publication step on idempotent reruns.
    if report:
        path = output/'changes.json'
        previous = json.loads(path.read_text(encoding='utf-8')) if path.exists() else []
        path.write_text(json.dumps(previous+report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'updated_pages': len(report)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
