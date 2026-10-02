---
title: "probesDict"
layout: reference
description: "教程中单独保存的探针采样配置。"
dictionary: true
cms_slug: "dictionary-probesdict"
---

<p>教程中单独保存的探针采样配置。</p><p>位置：<code>system/probesDict</code></p><h2>配置实例</h2><p>lagrangian/reactingParcelFoam/parcelInBox 中的 probesDict：</p><pre><code class="language-foam">FoamFile
{
    version         2.0;
    format          ascii;
    class           dictionary;
    location        system;
    object          probesDict;
}

// Fields to be probed. runTime modifiable!
fields
(
    T H2O p kT
);

// Locations to be probed. runTime modifiable!
probeLocations
(
    (0.005 0.0 0.0)
);</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/reactingParcelFoam/parcelInBox</summary><p>parcelInBox 在指定位置记录载气的温度、水蒸气、压力及 kT 字段，用于观察颗粒与气相的耦合响应。</p>
<ul>
<li><code>fields (T H2O p kT)</code> 选择四个实际场名，其中 H2O 对应求解器中的水蒸气组分场。</li>
<li><code>probeLocations ((0.005 0 0))</code> 把探针放在 x=5 mm 处，坐标单位与网格一致。</li>
<li>采样值来自该点所在单元及所用插值设置，输出时间间隔由调用此字典的采样对象控制。</li>
</ul>
<p>新增探针时在位置列表中增加三分量坐标，并确认点位于计算域内，再比较靠近颗粒与远离颗粒位置的响应。</p>
<p><a href="/assets/examples/v2512/probesdict/1-probesDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/parcelInBox/system/probesDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/parcelInBox">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version         2.0;
    format          ascii;
    class           dictionary;
    location        system;
    object          probesDict;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //


// Fields to be probed. runTime modifiable!
fields
(
    T H2O p kT
);

// Locations to be probed. runTime modifiable!
probeLocations
(
    (0.005 0.0 0.0)
);

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>未找到指定场或函数对象：<code>No field / No functionObject</code></td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
