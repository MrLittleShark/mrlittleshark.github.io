"""Parse v2512 help without attaching wrapped options to previous entries."""
import re
import json
import html
from pathlib import Path

TRANSLATIONS = json.loads(Path(__file__).with_name('command-options-zh.json').read_text(encoding='utf-8'))
SECONDARY = {'-debug-switch','-info-switch','-opt-switch','-lib','-fileHandler','-no-libs','-doc','-doc-source','-help-man','-help-notes','-help-compat','-hostRoots','-roots','-world','-mpi-no-comm-dup','-mpi-split-by-appnum','-mpi-threads','-listRegisteredSwitches','-listSwitches','-listUnsetSwitches'}


def parse_options(raw):
    entries = []
    active = None
    for line in raw.splitlines():
        start = re.match(r'^\s{1,8}(-(?:-?[A-Za-z0-9][^\n]*|-(?:\s.*)?))$', line.rstrip())
        if start:
            # Shell helpers sometimes pad before <arguments> or an alias.
            parts = re.split(r'\s{2,}(?=[^\s<|\-])', start.group(1), maxsplit=1)
            if len(parts) == 2:
                placeholder = re.match(r'^([A-Z][A-Z_]+)\s{2,}(.+)$', parts[1])
                if placeholder:
                    parts = [parts[0] + ' ' + placeholder[1], placeholder[2]]
            active = [parts[0].strip(), parts[1].strip() if len(parts) == 2 else '']
            entries.append(active)
        elif active is not None and re.match(r'^\s{10,}\S', line):
            active[1] = (active[1] + ' ' + line.strip()).strip()
        elif line.strip():
            active = None
    return [entry for entry in entries if entry[1]]


def parameter_sections(raw):
    entries = []
    for flag, description in parse_options(raw):
        if description not in TRANSLATIONS:
            raise ValueError('Missing Chinese option explanation: ' + flag + ': ' + description)
        entries.append((flag, TRANSLATIONS[description]))
    primary = [x for x in entries if x[0].split()[0] not in SECONDARY][:14]
    more = [x for x in entries if x not in primary]

    def table(rows):
        return '<table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody>' + ''.join(
            '<tr><td><code>' + html.escape(flag) + '</code></td><td>' + html.escape(desc) + '</td></tr>'
            for flag, desc in rows) + '</tbody></table>'
    return (
        '<h2>常用参数</h2>' + table(primary) if primary else '',
        '<details class="command-more-options"><summary>更多参数（' + str(len(more)) + ' 项）</summary>' + table(more) + '</details>' if more else ''
    )
