---
title: "particleTrackProperties"
layout: reference
description: "粒子轨迹重建或轨迹输出的控制。"
dictionary: true
cms_slug: "dictionary-particletrackproperties"
---

<p>粒子轨迹重建或轨迹输出的控制。</p><p>位置：<code>constant/particleTrackProperties</code></p><h2>配置实例</h2><p>lagrangian/reactingParcelFoam/airRecirculationRoom/transient 中的 particleTrackProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      particleTrackProperties;
}

cloud           reactingCloud1;

sampleFrequency 1;

maxPositions    1000000;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>cloud</td><td>输入颗粒云名称。</td></tr><tr><td>sampleFrequency</td><td>轨迹取样频率；改变它会影响每条输出轨迹的稠密程度。</td></tr><tr><td>maxPositions</td><td>单条轨迹保留位置数量的上限，较大的值增加内存或输出需求。</td></tr><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/reactingParcelFoam/airRecirculationRoom/transient</summary><p>airRecirculationRoom 将不同时刻保存的 reactingCloud1 粒子位置连成轨迹，用于观察颗粒在室内回流中的运动。</p>
<ul>
<li><code>cloud reactingCloud1</code> 选择已有粒子云。</li>
<li><code>sampleFrequency 1</code> 表示按粒子编号采样时每个粒子都保留；增大此值会减少展示的轨迹数量。</li>
<li><code>maxPositions 1000000</code> 给每条轨迹允许保存的位置数设置上限。轨迹在时间上的分辨率来自已保存的计算时刻。</li>
</ul>
<p>粒子过多导致图像难以辨认时先提高 sampleFrequency；需要更清晰的时间变化则调整原计算的颗粒输出间隔。</p>
<p><a href="/assets/examples/v2512/particletrackproperties/1-particleTrackProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/airRecirculationRoom/transient/constant/particleTrackProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/airRecirculationRoom/transient">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      particleTrackProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

cloud           reactingCloud1;

sampleFrequency 1;

maxPositions    1000000;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · lagrangian/reactingParcelFoam/filter</summary><p>filter 算例把粒子轨迹导出为可播放的 glTF 文件，并用粒径着色。</p>
<ul>
<li><code>cloud reactingCloud1</code>、<code>sampleFrequency 1</code> 选择全部采样粒子，<code>maxPositions 1000000</code> 限制单条轨迹的位置数。</li>
<li><code>setFormat gltf</code> 选择 glTF 格式，<code>animate yes</code> 生成动画信息。</li>
<li><code>colour yes</code>、<code>colour field</code> 和 <code>colourField d</code> 让颜色随粒径字段变化，<code>fields (d)</code> 同时指定该导出字段。</li>
</ul>
<p>如果粒径变化范围很窄，可换用温度等已保存字段，并同时更新 fields 与 colourField。</p>
<p><a href="/assets/examples/v2512/particletrackproperties/2-particleTrackProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/filter/constant/particleTrackProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/filter">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      particleTrackProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

cloud           reactingCloud1;

sampleFrequency 1;

maxPositions    1000000;

//maxTracks       5;

setFormat       gltf;

formatOptions
{
    animate         yes;
    colour          yes;

    animationInfo
    {
        colour          field;
        colourField     d;
        //min             0;
        //max             0.002;
        //alpha           1.0;
    }
}

fields          (d);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/particletracks/">particleTracks</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>未找到指定场或函数对象：<code>No field / No functionObject</code></td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
