---
title: "system/topoSetDict · topoSetDict"
layout: reference
description: "常用 source 一览"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>常用 source 一览</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/topoSetDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>actions</code> · <code>name</code> · <code>type</code> · <code>action</code> · <code>source</code> · <code>sourceInfo</code> · <code>cellSet</code> · <code>faceSet</code> · <code>cellZoneSet</code></p><h2>关联命令</h2><p><a href="/commands/?q=topoSet">topoSet</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/topoSetDict -keywords
topoSet -help</code></pre><h2>7.7 system/topoSetDict</h2><pre><code class="language-openfoam">FoamFile
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
<tr><td></td><td>surfaceToCell</td><td>file &quot;x.stl&quot;, outsidePoints, includeCut</td></tr>
<tr><td>拓扑选单元</td><td>zoneToCell / setToCell / labelToCell</td><td>zone/set/value</td></tr>
<tr><td></td><td>cellToCell</td><td>set</td></tr>
<tr><td>选面</td><td>boxToFace、patchToFace、normalToFace、cellToFace</td><td></td></tr>
<tr><td></td><td>boundaryToFace</td><td>全部边界面</td></tr>
<tr><td>选点</td><td>boxToPoint、labelToPoint、surfaceToPoint</td><td></td></tr>
<tr><td>转 zone</td><td>setToCellZone、setsToFaceZone、setToPointZone</td><td></td></tr>
</table></div>
<p>Set 与 Zone 的区别（重要）：Set 是临时选择结果，写在 constant/polyMesh/sets/；Zone 是网格的正式组成部分，写进 cellZones/faceZones。求解器里的多孔介质、MRF、fvOptions、动网格全都认 Zone 不认 Set，所以典型流程是”先 xxxToCell 造 Set，再 setToCellZone 转 Zone”。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>actions</td><td>topoSet 操作序列，每项说明目标集合、集合类型、操作和选择源。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><p>同一语法也可保存在 *.topoSetDict 等自定义名称中，通过 topoSet -dict 指定。createInletOutletSets.topoSetDict、cRefine.topoSetDict、f.topoSetDict 与 fBurner.topoSetDict 归在此文件族，不虚增为四种独立配置格式。</p><h3>示例 1 · multiphase/reactingTwoPhaseEulerFoam/laminar/mixerVessel2D</h3><p>原始路径：<code>tutorials/multiphase/reactingTwoPhaseEulerFoam/laminar/mixerVessel2D/system/topoSetDict</code>；求解器：<code>reactingTwoPhaseEulerFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/reactingTwoPhaseEulerFoam/laminar/mixerVessel2D/system/topoSetDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/toposetdict/1-topoSetDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/reactingTwoPhaseEulerFoam/laminar/mixerVessel2D">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

// ************************************************************************* //</code></pre><h3>示例 2 · compressible/acousticFoam/obliqueAirJet/precursor</h3><p>原始路径：<code>tutorials/compressible/acousticFoam/obliqueAirJet/precursor/system/topoSetDict</code>；求解器：<code>rhoPimpleAdiabaticFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/precursor/system/topoSetDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/toposetdict/2-topoSetDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/precursor">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/uniformityCellZone</h3><p>原始路径：<code>tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/uniformityCellZone/system/topoSetDict</code>；求解器：<code>adjointOptimisationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/uniformityCellZone/system/topoSetDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/toposetdict/3-topoSetDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/uniformityCellZone">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/toposet/">topoSet</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/topoSetDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/topoSetDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
