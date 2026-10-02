---
title: "surfaceFieldValue"
layout: reference
description: "在边界、面区域或采样面上计算场的求和、平均与面积积分。"
dictionary: true
cms_slug: "dictionary-surfacefieldvalue"
---

<p>在边界、面区域或采样面上计算场的求和、平均与面积积分。</p><p>位置：<code>system/controlDict → functions → surfaceFieldValue</code></p><p><code>surfaceFieldValue</code> 对网格 patch、faceZone 或采样表面上的场进行求和、平均和积分，适合出口流量、壁面平均温度及表面热流积分。</p>
<h3>示例：出口体积流量</h3>
<p>在 <code>simpleFoam</code> 等不可压缩算例的 <code>system/controlDict/functions</code> 中加入：</p>
<pre><code class="language-foam">outletFlow
{
    type surfaceFieldValue;
    libs (fieldFunctionObjects);
    regionType patch;
    name outlet;
    operation sum;
    fields (phi);
    writeFields false;
    writeArea true;
    writeControl timeStep;
    writeInterval 1;
}
</code></pre>
<p><code>name</code> 是实际出口 patch。<code>phi</code> 已包含每个网格面的面积贡献，<code>sum</code> 将其相加得到总流量。<code>writeArea</code> 同时记录所选面积，有助于检查边界选择是否正确。正值通常表示流出域外，负值表示流入。</p>
<p>不可压缩场的 <code>phi</code> 常以 m³/s 表示，可压缩场则常以 kg/s 表示，读取字段量纲确认。对壁面热流密度 W/m²，需要 <code>areaIntegrate</code> 才得到 W；对温度场使用 <code>areaAverage</code> 得到面积平均温度。</p>
<p>截面平均温度若用于流体携热量，通常应按质量通量加权。此时可研究 <code>weightedAverage</code> 或相应加权面积操作，并明确权重场是否已经包含面积。发生回流时，正负通量会抵消，可以按需要分别统计流入与流出部分。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/simpleReactingParcelFoam/verticalChannel</summary><p>稳态垂直通道用出口通量加权平均，获得更适合表示流出流体状态的温度和水蒸气含量。</p>
<ul>
<li><code>regionType patch</code>、<code>name outlet</code> 选择出口。</li>
<li><code>operation weightedAverage</code> 配合 <code>weightField phi</code> 按面通量加权。</li>
<li><code>fields (H2O T)</code> 输出组分与温度，<code>writeFields no</code> 只保存汇总结果。</li>
<li><code>writeControl writeTime</code> 跟随主结果写出，主场每 20 次迭代保存。</li>
</ul>
<p>出口存在回流时检查通量符号及加权结果的含义，必要时分别统计流入与流出部分。</p>
<p><a href="/assets/examples/v2512/surfacefieldvalue/1-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/simpleReactingParcelFoam/verticalChannel/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/simpleReactingParcelFoam/verticalChannel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      controlDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

application     simpleReactingParcelFoam;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         500;

deltaT          1;

writeControl    timeStep;

writeInterval   20;

purgeWrite      10;

writeFormat     ascii;

writePrecision  10;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;


functions
{
    avgOutlets
    {
        type            surfaceFieldValue;
        libs            (fieldFunctionObjects);
        enabled         yes;
        writeControl    writeTime;
        log             yes;
        writeFields     no;
        regionType      patch;
        name            outlet;
        operation       weightedAverage;
        weightField     phi;
        fields
        (
            H2O
            T
        );
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · lagrangian/reactingParcelFoam/verticalChannelLTS</summary><p>verticalChannelLTS 在局部时间步迭代中监测出口混合状态。</p>
<ul>
<li><code>surfaceFieldValue</code> 选择 outlet patch。</li>
<li><code>weightedAverage</code> 与 <code>weightField phi</code> 计算通量加权的 H2O、T。</li>
<li>主控制每 10 步写出，函数对象采用 <code>writeTime</code> 与之同步。</li>
<li><code>writeFields no</code> 保留简洁的统计文件，日志也会显示数值。</li>
</ul>
<p>判断稳态收敛时同时看加权出口量和残差；局部时间步的迭代编号应按该求解过程解释。</p>
<p><a href="/assets/examples/v2512/surfacefieldvalue/2-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/verticalChannelLTS/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/verticalChannelLTS">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      controlDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

application     reactingParcelFoam;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         300;

deltaT          1;

writeControl    timeStep;

writeInterval   10;

purgeWrite      20;

writeFormat     ascii;

writePrecision  10;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;

profiling
{
    memInfo     true;
}

functions
{
    surfaceFieldValue1
    {
        type            surfaceFieldValue;
        libs            (fieldFunctionObjects);
        writeControl    writeTime;
        log             yes;
        writeFields     no;
        regionType      patch;
        name            outlet;
        operation       weightedAverage;
        weightField     phi;
        fields
        (
            H2O
            T
        );
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · heatTransfer/chtMultiRegionFoam/windshieldDefrost</summary><p>挡风玻璃除霜的多区域计算每步监测 cabin 流体区入口通量。</p>
<ul>
<li><code>region cabin</code> 将函数对象绑定到客舱网格。</li>
<li><code>regionType patch</code>、<code>name inlet</code> 选择入口。</li>
<li><code>operation sum</code> 对已有面通量 phi 直接求和；phi 已包含面面积，求和时无需再乘面积。</li>
<li>每步记录并打印，主场则按 1 s 的可调时间间隔保存。</li>
</ul>
<p>按该区域 phi 的量纲解释质量或体积流率，再与出口及区域质量变化比较。</p>
<p><a href="/assets/examples/v2512/surfacefieldvalue/3-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/windshieldDefrost/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/windshieldDefrost">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      controlDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

application     chtMultiRegionFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         400;

deltaT          0.0001;

writeControl    adjustable;

writeInterval   1;

purgeWrite      0;

writeFormat     binary;

writePrecision  10;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;

adjustTimeStep  yes;

maxCo           5;

maxDeltaT       1;

functions
{
    massFlux
    {
        type            surfaceFieldValue;
        libs            (fieldFunctionObjects);
        enabled         yes;
        writeControl    timeStep;
        writeInterval   1;
        log             yes;
        writeFields     no;
        regionType      patch;
        name            inlet;
        operation       sum;
        fields          (phi);
        region          cabin;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
