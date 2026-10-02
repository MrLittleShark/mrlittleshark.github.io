---
title: "PDRMeshDict"
layout: reference
description: "PDR 网格处理工作流中的专用配置。"
dictionary: true
cms_slug: "dictionary-pdrmeshdict"
---

<p>PDR 网格处理工作流中的专用配置。</p><p>位置：<code>system/PDRMeshDict</code></p><h2>配置实例</h2><p>combustion/PDRFoam/flamePropagationWithObstacles 中的 PDRMeshDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      PDRMeshDict;
}

//- Per faceSet the patch the faces should go into blocked baffles
blockedFaces ((blockedFacesSet blockedFaces));

//- Per faceSet the patch the faces should go into coupled baffles
coupledFaces
{

    coupledFacesSet
    {
        wallPatch                   baffleWall;
        cyclicMasterPatch           baffleCyclic_half0;
    }
}

//- Name of cellSet that holds the cells to fully remove
blockedCells blockedCellsSet;

//- All exposed faces that are not specified in blockedFaces go into
//  this patch
defaultPatch outer;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>blockedFaces</td><td>faceSet 与封闭挡板 patch 的映射。</td></tr><tr><td>coupledFaces</td><td>耦合挡板的面集合及相关壁面/周期边界配置。</td></tr><tr><td>wallPatch</td><td>用于挡板壁面的 patch 名称。</td></tr><tr><td>cyclicMasterPatch</td><td>周期耦合主边界名称。</td></tr><tr><td>blockedCells</td><td>需要从网格中移除的单元集合。</td></tr><tr><td>defaultPatch</td><td>新暴露且没有明确指定去向的面归入此边界。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · combustion/PDRFoam/flamePropagationWithObstacles</summary><p>障碍物火焰传播算例先用集合标记被固体占据的单元和被阻挡的面，再由 PDRMesh 改造网格。</p>
<ul>
<li><code>blockedCells blockedCellsSet</code> 指向要从计算域移除的单元集合；这个集合应在运行前生成。</li>
<li><code>blockedFaces ((blockedFacesSet blockedFaces))</code> 把指定面集合转换到名为 blockedFaces 的边界。</li>
<li><code>coupledFacesSet</code> 对应混合耦合挡板，<code>wallPatch baffleWall</code> 与 <code>cyclicMasterPatch baffleCyclic_half0</code> 指定其壁面和周期耦合部分。</li>
<li><code>defaultPatch outer</code> 接收剔除单元后暴露、又未单独指定归属的面。</li>
</ul>
<p>更换障碍物后重新生成集合，再检查新边界的名称、面积和相邻单元；场文件中的边界条件应覆盖这些新边界。</p>
<p><a href="/assets/examples/v2512/pdrmeshdict/1-PDRMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/PDRFoam/flamePropagationWithObstacles/system/PDRMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/PDRFoam/flamePropagationWithObstacles">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      PDRMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

//- Per faceSet the patch the faces should go into blocked baffles
blockedFaces ((blockedFacesSet blockedFaces));

//- Per faceSet the patch the faces should go into coupled baffles
coupledFaces
{

    coupledFacesSet
    {
        wallPatch                   baffleWall;
        cyclicMasterPatch           baffleCyclic_half0;
    }
}

//- Name of cellSet that holds the cells to fully remove
blockedCells blockedCellsSet;

//- All exposed faces that are not specified in blockedFaces go into
//  this patch
defaultPatch outer;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · etc/caseDicts/annotated</summary><p>这个注释模板列出 PDR 网格处理中使用的单元集合、面集合和挡板边界。移植时可与上一个完整火焰传播算例对照。</p>
<ul>
<li><code>blockedCellsSet</code> 定义被实体堵塞的单元，<code>blockedFacesSet</code> 定义受阻面。</li>
<li><code>blockedFaces</code> 列表给出“面集合—目标边界”的对应关系，<code>defaultPatch outer</code> 指定其余暴露面的归属。</li>
<li>模板中的 <code>wallPatchName</code>、<code>cyclicMasterPatchName</code> 保留了旧写法；v2512 的 PDRMesh 实际读取 <code>wallPatch</code>、<code>cyclicMasterPatch</code>。使用本模板时将这两个键分别改成后者，值仍为 baffleWall 和 baffleCyclic_half0。</li>
</ul>
<p>用网格工具生成的集合名称替换示例名称，并让各个场文件使用生成后的边界名称。</p>
<p><a href="/assets/examples/v2512/pdrmeshdict/2-PDRMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/PDRMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      PDRMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

//- Per faceSet the patch the faces should go into blocked baffles
blockedFaces ((blockedFacesSet blockedFaces));

//- Per faceSet the duplicate baffles to generate (one &#x27;normal&#x27;, wall baffle,
//  one cyclic baffle). For use with active baffle boundary conditions.
coupledFaces
{
    coupledFacesSet
    {
        wallPatchName               baffleWall;
        cyclicMasterPatchName       baffleCyclic_half0;
    }
}

//- Name of cellSet that holds the cells to fully remove
blockedCells blockedCellsSet;

//- All exposed faces that are not specified in blockedFaces go into
//  this patch
defaultPatch outer;

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/pdrmesh/">PDRMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
