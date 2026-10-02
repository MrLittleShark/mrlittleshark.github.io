"""Check translated parameter tables and preserve original example code."""
from pathlib import Path
import json,re,sys,runpy
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'tools/content'))
from command_options import parse_options,parameter_sections,TRANSLATIONS
commands=json.loads((R/'source-openfoam/assets/commands.json').read_text(encoding='utf-8'))
rows={x['slug']:x for x in json.loads((R/'tools/content/reference-content.json').read_text(encoding='utf-8'))}
old={x['slug']:x for x in json.loads((R/'.source_foamlab/tools/content/reference-content.json').read_text(encoding='utf-8'))}
count=0;cells=0
def examples(body):
 soup=BeautifulSoup(body,'html.parser')
 for d in soup.select('details'):
  if d.find('summary') and d.find('summary').get_text(strip=True)=='完整命令帮助':d.decompose()
 return [p.get_text() for p in soup.select('pre')]
for cmd in commands:
 slug='command-'+cmd['url'].strip('/').split('/')[-1];row=rows[slug]
 p=R/'source-openfoam'/cmd.get('helpUrl','').lstrip('/')
 raw=p.read_text(encoding='utf-8') if p.is_file() else ''
 common,more=parameter_sections(raw)
 assert (not common or common in row['body']) and (not more or more in row['body']),slug
 assert '完整命令帮助</summary>' not in row['body'],slug
 if common:count+=1
 soup=BeautifulSoup(common+more,'html.parser')
 for tr in soup.select('tbody tr'):
  fields=tr.find_all('td');assert fields[0].find('code'),slug
  assert re.search('[\u4e00-\u9fff]',fields[1].get_text()),(slug,fields[1].get_text())
  cells+=1
 assert examples(row['body'])==examples(old[slug]['body']),('Code example changed',slug)
pp=dict(parse_options((R/'source-openfoam/assets/command-help/postprocess.txt').read_text(encoding='utf-8')))
assert pp['-funcs <list>']=="Specify the names of the functionObjects to execute, e.g. '(Q div(U))'"
assert pp['-decomposeParDict <file>']=='Alternative decomposePar dictionary file'
assert pp['-fields <list>']!=dict(parse_options((R/'source-openfoam/assets/command-help/decomposepar.txt').read_text(encoding='utf-8')))['-fields']
for case in ['  -long-name <argument>\n                    Its own description\n  -next           Next description', '  -a  First\n                    wraps\n  -b\n                    Second']:
 assert len(parse_options(case))==2
try:parameter_sections('  -new  Untranslated new option')
except ValueError:pass
else:raise AssertionError('Missing translation accepted')
print(json.dumps({'commands_checked':len(commands),'translated_parameter_pages':count,'chinese_parameter_rows':cells,'translation_entries':len(TRANSLATIONS),'code_examples':'unchanged','wrapped_options':'passed'},ensure_ascii=False,indent=2))
