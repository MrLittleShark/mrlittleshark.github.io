---
title: "topoSetDict"
layout: reference
description: "按位置、几何或已有集合选择单元、面和点，并创建 set 或 zone。"
dictionary: true
cms_slug: "dictionary-toposetdict"
---

<p>按位置、几何或已有集合选择单元、面和点，并创建 set 或 zone。</p><p>位置：<code>system/topoSetDict</code></p><h2>配置实例</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object topoSetDict;
}
actions
(
    {
        name heaterCells;
        type cellSet;
        action new;
        source boxToCell;
        box (0.2 0 0) (0.4 0.1 0.01);
    }
    {
        name heater;
        type cellZoneSet;
        action new;
        source setToCellZone;
        set heaterCells;
    }
);</code></pre>
<div class="table-scroll"><table>
<tr><th>条目</th><th>含义</th><th>设置方法与取值</th></tr>
<tr><td>name</td><td>输出集合或区域名称</td><td>与源项中的 cellZone 匹配</td></tr>
<tr><td>type</td><td>对象类别</td><td>cellSet、faceSet、pointSet、cellZoneSet、faceZoneSet</td></tr>
<tr><td>action</td><td>集合操作</td><td>new、add、subtract、subset、invert、clear、remove</td></tr>
<tr><td>source</td><td>选择算法</td><td>boxToCell、sphereToCell、cylinderToCell、patchToFace、fieldToCell 等</td></tr>
<tr><td>sourceInfo</td><td>选择源参数子字典</td><td>多数选择源可将参数直接写入动作字典；名称冲突时采用 sourceInfo</td></tr>
</table></div>
<h2>17.3 topoSetDict（选择集合）</h2><pre><code class="language-openfoam">actions
(
    {
        name    c0;
        type    cellSet;        // cellSet / faceSet / pointSet / cellZoneSet / faceZoneSet
        action  new;            // new / add / subtract / subset / invert / clear / remove
        source  boxToCell;
        box     (0 0 0) (1 1 1);
    }
    {
        name    porous;
        type    cellZoneSet;
        action  new;
        source  setToCellZone;
        set     c0;
    }
);</code></pre>
<p>常用 source 一览</p>
<div class="table-scroll"><table>
<tr><th>类别</th><th>source</th><th>关键参数</th></tr>
<tr><td>几何选单元</td><td>boxToCell</td><td>box (min) (max) 或 boxes ((..)(..))</td></tr>
<tr><td></td><td>rotatedBoxToCell</td><td>origin, i, j, k</td></tr>
<tr><td></td><td>sphereToCell</td><td>origin, radius</td></tr>
<tr><td></td><td>cylinderToCell</td><td>p1, p2, radius</td></tr>
<tr><td></td><td>surfaceToCell</td><td>file "x.stl", outsidePoints, includeCut</td></tr>
<tr><td>拓扑选单元</td><td>zoneToCell / setToCell / labelToCell</td><td>zone/set/value</td></tr>
<tr><td></td><td>cellToCell</td><td>set</td></tr>
<tr><td>选面</td><td>boxToFace、patchToFace、normalToFace、cellToFace</td><td></td></tr>
<tr><td></td><td>boundaryToFace</td><td>全部边界面</td></tr>
<tr><td>选点</td><td>boxToPoint、labelToPoint、surfaceToPoint</td><td></td></tr>
<tr><td>转 zone</td><td>setToCellZone、setsToFaceZone、setToPointZone</td><td></td></tr>
</table></div>
<p>Set 与 Zone 的区别（重要）：Set 是临时选择结果，写在 constant/polyMesh/sets/；Zone 是网格的正式组成部分，写进 cellZones/faceZones。求解器里的多孔介质、MRF、fvOptions、动网格全都认 Zone 不认 Set，所以典型流程是”先 xxxToCell 造 Set，再 setToCellZone 转 Zone”。</p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>actions</td><td>topoSet 操作序列，每项说明目标集合、集合类型、操作和选择源。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/reactingTwoPhaseEulerFoam/laminar/mixerVessel2D</summary><p>搅拌容器把已有 rotor 单元区转成 cellSet，供后续网格或区域操作调用。</p>
<ul>
<li><code>name rotor</code> 是要生成的集合名称。</li>
<li><code>type cellSet</code>、<code>action new</code> 创建新的单元集合。</li>
<li><code>source zoneToCell</code>、<code>zone rotor</code> 从现有同名 cellZone 读取单元，整个区域都被选中。</li>
</ul>
<p>更换转子区域名称时同时改 source 的 zone；cellSet 与 cellZone 是两种对象，后续工具应引用所需的对象类型。</p>
<p><a href="/assets/examples/v2512/toposetdict/1-topoSetDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/reactingTwoPhaseEulerFoam/laminar/mixerVessel2D/system/topoSetDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/reactingTwoPhaseEulerFoam/laminar/mixerVessel2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      topoSetDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

actions
(
    {
        name    rotor;
        type    cellSet;
        action  new;
        source  zoneToCell;
        zone    rotor;
    }
);

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · compressible/acousticFoam/obliqueAirJet/precursor</summary><p>射流预计算在局部盒子中选取面，形成后续操作使用的 f0 面集合。</p>
<ul>
<li><code>type faceSet</code>、<code>name f0</code> 定义面集合而非单元集合。</li>
<li><code>action new</code> 从本次选择建立集合，<code>source boxToFace</code> 按面位置选取。</li>
<li>盒子从 (1,−0.7,−0.01) 到 (1.5,−0.2,0.01)，厚度方向覆盖 z=0 附近。</li>
</ul>
<p>改变采样或接口位置时修改盒子，运行后查看所选面是否构成预期截面。</p>
<p><a href="/assets/examples/v2512/toposetdict/2-topoSetDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/precursor/system/topoSetDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/precursor">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      topoSetDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

actions
(
    {
        name    f0;
        type    faceSet;
        action  new;
        source  boxToFace;
        box     (1 -0.7 -0.01)(1.5 -0.2 0.01);
    }
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/uniformityCellZone</summary><p>S 弯管的均匀性优化在局部区域建立单元集合，为相关统计或后续区域转换提供选择。</p>
<ul>
<li><code>name zone</code> 为集合名，<code>type cellSet</code> 说明当前输出仍是单元集合。</li>
<li><code>action new</code> 新建集合，<code>source boxToCell</code> 根据单元中心选取。</li>
<li>盒子范围 (−0.5,−0.2,−0.1) 到 (0.5,0.38,0.2) 决定目标空间范围。</li>
</ul>
<p>改动目标测量区时先调整范围并查看选区，再确认优化字典引用的区域对象与名称。</p>
<p><a href="/assets/examples/v2512/toposetdict/3-topoSetDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/uniformityCellZone/system/topoSetDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/uniformityCellZone">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      topoSetDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

actions
(
    {
        name    zone;
        type    cellSet;
        action  new;
        source  boxToCell;
        box     (-0.5 -0.2 -0.1)(0.5 0.38 0.2);
    }
);

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/toposet/">topoSet</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
