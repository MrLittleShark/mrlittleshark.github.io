---
title: "refineMeshDict"
layout: reference
description: "指定要细化的单元集合、局部坐标系和细化方向。"
dictionary: true
cms_slug: "dictionary-refinemeshdict"
---

<p>指定要细化的单元集合、局部坐标系和细化方向。</p><p>位置：<code>system/refineMeshDict</code></p><h2>配置实例</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object refineMeshDict;
}
set heaterCells;
coordinateSystem global;
globalCoeffs
{
    tan1 (1 0 0);
    tan2 (0 1 0);
}
directions (tan1 tan2);
useHexTopology true;
geometricCut false;
writeMesh false;</code></pre>
<p>set 指定待细化的单元集合，directions 指定细化方向。二维网格仅沿面内方向细化，厚度方向保持 empty 边界要求的单层结构。运行 refineMesh -overwrite 后，检查场、区域和边界与新网格的对应关系。</p>
<h2>17.8 refineMeshDict</h2><pre><code class="language-openfoam">set             c0;                 // 对哪个 cellSet 加密
coordinateSystem global;
globalCoeffs    { tan1 (1 0 0); tan2 (0 1 0); }
directions      ( tan1 tan2 );      // 只在这两个方向加密（各向异性）
useHexTopology  yes;
geometricCut    no;
writeMesh       no;
$ topoSet &amp;&amp; refineMesh -overwrite -dict system/refineMeshDict</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>origin</td><td>局部坐标系、旋转或几何操作的参考原点。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/cavitatingFoam/LES/throttle</summary><p>节流空化算例对名为 c0 的单元集合做平面内细化。</p>
<ul>
<li><code>set c0</code> 限定需要细化的单元。</li>
<li><code>coordinateSystem global</code> 采用全局坐标，<code>tan1 (1 0 0)</code>、<code>tan2 (0 1 0)</code> 对应 x、y。</li>
<li><code>directions (tan1 tan2)</code> 同时沿这两个方向细化，保留其他方向的分辨率。</li>
<li><code>useHexTopology yes</code> 使用六面体拓扑信息，<code>geometricCut no</code> 采用相应拓扑切分路径。</li>
</ul>
<p>选择更小的局部区域时先更新 c0；二维算例保持厚度方向的一层结构并重新检查网格。</p>
<p><a href="/assets/examples/v2512/refinemeshdict/1-refineMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/cavitatingFoam/LES/throttle/system/refineMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/cavitatingFoam/LES/throttle">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      refineMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

set             c0;

coordinateSystem global;

globalCoeffs
{
    tan1            (1 0 0);
    tan2            (0 1 0);
}

directions      ( tan1 tan2 );

useHexTopology  yes;

geometricCut    no;

writeMesh       no;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · mesh/refineMesh/cylinder</summary><p>圆柱细化示例采用自定义柱坐标系，在局部方向上细化指定单元。</p>
<ul>
<li><code>set cellsToRefine</code> 指定单元集合，<code>coordinateSystem user</code> 读取用户坐标定义。</li>
<li><code>type cylindrical</code>、<code>origin (0 0 0)</code> 建立柱坐标；<code>e3 (0 1 0)</code> 给出轴向，<code>e1 (1 0 0)</code> 给参考方向。</li>
<li><code>directions (tan1)</code> 只选择一个局部细化方向，<code>useHexTopology true</code> 使用六面体拓扑。</li>
</ul>
<p>旋转轴改变时同步修改坐标系，查看实际切分方向后再用于边界层或环向加密。</p>
<p><a href="/assets/examples/v2512/refinemeshdict/2-refineMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/refineMesh/cylinder/system/refineMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/refineMesh/cylinder">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      refineMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

set cellsToRefine;

coordinateSystem user;

userCoeffs
{
    type    cylindrical;
    origin  (0 0 0);
    e1      (1 0 0);
    e3      (0 1 0);
}

directions
(
    //normal
    tan1
    //tan2
);

useHexTopology  true;

geometricCut    false;

writeMesh       false;

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interFoam/LES/nozzleFlow2D</summary><p>二维喷嘴流动只在一个全局方向细化 c0 区域，适合控制局部单元形状。</p>
<ul>
<li><code>coordinateSystem global</code> 和 <code>tan1 (1 0 0)</code> 确定 x 向细化。</li>
<li><code>directions (tan1)</code> 不选择 tan2，改变的方向比较明确。</li>
<li><code>useHexTopology no</code>、<code>geometricCut yes</code> 选择几何切分方式。</li>
<li>文件还保留 patchLocalCoeffs，但当前 coordinateSystem 为 global，解释实际设置时以选中的坐标系为准。</li>
</ul>
<p>需要沿壁面局部方向细化时，应同时改坐标系与相应系数，不能仅修改未被选用的子字典。</p>
<p><a href="/assets/examples/v2512/refinemeshdict/3-refineMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/LES/nozzleFlow2D/system/refineMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/LES/nozzleFlow2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      refineMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

set             c0;

coordinateSystem global;

globalCoeffs
{
    tan1            (1 0 0);
    tan2            (0 1 0);
}

patchLocalCoeffs
{
    patch           outside;
    tan1            (1 0 0);
}

directions      ( tan1 );

useHexTopology  no;

geometricCut    yes;

writeMesh       no;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/refinemesh/">refineMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
