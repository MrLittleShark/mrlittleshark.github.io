---
title: "probes"
layout: reference
description: "在固定空间位置记录场随时间的变化，输出探针数据文件。"
dictionary: true
cms_slug: "dictionary-probes"
---

<p>在固定空间位置记录场随时间的变化，输出探针数据文件。</p><p>位置：<code>system/controlDict → functions → probes</code></p><p><code>probes</code> 在固定空间位置记录场随时间的变化，常用于压力脉动、速度监测和温度响应。它输出体积很小的文本文件，适合每个时间步采样。</p>
<h3>示例：记录方腔中心速度与压力</h3>
<p>把以下对象加入 <code>system/controlDict</code> 的 <code>functions { ... }</code> 内：</p>
<pre><code class="language-foam">cavityProbes
{
    type probes;
    libs (sampling);
    fields (p U);
    interpolationScheme cell;
    writeControl timeStep;
    writeInterval 1;
    probeLocations
    (
        (0.05 0.05 0.005)
        (0.025 0.05 0.005)
    );
}
</code></pre>
<p><code>probeLocations</code> 以米给出探针坐标，两个位置位于基础方腔内部。<code>cell</code> 读取探针所在单元的值；需要插值到点时，可以研究 <code>cellPoint</code>。<code>writeInterval 1</code> 表示每步记录，独立于全场写出间隔。</p>
<p>数据位于 <code>postProcessing/cavityProbes/&lt;起始时间&gt;/p</code> 和 <code>U</code>。文件头记录探针编号，数据第一列为时间，之后按探针顺序排列；速度每个点有三个分量。变时间步计算的时间列一般不等间隔，做频谱前需要采用适合非均匀采样的方法，或先重采样。</p>
<p>探针落在域外时，日志会提示定位失败。几何缩放后更新坐标，移动网格中还需确认固定探针在整个采样阶段都位于目标流体区域。增加温度采样只需把 <code>fields</code> 改为 <code>(p U T)</code>，前提是案例中存在温度场。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common</summary><p>平面 Poiseuille 算例在一个固定位置监测速度随时间的变化。</p>
<ul>
<li><code>#includeEtc .../probes.cfg</code> 引入 probes 函数对象的公共设置。</li>
<li><code>fields (U)</code> 只采样速度向量。</li>
<li><code>probeLocations ((0 1 0))</code> 指定一个物理位置，应落在对应网格范围内。</li>
</ul>
<p>移动探针时按实际坐标修改位置；比较发展过程时保持采样间隔能够解析速度变化。</p>
<p><a href="/assets/examples/v2512/probes/1-probes.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common/system/probes">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common">案例目录</a></p><pre><code class="language-foam">// -*- C++ -*-

#includeEtc &quot;caseDicts/postProcessing/probes/probes.cfg&quot;

fields (U);
probeLocations
(
    (0 1 0)
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet</summary><p>cpuCabinet 同时监测部件平均温度和局部探针，用于区分整体温升与局部热点。</p>
<ul>
<li><code>Volume1_v_CPU</code>、<code>Volume3_v_fins</code> 采用 <code>volAverage</code> 对各自区域的 T 做体积加权平均。</li>
<li><code>probesFins/region v_fins</code> 在两个给定位置采样固体温度。</li>
<li><code>probesFluid/region domain0</code> 在流体区采样 <code>(T U)</code>，与固体探针使用不同网格。</li>
<li><code>writeControl timeStep</code>、<code>writeInterval 1</code> 每个求解步记录，<code>interpolationScheme cell</code> 读取所在单元值。</li>
</ul>
<p>改动部件几何后重新检查 region 名称和探针坐标，避免采样点落到其他区域或域外。</p>
<p><a href="/assets/examples/v2512/probes/2-probes.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet/system/probes">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet">案例目录</a></p><pre><code class="language-foam">// -*- C++ -*-

_volFieldValue
{
    type            volFieldValue;
    libs            (fieldFunctionObjects);
    enabled         true;
    writeControl    timeStep;
    writeInterval   1;
    log             true;
    valueOutput     false;
    writeFields     false;
}

Volume1_v_CPU
{
    ${_volFieldValue}

    regionType      cellZone;
    name            v_CPU;
    region          v_CPU;
    operation       volAverage;
    fields          ( T );
}

Volume3_v_fins
{
    ${_volFieldValue}

    regionType      cellZone;
    name            v_fins;
    region          v_fins;
    operation       volAverage;
    fields          ( T );
}

probesFins
{
    type            probes;
    libs            (sampling);
    writeControl    timeStep;
    writeInterval   1;
    interpolationScheme cell;
    region          v_fins;

    fields          ( T );

    probeLocations
    (
        (0.118 0.01 -0.125)
        (0.118 0.03 -0.125)
    );
}

probesFluid
{
    type            probes;
    libs            (sampling);
    writeControl    timeStep;
    writeInterval   1;
    interpolationScheme cell;
    region         domain0;
    log             true;
    verbose         true;

    fields          (T U);

    probeLocations
    (
        (0.118 0.035 -0.125)
        (0.118 0.07 -0.125)
    );
}
#remove (_volFieldValue _surfaceFieldValue)

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · compressible/rhoPimpleAdiabaticFoam/rutlandVortex2D</summary><p>Rutland 涡算例在两个对称位置记录压力，以观察可压缩涡运动的时间变化。</p>
<ul>
<li><code>functions/probes</code> 的 <code>type probes</code> 与 <code>libs (sampling)</code> 启用点采样。</li>
<li>位置为 <code>(3 2 0)</code> 和 <code>(3 -2 0)</code>，<code>fields (p)</code> 保存压力。</li>
<li>主计算从 0 到 0.22528 s，固定步长 <code>3.2e-5</code> s；主场每 100 步、即 0.0032 s 写出。</li>
<li><code>writeFormat binary</code> 使用二进制主场文件，采样文件由函数对象自身的输出设置管理。</li>
</ul>
<p>比较两个探针的相位和幅值时使用同一时间轴，并核对采样频率是否满足目标频率范围。</p>
<p><a href="/assets/examples/v2512/probes/3-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoPimpleAdiabaticFoam/rutlandVortex2D/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleAdiabaticFoam/rutlandVortex2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

application       rhoPimpleAdiabaticFoam;

startFrom         startTime;

startTime         0;

stopAt            endTime;

endTime           0.22528;

deltaT            3.2e-05;

writeControl      timeStep;

writeInterval     100;

purgeWrite        0;

writeFormat       binary;

writePrecision    10;

writeCompression  off;

timeFormat        general;

timePrecision     6;

runTimeModifiable true;

functions
{
    probes
    {
        type probes;

        libs (sampling);

        probeLocations
        (
            (3.0  2.0  0.0)
            (3.0 -2.0  0.0)
        );

        fields
        (
            p
        );
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
