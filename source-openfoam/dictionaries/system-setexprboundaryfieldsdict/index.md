---
title: "setExprBoundaryFieldsDict"
layout: reference
description: "通过表达式为边界场赋值。"
dictionary: true
cms_slug: "dictionary-setexprboundaryfieldsdict"
---

<p>通过表达式为边界场赋值。</p><p>位置：<code>system/setExprBoundaryFieldsDict</code></p><h2>配置实例</h2><p>compressible/rhoPimpleFoam/RAS/TJunctionAverage 中的 setExprBoundaryFieldsDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      setExprBoundaryFieldsDict;
}

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
}</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · compressible/rhoPimpleFoam/RAS/TJunctionAverage</summary><p>TJunctionAverage 用表达式向温度字段的指定边界条目写入空间分段数值，演示 setExprBoundaryFields 的字典操作。</p>
<ul>
<li><code>field T</code> 选择温度场，<code>patch outlet2</code> 指定要处理的边界。</li>
<li>表达式 <code>pos().x() &lt; 1e-4 ? 60 : 120</code> 按面中心 x 坐标分成两区，分别生成 60 和 120。</li>
<li><code>target something</code> 会将结果写入该边界下名为 something 的条目。若目的是设置边界的实际 value，应改成 <code>target value</code>，并选用使用 value 的边界条件。</li>
</ul>
<p>移植为实际温度设置时，数值使用 K，阈值使用网格坐标的长度单位；先检查分区位置，再执行写入。</p>
<p><a href="/assets/examples/v2512/setexprboundaryfieldsdict/1-setExprBoundaryFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunctionAverage/system/setExprBoundaryFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunctionAverage">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/simpleFoam/turbineSiting</summary><p>turbineSiting 从入口、出口、侧面和顶面的速度计算风功率密度，并写入 windPowerDensity 的边界值。</p>
<ul>
<li><code>readFields (U)</code> 提前载入速度场，<code>updateBCs</code> 子字典中的 <code>field windPowerDensity</code> 指定要更新的目标场。</li>
<li><code>rho=1.2</code> 使用空气密度 1.2 kg/m³，表达式 <code>0.5*rho*pow(mag(U),3)</code> 给出单位面积动能通量，单位 W/m²。</li>
<li><code>target value</code> 将结果写到实际边界值；后续边界条目复用同一表达式，减少重复配置。</li>
</ul>
<p>风速翻倍时该表达式结果变为原来的八倍。采用其他空气密度时修改 rho，并确认 U 的单位为 m/s。</p>
<p><a href="/assets/examples/v2512/setexprboundaryfieldsdict/2-setExprBoundaryFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbineSiting/system/setExprBoundaryFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbineSiting">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
        { $_value1; patch inlet; }
        { $_value1; patch outlet; }
        { $_value1; patch sides; }
        { $_value1; patch top; }
    );
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · etc/caseDicts/annotated</summary><p>这个注释模板展示如何通过边界表达式写入自定义条目，适合学习字段、边界和目标条目的对应关系。</p>
<ul>
<li><code>field T</code> 和 <code>patch outlet2</code> 定位到 T 的 outlet2 边界；<code>readFields (U)</code> 可供表达式引用已有速度数据。</li>
<li>条件表达式按 x=0.0001 m 将结果分为 60、120 两个值。</li>
<li><code>target something</code> 是演示用的条目名；要更新 T 的 value，将它改为 <code>target value</code>，并按实际温度设置数值。</li>
</ul>
<p>表达式使用面中心坐标，几何移动或缩放后应同步调整分区阈值。</p>
<p><a href="/assets/examples/v2512/setexprboundaryfieldsdict/3-setExprBoundaryFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/setExprBoundaryFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/setexprboundaryfields/">setExprBoundaryFields</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
