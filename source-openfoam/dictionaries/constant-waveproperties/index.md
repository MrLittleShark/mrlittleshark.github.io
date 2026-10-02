---
title: "waveProperties"
layout: reference
description: "定义造波或吸波边界使用的波浪模型、周期、波高、水深和方向。"
dictionary: true
cms_slug: "dictionary-waveproperties"
---

<p>定义造波或吸波边界使用的波浪模型、周期、波高、水深和方向。</p><p>位置：<code>constant/waveProperties</code></p><h2>配置实例</h2><p>multiphase/interFoam/laminar/waves/waveMakerSolitary 中的 waveProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      wavesProperties;
}

outlet
{
    alpha           alpha.water;

    waveModel       shallowWaterAbsorption;

    nPaddle         1;
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>waveModel</td><td>采用的波浪理论或造波模型，决定色散关系和所需波参数。</td></tr><tr><td>waveHeight</td><td>波峰到波谷的高度，一般为振幅的两倍。</td></tr><tr><td>waveAngle</td><td>波浪传播方向角，其单位与参考方向由模型定义。</td></tr><tr><td>rampTime</td><td>造波信号逐渐增长到目标幅值的时间，用于减小启动瞬态。</td></tr><tr><td>wavePeriod</td><td>波浪周期。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/interFoam/laminar/waves/waveMakerSolitary</summary><p>waveMakerSolitary 的 waveProperties 配置出口消波，使传播到出口的长波尽量平顺地离开计算域。</p>
<ul>
<li><code>outlet</code> 是实际出口边界名称，<code>alpha alpha.water</code> 指定用于识别水面的体积分数字段。</li>
<li><code>waveModel shallowWaterAbsorption</code> 根据浅水波关系构造吸收处理。</li>
<li><code>nPaddle 1</code> 使用一个横向控制分段，适合该演示中的简单波面。</li>
</ul>
<p>孤立波的产生还由算例其他初始或运动设置给出；调整出口后比较入射波离开时的水位时序和反射波幅。</p>
<p><a href="/assets/examples/v2512/waveproperties/1-waveProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerSolitary/constant/waveProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerSolitary">案例目录</a></p><pre><code class="language-foam">/*---------------------------------------------------------------------------*\
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
    object      wavesProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

outlet
{
    alpha           alpha.water;

    waveModel       shallowWaterAbsorption;

    nPaddle         1;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/interIsoFoam/waveExampleStreamFunction</summary><p>waveExampleStreamFunction 在入口使用流函数波浪理论生成非线性规则波，在出口吸收传播过来的波。</p>
<ul>
<li>入口 <code>waveHeight 0.1517</code> m、<code>wavePeriod 3.017</code> s、<code>waveLength 6.2832</code> m 分别给出波高、周期和波长。</li>
<li><code>waveAngle 0</code> 设置传播方向，<code>uMean 2.0825</code> 提供流函数波解中的平均速度参数，应与所用理论解配套。</li>
<li><code>Bjs</code>、<code>Ejs</code> 是该波解的级数系数，改变波高、水深或周期时应重新求解这些系数。</li>
<li><code>rampTime 3.017</code> 使造波在一个周期内逐步建立，<code>activeAbsorption yes</code> 启用入口的主动吸收处理。</li>
<li>出口使用 shallowWaterAbsorption，<code>nPaddle 1</code> 对整个边界采用单个控制分段。</li>
</ul>
<p>通过入口下游的水位探针检查实际周期和波高，再逐步分析反射与耗散。</p>
<p><a href="/assets/examples/v2512/waveproperties/2-waveProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/waveExampleStreamFunction/constant/waveProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/waveExampleStreamFunction">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      waveProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

inlet
{
    alpha           alpha.water;

    waveModel       streamFunction;

    nPaddle         1;

    waveHeight      0.1517;

    waveAngle       0.0;

    rampTime        3.017;

    activeAbsorption yes;

    wavePeriod      3.017;

    uMean           2.0825;

    waveLength      6.2832;

    Bjs
    (
        8.6669014e-002
        2.4849799e-002
        7.7446850e-003
        2.3355420e-003
        6.4497731e-004
        1.5205114e-004
        2.5433769e-005
       -2.2045436e-007
       -2.8711504e-006
       -1.2287334e-006
    );

    Ejs
    (
        5.6009609e-002
        3.1638171e-002
        1.5375952e-002
        7.1743178e-003
        3.3737077e-003
        1.6324880e-003
        8.2331980e-004
        4.4403497e-004
        2.7580059e-004
        2.2810557e-004
    );
}

outlet
{
    alpha           alpha.water;

    waveModel       shallowWaterAbsorption;

    nPaddle         1;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interFoam/laminar/waves/waveMakerFlap</summary><p>waveMakerFlap 的这个文件负责右侧边界的波浪吸收，翻板自身的运动由其他运动配置提供。</p>
<ul>
<li><code>rightwall</code> 是吸收边界名称，应与网格和场文件中的 patch 一致。</li>
<li><code>alpha alpha.water</code> 读取水相体积分数来识别自由表面。</li>
<li><code>waveModel shallowWaterAbsorption</code> 采用浅水波吸收关系，<code>nPaddle 1</code> 使用一个边界控制分段。</li>
</ul>
<p>改变水深或造波频率后，可在不同位置设置水位探针，比较入射与反射波幅，判断出口吸收效果。</p>
<p><a href="/assets/examples/v2512/waveproperties/3-waveProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerFlap/constant/waveProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerFlap">案例目录</a></p><pre><code class="language-foam">/*---------------------------------------------------------------------------*\
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
    object      wavesProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

rightwall
{
    alpha           alpha.water;

    waveModel       shallowWaterAbsorption;

    nPaddle         1;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/interfoam/">interFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
