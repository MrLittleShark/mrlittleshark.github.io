"""Redraw FoamLab teaching diagrams in one visual language.

Usage: python tools/content/draw-diagrams.py
Writes source-openfoam/assets/diagrams/*.svg. Run it after build-core.py and the
programming/reference generators, which still emit the older drawings.

Part A draws the 24 core-* concept figures by hand.
Part B re-lays out the numbered flow figures (cpp-*, programming-*, reference-*),
keeping their wording but reading it from the existing files.
"""
from pathlib import Path
import html, math, re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'source-openfoam/assets/diagrams'

C = dict(ink='#22302c', muted='#66756f', faint='#9aa59f', line='#d9ddd3', paper='#fbfaf6', white='#ffffff',
         green='#2c6e5a', greenL='#e4efe8', greenM='#9cc5b1', teal='#2f8a86', tealL='#ddefed', tealM='#8fcac4',
         amber='#c98a2b', amberL='#fbeed8', red='#c8553d', redL='#f7e1da', blue='#3b78b5', blueL='#e2edf8', blueM='#9fc1e3',
         grid='#cfd8d1')
FONT = "'Noto Sans SC','PingFang SC','Microsoft YaHei','Source Han Sans SC',sans-serif"
MONO = "'Cascadia Code','JetBrains Mono',Consolas,'DejaVu Sans Mono',monospace"
STYLE = f"""text{{font-family:{FONT};fill:{C['ink']}}}.t{{font-size:19px}}.tb{{font-size:19px;font-weight:700}}.s{{font-size:16px;fill:{C['muted']}}}
.h{{font-size:25px;font-weight:700}}.k{{font-size:13px;fill:{C['green']};font-weight:700;letter-spacing:.12em}}.m{{font-family:{MONO};font-size:16px}}.mb{{font-family:{MONO};font-size:17px;font-weight:700}}
.tag{{font-size:12px;fill:{C['faint']}}}.c{{text-anchor:middle}}.e{{text-anchor:end}}.w{{fill:#fff}}"""

def esc(s): return html.escape(str(s), quote=True)
def T(x, y, s, cls='t', fill=None, anchor=None, extra=''):
    a = f' text-anchor="{anchor}"' if anchor else ''
    style = f'fill:{fill};' if fill else ''
    m = re.search(r'\s*style="([^"]*)"', extra)
    if m:
        style += m.group(1); extra = extra.replace(m.group(0), '')
    f = f' style="{style}"' if style else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}"{a}{f}{extra}>{esc(s)}</text>'
def L(x1, y1, x2, y2, color=C['ink'], w=2, arrow=None, dash=None, cap='round'):
    m = f' marker-end="url(#a-{arrow})"' if arrow else ''
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{w}" stroke-linecap="{cap}"{d}{m}/>'
def P(d, stroke=C['ink'], w=2, fill='none', arrow=None, dash=None, extra=''):
    m = f' marker-end="url(#a-{arrow})"' if arrow else ''
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{ds}{m}{extra}/>'
def R(x, y, w, h, fill=C['white'], stroke=C['line'], rx=12, sw=1.5, extra=''):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'
def Ci(x, y, r, fill=C['ink'], stroke='none', sw=0):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def textw(s, size):
    return sum(size * (1.0 if ord(ch) > 0x2e80 else 0.6) for ch in str(s))
def fit(s, room, size, low=13):
    while size > low and textw(s, size) > room: size -= 0.5
    return size
def card(x, y, w, h, title, sub='', accent=C['green'], fill=C['white'], num=None):
    out = R(x, y, w, h, fill, C['line']) + f'<rect x="{x:.1f}" y="{y + 14:.1f}" width="4" height="{h - 28:.1f}" rx="2" fill="{accent}"/>'
    tx = x + 22
    if num is not None:
        out += Ci(x + 36, y + h / 2, 15, accent) + T(x + 36, y + h / 2 + 5.5, num, 'tb w', anchor='middle', extra=' style="font-size:15px;fill:#fff"')
        tx = x + 62
    room = x + w - tx - 14
    f1 = fit(title, room, 19); f2 = fit(sub, room, 16) if sub else 16
    st = f' style="font-size:{f1}px"' if f1 != 19 else ''
    if sub:
        out += T(tx, y + h / 2 - 4, title, 'tb', extra=st) + T(tx, y + h / 2 + 22, sub, 's', extra=f' style="font-size:{f2}px"' if f2 != 16 else '')
    else:
        out += T(tx, y + h / 2 + 7, title, 'tb', extra=st)
    return out

def svg(name, title, body, w=960, h=500, kicker=None, note='FoamLab 示意图'):
    markers = ''.join(f'<marker id="a-{k}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1.2 9 5 1 8.8 2.8 5z" fill="{v}"/></marker>'
                      for k, v in [('ink', C['ink']), ('green', C['green']), ('teal', C['teal']), ('muted', C['muted']), ('amber', C['amber']), ('red', C['red']), ('blue', C['blue'])])
    head = (T(36, 44, kicker, 'k') if kicker else '') + T(36, 76 if kicker else 54, title, 'h')
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}">'
           f'<title>{esc(title)}</title><defs>{markers}<pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0v8" stroke="{C["muted"]}" stroke-width="1.6"/></pattern></defs><style>{STYLE}</style>'
           f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="20" fill="{C["paper"]}" stroke="{C["line"]}" stroke-width="1.5"/>'
           f'{head}{body}{T(w - 28, h - 20, note, "tag", anchor="end")}</svg>')
    (OUT / f'{name}.svg').write_text(doc, encoding='utf-8')
    return name

def grid(x, y, nx, ny, dx, dy, color=C['grid'], w=1.2):
    s = ''.join(L(x + i * dx, y, x + i * dx, y + ny * dy, color, w, cap='butt') for i in range(nx + 1))
    return s + ''.join(L(x, y + j * dy, x + nx * dx, y + j * dy, color, w, cap='butt') for j in range(ny + 1))

def poly(pts, stroke=C['ink'], w=2, fill='none', close=False):
    d = 'M' + ' L'.join(f'{a:.1f} {b:.1f}' for a, b in pts) + (' Z' if close else '')
    return P(d, stroke, w, fill)

