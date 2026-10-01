from pathlib import Path
import re,colorsys
root=Path(__file__).resolve().parents[1]
files=[root/'themes/foam-lab/source/assets/site.css',root/'themes/foam-lab/source/assets/favicon.svg',root/'themes/foam-lab/layout/_partial/bubble.ejs',root/'themes/foam-lab/layout/layout.ejs']
def blue(match):
    text=match.group(0);s=text[1:];color=s[:6];alpha=s[6:]
    r,g,b=[int(color[i:i+2],16)/255 for i in [0,2,4]]
    h,l,sat=colorsys.rgb_to_hls(r,g,b)
    if 65/360<h<185/360 and sat>.025:
        r,g,b=colorsys.hls_to_rgb(210/360,l,min(.6,max(sat,.14)))
        return '#'+''.join(f'{round(c*255):02x}' for c in [r,g,b])+alpha
    return text
for p in files:
    text=p.read_text(encoding='utf-8');text=re.sub(r'#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b',blue,text)
    p.write_text(text,encoding='utf-8')
print('Applied restrained blue palette.')
