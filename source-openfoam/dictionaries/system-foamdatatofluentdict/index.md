---
title: "foamDataToFluentDict"
layout: reference
description: "将 OpenFOAM 场数据导出为 Fluent 数据格式时的字段映射。"
dictionary: true
cms_slug: "dictionary-foamdatatofluentdict"
---

<p>将 OpenFOAM 场数据导出为 Fluent 数据格式时的字段映射。</p><p>位置：<code>system/foamDataToFluentDict</code></p><h2>配置实例</h2><p>incompressible/icoFoam/elbow 中的 foamDataToFluentDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      foamDataToFluentDict;
}

p               1;

U               2;

T               3;

h               4;

k               5;

epsilon         6;

alpha1          150;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/icoFoam/elbow</summary><p>弯管算例将 OpenFOAM 结果导出为 Fluent 数据格式时，需要指定各字段对应的目标变量编号。</p>
<ul>
<li><code>p 1</code>、<code>U 2</code> 将压力与速度关联到编号 1、2。</li>
<li><code>T 3</code>、<code>h 4</code>、<code>k 5</code>、<code>epsilon 6</code> 给出温度、焓和湍流量的对应编号。</li>
<li><code>alpha1 150</code> 为体积分数字段指定编号；各行数值是导出标识，实际数值来自已有场文件。</li>
</ul>
<p>导出后在目标软件中核对字段名称、单位及分量，尤其注意不可压缩 p 的运动学压力单位。</p>
<p><a href="/assets/examples/v2512/foamdatatofluentdict/1-foamDataToFluentDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/elbow/system/foamDataToFluentDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/elbow">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      foamDataToFluentDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

p               1;

U               2;

T               3;

h               4;

k               5;

epsilon         6;

alpha1          150;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · etc/caseDicts/annotated</summary><p>这个简短模板只给出压力和速度的 Fluent 导出映射，适合最基本的流动结果转换。</p>
<ul>
<li><code>p 1</code> 指定压力场的目标变量编号。</li>
<li><code>U 2</code> 指定速度矢量的目标变量编号，三个速度分量由导出工具处理。</li>
<li>字典中的键应与时间目录内的实际字段名一致，附加字段可按所需格式添加对应关系。</li>
</ul>
<p>转换后用一个已知点或截面比较速度值，并确认目标软件采用的压力单位与原始求解器一致。</p>
<p><a href="/assets/examples/v2512/foamdatatofluentdict/2-foamDataToFluentDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/foamDataToFluentDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    note        &quot;OpenFOAM to Fluent interface control dictionary&quot;;
    class       dictionary;
    object      foamDataToFluentDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

p               1;
U               2;

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/foamdatatofluent/">foamDataToFluent</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>No field / No functionObject</td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
