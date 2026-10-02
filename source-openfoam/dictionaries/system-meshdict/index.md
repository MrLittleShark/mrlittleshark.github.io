---
title: "meshDict"
layout: reference
description: "cfMesh 教程中的网格控制字典，描述表面文件、尺寸与局部细化等。"
dictionary: true
cms_slug: "dictionary-meshdict"
---

<p>cfMesh 教程中的网格控制字典，描述表面文件、尺寸与局部细化等。</p><p>位置：<code>system/meshDict</code></p><h2>配置实例</h2><p>incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval 中的 meshDict：</p><pre><code class="language-foam">FoamFile
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
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>maxCellSize</td><td>cfMesh 的基准或最大单元尺寸，长度单位随几何坐标单位确定。</td></tr><tr><td>surfaceFile</td><td>网格生成使用的表面几何文件路径；单位与表面闭合性需在前处理中检查。</td></tr><tr><td>boundaryCellSize</td><td>cfMesh 边界附近的尺寸控制，与局部细化及边界层设置共同作用。</td></tr><tr><td>boundaryLayers</td><td>cfMesh 边界层生成控制，与 snappyHexMesh 的 addLayersControls 结构不同。</td></tr><tr><td>nLayers</td><td>挤出或边界层生成的层数；同时检查层厚与总厚度。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval</summary><p>拓扑优化的 reEval 阶段利用表面几何重新生成网格，meshDict 控制整体尺度及壁面层。</p>
<ul>
<li><code>maxCellSize 0.006</code> 将主体网格尺度设为 6 mm，<code>boundaryCellSize 0.004</code> 将边界附近细化到 4 mm。</li>
<li><code>boundaryCellSizeRefinementThickness 0.015</code> 给出距边界约 15 mm 的细化影响范围。</li>
<li><code>surfaceFile fileName</code> 是等待工作流替换的几何文件名占位符；单独使用时填入实际表面文件路径。</li>
<li>正则表达式选择 lower、upper、left、right、topOPatch 等边界，<code>nLayers 5</code>、<code>thicknessRatio 1.8</code> 在这些壁面生成 5 层逐步增长的边界层单元。</li>
</ul>
<p>几何更新后重点查看狭窄通道是否有足够单元，以及边界层是否因局部间隙而被截断。</p>
<p><a href="/assets/examples/v2512/meshdict/1-meshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval/system/meshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><code>cartesianMesh</code>（扩展工具）</p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
