"""Apply the scoped title/summary review; leave lesson bodies and code unchanged."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
EDITS={
 'start-openfoam-v2512':('01 · OpenFOAM v2512 软件组成与环境配置','介绍求解器、工具程序、C++ 库与算例的关系，检查发行分支、环境变量和实际运行版本。'),
 'case-structure-dimensions':('03 · 算例结构、字典语法与量纲','说明 0、constant、system 的职责，以及 FoamFile、列表、宏替换与量纲指数的读取方法。'),
 'first-cavity-result':('04 · 顶盖驱动方腔：计算流程与结果分析','使用官方方腔完成网格生成、检查与求解，分析 Reynolds 数、二维 empty 边界和速度场，并说明验证范围。'),
 'control-time-restart':('06 · 时间控制、结果写出与续算','解释 controlDict 的时间参数、writeInterval 的含义与 latestTime 续算条件，检查重启所需的完整状态。'),
 'blockmesh-first-principles':('07 · blockMesh 结构网格生成与尺度检查','解释 blockMeshDict 的顶点、块连接、单元数、分级与边界面定义，并以官方方腔检查几何尺度。'),
 'checkmesh-and-quality':('08 · checkMesh 网格质量检查与异常定位','分析非正交、偏斜、负体积和边界连通性，结合日志与异常单元位置评估网格问题。'),
 'snappyhexmesh-workflow':('10 · snappyHexMesh 分阶段网格生成与检查','分别说明背景网格、局部细化、表面贴合与边界层生成，检查各阶段的几何匹配和网格质量。'),
 'linear-solvers-residuals':('16 · 线性求解器、残差与收敛判据','解释 tolerance、relTol、pFinal 和初始、最终残差，区分代数求解误差、非线性迭代误差与离散误差。'),
 'grid-time-verification':('18 · 网格与时间步细化及误差分析','建立目标量的细化序列，分析观测收敛阶与外推条件，报告网格和时间步变化造成的数值差异。'),
 'heat-and-multiregion':('23 · 传热、多区域耦合与能量收支','区分温度扩散、流体能量与流固耦合传热，检查区域定义、界面条件和整体热量平衡。'),
 'sampling-functions-and-observables':('27 · 采样、监测与 function objects','配置点探针、中心线采样、截面积分和时间平均，明确变量、数据位置、单位与统计窗口。'),
 'verification-validation-uncertainty':('28 · 数值验证、物理确认与不确定性','区分代码与数值解验证、物理模型确认及不确定性来源，说明各类结论所需的证据和适用条件。'),
 'reproducible-case-and-sharing':('29 · 可复现算例的组织与共享','组织算例输入、运行脚本、环境记录、数据和图，注明执行顺序、检查方法及实际验证范围。'),
 'tool-paraview':('ParaView · 场数据可视化与结果检查','介绍 OpenFOAM Reader、Slice、Plot Over Line 与固定色标，保存状态文件和批量出图脚本。'),
 'tool-pyvista':('PyVista · Python 截面提取与数据分析','读取 .foam、多块网格与时间步，保留单元和点数据关联，编写用于批量比较的后处理脚本。'),
 'tool-freecad-geometry':('FreeCAD 与几何工具 · 实体建模与 CFD 表面导出','保留 CAD 源文件，控制单位和三角化误差，记录几何简化、表面导出与网格检查过程。'),
 'programming-00':('编程 00｜OpenFOAM 应用程序结构与 wmake 编译','说明程序入口、OpenFOAM 环境、Make 文件与编译目标，检查程序启动和执行路径。'),
 'programming-03':('编程 03｜网格拓扑、几何量与 patch 数据访问','区分网格拓扑与几何数据，说明内部面、边界面、owner/neighbour 和 patch 局部索引的访问方法。'),
 'programming-05':('编程 05｜MPI 场操作、数据通信与一致性检查','区分局部量与全局量，使用 reduce、Pstream 和 processor 边界完成通信，并比较串行与并行结果。'),
 'programming-06':('编程 06｜自定义类与 IOdictionary 扩展','通过构造函数、访问控制、引用和继承组织程序状态，核对接口声明、实现与源码注释。'),
 'programming-09':('编程 09｜流量监测 functionObject 的实现','在求解过程中读取注册场、计算截面流量，并管理监测频率、文件输出与并行规约。'),
 'programming-10':('编程 10｜对流扩散方程的求解器实现','将守恒方程对应到 fvm 矩阵、面通量和离散配置，通过稳态标量算例检查编译、求解与结果输出。'),
 'programming-12':('编程 12｜自定义动量源向 v2512 fvOptions 的迁移','以执行器盘为例说明区域选择、源项量纲和运行时接口，并核对 Foundation 与 OpenCFD 的迁移差异。'),
 'programming-14':('编程 14｜SIMPLE 压力速度耦合的矩阵实现','解释 A、H、压力方程、欠松弛与速度修正，比较教学实现和标准求解器的通量处理。'),
 'programming-15':('编程 15｜混合插值格式的实现与评估','根据 owner/neighbour 权重构造面插值，比较数值扩散、过冲、积分误差与网格敏感性。'),
}

def main():
    updates=[]
    for filename,script in [('core-content.json','build-core.py'),('programming-content.json','build-programming-content.py')]:
        data=json.loads((ROOT/filename).read_text(encoding='utf-8'))
        src=(ROOT/script).read_text(encoding='utf-8')
        for item in data:
            if item['slug'] not in EDITS:continue
            title,summary=EDITS[item['slug']]
            old_title,old_summary=item['title'],item['summary']
            if old_title==title and old_summary==summary:continue
            assert src.count(old_title)==1,(script,item['slug'],'title occurrence count')
            assert src.count(old_summary)==1,(script,item['slug'],'summary occurrence count')
            src=src.replace(old_title,title).replace(old_summary,summary)
            updates.append(dict(slug=item['slug'],old_title=old_title,title=title,summary=summary))
            item['title']=title;item['summary']=summary
        (ROOT/script).write_text(src,encoding='utf-8')
        (ROOT/filename).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if updates:
        (ROOT/'editorial-title-updates.json').write_text(json.dumps(updates,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'updated':len(updates),'slugs':[x['slug'] for x in updates]},ensure_ascii=False))

if __name__=='__main__':main()
