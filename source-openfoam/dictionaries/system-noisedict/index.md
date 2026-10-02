---
title: "noiseDict"
layout: reference
description: "设置压力时序的频谱分析，包括数据来源、采样分块、窗函数和输出。"
dictionary: true
cms_slug: "dictionary-noisedict"
---

<p>设置压力时序的频谱分析，包括数据来源、采样分块、窗函数和输出。</p><p>位置：<code>system/noiseDict</code></p><h2>配置实例</h2><p>noiseDict 通过 noiseModel 选择 pointNoise、surfaceNoise 等模型，并定义输入数据、FFT 分块和窗函数。频谱分析采用等时间间隔采样，采样时长决定频率分辨率，Nyquist 频率为采样频率的一半。</p>
<p>particleTracksDict 指定粒子云、采样频率和轨迹长度，轨迹重建使用求解阶段保存的粒子标识。steadyParticleTracksDict 用于稳态轨迹处理。字段设置采用对应粒子模型的教程结构。</p><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · etc/caseDicts/annotated</summary><p>noiseDict 的附注示例演示从表面压力时间序列计算噪声频谱。</p>
<ul>
<li><code>noiseModel surfaceNoise</code> 选中表面分析，读取指定 Ensight <code>.case</code> 文件并使用 Ensight 输出。</li>
<li><code>windowModel Hanning</code>、<code>overlapPercent 50</code> 采用 Hann 窗和 50% 重叠分段。</li>
<li><code>N 4096</code> 指定每段样本数量；采样间隔为 Δt 时，基本频率间隔约为 1/(4096Δt)。</li>
<li><code>fu 15000</code> 限定分析的高频范围，需与采样的 Nyquist 频率相容。</li>
<li><code>rhoRef 1.205</code> 给参考密度；文件中 pointNoiseCoeffs 是另一种输入方式的配置入口。</li>
</ul>
<p>改变采样频率或记录长度后同时重新选择 N、频率范围与分段重叠。</p>
<p><a href="/assets/examples/v2512/noisedict/1-noiseDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/noiseDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;system&quot;;
    object      noiseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

noiseModel      surfaceNoise;

surfaceNoiseCoeffs
{
    windowModel     Hanning;

    HanningCoeffs
    {
        // Window overlap percentage
        overlapPercent  50;
        symmetric       yes;
        extended        yes;

        // Optional number of windows, default = all available
        // nWindow         1;
    }

/*
    windowModel     uniform;

    uniformCoeffs
    {
        // Window overlap percentage
        overlapPercent  50;

        value           1;

        // Optional number of windows, default = all available
        // nWindow         1;
    }
*/


    // Input file(s)
    file   &quot;postProcessing/faceSource1/surface/patch1/patch1.case&quot;;
    // Multiple inputs
    //files   ( &quot;postProcessing/faceSource1/surface/patch1/patch1.case&quot;
    //          &quot;postProcessing/faceSource2/surface/patch2/patch2.case&quot; );

    // Surface reader
    reader      ensight;

    // Surface writer
    writer      ensight;

    // Collate times for ensight output - ensures geometry is only written once
    writeOptions
    {
        ensight
        {
            collateTimes true;
        }
    }

    // Reference density (to convert from kinematic to static pressure)
    rhoRef          1.205;

    // Number of samples in sampling window, default = 2^16 (=65536)
    N               4096; // 8192; // 4096;

    // Lower frequency limit, default = 25Hz
    //fl              25;

    // Upper frequency limit, default = 10kHz
    fu              15000;

    // Start time, default = 0s
    //startTime       0;

    // Write interval for FFT data, default = 1
    //fftWriteInterval 100;

    // Bounds for valid pressure from input source
        // Maximum pressure, default 0.5*VGREAT
        //maxPressure 150e5;

        // Minimum pressure, default -0.5*VGREAT
        //minPressure -150e5;
}

pointNoiseCoeffs
{
    file            &quot;pressureData&quot;;
    //files           ( &quot;pressureData&quot; &quot;pressureData2&quot;);
    nHeaderLine     1;
    refColumn       0;
    componentColumns (1);
    separator       &quot; &quot;;
    mergeSeparators yes;

    HanningCoeffs
    {
        // Window overlap percentage
        overlapPercent  50;
        symmetric       yes;
        extended        yes;

        // Optional number of windows, default = all available
        //nWindow         5;
    }

    // Graph format, default = raw
    graphFormat     raw;

    // Reference density (to convert from kinematic to static pressure)
    rhoRef          1.2;

    // Number of samples in sampling window, default = 2^16 (=65536)
    N               4096;

    // Lower frequency limit, default = 25Hz
    //fl              25;

    // Upper frequency limit, default = 10kHz
    //fu              10000;

    // Start time, default = 0s
    //startTime       0;

    // Write interval for FFT data, default = 1
    fftWriteInterval 100;

    // Bounds for valid pressure from input source
        // Maximum pressure, default 0.5*VGREAT
        //maxPressure 150e5;

        // Minimum pressure, default -0.5*VGREAT
        //minPressure -150e5;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/noise/">noise</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>未找到指定场或函数对象：<code>No field / No functionObject</code></td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
