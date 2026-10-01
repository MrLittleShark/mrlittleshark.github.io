from pathlib import Path
import shutil
R=Path(__file__).resolve().parents[1]
S=R/'source-openfoam'
pages={
'courses':('系统学习','从工作环境和基本算例开始，逐步理解网格、物理模型、离散算法与结果验证。','LEARNING PATHS'),
'programming':('OpenFOAM 编程','从应用程序、网格与场操作，到自定义边界、源项和求解器。结合 BasicOFProgramming 的 17 个示例阅读代码。','DEVELOP WITH OPENFOAM'),
'algorithms':('数值方法与算法','从控制体积分到线性系统，理解离散、稳定性、压力速度耦合与数值误差。','NUMERICS & VERIFICATION'),
'tools':('OpenFOAM 工具生态','围绕几何、网格、可视化与自动化，选择合适的工具并理解数据接口。','TOOLS & ECOSYSTEM'),
'resources':('资料与算例','下载配套源码、配置示例和验证记录；按来源与软件版本查找资料。','DATA, CODE & REFERENCES'),
'sharing':('实践与分享','分享可复现的计算经验，记录建模依据、调试过程和数值结果。','ARTICLES & FIELD NOTES'),
'authors':('作者专栏','作者日志、学习记录与专题文章。持续记录方法、问题与改进。','AUTHORS & RESEARCH NOTES'),
'announcements':('网站公告','课程更新、资料修订与社区通知。','UPDATES & ANNOUNCEMENTS'),
'assignments':('作业与实践','阅读练习要求，提交公开的配置、结果与分析。','PRACTICE & ASSIGNMENTS')}
for slug,(title,desc,eyebrow) in pages.items():
 p=S/slug/'index.md';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(f'---\ntitle: {title}\nlayout: catalog\nsection: {slug}\ndescription: {desc}\neyebrow: {eyebrow}\n---\n',encoding='utf-8')
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
