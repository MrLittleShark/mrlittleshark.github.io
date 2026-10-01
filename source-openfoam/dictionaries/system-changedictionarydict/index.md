---
title: "system/changeDictionaryDict · changeDictionaryDict"
layout: reference
description: "dictionaryReplacement 按目标文件名组织替换条目，运行 changeDictionary 后写回相应文件。-instance 指定目标实例目录。单个键值可直接通过 foamDictionary 修改。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>dictionaryReplacement 按目标文件名组织替换条目，运行 changeDictionary 后写回相应文件。-instance 指定目标实例目录。单个键值可直接通过 foamDictionary 修改。</p><figure><img src="/assets/diagrams/reference-1.svg" alt="初始化配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/changeDictionaryDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dictionaryReplacement</code> · <code>boundaryField</code></p><h2>关联命令</h2><p><a href="/commands/?q=changeDictionary">changeDictionary</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/changeDictionaryDict -keywords
changeDictionary -help</code></pre><h2>7.13 system/changeDictionaryDict</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object changeDictionaryDict;
}
dictionaryReplacement
{
    U
    {
        boundaryField
        {
            inlet { type fixedValue; value uniform (2 0 0); }
        }
    }
}</code></pre>
<p>dictionaryReplacement 按目标文件名组织替换条目，运行 changeDictionary 后写回相应文件。-instance 指定目标实例目录。单个键值可直接通过 foamDictionary 修改。</p>
<h2>17.10 changeDictionaryDict</h2><pre><code class="language-openfoam">dictionaryReplacement
{
    boundary
    {
        minZ { type wall; }
    }
    U
    {
        boundaryField
        {
            &quot;(inlet|outlet)&quot; { type zeroGradient; }
        }
    }
}</code></pre>
<p>多区域算例（chtMultiRegionFoam）里，每个 region 一份，放在 system/&lt;region&gt;/changeDictionaryDict。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>dictionaryReplacement</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>boundary</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>mirrorMeshDict</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · preProcessing/createZeroDirectory/snappyMultiRegionHeater</h3><p>原始路径：<code>tutorials/preProcessing/createZeroDirectory/snappyMultiRegionHeater/system/topAir/changeDictionaryDict</code>；求解器：<code>chtMultiRegionFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/snappyMultiRegionHeater/system/topAir/changeDictionaryDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/changedictionarydict/1-changeDictionaryDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/snappyMultiRegionHeater">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      changeDictionaryDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dictionaryReplacement
{
}


// ************************************************************************* //</code></pre><h3>示例 2 · compressible/acousticFoam/obliqueAirJet/precursor</h3><p>原始路径：<code>tutorials/compressible/acousticFoam/obliqueAirJet/precursor/system/changeDictionaryDict</code>；求解器：<code>rhoPimpleAdiabaticFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/precursor/system/changeDictionaryDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/changedictionarydict/2-changeDictionaryDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/precursor">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      changeDictionaryDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

boundary
{
    box
    {
        type      patch;
        inGroups  1 ( patch );
    }
}


// ************************************************************************* //</code></pre><h3>示例 3 · incompressible/pimpleFoam/RAS/ellipsekkLOmega</h3><p>原始路径：<code>tutorials/incompressible/pimpleFoam/RAS/ellipsekkLOmega/system/changeDictionaryDict</code>；求解器：<code>pimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/ellipsekkLOmega/system/changeDictionaryDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/changedictionarydict/3-changeDictionaryDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/ellipsekkLOmega">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      changeDictionaryDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

mirrorMeshDict
{
    pointAndNormalDict
    {
        point   (0 0 0);
        normal  (0 -1 0);
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/changedictionary/">changeDictionary</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/topAir/changeDictionaryDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/topAir/changeDictionaryDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
