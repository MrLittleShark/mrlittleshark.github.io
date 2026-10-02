---
title: "extrudeMeshDict"
layout: reference
description: "把表面或已有边界沿指定方向挤出，生成分层体网格。"
dictionary: true
cms_slug: "dictionary-extrudemeshdict"
---

<p>把表面或已有边界沿指定方向挤出，生成分层体网格。</p><p>位置：<code>system/extrudeMeshDict</code></p><h2>配置实例</h2><p>constructFrom 指定挤出来源，sourceCase 和 sourcePatches 指定源算例及边界，exposedPatchName 定义新暴露边界。extrudeModel 选择挤出模型，nLayers 和 expansionRatio 控制层数及层厚比，mergeFaces 和 mergeTol 控制合并。linearNormal 通过 linearNormalCoeffs/thickness 设置总厚度；其他模型采用各自的系数字典。</p>
<pre><code class="language-openfoam">// 片段：沿已有 patch 外法向挤出
constructFrom patch;
sourceCase ".";
sourcePatches (front);
exposedPatchName back;
extrudeModel linearNormal;
nLayers 5;
expansionRatio 1;
linearNormalCoeffs { thickness 0.01; }
mergeFaces false;
mergeTol 0;</code></pre>
<h2>17.6 extrudeMeshDict</h2><pre><code class="language-openfoam">constructFrom   patch;              // mesh / patch / surface
sourceCase      "../base";
sourcePatches   (front);
exposedPatchName back;

extrudeModel    linearNormal;       // linearNormal/linearDirection/wedge/sector/plane
linearNormalCoeffs { thickness 0.01; }
sectorCoeffs   { axisPt (0 0 0); axis (0 0 1); angle 5; }

nLayers         1;
expansionRatio  1.0;
mergeFaces      false;</code></pre>
<p>典型用途：把一个二维面拉伸成一层网格做二维算例；用 sector 模型做轴对称（wedge）算例。</p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>constructFrom</td><td>指定挤出源来自已有网格、表面或其他受支持的输入。</td></tr><tr><td>sourceCase</td><td>提供源网格或场的算例位置。相对路径以执行时工作目录为准。</td></tr><tr><td>sourcePatches</td><td>作为挤出源的边界名称列表。</td></tr><tr><td>extrudeModel</td><td>挤出几何模型，例如平移、旋转或法向挤出；各模型需要不同系数。</td></tr><tr><td>nLayers</td><td>挤出或边界层生成的层数；同时检查层厚与总厚度。</td></tr><tr><td>expansionRatio</td><td>相邻挤出层的厚度增长比例。</td></tr><tr><td>axis</td><td>旋转轴或方向向量；需明确是否要求单位向量。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · mesh/extrudeMesh/faceZoneExtrusion</summary><p>faceZoneExtrusion 从已有面区挤出体网格，可用于由界面生成薄层区域。</p>
<ul>
<li><code>constructFrom mesh</code>、<code>sourceCase "&lt;case&gt;"</code> 指向源网格；<code>sourceFaceZones (f0Zone)</code> 选择挤出面区。</li>
<li><code>extrudeModel linearNormal</code> 沿局部法向挤出，<code>thickness 0.05</code> 给出 0.05 m 厚度。</li>
<li><code>exposedPatchName front</code> 命名暴露面，<code>flipNormals false</code> 保持源面的方向。</li>
<li><code>mergeFaces false</code> 保留面分离结构。</li>
</ul>
<p>改变厚度前检查法向是否指向目标区域，完成后检查薄层单元质量和新边界名称。</p>
<p><a href="/assets/examples/v2512/extrudemeshdict/1-extrudeMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/extrudeMesh/faceZoneExtrusion/system/extrudeMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/extrudeMesh/faceZoneExtrusion">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      extrudeMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

constructFrom mesh;
sourceCase    &quot;&lt;case&gt;&quot;;

//sourcePatches ();
sourceFaceZones (f0Zone);
exposedPatchName front;

extrudeModel  linearNormal;
thickness     0.05;

flipNormals false;
mergeFaces false;

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</code></pre></details><details class="reference-example"><summary>示例 2 · compressible/rhoPimpleFoam/RAS/aerofoilNACA0012</summary><p>NACA0012 网格从 back 边界沿固定方向挤出，形成有限厚度的翼型网格。</p>
<ul>
<li><code>constructFrom patch</code>、<code>sourcePatches (back)</code> 选择源边界。</li>
<li><code>linearDirection</code> 采用统一方向 <code>(0 -1 0)</code>，而非各面法向。</li>
<li><code>thickness 0.1</code> 指定挤出厚度，<code>exposedPatchName front</code> 命名新暴露面。</li>
<li><code>flipNormals false</code> 与 <code>mergeFaces false</code> 保持本例的方向和面结构。</li>
</ul>
<p>展向宽度改变时同步调整厚度、网格层数及后处理参考面积。</p>
<p><a href="/assets/examples/v2512/extrudemeshdict/2-extrudeMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/aerofoilNACA0012/system/extrudeMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/aerofoilNACA0012">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      extrudeMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

constructFrom patch;
sourceCase    &quot;&lt;case&gt;&quot;;

sourcePatches (back);
exposedPatchName front;

extrudeModel  linearDirection;
direction     (0 -1 0);
thickness     0.1;

flipNormals false;
mergeFaces false;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/compressibleInterFoam/laminar/climbingRod</summary><p>爬杆流动采用窄楔形挤出，把二维截面变为轴对称近似网格。</p>
<ul>
<li><code>sourcePatches (front)</code> 是源面，<code>exposedPatchName back</code> 命名另一侧。</li>
<li><code>extrudeModel wedge</code> 选择楔形模型，<code>point (0 0 0)</code>、<code>axis (0 -1 0)</code> 定义转轴。</li>
<li><code>angle 1</code> 指定 1° 的扇角，<code>flipNormals false</code> 保持源面方向。</li>
</ul>
<p>改变轴线或扇角时检查两个楔面及其场边界类型，确保几何与轴对称假设一致。</p>
<p><a href="/assets/examples/v2512/extrudemeshdict/3-extrudeMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/climbingRod/system/extrudeMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/climbingRod">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      extrudeMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

constructFrom patch;
sourceCase    &quot;&lt;case&gt;&quot;;

sourcePatches (front);
exposedPatchName back;

extrudeModel    wedge;

sectorCoeffs    //&lt;- Also used for wedge
{
    point       (0 0 0);
    axis        (0 -1 0);
    angle       1;
}

flipNormals false;

mergeFaces  false;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/extrudemesh/">extrudeMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