# ---------------------------------------------------------------- Part A
def core():
    made = []
    # 1 architecture
    b = ''
    xs = [40, 270, 500, 730]
    items = [('物理问题', '假设 · 参数 · 关心的量', C['amber']), ('算例文件', '0 / constant / system', C['green']), ('求解器与库', '离散 · 线性求解 · 模型', C['teal']), ('数值结果', '场 · 曲线 · 积分量', C['blue'])]
    for x, (t, s, c) in zip(xs, items):
        b += card(x, 120, 190, 96, t, s, c)
    for x in xs[:-1]:
        b += L(x + 194, 168, x + 226, 168, C['ink'], 2, 'ink')
    b += R(150, 296, 660, 112, C['greenL'], C['greenM'])
    b += T(480, 330, '工具程序贯穿整个流程', 'tb', anchor='middle')
    tools = ['blockMesh', 'checkMesh', 'decomposePar', 'postProcess', 'foamToVTK']
    for i, t in enumerate(tools):
        x = 186 + i * 122
        b += R(x, 350, 112, 36, C['white'], C['greenM'], 8) + T(x + 56, 374, t, 'm', anchor='middle', extra=' style="font-size:14px"')
    for x in [365, 595, 825]:
        b += L(x - 230 + 115 if False else x - 230 + 0, 0, 0, 0, 'none', 0) if False else ''
    b += L(365, 292, 365, 222, C['green'], 2, 'green', '5 5') + L(595, 292, 595, 222, C['green'], 2, 'green', '5 5')
    b += T(480, 448, '记录 OpenFOAM 版本与编译信息，结果才能追溯到产生它的程序', 's', anchor='middle')
    made.append(svg('core-architecture', 'OpenFOAM：从物理问题到数值结果', b))

    # 2 case tree
    b = R(60, 96, 420, 344, '#1f2a27', '#1f2a27', 14)
    rows = [('cavity/', '#ffffff'), ('├─ 0/', '#f2c879'), ('│  ├─ U', '#cfd8d3'), ('│  └─ p', '#cfd8d3'), ('├─ constant/', '#9fdcc6'), ('│  ├─ transportProperties', '#cfd8d3'),
            ('│  └─ polyMesh/  (blockMesh 生成)', '#8aa39a'), ('└─ system/', '#93cde8'), ('   ├─ controlDict', '#cfd8d3'), ('   ├─ fvSchemes', '#cfd8d3'), ('   ├─ fvSolution', '#cfd8d3'), ('   └─ blockMeshDict', '#cfd8d3')]
    y = 126
    for txt, col in rows:
        b += f'<text x="84" y="{y}" class="m" style="fill:{col};font-size:16px;white-space:pre" xml:space="preserve">{esc(txt)}</text>'
        y += 26.5
    ann = [(150, '0/', '初始条件与边界条件', '每个场一个文件，首行写明量纲', C['amber'], C['amberL']),
           (258, 'constant/', '网格与物性', '运行中不变的数据', C['green'], C['greenL']),
           (378, 'system/', '怎么算', '时间控制、离散格式、线性求解', C['blue'], C['blueL'])]
    for yy, k, t, s, c, cl in ann:
        b += R(540, yy - 44, 360, 82, cl, c, 12, 1.2) + T(560, yy - 12, t, 'tb', fill=c) + T(560, yy + 16, s, 's')
    b += L(486, 148, 534, 148, C['amber'], 2, 'amber', '4 4') + L(486, 256, 534, 256, C['green'], 2, 'green', '4 4') + L(486, 376, 534, 376, C['blue'], 2, 'blue', '4 4')
    made.append(svg('core-case-tree', '一个算例的三个输入目录', b))

    # 3 cavity
    x0, y0, s = 320, 150, 270
    b = R(x0, y0, s, s, C['blueL'], 'none', 0)
    b += f'<rect x="{x0 - 12}" y="{y0}" width="12" height="{s + 12}" fill="url(#hatch)"/><rect x="{x0 + s}" y="{y0}" width="12" height="{s + 12}" fill="url(#hatch)"/><rect x="{x0}" y="{y0 + s}" width="{s}" height="12" fill="url(#hatch)"/>'
    b += L(x0, y0, x0, y0 + s, C['ink'], 3, cap='butt') + L(x0 + s, y0, x0 + s, y0 + s, C['ink'], 3, cap='butt') + L(x0, y0 + s, x0 + s, y0 + s, C['ink'], 3, cap='butt')
    b += L(x0 - 10, y0 - 4, x0 + s + 10, y0 - 4, C['red'], 6, cap='butt')
    for i in range(4): b += L(x0 + 30 + i * 70, y0 - 24, x0 + 80 + i * 70, y0 - 24, C['red'], 2.5, 'red')
    cx, cy = x0 + s * .56, y0 + s * .4
    for k, (rx, ry) in enumerate([(118, 104), (82, 70), (46, 38)]):
        b += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{C["blue"]}" stroke-width="{2.6 - k * .5}" opacity="{.9 - k * .2}"/>'
        b += P(f'M{cx + 8} {cy - ry} l-14 -7 M{cx + 8} {cy - ry} l-14 7', C['blue'], 2.4 - k * .4)
    b += Ci(cx, cy, 4, C['blue'])
    b += T(x0 + s / 2, y0 - 44, 'movingWall：U = (1 0 0) m/s', 'mb', anchor='middle', fill=C['red'])
    b += T(x0 - 26, y0 + s / 2, 'fixedWalls', 'm', anchor='end') + T(x0 - 26, y0 + s / 2 + 24, 'noSlip', 's', anchor='end')
    b += T(x0 + s + 26, y0 + s / 2, 'fixedWalls', 'm') + T(x0 + s + 26, y0 + s / 2 + 24, 'noSlip', 's')
    b += L(x0, y0 + s + 36, x0 + s, y0 + s + 36, C['muted'], 1.5, 'muted') + L(x0 + s, y0 + s + 36, x0, y0 + s + 36, C['muted'], 1.5, 'muted') + T(x0 + s / 2, y0 + s + 58, 'L = 0.1 m', 's', anchor='middle')
    b += R(690, 290, 240, 132, C['white'], C['line']) + T(708, 320, '二维算例', 'tb') + T(708, 348, 'frontAndBack：empty', 'm', extra=' style="font-size:14px"') + T(708, 376, 'ν = 0.01 m²/s', 's') + T(708, 402, 'Re = UL/ν = 10', 's')
    made.append(svg('core-cavity', '顶盖驱动方腔：边界条件与主涡', b))

    # 4 dimensions
    b = ''
    heads = [('M', '质量', 'kg'), ('L', '长度', 'm'), ('T', '时间', 's'), ('Θ', '温度', 'K'), ('N', '物质的量', 'mol'), ('I', '电流', 'A'), ('J', '发光强度', 'cd')]
    x0, cw = 250, 92
    for i, (sym, name, unit) in enumerate(heads):
        x = x0 + i * cw
        b += R(x + 4, 104, cw - 8, 74, C['greenL'], 'none', 10) + T(x + cw / 2, 136, sym, 'mb', anchor='middle', fill=C['green']) + T(x + cw / 2, 160, name, 's', anchor='middle', extra=' style="font-size:13px"')
    rows = [('U  速度', [0, 1, -1, 0, 0, 0, 0], 'm/s'), ('p  运动学压力', [0, 2, -2, 0, 0, 0, 0], 'm²/s²'), ('nu  运动黏度', [0, 2, -1, 0, 0, 0, 0], 'm²/s'), ('T  温度', [0, 0, 0, 1, 0, 0, 0], 'K')]
    for j, (lab, v, unit) in enumerate(rows):
        y = 214 + j * 62
        b += R(40, y, 880, 50, C['white'], C['line'], 10) + T(60, y + 32, lab, 'tb')
        for i, n in enumerate(v):
            x = x0 + i * cw + cw / 2
            if n: b += Ci(x, y + 25, 18, C['amberL'], C['amber'], 1.2)
            b += T(x, y + 31, str(n).replace('-', '−'), 'mb', anchor='middle', fill=C['ink'] if n else C['faint'])
        b += T(905, y + 32, unit, 'm', anchor='end', fill=C['green'])
    b += T(480, 480 - 8, 'dimensions [0 1 −1 0 0 0 0]; 七个指数依次对应上面七个基本量', 's', anchor='middle')
    made.append(svg('core-dimensions', '量纲：七个指数的排列顺序', b))

    # 5 time
    b = ''
    x0, x1, y = 90, 870, 230
    b += L(x0, y, x1 + 20, y, C['ink'], 2.5, 'ink')
    n = 100
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        b += L(x, y - 7, x, y + 7, C['faint'], 1.2)
    for k in range(6):
        x = x0 + (x1 - x0) * k / 5
        b += Ci(x, y, 8, C['green'])
        b += R(x - 34, y + 34, 68, 46, C['greenL'], C['greenM'], 8) + P(f'M{x - 34} {y + 42} h22 l6 -8 h12', C['greenM'], 1.2) + T(x, y + 64, f'{k / 10:.1f}' if k else '0', 'mb', anchor='middle', fill=C['green'])
        b += L(x, y + 10, x, y + 32, C['green'], 1.5, dash='3 3')
    # zoom
    b += P(f'M{x0} {y - 12} L{x0 + 8} {y - 70} M{x0 + 7.8 * 3} {y - 12} L{x0 + 7.8 * 3 + 8} {y - 70}', C['muted'], 1, dash='3 3')
    b += R(x0 + 8, y - 120, 170, 50, C['white'], C['line'], 8) + ''.join(L(x0 + 30 + i * 42, y - 104, x0 + 30 + i * 42, y - 86, C['ink'], 1.5) for i in range(4)) + L(x0 + 30, y - 95, x0 + 156, y - 95, C['ink'], 1.5)
    b += T(x0 + 51, y - 128, 'Δt = 0.005 s', 's', anchor='middle', extra=' style="font-size:14px"')
    b += T(330, y - 92, '每个小刻度：求解器推进一个时间步 Δt', 't') + T(330, y - 62, '每个文件夹：写出一个时间目录', 't', fill=C['green'])
    b += R(170, 370, 620, 76, C['white'], C['line']) + T(480, 400, 'deltaT 0.005;  writeControl timeStep;  writeInterval 20;', 'm', anchor='middle') + T(480, 428, '→ 每 20 步、即每 0.1 s 保存一次结果', 's', anchor='middle')
    b += T(x1 + 12, y + 30, 't / s', 's')
    made.append(svg('core-time', '时间步与写出间隔', b))

    # 6 block vertices (oblique projection)
    def pr(x, y, z):  # x right, y depth, z up
        return 330 + x * 260 + y * 120, 400 - z * 220 - y * 90
    V = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
    E = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    hidden = {(2, 3), (3, 0), (3, 7)}
    b = poly([pr(*V[i]) for i in [0, 1, 5, 4]], 'none', 0, C['greenL'], True)
    for a, c in E:
        (xa, ya), (xc, yc) = pr(*V[a]), pr(*V[c])
        h_ = (a, c) in hidden or (c, a) in hidden
        b += L(xa, ya, xc, yc, C['faint'] if h_ else C['ink'], 1.8 if h_ else 2.4, dash='6 5' if h_ else None)
    for i, v in enumerate(V):
        x, y = pr(*v)
        b += Ci(x, y, 15, C['white'], C['green'], 2) + T(x, y + 6, str(i), 'mb', anchor='middle', fill=C['green'])
    ox, oy = pr(0, 0, 0)
    b += L(ox - 120, oy + 30, ox - 50, oy + 30, C['red'], 2.5, 'red') + T(ox - 44, oy + 36, 'x₁', 'tb', fill=C['red'])
    b += L(ox - 120, oy + 30, ox - 120, oy - 40, C['blue'], 2.5, 'blue') + T(ox - 128, oy - 48, 'x₃', 'tb', fill=C['blue'])
    b += L(ox - 120, oy + 30, ox - 78, oy - 2, C['teal'], 2.5, 'teal') + T(ox - 74, oy - 6, 'x₂', 'tb', fill=C['teal'])
    b += R(40, 100, 230, 160, C['white'], C['line']) + T(58, 132, 'hex (0 1 2 3 4 5 6 7)', 'm', extra=' style="font-size:14px"') + T(58, 164, '底面 0-1-2-3', 's') + T(58, 188, '顶面 4-5-6-7', 's') + T(58, 218, '按右手法则排列；', 's') + T(58, 242, '0→1 定义 x₁ 方向', 's')
    made.append(svg('core-block-vertices', 'blockMesh：六面体块的八个顶点', b))

    # 7 mesh quality
    def cellpair(ox, skew):
        out = ''
        Pc = (ox + 110, 280)
        f0 = (ox + 220, 170 - skew * .2); f1 = (ox + 220 + skew, 390)
        left = [(ox, 170), f0, f1, (ox, 390)]
        right = [f0, (ox + 420 - 40 + skew * .2, 150 + skew * .4), (ox + 420 - 20 + skew * .6, 400), f1]
        out += poly(left, C['ink'], 2, C['blueL'], True) + poly(right, C['ink'], 2, C['tealL'], True)
        N = ((right[0][0] + right[1][0] + right[2][0] + right[3][0]) / 4, (right[0][1] + right[1][1] + right[2][1] + right[3][1]) / 4 + skew * .5)
        fm = ((f0[0] + f1[0]) / 2, (f0[1] + f1[1]) / 2)
        out += L(*Pc, *N, C['red'], 2.4, 'red')
        dx, dy = f1[1] - f0[1], -(f1[0] - f0[0]); n = math.hypot(dx, dy); dx, dy = dx / n * 70, dy / n * 70
        out += L(fm[0], fm[1], fm[0] + dx, fm[1] + dy, C['green'], 3, 'green')
        out += Ci(*Pc, 6) + T(Pc[0] - 10, Pc[1] - 14, 'P', 'tb') + Ci(*N, 6) + T(N[0] + 10, N[1] - 12, 'N', 'tb')
        out += T(fm[0] + dx + 6, fm[1] + dy - 8, 'S_f', 'mb', fill=C['green'])
        return out, Pc, N, fm
    b, *_ = cellpair(60, 0)
    b += T(270, 450, '正交：d ∥ S_f', 'tb', anchor='middle')
    b2, Pc, N, fm = cellpair(500, 70)
    b += b2 + T(710, 450, '非正交：d 与 S_f 夹角 θ', 'tb', anchor='middle')
    b += T(Pc[0] + 60, Pc[1] + 26, 'd', 'mb', fill=C['red']) + T(140 + 60, 306, 'd', 'mb', fill=C['red'])
    b += T(480, 114, 'checkMesh 报告最大非正交角；角度越大，扩散项越依赖非正交修正', 's', anchor='middle')
    made.append(svg('core-mesh-quality', '网格质量：非正交角从哪里来', b))

    # 8 CAD tessellation
    cx, cy, r = 300, 400, 210
    arc = 'M{} {} A{} {} 0 0 1 {} {}'.format(cx - r, cy, r, r, cx + r, cy)
    b = P(arc, C['blue'], 4)
    seg = 4
    pts = [(cx - r * math.cos(math.pi * i / seg), cy - r * math.sin(math.pi * i / seg)) for i in range(seg + 1)]
    b += poly(pts, C['teal'], 2.6) + ''.join(Ci(x, y, 5, C['teal']) for x, y in pts)
    a = math.pi * 1.5 / seg; mx, my = cx - r * math.cos(a), cy - r * math.sin(a)
    ch = ((pts[1][0] + pts[2][0]) / 2, (pts[1][1] + pts[2][1]) / 2)
    b += L(mx, my, ch[0], ch[1], C['red'], 3) + T(mx - 24, my - 14, '弦高误差 h', 'tb', fill=C['red'], anchor='end')
    b += R(560, 130, 360, 260, C['white'], C['line'])
    b += L(584, 168, 620, 168, C['blue'], 4) + T(632, 174, '连续曲面：STEP / 原生 CAD', 't')
    b += L(584, 210, 620, 210, C['teal'], 2.6) + Ci(584, 210, 5, C['teal']) + Ci(620, 210, 5, C['teal']) + T(632, 216, '三角面片：STL / OBJ', 't')
    b += T(584, 262, 'h ≈ R(1 − cos(θ/2))', 'mb') + T(584, 296, '曲率大的地方需要更密的三角面，', 's') + T(584, 322, '否则 snappyHexMesh 贴合的', 's') + T(584, 348, '是一个“多边形”而不是曲面。', 's')
    made.append(svg('core-cad-tessellation', 'CAD 曲面与离散三角面不等价', b))

    # 9 snappy stages
    b = ''
    titles = [('1  castellatedMesh', '切除体内单元，局部加密'), ('2  snap', '把边界点投影到表面'), ('3  addLayers', '在壁面插入边界层')]
    for k, (tt, ss) in enumerate(titles):
        ox, oy, w = 40 + k * 300, 110, 280
        b += R(ox, oy, w, 330, C['white'], C['line'])
        gx, gy, cs = ox + 30, oy + 30, 22
        cxk, cyk, rr = ox + w / 2, oy + 140, 62
        b += f'<g>'
        for i in range(10):
            for j in range(10):
                x, y = gx + i * cs, gy + j * cs
                c = (x + cs / 2, y + cs / 2)
                inside = math.hypot(c[0] - cxk, c[1] - cyk) < rr
                if k == 0 and inside: continue
                b += f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{C["blueL"]}" stroke="{C["blueM"]}" stroke-width="1"/>'
        b += '</g>'
        if k == 0:
            b += f'<circle cx="{cxk}" cy="{cyk}" r="{rr}" fill="none" stroke="{C["red"]}" stroke-width="2.5" stroke-dasharray="6 5"/>'
        else:
            b += f'<circle cx="{cxk}" cy="{cyk}" r="{rr + (14 if k == 2 else 0)}" fill="{C["blueL"]}" stroke="{C["blueM"]}" stroke-width="1"/>'
            if k == 2:
                for rr2 in [rr + 4, rr + 8]:
                    b += f'<circle cx="{cxk}" cy="{cyk}" r="{rr2}" fill="none" stroke="{C["teal"]}" stroke-width="1.4"/>'
                for i in range(16):
                    a = 2 * math.pi * i / 16
                    b += L(cxk + rr * math.cos(a), cyk + rr * math.sin(a), cxk + (rr + 14) * math.cos(a), cyk + (rr + 14) * math.sin(a), C['teal'], 1.2)
            b += f'<circle cx="{cxk}" cy="{cyk}" r="{rr}" fill="{C["paper"]}" stroke="{C["red"]}" stroke-width="2.5"/>'
        b += T(ox + 20, oy + 278, tt, 'mb', fill=C['green']) + T(ox + 20, oy + 306, ss, 's')
    for k in range(2):
        b += L(325 + k * 300, 270, 337 + k * 300, 270, C['ink'], 2, 'ink')
    made.append(svg('core-snappy-stages', 'snappyHexMesh 的三个阶段', b))

    # 10 finite volume
    cx, cy, s = 330, 280, 130
    b = ''
    for dx_, dy_, lab in [(-1, 0, 'W'), (1, 0, 'E'), (0, -1, 'N'), (0, 1, 'S')]:
        b += R(cx - s / 2 + dx_ * s, cy - s / 2 + dy_ * s, s, s, C['white'], C['grid'], 0, 1.5) + Ci(cx + dx_ * s, cy + dy_ * s, 5, C['muted']) + T(cx + dx_ * s + 10, cy + dy_ * s - 10, lab, 't', fill=C['muted'])
    b += R(cx - s / 2, cy - s / 2, s, s, C['greenL'], C['green'], 0, 3) + Ci(cx, cy, 6, C['green']) + T(cx + 10, cy - 10, 'P', 'tb', fill=C['green'])
    fx = cx + s / 2
    b += L(fx, cy - s / 2, fx, cy + s / 2, C['red'], 5, cap='butt') + L(fx, cy + 30, fx + 70, cy + 30, C['red'], 3, 'red') + T(fx + 76, cy + 36, 'S_f', 'mb', fill=C['red']) + T(fx + 8, cy - s / 2 - 10, 'f', 'tb', fill=C['red'])
    b += L(cx, cy, cx + s, cy, C['muted'], 1.5, dash='4 4') + T(cx + s / 2 + 10, cy - 8, 'd', 'm', fill=C['muted'], extra='')
    b += R(600, 130, 320, 300, C['white'], C['line'])
    b += T(620, 166, '1. 对控制体 P 积分', 'tb') + T(620, 196, '∫∇·U dV = ∮U·dS', 'mb', fill=C['green'])
    b += T(620, 246, '2. 体积分变成面通量之和', 'tb') + T(620, 276, 'Σ_f S_f·U_f = 0', 'mb', fill=C['green'])
    b += T(620, 326, '3. 面值由相邻单元插值', 'tb') + T(620, 356, 'U_f ≈ w U_P + (1−w) U_E', 'mb', fill=C['green'])
    b += T(620, 400, '相邻单元共享一个面：P 流出的', 's') + T(620, 422, '就是 E 流入的，守恒自然成立。', 's')
    made.append(svg('core-finite-volume', '有限体积：把守恒方程积分到单元', b))

    # 11 convection
    ox, oy, w, h = 90, 100, 780, 230
    b = L(ox, oy + h, ox + w + 10, oy + h, C['ink'], 2, 'ink') + L(ox, oy + h, ox, oy - 10, C['ink'], 2, 'ink') + T(ox + w + 14, oy + h + 6, 'x', 't') + T(ox - 10, oy - 18, 'φ', 'tb')
    y0, y1 = oy + h - 10, oy + 40
    b += P(f'M{ox} {y0} H{ox + 260} V{y1} H{ox + 520} V{y0} H{ox + w}', C['ink'], 2.5, dash='7 6')
    b += P(f'M{ox} {y0} C{ox + 190} {y0} {ox + 220} {y1 + 60} {ox + 300} {y1 + 30} S{ox + 450} {y1 + 20} {ox + 500} {y1 + 60} S{ox + 600} {y0} {ox + w} {y0}', C['blue'], 3.5)
    b += P(f'M{ox} {y0} H{ox + 220} Q{ox + 245} {y0 + 28} {ox + 258} {y0} L{ox + 262} {y1} Q{ox + 280} {y1 - 34} {ox + 302} {y1} H{ox + 480} Q{ox + 505} {y1 - 30} {ox + 518} {y1} L{ox + 522} {y0} Q{ox + 540} {y0 + 30} {ox + 560} {y0} H{ox + w}', C['red'], 2.6)
    lg = [(C['ink'], '参考解（间断）', '7 6'), (C['blue'], '一阶迎风：抹平间断（数值扩散）', None), (C['red'], '中心格式：间断附近振荡（过冲 / 欠冲）', None)]
    for i, (c, t, d) in enumerate(lg):
        b += L(110, 420 + i * 0 + 0, 110, 420, c, 0)
    for i, (c, t, d) in enumerate(lg):
        b += L(110, 372 + i * 28, 150, 372 + i * 28, c, 3, dash=d) + T(162, 378 + i * 28, t, 's', extra=' style="font-size:15px"')
    b += T(900, 462, '有界的限制器格式（limitedLinear、vanLeer）在两者之间折中', 's', anchor='end')
    made.append(svg('core-convection', '对流离散：数值扩散与振荡', b))

    # 12 diffusion
    b = ''
    x0, x1, yb = 150, 810, 200
    b += R(x0, yb, x1 - x0, 60, C['white'], C['ink'], 4, 2)
    for i in range(10):
        x = x0 + (x1 - x0) * (i + .5) / 10
        b += L(x0 + (x1 - x0) * i / 10, yb, x0 + (x1 - x0) * i / 10, yb + 60, C['grid'], 1)
    b += R(x0 - 44, yb - 10, 44, 80, C['redL'], C['red'], 6) + T(x0 - 22, yb + 36, '热', 'tb', anchor='middle', fill=C['red'])
    b += R(x1, yb - 10, 44, 80, C['blueL'], C['blue'], 6) + T(x1 + 22, yb + 36, '冷', 'tb', anchor='middle', fill=C['blue'])
    py0, py1 = 318, 432
    b += L(x0, py1, x1 + 20, py1, C['ink'], 1.5, 'ink') + L(x0, py1, x0, py0 - 20, C['ink'], 1.5, 'ink') + T(x0 - 8, py0 - 28, 'T', 'tb', anchor='end')
    b += L(x0, py0, x1, py1 - 10, C['green'], 3)
    for i in range(10):
        x = x0 + (x1 - x0) * (i + .5) / 10; y = py0 + (py1 - 10 - py0) * (i + .5) / 10
        b += Ci(x, y, 5.5, C['white'], C['green'], 2) + L(x, yb + 62, x, py1, C['grid'], 1, dash='2 4')
    b += T(x0, py1 + 26, '400 K', 's', anchor='middle') + T(x1, py1 + 26, '300 K', 's', anchor='middle')
    b += T(480, 120, '常导热系数、无热源、稳态：T(x) = T₀ + (T₁ − T₀)·x / L', 't', anchor='middle')
    b += T(480, 150, '线性分布在任何均匀网格上都应被精确求出——适合检验扩散离散', 's', anchor='middle')
    made.append(svg('core-diffusion', '一维导热：用解析解检验扩散离散', b))

    # 13 courant
    b = ''
    for row, (co, col, lab, sub) in enumerate([(0.6, C['green'], 'Co = 0.6', '一个时间步内，信息只走到相邻单元'), (2.2, C['red'], 'Co = 2.2', '一步跨过两个单元，显式格式会失稳')]):
        oy = 130 + row * 160
        for i in range(6):
            b += R(120 + i * 110, oy, 110, 70, C['white'] if i != 1 else C['greenL'], C['grid'], 0, 1.4)
        sx = 175 + 110
        ex = sx + co * 110
        b += Ci(sx, oy + 35, 8, col) + L(sx, oy + 35, ex, oy + 35, col, 3, 'green' if row == 0 else 'red')
        b += T(sx, oy - 10, 'U·Δt', 'm', fill=col)
        b += T(820, oy + 42, lab, 'mb', fill=col) + T(120, oy + 98, sub, 's')
    b += L(450, 112, 560, 112, C['muted'], 1.4, 'muted') + L(560, 112, 450, 112, C['muted'], 1.4, 'muted') + T(505, 104, 'Δx', 'm', anchor='middle', fill=C['muted'])
    b += R(180, 430 - 8, 600, 46, C['greenL'], 'none', 10) + T(480, 452, 'Co = U·Δt / Δx      maxCo + adjustTimeStep 可自动控制', 'm', anchor='middle', extra=' style="font-size:15px"')
    made.append(svg('core-courant', 'Courant 数：一步走过几个网格', b))

    # 14 coupling
    b = ''
    nodes = [(90, 150, '动量预测', '用当前压力求 U*', C['amber']), (370, 150, '压力方程', '由连续性 ∇·U = 0 导出', C['green']), (650, 150, '修正', '更新通量 φ、速度 U', C['teal'])]
    for x, y, t, s, c in nodes:
        b += card(x, y, 230, 96, t, s, c)
    b += L(324, 198, 364, 198, C['ink'], 2, 'ink') + L(604, 198, 644, 198, C['ink'], 2, 'ink')
    b += P('M765 250 V300 H485 V256', C['green'], 2, arrow='green', dash='6 5') + T(625, 290, 'PISO：时间步内多次压力校正', 's', anchor='middle', extra=' style="font-size:14px"')
    b += P('M765 250 V340 H205 V256', C['amber'], 2, arrow='amber') + T(485, 362, '外迭代：回到动量方程', 's', anchor='middle', extra=' style="font-size:14px"')
    rows = [('SIMPLE', '稳态；外迭代 + 松弛', C['amber']), ('PISO', '瞬态；小时间步内的压力校正', C['green']), ('PIMPLE', '瞬态；PISO 外面再套外迭代，可用大时间步', C['teal'])]
    for i, (k, s, c) in enumerate(rows):
        b += T(110 + i * 270, 418, k, 'mb', fill=c) + T(110 + i * 270, 444, s, 's', extra=' style="font-size:13.5px"')
    made.append(svg('core-coupling', '压力–速度耦合：预测、校正、再预测', b))

    # 15 residual
    ox, oy, w, h = 100, 120, 620, 270
    b = L(ox, oy + h, ox + w + 10, oy + h, C['ink'], 2, 'ink') + L(ox, oy + h, ox, oy - 10, C['ink'], 2, 'ink') + L(ox + w, oy + h, ox + w, oy - 10, C['ink'], 1.2)
    b += T(ox + w + 8, oy + h + 24, '迭代步', 's', anchor='end') + T(ox - 10, oy - 18, 'log 残差', 's', fill=C['blue']) + T(ox + w + 10, oy - 18, '监测量', 's', fill=C['amber'])
    pts = [(ox + i * w / 60, oy + 20 + (h - 40) * (1 - math.exp(-i / 14)) + 6 * math.sin(i * 1.7)) for i in range(61)]
    b += poly(pts, C['blue'], 2.6)
    pts2 = [(ox + i * w / 60, oy + h - 40 - 150 * (1 - math.exp(-i / 30)) + 8 * math.sin(i / 3)) for i in range(61)]
    b += poly(pts2, C['amber'], 3)
    b += f'<rect x="{ox + 250}" y="{oy}" width="200" height="{h}" fill="{C["amber"]}" opacity=".08"/>' + T(ox + 350, oy + 30, '残差已经很低', 's', anchor='middle') + T(ox + 350, oy + 54, '监测量仍在变化', 'tb', anchor='middle', fill=C['amber'])
    b += R(750, 140, 180, 220, C['white'], C['line'])
    for i, t in enumerate(['残差下降', '质量守恒', '监测量平稳', '网格加密对比']):
        b += Ci(772, 176 + i * 46, 9, C['greenL'], C['green'], 1.5) + P(f'M767 {176 + i * 46} l4 4 7 -8', C['green'], 1.8) + T(790, 182 + i * 46, t, 't', extra=' style="font-size:16px"')
    b += T(480, 456, '判断收敛要同时看几项，残差只是其中之一', 's', anchor='middle')
    made.append(svg('core-residual', '残差下降，不等于结果已经收敛', b))

    # 16 wall
    b = ''
    x0, x1, yw = 100, 560, 420
    b += f'<rect x="{x0}" y="{yw}" width="{x1 - x0}" height="16" fill="url(#hatch)"/>' + L(x0, yw, x1, yw, C['ink'], 3, cap='butt')
    ys = [0]; d = 10
    while ys[-1] < 240: ys.append(ys[-1] + d); d *= 1.35
    for yy in ys[1:]:
        b += L(x0, yw - yy, x1, yw - yy, C['grid'], 1.2)
    for i in range(9): b += L(x0 + i * 57.5, yw, x0 + i * 57.5, yw - ys[-1], C['grid'], 1.2)
    top = ys[-1]
    prof = [(x0 + 20 + 380 * (min(1, (y / top)) ** (1 / 7)), yw - y) for y in [top * (i / 30) ** 2 for i in range(0, 31)]]
    b += poly(prof, C['blue'], 3)
    for y in [ys[1] * .5, 50, 130, 230]:
        u = 380 * (min(1, y / top)) ** (1 / 7)
        b += L(x0 + 20, yw - y, x0 + 20 + u - 4, yw - y, C['blue'], 1.6, 'blue')
    b += Ci(x0 + 48, yw - ys[1] / 2, 4.5, C['red']) + L(x0 + 30, yw, x0 + 30, yw - ys[1] / 2, C['red'], 2) + T(x0 + 60, yw - 2, '第一层中心距 y', 's', fill=C['red'], extra=' style="font-size:14px"') if False else ''
    b += Ci(x0 + 48, yw - ys[1] / 2, 4.5, C['red']) + T(x0 + 60, yw - 10, '← 第一层单元中心 y', 's', fill=C['red'], extra=' style="font-size:14px"')
    bands = [(0, 5, '黏性底层', 'y⁺ < 5', C['tealL']), (5, 30, '缓冲层', '5 – 30', C['amberL']), (30, 300, '对数层', '30 – 300', C['greenL'])]
    bx = 620
    for i, (a, c, t, r_, col) in enumerate(bands):
        y = 340 - i * 100
        b += R(bx, y - 10, 300, 84, col, 'none', 12) + T(bx + 18, y + 22, t, 'tb') + T(bx + 18, y + 50, 'y⁺ ' + r_ if i else r_, 'm', extra=' style="font-size:15px"')
    b += T(bx + 150, 112, 'y⁺ = u_τ · y / ν', 'mb', anchor='middle', fill=C['green'])
    b += T(bx, 446, '低 Re 模型：第一层落在黏性底层', 's', extra=' style="font-size:14px"') + T(bx, 470, '壁面函数：第一层落在对数层', 's', extra=' style="font-size:14px"')
    made.append(svg('core-wall', '壁面分辨率：第一层单元放在哪一层', b))

    # 17 vof
    b = ''
    gx, gy, cs, n = 90, 110, 46, 8
    def surf(x): return gy + 150 + 40 * math.sin((x - gx) / 110)
    for i in range(n * 2 - 1):
        for j in range(n - 1):
            x, y = gx + i * cs, gy + j * cs
            # fraction below the surface (water)
            sub = 0
            for k in range(8):
                xx = x + (k + .5) * cs / 8; ys_ = surf(xx)
                sub += min(1, max(0, (y + cs - ys_) / cs))
            a = sub / 8
            col = f'rgba(59,120,181,{0.12 + 0.62 * a:.2f})'
            b += f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{col}" stroke="#ffffff" stroke-width="1.5"/>'
            if i in (3, 7, 11) and j in (1, 2, 3, 4):
                b += T(x + cs / 2, y + cs / 2 + 5, f'{a:.1f}' if 0 < a < 1 else str(int(round(a))), 'm', anchor='middle', fill='#fff' if a > .55 else C['ink'], extra=' style="font-size:13px"')
    pts = [(gx + k * 5, surf(gx + k * 5)) for k in range(int((n * 2 - 1) * cs / 5) + 1)]
    b += poly(pts, C['red'], 2.6)
    b += T(gx + 6, gy - 14, 'alpha.water', 'mb', fill=C['blue']) + T(gx + 150, gy - 14, '1 = 水   0 = 空气   0 < α < 1 = 界面所在单元', 's')
    b += T(480, 470, '红线是真实界面；VOF 只知道每个单元里水占的体积分数', 's', anchor='middle')
    made.append(svg('core-vof', 'VOF：用体积分数表示界面', b))

    # 18 heat
    b = R(90, 120, 380, 260, C['blueL'], 'none', 0) + R(470, 120, 380, 260, C['amberL'], 'none', 0)
    b += f'<rect x="470" y="120" width="380" height="260" fill="url(#hatch)" opacity=".18"/>'
    b += L(470, 110, 470, 390, C['red'], 4, cap='butt')
    for k in range(4):
        y = 160 + k * 60
        b += P(f'M110 {y} C180 {y - 14} 250 {y + 14} 330 {y}', C['blue'], 2, arrow='blue')
    b += T(280, 150, '流体：对流 + 导热', 'tb', anchor='middle') + T(660, 150, '固体：只导热', 'tb', anchor='middle')
    b += L(600, 250, 520, 250, C['red'], 3, 'red') + L(420, 250, 360, 250, C['red'], 3, 'red') + T(660, 256, 'q', 'mb', fill=C['red'])
    b += R(300, 400, 340, 72, C['white'], C['line']) + T(470, 428, 'T_f = T_s       k_f ∂T/∂n = k_s ∂T/∂n', 'm', anchor='middle', extra=' style="font-size:15px"') + T(470, 456, '界面上温度与热流都要连续', 's', anchor='middle')
    b += T(470, 104, '界面', 'tb', anchor='middle', fill=C['red'])
    made.append(svg('core-heat', '共轭传热：界面上的两个条件', b))

    # 19 parallel
    b = ''
    cols = [C['blueL'], C['greenL'], C['amberL'], C['tealL']]
    edge = [C['blue'], C['green'], C['amber'], C['teal']]
    gx, gy, cs = 90, 110, 30
    for i in range(16):
        for j in range(10):
            k = (0 if i < 8 else 1) + (0 if j < 5 else 2)
            b += f'<rect x="{gx + i * cs}" y="{gy + j * cs}" width="{cs}" height="{cs}" fill="{cols[k]}" stroke="#fff" stroke-width="1.2"/>'
    b += L(gx + 8 * cs, gy, gx + 8 * cs, gy + 10 * cs, C['red'], 3.5, cap='butt') + L(gx, gy + 5 * cs, gx + 16 * cs, gy + 5 * cs, C['red'], 3.5, cap='butt')
    for k, (i, j) in enumerate([(4, 2.5), (12, 2.5), (4, 7.5), (12, 7.5)]):
        b += R(gx + i * cs - 58, gy + j * cs - 17, 116, 34, '#ffffffd9', edge[k], 17, 1.5) + T(gx + i * cs, gy + j * cs + 6, f'processor{k}', 'm', anchor='middle', fill=edge[k], extra=' style="font-size:14px"')
    b += R(620, 110, 300, 300, C['white'], C['line'])
    b += T(640, 146, '计算量', 'tb') + T(640, 172, '≈ 每个子域的单元数', 's')
    b += L(640, 206, 680, 206, C['red'], 3.5) + T(690, 212, '通信量', 'tb', fill=C['red']) + T(640, 238, '≈ 子域间界面的面数', 's')
    b += T(640, 282, 'decomposePar', 'm') + T(640, 306, 'mpirun -np 4 simpleFoam -parallel', 'm', extra=' style="font-size:13px"') + T(640, 330, 'reconstructPar', 'm')
    b += T(640, 372, '子域太小时，通信会抵消', 's') + T(640, 394, '增加进程带来的加速。', 's')
    made.append(svg('core-parallel', '并行计算：域分解与通信界面', b))

    # 20 sampling
    b = ''
    gx, gy, w, h = 70, 120, 440, 260
    for i in range(44):
        for j in range(26):
            x = i / 43; y = j / 25
            v = math.sin(math.pi * y) * (0.35 + 0.65 * x)
            r_ = int(225 - 150 * v); g_ = int(238 - 90 * v); b_ = int(242 - 30 * v)
            b += f'<rect x="{gx + i * 10}" y="{gy + j * 10}" width="10.4" height="10.4" fill="rgb({r_},{g_},{b_})"/>'
    b += L(gx + 320, gy - 10, gx + 320, gy + h + 10, C['red'], 3) + T(gx + 326, gy - 16, 'line：x = 0.7', 'm', fill=C['red'], extra=' style="font-size:14px"')
    px, py, pw, ph = 600, 120, 300, 260
    b += R(px - 20, py - 20, pw + 40, ph + 40, C['white'], C['line'])
    b += L(px, py + ph, px + pw, py + ph, C['ink'], 1.5, 'ink') + L(px, py + ph, px, py - 6, C['ink'], 1.5, 'ink') + T(px + pw, py + ph + 22, 'U', 'mb', anchor='end') + T(px - 8, py + 4, 'y', 'mb', anchor='end')
    pts = [(px + 10 + 250 * math.sin(math.pi * k / 30) * 0.8, py + ph - k * ph / 30) for k in range(31)]
    b += poly(pts, C['red'], 2.8)
    pts = [(px + 10 + 250 * math.sin(math.pi * k / 30) * 0.55, py + ph - k * ph / 30) for k in range(31)]
    b += P('M' + ' L'.join(f'{a:.1f} {c:.1f}' for a, c in pts), C['blue'], 2.2, dash='6 5')
    b += T(px + 150, py + ph + 52, '红：本算例   蓝虚线：对照数据', 's', anchor='middle', extra=' style="font-size:14px"')
    b += L(gx + w + 14, gy + h / 2, px - 34, gy + h / 2, C['muted'], 1.8, 'muted')
    b += T(290, 430, '同一位置、同一分量、同一时刻、同样的归一化——曲线才可以比较', 's', anchor='middle')
    made.append(svg('core-sampling', '从云图到可比较的曲线', b))

    # 21 refinement
    b = ''
    for k, (n, lab) in enumerate([(4, '粗 h'), (8, '中 h/2'), (16, '细 h/4')]):
        ox = 60 + k * 190; s = 150
        b += grid(ox, 140, n, n, s / n, s / n, C['blueM'], 1.2 if n < 16 else .8) + T(ox + s / 2, 320, lab, 'tb', anchor='middle')
    px, py, pw, ph = 640, 120, 270, 220
    b += R(px - 24, py - 20, pw + 48, ph + 80, C['white'], C['line'])
    b += L(px, py + ph, px + pw, py + ph, C['ink'], 1.5, 'ink') + L(px, py + ph, px, py - 6, C['ink'], 1.5, 'ink')
    b += T(px + pw, py + ph + 24, '网格尺寸 h →', 's', anchor='end', extra=' style="font-size:13px"') + T(px + 6, py + 6, '目标量（如压降）', 's', extra=' style="font-size:13px"')
    hs = [(px + 40, py + 90), (px + 110, py + 108), (px + 250, py + 170)]
    b += L(px, py + 82, px + pw, py + 82, C['green'], 1.6, dash='6 5') + T(px + pw - 4, py + 74, '外推值', 's', anchor='end', fill=C['green'], extra=' style="font-size:13px"')
    b += poly(hs[::-1], C['amber'], 2.6) + ''.join(Ci(x, y, 6, C['amber']) for x, y in hs)
    b += T(px + 2, py + ph + 54, '相邻两次加密的差值在缩小？', 's', extra=' style="font-size:14px"')
    b += T(330, 380, '保持几何、边界和模型不变，只按固定比例细化网格', 't', anchor='middle') + T(330, 410, '比较的是目标量，不是“云图看起来差不多”', 's', anchor='middle')
    made.append(svg('core-refinement', '网格研究：比较目标量怎样变化', b))

    # 22 uncertainty
    b = ''
    q = [('离散误差', '网格、时间步、离散格式', '→ 系统加密，看目标量变化', C['blue'], C['blueL']), ('模型误差', '湍流、界面、物性、简化几何', '→ 换模型或对照实验', C['amber'], C['amberL']),
         ('输入不确定性', '流量、尺寸、材料参数', '→ 参数扰动、敏感性分析', C['green'], C['greenL']), ('实验不确定性', '标定、分辨率、重复性', '→ 查看数据的误差棒', C['teal'], C['tealL'])]
    for i, (t, s, h_, c, cl) in enumerate(q):
        x = 50 + (i % 2) * 440; y = 110 + (i // 2) * 170
        b += R(x, y, 420, 150, cl, 'none', 16) + f'<rect x="{x}" y="{y}" width="6" height="150" rx="3" fill="{c}"/>' + T(x + 28, y + 44, t, 'h', fill=c, extra=' style="font-size:22px"') + T(x + 28, y + 80, s, 't', extra=' style="font-size:17px"') + T(x + 28, y + 114, h_, 's')
    b += T(480, 470 - 4, '“和实验对不上”可能来自任何一项；先分清来源，再决定改哪里', 's', anchor='middle')
    made.append(svg('core-uncertainty', '误差的四种来源', b))

    # 23 reproducibility
    b = ''
    steps = [('固定输入', ['OpenFOAM 版本', '全部字典与网格', '初始场'], C['amber']), ('记录运行', ['完整命令与进程数', '求解日志', '时间步与耗时'], C['green']), ('保存证据', ['采样数据', '绘图脚本', '检查结果'], C['blue'])]
    for i, (t, items, c) in enumerate(steps):
        x = 50 + i * 300
        b += R(x, 120, 260, 230, C['white'], C['line']) + f'<rect x="{x}" y="120" width="260" height="56" rx="12" fill="{c}"/><rect x="{x}" y="160" width="260" height="16" fill="{c}"/>' + T(x + 130, 156, t, 'tb w', anchor='middle', extra=' style="fill:#fff"')
        for j, it in enumerate(items):
            b += Ci(x + 30, 214 + j * 42, 4, c) + T(x + 44, 220 + j * 42, it, 't', extra=' style="font-size:17px"')
        if i < 2: b += L(x + 266, 235, x + 294, 235, C['ink'], 2, 'ink')
    b += R(150, 384, 660, 56, C['greenL'], 'none', 12) + T(480, 418, 'git 管理算例 · 结果文件夹附 README · 图能追溯到数据和输入', 't', anchor='middle', extra=' style="font-size:17px"')
    made.append(svg('core-reproducibility', '可复现的计算：输入、运行、证据', b))

    # 24 ecosystem
    b = ''
    cx, cy = 480, 270
    b += Ci(cx, cy, 82, C['green']) + T(cx, cy - 4, 'OpenFOAM', 'tb', anchor='middle', extra=' style="fill:#fff;font-size:21px"') + T(cx, cy + 22, 'v2512', 'm', anchor='middle', extra=' style="fill:#dff0e8"')
    sats = [(-300, -100, '几何', 'FreeCAD · SALOME', C['amber'], C['amberL']), (-300, 100, '网格', 'Gmsh · snappyHexMesh', C['blue'], C['blueL']),
            (300, -100, '可视化', 'ParaView', C['teal'], C['tealL']), (300, 100, '数据分析', 'Python · PyVista', C['teal'], C['tealL']), (0, 175, '批处理与记录', 'Shell · PyFoam · Git', C['muted'], '#eceee8')]
    for dx, dy, t, s, c, cl in sats:
        x, y = cx + dx, cy + dy
        b += R(x - 120, y - 38, 240, 76, cl, c, 14, 1.4) + T(x, y - 6, t, 'tb', anchor='middle', fill=c) + T(x, y + 22, s, 's', anchor='middle', extra=' style="font-size:14px"')
        k = 82 / math.hypot(dx, dy)
        sx, sy = cx + dx * k, cy + dy * k
        ex, ey = x - (120 if dx > 0 else -120 if dx < 0 else 0), y - (38 if dy > 0 and dx == 0 else 0)
        if dx: ex = x - 120 * (1 if dx > 0 else -1); ey = y
        b += L(sx, sy, ex, ey, c, 1.8, dash='5 5')
    b += T(480, 108, '文件格式是接口：STL / msh → polyMesh → VTK / CSV', 's', anchor='middle')
    made.append(svg('core-ecosystem', '工具生态：围绕数据格式协作', b, h=500))
    return made

# ---------------------------------------------------------------- Part B
def texts(s):
    out = []
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>', s, re.S):
        a = m.group(1); fs = re.search(r'font-size="([\d.]+)"', a); cl = re.search(r'class="(\w+)"', a)
        out.append((float(fs.group(1)) if fs else None, cl.group(1) if cl else None, html.unescape(re.sub('<[^>]+>', '', m.group(2))).strip()))
    return out

def flow(name, title, steps, kicker=None, links=(), cols=None, note='FoamLab 示意图', chain=True):
    loop = bool(links)
    n = len(steps)
    cols = cols or (n if n <= 4 else 3)
    rows = math.ceil(n / cols)
    W = 1080; gap = 36; mx = 40
    cw = (W - 2 * mx - gap * (cols - 1)) / cols
    ch = 104 if any(s for _, s in steps) else 84
    top = 104 if kicker else 84
    if title is None: top = 34
    H = top + rows * ch + (rows - 1) * 46 + (56 if loop else 0) + 46
    b = ''
    pal = [C['green'], C['teal'], C['blue'], C['amber']]
    for i, (t, s) in enumerate(steps):
        r_, c_ = divmod(i, cols)
        x = mx + c_ * (cw + gap); y = top + r_ * (ch + 46)
        b += card(x, y, cw, ch, t, s, pal[min(r_, 3)] if rows > 1 else C['green'], num=f'{i + 1:02d}' if n > 1 and chain else None)
        if not chain: pass
        elif c_ < cols - 1 and i < n - 1:
            b += L(x + cw + 6, y + ch / 2, x + cw + gap - 6, y + ch / 2, C['ink'], 2, 'ink')
        elif i < n - 1:
            ny = y + ch + 46
            b += P(f'M{x + cw / 2} {y + ch + 4} V{y + ch + 23} H{mx + cw / 2} V{ny - 6}', C['muted'], 1.8, arrow='muted')
    if links:
        y = top + rows * ch + (rows - 1) * 46
        for k, (i, j) in enumerate(links):
            xi = mx + i * (cw + gap) + cw / 2 + (k - (len(links) - 1) / 2) * 10; xj = mx + j * (cw + gap) + cw / 2 + (k - (len(links) - 1) / 2) * 10
            yy = y + 18 + k * 12
            back = j < i and chain
            b += P(f'M{xi} {y + 4} V{yy} H{xj} V{y + 8}', C['amber'] if back else C['muted'], 1.8, arrow='amber' if back else 'muted', dash=None if back else '5 4')
            if back: b += T((xi + xj) / 2, yy + 20, '回到开头，继续下一轮', 's', anchor='middle', extra=' style="font-size:14px"')
    if title is None:
        doc_title = ' → '.join(t for t, _ in steps)
        markers = ''
    svg_title = title if title is not None else ' → '.join(t for t, _ in steps)
    if title is None:
        # Strip figures keep a compact header-less layout.
        markers = ''.join(f'<marker id="a-{k}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1.2 9 5 1 8.8 2.8 5z" fill="{v}"/></marker>' for k, v in [('ink', C['ink']), ('muted', C['muted']), ('amber', C['amber'])])
        doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(svg_title)}"><title>{esc(svg_title)}</title><defs>{markers}</defs><style>{STYLE}</style>'
               f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="20" fill="{C["paper"]}" stroke="{C["line"]}" stroke-width="1.5"/>{b}{T(W - 28, H - 16, note, "tag", anchor="end")}</svg>')
        (OUT / f'{name}.svg').write_text(doc, encoding='utf-8')
        return name
    return svg(name, title, b, W, H, kicker, note)

