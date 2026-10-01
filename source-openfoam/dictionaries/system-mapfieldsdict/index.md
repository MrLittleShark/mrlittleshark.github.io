---
title: "system/mapFieldsDict · mapFieldsDict"
layout: reference
description: "mapFieldsDict 用于源算例与目标算例边界不一致时的场映射。patchMap 中每组名称依次为目标边界和源边界。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>mapFieldsDict 用于源算例与目标算例边界不一致时的场映射。patchMap 中每组名称依次为目标边界和源边界。</p><figure><img src="/assets/diagrams/reference-1.svg" alt="初始化配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/mapFieldsDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>patchMap</code> · <code>cuttingPatches</code></p><h2>关联命令</h2><p><a href="/commands/?q=mapFields">mapFields</a> · <a href="/commands/?q=mapFieldsPar">mapFieldsPar</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/mapFieldsDict -keywords
mapFields -help</code></pre><h2>7.12 system/mapFieldsDict</h2><p>mapFieldsDict 用于源算例与目标算例边界不一致时的场映射。patchMap 中每组名称依次为目标边界和源边界。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object mapFieldsDict;
}
patchMap
(
    inlet sourceInlet
    outlet sourceOutlet
);
cuttingPatches (newCutBoundary);</code></pre>
<p>在目标算例中执行 mapFields ../sourceCase -sourceTime latestTime。cuttingPatches 指定切穿源计算域的目标边界，其数值由源域内部插值得到。-consistent 适用于边界拓扑匹配的算例。映射体积分数等守恒量后，应检查有界性及积分守恒。</p>
<h2>17.9 mapFieldsDict</h2><pre><code class="language-openfoam">patchMap        ( inlet1 inlet );   // 源算例 patch → 目标算例 patch
cuttingPatches  ( outlet );         // 被切开的 patch（源网格不覆盖的部分）</code></pre>
<p>网格边界一致时可以完全不用这个文件，直接 mapFields ../src -consistent。</p><h2>从真实配置理解关键条目</h2><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>patchMap</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/icoFoam/cavity/cavityGrade</h3><p>原始路径：<code>tutorials/incompressible/icoFoam/cavity/cavityGrade/system/mapFieldsDict</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavityGrade/system/mapFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/mapfieldsdict/1-mapFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavityGrade">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mapFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

patchMap        ( );

cuttingPatches  ( );


// ************************************************************************* //</code></pre><h3>示例 2 · verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common</h3><p>原始路径：<code>tutorials/verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common/system/mapFieldsDict</code>；求解器：<code>buoyantBoussinesqSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common/system/mapFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/mapfieldsdict/2-mapFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mapFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

patchMap ( );

cuttingPatches
(
    terrain top
);


// ************************************************************************* //</code></pre><h3>示例 3 · incompressible/icoFoam/cavity/cavityClipped</h3><p>原始路径：<code>tutorials/incompressible/icoFoam/cavity/cavityClipped/system/mapFieldsDict</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavityClipped/system/mapFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/mapfieldsdict/3-mapFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavityClipped">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mapFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

patchMap        (lid movingWall);

cuttingPatches  ();


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/mapfields/">mapFields</a> · <a href="/commands/mapfieldspar/">mapFieldsPar</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/mapFieldsDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/mapFieldsDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
