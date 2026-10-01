---
title: "system/setExprFieldsDict · setExprFieldsDict"
layout: reference
description: "下例在已有温度场 T 上设置随坐标变化的温度，运行 setExprFields 后生效。fieldMask 限定赋值区域，create 和 dimensions 用于新建场。表达式语法可通过 foamExprParserInfo 查询。边界表达式使用 setExprBoundaryFieldsDict，其结构按边界场接口配置。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>下例在已有温度场 T 上设置随坐标变化的温度，运行 setExprFields 后生效。fieldMask 限定赋值区域，create 和 dimensions 用于新建场。表达式语法可通过 foamExprParserInfo 查询。边界表达式使用 setExprBoundaryFieldsDict，其结构按边界场接口配置。</p><figure><img src="/assets/diagrams/reference-1.svg" alt="初始化配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/setExprFieldsDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>expressions</code> · <code>field</code> · <code>expression</code> · <code>fieldMask</code> · <code>dimensions</code> · <code>create</code></p><h2>关联命令</h2><p><a href="/commands/?q=setExprFields">setExprFields</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/setExprFieldsDict -keywords
setExprFields -help</code></pre><h2>7.6 system/setExprFieldsDict</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object setExprFieldsDict;
}
expressions
(
    setTemperature
    {
        field T;
        expression &quot;300 + 10*pos().x()&quot;;
    }
);</code></pre>
<p>下例在已有温度场 T 上设置随坐标变化的温度，运行 setExprFields 后生效。fieldMask 限定赋值区域，create 和 dimensions 用于新建场。表达式语法可通过 foamExprParserInfo 查询。边界表达式使用 setExprBoundaryFieldsDict，其结构按边界场接口配置。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>dimensions</td><td>七个指数依次表示质量、长度、时间、温度、物质量、电流、发光强度。量纲错误常在矩阵组装或赋值时暴露。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>readFields</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // Preload any required fields (optional)</td></tr><tr><td>expressions</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/simpleFoam/turbineSiting</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/turbineSiting/system/setExprFieldsDict</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbineSiting/system/setExprFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setexprfieldsdict/1-setExprFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbineSiting">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      setExprFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Preload any required fields (optional)
readFields      ( U );

_value1
{
    variables   ( &quot;rho=1.2&quot; );
    expression  #{ 0.5*rho*pow(mag(U),3) #};
    dimensions  [ kg s^-3 ];
}

expressions
(
    windPowerDensity
    {
        field   windPowerDensity;
        create  yes;
        &#36;_value1;
    }
);


// ************************************************************************* //</code></pre><h3>示例 2 · compressible/rhoPimpleFoam/RAS/TJunctionAverage</h3><p>原始路径：<code>tutorials/compressible/rhoPimpleFoam/RAS/TJunctionAverage/system/setExprFieldsDict</code>；求解器：<code>rhoPimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunctionAverage/system/setExprFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setexprfieldsdict/2-setExprFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunctionAverage">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      setExprFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

expressions
(
    T
    {
        field       T;
        dimensions  [0 0 0 1 0 0 0];

        constants
        {
            centre (0.21 0 0.01);
        }

        variables
        (
            &quot;radius = 0.1&quot;
        );

        fieldMask
        #{
            // Within the radius
            (mag(pos() - &#36;[(vector)constants.centre]) &lt; radius)

            // but only +ve y!
          &amp;&amp; pos((pos() - &#36;[(vector)constants.centre]).y()) &gt; 0
        #};

        expression
        #{
            300
          + 200 * (1 - mag(pos() - &#36;[(vector)constants.centre]) / radius)
        #};
    }
);


// ************************************************************************* //</code></pre><h3>示例 3 · etc/caseDicts/annotated</h3><p>原始路径：<code>etc/caseDicts/annotated/setExprFieldsDict</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/setExprFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setexprfieldsdict/3-setExprFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      setExprFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Preload any required fields (optional)
readFields      ( U );

expressions
(
    T
    {
        field       T;
        dimensions  [0 0 0 1 0 0 0];

        constants
        {
            centre (0.21 0 0.01);
        }

        variables
        (
            &quot;radius = 0.1&quot;
        );

        fieldMask
        #{
            // Within the radius
            (mag(pos() - &#36;[(vector)constants.centre]) &lt; radius)

            // but only +ve y!
          &amp;&amp; pos((pos() - &#36;[(vector)constants.centre]).y()) &gt; 0
        #};

        expression
        #{
            300
          + 200 * (1 - mag(pos() - &#36;[(vector)constants.centre]) / radius)
        #};
    }
);


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/setexprfields/">setExprFields</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/setExprFieldsDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/setExprFieldsDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
