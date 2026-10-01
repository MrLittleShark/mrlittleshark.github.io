---
title: "system/noiseDict · noiseDict"
layout: reference
description: "noiseDict 通过 noiseModel 选择 pointNoise、surfaceNoise 等模型，并定义输入数据、FFT 分块和窗函数。频谱分析采用等时间间隔采样，采样时长决定频率分辨率，Nyquist 频率为采样频率的一半。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>noiseDict 通过 noiseModel 选择 pointNoise、surfaceNoise 等模型，并定义输入数据、FFT 分块和窗函数。频谱分析采用等时间间隔采样，采样时长决定频率分辨率，Nyquist 频率为采样频率的一半。</p><figure><img src="/assets/diagrams/reference-8.svg" alt="后处理配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/noiseDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>noiseModel</code> · <code>pointNoise</code> · <code>surfaceNoise</code></p><h2>关联命令</h2><p><a href="/commands/?q=noise">noise</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/noiseDict -keywords
noise -help</code></pre><h2>10.7 system/noiseDict 与粒子后处理</h2><p>noiseDict 通过 noiseModel 选择 pointNoise、surfaceNoise 等模型，并定义输入数据、FFT 分块和窗函数。频谱分析采用等时间间隔采样，采样时长决定频率分辨率，Nyquist 频率为采样频率的一半。</p>
<p>particleTracksDict 指定粒子云、采样频率和轨迹长度，轨迹重建使用求解阶段保存的粒子标识。steadyParticleTracksDict 用于稳态轨迹处理。字段设置采用对应粒子模型的教程结构。</p><h2>从真实配置理解关键条目</h2><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>noiseModel</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>overlapPercent</td><td>Window overlap percentage</td></tr><tr><td>file</td><td>Input file(s)</td></tr><tr><td>reader</td><td>files   ( &quot;postProcessing/faceSource1/surface/patch1/patch1.case&quot; &quot;postProcessing/faceSource2/surface/patch2/patch2.case&quot; ); Surface reader</td></tr><tr><td>writer</td><td>Surface writer</td></tr><tr><td>writeOptions</td><td>Collate times for ensight output - ensures geometry is only written once</td></tr><tr><td>rhoRef</td><td>Reference density (to convert from kinematic to static pressure)</td></tr><tr><td>N</td><td>8192; // 4096;</td></tr><tr><td>fu</td><td>Lower frequency limit, default = 25Hz fl              25; Upper frequency limit, default = 10kHz</td></tr><tr><td>nHeaderLine</td><td>files           ( &quot;pressureData&quot; &quot;pressureData2&quot;);</td></tr><tr><td>graphFormat</td><td>Graph format, default = raw</td></tr><tr><td>fftWriteInterval</td><td>Start time, default = 0s startTime       0; Write interval for FFT data, default = 1</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 1 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><p>该文件族在本次固定版本源码中仅选到一份不同的完整配置；不重复同一个文件充当多个案例。</p><h3>示例 1 · etc/caseDicts/annotated</h3><p>原始路径：<code>etc/caseDicts/annotated/noiseDict</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/noiseDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/noisedict/1-noiseDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/noise/">noise</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;noiseDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;noiseDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>No field / No functionObject</td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
