---
title: "system/setExprBoundaryFieldsDict · setExprBoundaryFieldsDict"
layout: reference
description: "通过表达式为边界场赋值。表达式中坐标、时间、场名及量纲需要与解析器上下文一致；它修改场值，并不自动把边界条件替换为随时间重复求值的 coded 边界。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>通过表达式为边界场赋值。表达式中坐标、时间、场名及量纲需要与解析器上下文一致；它修改场值，并不自动把边界条件替换为随时间重复求值的 coded 边界。</p><figure><img src="/assets/diagrams/reference-1.svg" alt="初始化配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>pattern</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>readFields</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // Preload any required fields (optional)</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · compressible/rhoPimpleFoam/RAS/TJunctionAverage</h3><p>原始路径：<code>tutorials/compressible/rhoPimpleFoam/RAS/TJunctionAverage/system/setExprBoundaryFieldsDict</code>；求解器：<code>rhoPimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunctionAverage/system/setExprBoundaryFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setexprboundaryfieldsdict/1-setExprBoundaryFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunctionAverage">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      setExprBoundaryFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

pattern
{
    field   T;

    expressions
    (
        {
            patch   outlet2;
            target  something;
            expression #{ (pos().x() &lt; 1e-4 ? 60 : 120) #};
        }
    );
}


// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/simpleFoam/turbineSiting</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/turbineSiting/system/setExprBoundaryFieldsDict</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbineSiting/system/setExprBoundaryFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setexprboundaryfieldsdict/2-setExprBoundaryFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbineSiting">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      setExprBoundaryFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Preload any required fields (optional)
readFields      ( U );

updateBCs
{
    field   windPowerDensity;

    _value1
    {
        target      value;
        variables   ( &quot;rho=1.2&quot; );
        expression  #{ 0.5*rho*pow(mag(U),3) #};
    }

    expressions
    (
        { &#36;_value1; patch inlet; }
        { &#36;_value1; patch outlet; }
        { &#36;_value1; patch sides; }
        { &#36;_value1; patch top; }
    );
}


// ************************************************************************* //</code></pre><h3>示例 3 · etc/caseDicts/annotated</h3><p>原始路径：<code>etc/caseDicts/annotated/setExprBoundaryFieldsDict</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/setExprBoundaryFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setexprboundaryfieldsdict/3-setExprBoundaryFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      setExprBoundaryFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Preload any required fields (optional)
readFields      ( U );

pattern
{
    field   T;

    expressions
    (
        {
            patch   outlet2;
            target  something;
            expression #{ (pos().x() &lt; 1e-4 ? 60 : 120) #};
        }
    );
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/setexprboundaryfields/">setExprBoundaryFields</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/setExprBoundaryFieldsDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/setExprBoundaryFieldsDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
