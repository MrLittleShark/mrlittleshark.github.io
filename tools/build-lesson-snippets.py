"""Bundle theory and Linux examples without adding an automatic execution script."""
from pathlib import Path
import json,re,zipfile,hashlib
ROOT=Path(__file__).resolve().parents[1]
for name,kind in [('algorithm-theory-content.json','algorithms'),('linux-content.json','linux')]:
    file=ROOT/'tools/content'/name
    rows=json.loads(file.read_text(encoding='utf-8'))
    for row in rows:
        dest=ROOT/'source-openfoam/downloads'/kind/(row['slug']+'.zip');dest.parent.mkdir(parents=True,exist_ok=True)
        blocks=re.findall(r'```([^\n]*)\n([\s\S]*?)\n```',row['body'])
        intro=row['title']+'\n\n对应课程：https://foamlabshark.github.io/read/?slug='+row['slug']+'\n\n'
        intro+='examples.md 保存本课全部示例及说明。Python 文件可独立运行；Linux 命令按正文顺序逐段练习，先创建自己的练习目录。\n' if kind=='linux' else 'examples.md 保存讲解与示例。Python 文件分别对应课中的数值演示，运行方式：python3 文件名。\n'
        files={'README.txt':intro,'examples.md':row['body']}
        count=0
        for lang,body in blocks:
            if lang.strip()=='python':count+=1;files[f'example-{count:02}.py']=body+'\n'
        with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED) as bundle:
            for filename,text in files.items():
                entry=zipfile.ZipInfo(filename,(2026,10,2,0,0,0));entry.compress_type=zipfile.ZIP_DEFLATED;bundle.writestr(entry,text.encode('utf-8'))
        url='/downloads/'+kind+'/'+dest.name
        row.setdefault('metadata',{})['downloads']=[{'label':'本课代码与练习说明（ZIP）','url':url,'description':'包含讲解与命令示例。' if kind=='linux' else '包含理论讲解与 Python 数值示例。','size_bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'kind':'source'}]
    file.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(name,len(rows),'download packages')
