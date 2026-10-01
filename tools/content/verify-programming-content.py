from pathlib import Path
import re,json,zipfile,hashlib
ROOT=Path(r'E:\Hexo');LOG=Path(r'F:\UbuntuShareFolder\.foamlab-build\programming');OUT=ROOT/'source-openfoam/downloads/programming'
status={}
for name in ('packages-validation.log','retest-validation.log','final-validation.log','meshfinal-validation.log'):
    for tutorial,kind,result in re.findall(r'^(OFtutorial\S+) (BUILD|RUN)_(PASS|FAIL)$',(LOG/name).read_text(),re.M):status[(tutorial,kind)]=result
lessons=json.loads((ROOT/'tools/content/programming-content.json').read_text(encoding='utf-8'))
assert len(lessons)==17
assert len({x['slug'] for x in lessons})==17
table=[];evidence=[]
for i,x in enumerate(lessons):
    tutorial=x['metadata']['source'].split('/')[-1]
    assert status[(tutorial,'BUILD')]=='PASS'
    assert status[(tutorial,'RUN')]=='PASS'
    run=(LOG/(tutorial+'.package-run.log')).read_text(errors='replace')
    assert 'FOAM FATAL' not in run
    mesh='不适用 / 未单独作为质量认证'
    if i==11:
        assert 'Failed 1 mesh checks.' in run
        assert 'underdeterminedCells' in run
        mesh='1 项 underdeterminedCells 失败；仅拓扑教学'
    scope='原教学运行链'
    if i in (8,9,12,14,16):scope='20 次流动迭代，非充分收敛验证'
    elif i==13:scope='至 t=0.1，非传播误差收敛验证'
    elif i==11:scope='写出5单元演示网格；网格质量未通过'
    table.append(f'| {i:02} | 通过 | 完成 | {scope} |')
    evidence.append(dict(slug=x['slug'],build='passed',run_exit='passed',scope=scope,mesh_quality=mesh))
    for url in re.findall(r'\]\((/[^)]+)\)',x['body']):
        if url.startswith('/read/'):continue
        assert (ROOT/'source-openfoam'/url.lstrip('/')).is_file(),url
    assert x['body'].count('```')%2==0,x['slug']
with zipfile.ZipFile(OUT/'v2512-programming-validation-logs.zip','w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(LOG.glob('*.package-*.log')):z.write(f,f.name)
    for n in ('packages-validation.log','retest-validation.log','final-validation.log','meshfinal-validation.log','export-transport.log','render-transport.log'):
        z.write(LOG/n,n)
    z.write(LOG/'render-transport.py','render-transport.py')
    z.write(LOG/'export-transport.sh','export-transport.sh')
    z.writestr('README.txt','OpenCFD v2512 independent compilation and shortened teaching runs. Intermediate failures are retained in summary logs; the final per-tutorial build/run logs correspond to the most recent attempt. Tutorial 11 intentionally remains a 5-cell topology demonstration and fails one full mesh quality check. No passwords or API keys are included.\n')
text='''# BasicOFProgramming v2512 核验与迁移记录

日期：2026-10-02。环境：用户 VMware Ubuntu 中的 OpenCFD OpenFOAM v2512；用户副本和网站精简包均保留原材料不变。

17 个目标完成独立编译，17 条运行脚本完成；其中 tutorial11 的网格写出完成，但完整 checkMesh 仍有 1 项质量检查失败，不能列为合格网格。流动例的缩短运行仅检验接口和启动流程，不构成物理正确性或充分收敛认证。

| 实验 | 编译 | 执行链 | 范围 |
| --- | --- | --- | --- |
'''+ '\n'.join(table)+'''

## 真实发现与修复

- 05：添加 processorPolyPatch.H，避免依赖另一版本间接包含的头文件。
- 08：字段写出接口改为 writeEntry("value", os)，重新编译后完成四进程 simpleFoam 短运行、重构和后处理。
- 09：采用 logFiles::files(index)，显式写入文件头，完成函数对象短运行。
- 11：polyMesh 点参数采用 pointField(points)；默认外表面由 empty 改为 patch，清理脚本允许目标尚不存在。三维方向恢复正常，但少量演示单元仍未通过 underdeterminedCells 检查。保留该例用于拓扑教学，不伪造网格通过结论。
- 12：Foundation fvModel/fvModels 转为 OpenCFD fv::option/fvOptions；修复构造参数、场注册和 addSup 签名，增加参数及选区检查，采用上游速度法向投影，避免零除。
- 15：lineCell 采样改为 v2512 cellCentre；计算运行至原设定 t=0.99。
- 通用字典：convertToMeters 改为 scale；obsolete uncompressed 改为 off。每包提供原版权、GPL-3.0 许可证、说明和差异文件。

## 标量输运真实图

tutorial10 的 result 由实际 v2512 求解生成，经 foamToVTK 导出，再由 ParaView 6.1.1 无界面渲染。网格20×20×1，result 为无量纲单元场，VTK 输出范围约 3.56275e-5 至 0.999964。场的线性求解日志记录 GAMG 初始残差1、最终残差1.40597e-7、3次迭代。此图与原资料图片在网页中分别标注。

## 证据

详细日志下载：v2512-programming-validation-logs.zip。早期失败保留在总体日志中，最新逐例日志对应修复后的复测。公共日志中不含任何访问令牌或密码。源码压缩包排除编译产物、生成网格、历史解、processor 数据和 VTK。

算例仍需对具体任务开展网格、时间步、守恒和基准解检查。编译通过不等于数值模型得到验证。
'''
(OUT/'VERIFICATION.md').write_text(text,encoding='utf-8')
(OUT/'verification.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),encoding='utf-8')
for p in OUT.glob('OFtutorial*-v2512.zip'):
    with zipfile.ZipFile(p) as z:
        names=z.namelist();assert any(n.endswith('/LICENSE') for n in names)
        assert any(n.endswith('/FOAMLAB-README.md') for n in names)
        assert not any(re.search(r'/(processor\d*|postProcessing|VTK|linux64[^/]*)/',n) or n.endswith(('.o','.so','.dep')) for n in names)
print(json.dumps(dict(lessons=17,compile_passed=17,execution_completed=17,mesh_quality_failure='tutorial11: 1 underdeterminedCells check',characters=sum(len(x['body']) for x in lessons)),ensure_ascii=False))
