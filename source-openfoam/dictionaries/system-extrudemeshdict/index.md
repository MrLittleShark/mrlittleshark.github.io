---
title: "system/extrudeMeshDict · extrudeMeshDict"
layout: reference
description: "constructFrom 指定挤出来源，sourceCase 和 sourcePatches 指定源算例及边界，exposedPatchName 定义新暴露边界。extrudeModel 选择挤出模型，nLayers 和 expansionRatio 控制层数及层厚比，mergeFaces 和 mergeTol 控制合并。linearNormal 通过 linearNormalCoeffs/thickness 设置总厚度；其他模型采用各自的系数字典。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>constructFrom 指定挤出来源，sourceCase 和 sourcePatches 指定源算例及边界，exposedPatchName 定义新暴露边界。extrudeModel 选择挤出模型，nLayers 和 expansionRatio 控制层数及层厚比，mergeFaces 和 mergeTol 控制合并。linearNormal 通过 linearNormalCoeffs/thickness 设置总厚度；其他模型采用各自的系数字典。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/extrudeMeshDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>constructFrom</code> · <code>sourceCase</code> · <code>sourcePatches</code> · <code>exposedPatchName</code> · <code>extrudeModel</code> · <code>nLayers</code> · <code>expansionRatio</code> · <code>thickness</code></p><h2>关联命令</h2><p><a href="/commands/?q=extrudeMesh">extrudeMesh</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/extrudeMeshDict -keywords
extrudeMesh -help</code></pre><h2>7.11 system/extrudeMeshDict</h2><p>constructFrom 指定挤出来源，sourceCase 和 sourcePatches 指定源算例及边界，exposedPatchName 定义新暴露边界。extrudeModel 选择挤出模型，nLayers 和 expansionRatio 控制层数及层厚比，mergeFaces 和 mergeTol 控制合并。linearNormal 通过 linearNormalCoeffs/thickness 设置总厚度；其他模型采用各自的系数字典。</p>
<pre><code class="language-openfoam">// 片段：沿已有 patch 外法向挤出
constructFrom patch;
sourceCase &quot;.&quot;;
sourcePatches (front);
exposedPatchName back;
extrudeModel linearNormal;
nLayers 5;
expansionRatio 1;
linearNormalCoeffs { thickness 0.01; }
mergeFaces false;
mergeTol 0;</code></pre>
<h2>17.6 extrudeMeshDict</h2><pre><code class="language-openfoam">constructFrom   patch;              // mesh / patch / surface
sourceCase      &quot;../base&quot;;
sourcePatches   (front);
exposedPatchName back;

extrudeModel    linearNormal;       // linearNormal/linearDirection/wedge/sector/plane
linearNormalCoeffs { thickness 0.01; }
sectorCoeffs   { axisPt (0 0 0); axis (0 0 1); angle 5; }

nLayers         1;
expansionRatio  1.0;
mergeFaces      false;</code></pre>
<p>典型用途：把一个二维面拉伸成一层网格做二维算例；用 sector 模型做轴对称（wedge）算例。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>constructFrom</td><td>指定挤出源来自已有网格、表面或其他受支持的输入。</td></tr><tr><td>sourceCase</td><td>提供源网格或场的算例位置。相对路径以执行时工作目录为准。</td></tr><tr><td>extrudeModel</td><td>挤出几何模型，例如平移、旋转或法向挤出；各模型需要不同系数。</td></tr><tr><td>sourcePatches</td><td>作为挤出源的边界名称列表。</td></tr><tr><td>axis</td><td>旋转轴或方向向量；需明确是否要求单位向量。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>sourceFaceZones</td><td>sourcePatches ();</td></tr><tr><td>sectorCoeffs</td><td>&lt;- Also used for wedge</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · mesh/extrudeMesh/faceZoneExtrusion</h3><p>原始路径：<code>tutorials/mesh/extrudeMesh/faceZoneExtrusion/system/extrudeMeshDict</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/extrudeMesh/faceZoneExtrusion/system/extrudeMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/extrudemeshdict/1-extrudeMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/extrudeMesh/faceZoneExtrusion">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</code></pre><h3>示例 2 · compressible/rhoPimpleFoam/RAS/aerofoilNACA0012</h3><p>原始路径：<code>tutorials/compressible/rhoPimpleFoam/RAS/aerofoilNACA0012/system/extrudeMeshDict</code>；求解器：<code>rhoPimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/aerofoilNACA0012/system/extrudeMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/extrudemeshdict/2-extrudeMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/aerofoilNACA0012">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · multiphase/compressibleInterFoam/laminar/climbingRod</h3><p>原始路径：<code>tutorials/multiphase/compressibleInterFoam/laminar/climbingRod/system/extrudeMeshDict</code>；求解器：<code>compressibleInterFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/climbingRod/system/extrudeMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/extrudemeshdict/3-extrudeMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/climbingRod">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/extrudemesh/">extrudeMesh</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/extrudeMeshDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/extrudeMeshDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
