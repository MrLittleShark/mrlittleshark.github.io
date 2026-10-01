from pathlib import Path
import zipfile,json,xml.etree.ElementTree as E
root=Path(r'E:\PKU\2024\MyPHD\LearningMaterials\OpenFoam\大纲')
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
names=['OpenFOAM_v2512命令与配置参考手册（GPT整理）','OpenFOAM命令与文件大全_v2512（Claude整理）','OpenFOAM教学备课大纲_28讲_电极气泡','OpenFOAM教学课程大纲_电极气泡']
for i,name in enumerate(names):
 with zipfile.ZipFile(root/(name+'.docx')) as z:
  body=E.fromstring(z.read('word/document.xml')).find('w:body',ns)
  blocks=[]
  for b in body:
   if b.tag.endswith('}p'):
    t=''.join(b.itertext()) if False else ''.join(n.text or '' for n in b.findall('.//w:t',ns))
    style=b.find('w:pPr/w:pStyle',ns)
    if t.strip(): blocks.append({'type':'p','style':style.get('{'+ns['w']+'}val') if style is not None else '', 'text':t})
   elif b.tag.endswith('}tbl'):
    rows=[['\n'.join(''.join(n.text or '' for n in p.findall('.//w:t',ns)) for p in c.findall('w:p',ns)) for c in row.findall('w:tc',ns)] for row in b.findall('w:tr',ns)]
    blocks.append({'type':'table','rows':rows})
  Path(r'E:\Hexo\.openfoam-work',f'doc{i+1}.json').write_text(json.dumps({'name':name,'blocks':blocks},ensure_ascii=False,indent=2),encoding='utf-8')
  lines=[f'[{j}] '+(b['style']+' '+b['text'] if b['type']=='p' else 'TABLE\n'+'\n'.join(' | '.join(r) for r in b['rows'])) for j,b in enumerate(blocks)]
  Path(r'E:\Hexo\.openfoam-work',f'doc{i+1}.txt').write_text('\n'.join(lines),encoding='utf-8')
  print(i+1,name,len(blocks),'blocks',sum(len(t) for t in lines),'characters')
