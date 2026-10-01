---
title: "system/meshDict · meshDict"
layout: reference
description: "cfMesh 教程中的网格控制字典，描述表面文件、尺寸与局部细化等。该文件来自核心仓库所携带的 cfMesh 教程；运行依赖独立 cfMesh 模块，不应当用 snappyHexMesh 直接读取。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>cfMesh 教程中的网格控制字典，描述表面文件、尺寸与局部细化等。该文件来自核心仓库所携带的 cfMesh 教程；运行依赖独立 cfMesh 模块，不应当用 snappyHexMesh 直接读取。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>maxCellSize</td><td>cfMesh 的基准或最大单元尺寸，长度单位随几何坐标单位确定。</td></tr><tr><td>surfaceFile</td><td>网格生成使用的表面几何文件路径；单位与表面闭合性需在前处理中检查。</td></tr><tr><td>boundaryCellSize</td><td>cfMesh 边界附近的尺寸控制，与局部细化及边界层设置共同作用。</td></tr><tr><td>boundaryLayers</td><td>cfMesh 边界层生成控制，与 snappyHexMesh 的 addLayersControls 结构不同。</td></tr><tr><td>nLayers</td><td>挤出或边界层生成的层数；同时检查层厚与总厚度。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 1 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><p>该文件族在本次固定版本源码中仅选到一份不同的完整配置；不重复同一个文件充当多个案例。</p><h3>示例 1 · incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval</h3><p>原始路径：<code>tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval/system/meshDict</code>；求解器：<code>adjointOptimisationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval/system/meshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/meshdict/1-meshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
FoamFile
{
    version         2;
    format          ascii;
    class           dictionary;
    object          meshDict;
}

maxCellSize     0.006;

surfaceFile     fileName;

boundaryCellSize 0.004;

boundaryCellSizeRefinementThickness 0.015;

boundaryLayers
{
    patchBoundaryLayers
    {
        &quot;lower.*|upper.*|left.*|right.*|topOPatch&quot;
        {
            nLayers         5;
            thicknessRatio  1.8;
        }
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/meshDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/meshDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
