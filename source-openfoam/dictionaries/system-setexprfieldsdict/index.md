---
title: "setExprFieldsDict"
layout: reference
description: "通过坐标、时间或已有场的表达式，生成或修改单元场。"
dictionary: true
cms_slug: "dictionary-setexprfieldsdict"
---

<p>通过坐标、时间或已有场的表达式，生成或修改单元场。</p><p>位置：<code>system/setExprFieldsDict</code></p><h2>配置实例</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object setExprFieldsDict;
}
expressions
(
    setTemperature
    {
        field T;
        expression "300 + 10*pos().x()";
    }
);</code></pre>
<p>下例在已有温度场 T 上设置随坐标变化的温度，运行 setExprFields 后生效。fieldMask 限定赋值区域，create 和 dimensions 用于新建场。表达式语法可通过 foamExprParserInfo 查询。边界表达式使用 setExprBoundaryFieldsDict，其结构按边界场接口配置。</p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>dimensions</td><td>七个指数依次表示质量、长度、时间、温度、物质量、电流、发光强度。量纲错误常在矩阵组装或赋值时暴露。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/simpleFoam/turbineSiting</summary><p>turbineSiting 根据已有风速场计算风功率密度，结果供风机选址比较。</p>
<ul>
<li><code>readFields (U)</code> 先读取速度。</li>
<li>变量 <code>rho=1.2</code> 指定空气密度，表达式 <code>0.5*rho*pow(mag(U),3)</code> 计算与风速三次方成正比的通量密度。</li>
<li><code>field windPowerDensity</code>、<code>create yes</code> 创建新字段，量纲 <code>[kg s^-3]</code> 等于 W/m²。</li>
<li><code>$_value1</code> 复用已定义的表达式与量纲。</li>
</ul>
<p>更换空气密度或速度统计方式时相应修改输入；平均速度的三次方与速度三次方的平均并不相同。</p>
<p><a href="/assets/examples/v2512/setexprfieldsdict/1-setExprFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbineSiting/system/setExprFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbineSiting">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
        $_value1;
    }
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · compressible/rhoPimpleFoam/RAS/TJunctionAverage</summary><p>T 形混合管用表达式在指定半球状区域内设置温度分布，便于构造非均匀初始条件。</p>
<ul>
<li>目标为字段 <code>T</code>，量纲 <code>[0 0 0 1 0 0 0]</code> 表示 K。</li>
<li><code>centre (0.21 0 0.01)</code> 与 <code>radius=0.1</code> 定义区域中心和尺寸。</li>
<li><code>fieldMask</code> 同时限制到中心的距离与 y 方向位置，使赋值只覆盖所选半区。</li>
<li>温度表达式 <code>300 + 200*(1-r/radius)</code> 在中心为 500 K，在半径边缘降到 300 K。</li>
</ul>
<p>移动热区时修改 centre，改变幅值时修改 200；同时检查未被掩膜选中的原温度场。</p>
<p><a href="/assets/examples/v2512/setexprfieldsdict/2-setExprFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunctionAverage/system/setExprFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunctionAverage">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
            (mag(pos() - $[(vector)constants.centre]) &lt; radius)

            // but only +ve y!
          &amp;&amp; pos((pos() - $[(vector)constants.centre]).y()) &gt; 0
        #};

        expression
        #{
            300
          + 200 * (1 - mag(pos() - $[(vector)constants.centre]) / radius)
        #};
    }
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · etc/caseDicts/annotated</summary><p>这是 setExprFields 的附注模板，用一个局部温度分布演示掩膜、常量与表达式的配合。</p>
<ul>
<li><code>field T</code> 和温度量纲声明要修改的字段。</li>
<li><code>centre (0.21 0 0.01)</code>、<code>radius=0.1</code> 定义局部坐标尺度。</li>
<li><code>fieldMask</code> 选择球内且位于中心 y 正侧的区域。</li>
<li>表达式从中心 500 K 线性过渡到区域边缘 300 K；<code>readFields (U)</code> 演示预读其他场的入口。</li>
</ul>
<p>复制到自己的算例时换成实际坐标，并确认目标时间目录中已存在所需字段。</p>
<p><a href="/assets/examples/v2512/setexprfieldsdict/3-setExprFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/setExprFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
            (mag(pos() - $[(vector)constants.centre]) &lt; radius)

            // but only +ve y!
          &amp;&amp; pos((pos() - $[(vector)constants.centre]).y()) &gt; 0
        #};

        expression
        #{
            300
          + 200 * (1 - mag(pos() - $[(vector)constants.centre]) / radius)
        #};
    }
);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/setexprfields/">setExprFields</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