FLOWS = Path(__file__).with_name('diagram-flows.json')

def extract_flows():
    """Read the wording of the older generated flow figures once and keep it in JSON."""
    import json
    if FLOWS.exists():
        return json.loads(FLOWS.read_text(encoding='utf-8'))
    data = {}
    for p in sorted(OUT.glob('programming-*.svg')):
        t = texts(p.read_text(encoding='utf-8'))
        data[p.stem] = {'title': next(x for f, c, x in t if f == 28), 'kicker': 'OPENFOAM 编程 · ' + p.stem.split('-')[1],
                        'steps': [[x, ''] for f, c, x in t if f == 22]}
    for p in sorted(OUT.glob('cpp-*.svg')):
        s = p.read_text(encoding='utf-8'); t = texts(s)
        steps = []
        for f, c, x in t:
            if c == 'label': steps.append([x, ''])
            elif c == 'value' and steps: steps[-1][1] = x
        centres = [134, 369, 604, 839]
        idx = lambda v: min(range(len(steps)), key=lambda i: abs(centres[i] - float(v)))
        links = [[idx(a), idx(b)] for a, b in re.findall(r'<path d="M ?(\d+) 208 V22\d H(\d+) V211"', s)]
        data[p.stem] = {'title': next(x for f, c, x in t if f == 24), 'kicker': 'C++ 入门 · ' + p.stem.split('-')[1],
                        'steps': steps, 'links': links, 'cols': len(steps), 'chain': 'h 17' in s}
    for p in sorted(OUT.glob('reference-*.svg')):
        t = texts(p.read_text(encoding='utf-8')); steps = []
        for i, (f, c, x) in enumerate(t):
            if f in (18.0, 19.0):
                sub = t[i + 1][2] if i + 1 < len(t) and t[i + 1][0] == 13.0 and not re.fullmatch(r'\d\d', t[i + 1][2]) else ''
                steps.append([x, sub])
        data[p.stem] = {'title': None, 'steps': steps, 'cols': len(steps)}
    FLOWS.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
    return data

def restyle_flows():
    made = []
    for name, d in extract_flows().items():
        made.append(flow(name, d['title'], [tuple(x) for x in d['steps']], kicker=d.get('kicker'), links=d.get('links', []), cols=d.get('cols'), chain=d.get('chain', True)))
    return made

if __name__ == '__main__':
    a = core(); b = restyle_flows()
    print({'core': len(a), 'flows': len(b)})
