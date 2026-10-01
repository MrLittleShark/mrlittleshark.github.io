"""Build self-hosted Noto subsets from site text. Font sources remain outside the public tree."""
from pathlib import Path
import sys,json,shutil,hashlib
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'.openfoam-work/font-deps'))
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools import subset
chars=set(chr(n) for n in range(32,127))
for directory in [R/'tools/content',R/'source-openfoam',R/'themes/foam-lab/layout',R/'themes/foam-lab/source/assets']:
 for p in directory.rglob('*'):
  if p.suffix.lower() in ['.json','.md','.ejs','.js'] and 'vendor' not in p.parts:
   try:chars.update(p.read_text(encoding='utf-8'))
   except UnicodeDecodeError:pass
chars={c for c in chars if ord(c)>=32 and ord(c)<=0xffff}
out=R/'source-openfoam/assets/fonts';out.mkdir(parents=True,exist_ok=True)
report=[]
for family,weight,target in [('NotoSansSC',400,'foamlab-sans-regular.woff2'),('NotoSansSC',600,'foamlab-sans-semibold.woff2'),('NotoSerifSC',600,'foamlab-serif-semibold.woff2')]:
 source=R/'.openfoam-work/font-sources'/f'{family}-VF.ttf';font=TTFont(source)
 options=subset.Options();options.flavor='woff2';options.layout_features=['*'];options.name_IDs=['*'];options.name_languages=['*'];options.notdef_glyph=True;options.notdef_outline=True
 sub=subset.Subsetter(options=options);sub.populate(text=''.join(sorted(chars)));sub.subset(font)
 instantiateVariableFont(font,{'wght':weight},inplace=True)
 font.flavor='woff2';font.save(out/target)
 # Keep original names, copyright and license metadata; Noto's OFL has no Reserved Font Names.
 shutil.copy2(R/'.openfoam-work/font-sources'/f'{family}-OFL.txt',out/f'{family}-OFL.txt')
 report.append({'file':target,'bytes':(out/target).stat().st_size,'source':f'https://github.com/google/fonts/tree/main/ofl/{family.lower()}','weight':weight,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
(out/'SOURCE.json').write_text(json.dumps({'glyph_input_count':len(chars),'font_display':'swap','license':'SIL Open Font License 1.1','fonts':report},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'characters':len(chars),'fonts':report},ensure_ascii=False))
