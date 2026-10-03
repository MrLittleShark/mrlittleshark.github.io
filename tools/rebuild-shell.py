from pathlib import Path
import shutil
R=Path(__file__).resolve().parents[1]
S=R/'source-openfoam'
pages={
'courses':('系统学习','OpenFOAM、数值方法、Linux 与 C++ 课程。','LEARNING PATHS'),
'linux':('Linux 入门','目录与文件、终端、日志、脚本和远程计算。','LINUX BASICS'),
'cpp':('C++ 入门','变量、函数、引用、类、模板与多文件程序。','C++ BASICS'),
'programming':('OpenFOAM 编程','17 个编程实例：字典读写、网格与场、自定义边界、源项和求解器。','DEVELOP WITH OPENFOAM'),
'tools':('OpenFOAM 工具生态','围绕几何、网格、可视化与自动化，选择合适的工具并理解数据接口。','TOOLS & ECOSYSTEM'),
'resources':('资料与算例','课程讲义、源码与算例下载。','DATA, CODE & REFERENCES'),
'sharing':('实践与分享','分享可复现的计算经验，记录建模依据、调试过程和数值结果。','ARTICLES & FIELD NOTES'),
'authors':('作者专栏','作者日志、学习记录与专题文章。持续记录方法、问题与改进。','AUTHORS & RESEARCH NOTES'),
'announcements':('网站公告','课程更新、资料修订与社区通知。','UPDATES & ANNOUNCEMENTS'),
'assignments':('作业与实践','阅读练习要求，提交公开的配置、结果与分析。','PRACTICE & ASSIGNMENTS')}
for slug,(title,desc,eyebrow) in pages.items():
 p=S/slug/'index.md';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(f'---\ntitle: {title}\nlayout: catalog\nsection: {slug}\ndescription: {desc}\neyebrow: {eyebrow}\n---\n',encoding='utf-8')
(S/'algorithms').mkdir(exist_ok=True)
(S/'algorithms/index.md').write_text('---\ntitle: 有限体积法\nlayout: catalog-redirect\nsection: algorithms\n---\n',encoding='utf-8')
for slug,title,layout in [('read','内容阅读','read'),('community','讨论中心','forum'),('studio','作者工作台','admin')]:
 p=S/slug/'index.md';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(f'---\ntitle: {title}\nlayout: {layout}\nsection: {slug}\n---\n',encoding='utf-8')
target=S/'assets/science';target.mkdir(parents=True,exist_ok=True)
for name in ['cavity-velocity.png','cavity-mesh.png']:
 shutil.copy2(Path(r'F:\UbuntuShareFolder\.foamlab-build')/name,target/name)
# Preserve the previous course as a local archive, not as the active curriculum.
backup=R/'.openfoam-backup/2026-10-02-rebuild';backup.mkdir(parents=True,exist_ok=True)
for name in ['lessons','bubble']:
 p=(S/name).resolve()
 if p.exists():
  assert p.is_relative_to(S.resolve())
  if not (backup/name).exists():shutil.copytree(p,backup/name)
  shutil.rmtree(p)
print('New catalog shells created; previous lessons preserved in local backup.')
