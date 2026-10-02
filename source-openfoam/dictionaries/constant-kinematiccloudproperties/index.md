---
title: "kinematicCloudProperties"
layout: reference
description: "运动学颗粒云的离散相控制文件，包含载体耦合、积分格式、注入方式、阻力与碰撞等子模型。"
dictionary: true
cms_slug: "dictionary-kinematiccloudproperties"
---

<p>运动学颗粒云的离散相控制文件，包含载体耦合、积分格式、注入方式、阻力与碰撞等子模型。</p><p>位置：<code>constant/kinematicCloudProperties</code></p><h2>配置实例</h2><p>lagrangian/kinematicParcelFoam/drippingChair 中的 kinematicCloudProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      kinematicCloudProperties;
}

solution
{
    active          true;
    coupled         yes;
    transient       yes;
    cellValueSourceCorrection no;
    maxCo           0.3;

    sourceTerms
    {
        schemes
        {
            U               semiImplicit 1;
        }
    }

    interpolationSchemes
    {
        rho             cell;
        U               cellPoint;
        muc             cell;
        p               cell;
    }

    integrationSchemes
    {
        U               Euler;
    }
}

constantProperties
{
    rho0            1000;
}

subModels
{
    particleForces
    {
        sphereDrag;
        gravity;
    }

    injectionModels
    {
    }

    dispersionModel none;

    patchInteractionModel standardWallInteraction;

    stochasticCollisionModel none;

    surfaceFilmModel kinematicSurfaceFilm;

    standardWallInteractionCoeffs
    {
        type            rebound;
    }

    kinematicSurfaceFilmCoeffs
    {
        interactionType absorb;
    }
}

cloudFunctions
{}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>solution</td><td>颗粒云的求解控制，包含稳态/瞬态、载体耦合、源项与时间积分等。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>coupled</td><td>是否向连续相反馈颗粒源项。</td></tr><tr><td>transient</td><td>选择瞬态或稳态颗粒云控制方式，必须与求解器匹配。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>constantProperties</td><td>单个颗粒或材料的基本属性，例如密度、温度和热容；具体键由云类型决定。</td></tr><tr><td>subModels</td><td>颗粒云注入、力、传热、碰撞和相变等子模型集合。</td></tr><tr><td>particleForces</td><td>作用于颗粒的力模型列表，例如阻力和重力，实际可选模型由云类型决定。</td></tr><tr><td>injectionModels</td><td>注入时间、位置、流量与粒径分布等设置；需要同时满足总注入质量与统计分辨率要求。</td></tr><tr><td>patchInteractionModel</td><td>颗粒与边界接触时的反弹、粘附或逸出处理。</td></tr><tr><td>surfaceFilmModel</td><td>表面液膜模型选择，需与液膜区域和主流体耦合条件配套。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>cloudFunctions</td><td>颗粒云附加监测或后处理功能。</td></tr><tr><td>mu</td><td>通常表示动力黏度，也可能在特定模型中表示其他系数；必须结合量纲和源码语境确认。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/kinematicParcelFoam/drippingChair</summary><p><code>drippingChair</code> 将液膜与离散液滴连接起来：液滴在空间中运动，与液膜区域相遇后可转入膜内。</p>
<ul>
<li><code>active true</code>、<code>transient yes</code> 启用非定常颗粒跟踪；<code>coupled yes</code> 让颗粒对连续相产生反作用，动量源项采用 <code>semiImplicit 1</code>。</li>
<li><code>maxCo 0.3</code> 限制颗粒跟踪子步相对单元尺度的移动程度；流体时间步仍由运行设置控制。</li>
<li><code>rho0 1000</code> kg/m³ 给出水滴密度。<code>sphereDrag</code> 与 <code>gravity</code> 分别考虑球形颗粒阻力和重力。</li>
<li><code>injectionModels</code> 为空，当前云没有独立的常规喷射器。与液膜的颗粒交换由 <code>kinematicSurfaceFilm</code> 及液膜端模型配合处理。</li>
<li><code>interactionType absorb</code> 表示液滴撞到适用液膜区域后被吸收；其他壁面使用 <code>standardWallInteraction</code> 的 <code>rebound</code> 设置。</li>
</ul>
<p>可先降低 <code>maxCo</code> 比较液滴撞击位置，再改变液膜侧的脱落设置观察滴落频率。若加入独立喷嘴，则需要补充注入模型、流量、粒径和速度，并检查两种液滴来源的质量收支。</p>
<p><a href="/assets/examples/v2512/kinematiccloudproperties/1-kinematicCloudProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/drippingChair/constant/kinematicCloudProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/drippingChair">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      kinematicCloudProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solution
{
    active          true;
    coupled         yes;
    transient       yes;
    cellValueSourceCorrection no;
    maxCo           0.3;

    sourceTerms
    {
        schemes
        {
            U               semiImplicit 1;
        }
    }

    interpolationSchemes
    {
        rho             cell;
        U               cellPoint;
        muc             cell;
        p               cell;
    }

    integrationSchemes
    {
        U               Euler;
    }
}

constantProperties
{
    rho0            1000;
}

subModels
{
    particleForces
    {
        sphereDrag;
        gravity;
    }

    injectionModels
    {
    }

    dispersionModel none;

    patchInteractionModel standardWallInteraction;

    stochasticCollisionModel none;

    surfaceFilmModel kinematicSurfaceFilm;

    standardWallInteractionCoeffs
    {
        type            rebound;
    }

    kinematicSurfaceFilmCoeffs
    {
        interactionType absorb;
    }
}


cloudFunctions
{}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · lagrangian/kinematicParcelFoam/windshield</summary><p><code>windshield</code> 从入口释放液滴，展示液滴与挡风玻璃表面液膜的相互作用。</p>
<ul>
<li><code>coupled no</code> 采用单向耦合，颗粒不会把动量反馈给连续相。本文件中的 <code>sphereDrag</code> 和 <code>gravity</code> 行均被注释，当前受力列表为空，适合观察按给定初速度到达壁面的几何过程。</li>
<li><code>patchInjection</code> 从 <code>inlet</code> 注入，<code>SOI 0</code>、<code>duration 1000</code> 表示从零时刻开始、持续 1000 s；<code>massTotal 1</code> kg 对应整个注入时段的总质量。</li>
<li><code>parcelsPerSecond 100</code> 控制每秒注入的计算包数量；<code>U0 (0 0 -1)</code> 给出沿负 z 方向的 1 m/s 初速度。</li>
<li>Rosin–Rammler 分布的直径范围为 1–3 mm，<code>lambda 7.5e-05</code>、<code>n 0.5</code> 决定被该范围截取的分布形状。粒径统计应结合上下限理解。</li>
<li><code>kinematicSurfaceFilm</code> 的 <code>absorb</code> 把落在液膜区域的液滴转入膜内；普通壁面使用反弹模型。</li>
</ul>
<p>加入空气阻力或重力时，取消相应力项的注释，再比较落点与撞击速度。改变采样包数量时保持总质量和粒径分布一致，可以观察随机抽样误差。</p>
<p><a href="/assets/examples/v2512/kinematiccloudproperties/2-kinematicCloudProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/windshield/constant/kinematicCloudProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/windshield">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      kinematicCloudProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solution
{
    active          true;
    coupled         no;
    transient       yes;
    cellValueSourceCorrection no;
    maxCo           0.3;

    sourceTerms
    {
        schemes
        {
            U               explicit 1;
        }
    }

    interpolationSchemes
    {
        rho             cell;
        U               cellPoint;
        muc             cell;
        p               cell;
    }

    integrationSchemes
    {
        U               Euler;
    }
}

constantProperties
{
    rho0            1000;
}

subModels
{
    particleForces
    {
//        sphereDrag;
//        gravity;
    }

    injectionModels
    {
        model1
        {
            type            patchInjection;
            SOI             0;
            duration        1000.000;
            parcelBasisType mass;
            massTotal       1;
            patch           inlet;
            parcelsPerSecond 100;
            U0              (0 0 -1);
            flowRateProfile 1;
            sizeDistribution
            {
                type         RosinRammler;
                RosinRammlerDistribution
                {
                    minValue        0.001;
                    maxValue        0.003;
                    lambda          7.5e-05;
                    n               0.5;
                }
            }
        }
    }

    dispersionModel none;

    patchInteractionModel standardWallInteraction;

    stochasticCollisionModel none;

    surfaceFilmModel kinematicSurfaceFilm;

    standardWallInteractionCoeffs
    {
        type            rebound;
    }

    kinematicSurfaceFilmCoeffs
    {
        interactionType absorb;
    }
}


cloudFunctions
{}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/uncoupledKinematicParcelDyMFoam/rotor2DAMI</summary><p><code>rotor2DAMI</code> 用旋转网格与 AMI 接口测试颗粒跨区域跟踪。注入发生在一个很短的时间窗内，便于观察一批颗粒穿过旋转区域。</p>
<ul>
<li><code>coupled false</code> 采用单向耦合，<code>particleForces</code> 中的阻力和重力被注释；初始颗粒速度设为 <code>U0 (0.1 0 0)</code> m/s。</li>
<li><code>patchInjection</code> 在 <code>inlet</code> 注入，<code>SOI 0</code>、<code>duration 0.00001</code> s 与 <code>parcelsPerSecond 20000000</code> 对应名义约 200 个计算包。</li>
<li><code>parcelBasisType fixed</code>、<code>nParticle 1</code> 指定每个计算包代表一个真实颗粒，粒径为固定 50 μm。统计权重在这里由 <code>nParticle</code> 决定。</li>
<li><code>maxCo 0.3</code> 控制颗粒跟踪子步。AMI 传递与旋转网格运动还依赖配套网格和动网格文件。</li>
<li>文件末尾给出 <code>standardWallInteraction</code>：<code>e 0.9</code> 控制法向反弹，<code>mu 0.09</code> 控制切向衰减。整理自己的配置时，将文件中重复出现的 <code>patchInteractionModel</code> 合并为一次明确选择。</li>
</ul>
<p>改变旋转速度后，可追踪同一批颗粒的穿越位置与数量。提高 <code>parcelsPerSecond</code> 会增加这次短脉冲中的样本数；延长 <code>duration</code> 则把单批穿越实验扩展为连续注入。</p>
<p><a href="/assets/examples/v2512/kinematiccloudproperties/3-kinematicCloudProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/uncoupledKinematicParcelDyMFoam/rotor2DAMI/constant/kinematicCloudProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/uncoupledKinematicParcelDyMFoam/rotor2DAMI">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      kinematicCloudProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solution
{
    active          true;
    coupled         false;
    transient       yes;
    cellValueSourceCorrection off;
    maxCo           0.3;

    sourceTerms
    {
        schemes
        {
        }
    }

    interpolationSchemes
    {
        rho             cell;
        U               cellPoint;
        thermo:mu       cell;
    }

    integrationSchemes
    {
        U               Euler;
    }
}

constantProperties
{

    rho0            1000;
    constantVolume  true;

}

subModels
{
    particleForces
    {
        //sphereDrag;
        //gravity;
    }

    injectionModels
    {
         model1
        {
            type            patchInjection;
            parcelBasisType fixed;
            patch           inlet;
            U0              (0.1 0 0);
            nParticle       1;
            parcelsPerSecond  20000000;

            sizeDistribution
            {
                type uniform;
                uniformDistribution
                {
                    minValue        50e-06;
                    maxValue        50e-06;
                }
            }

            flowRateProfile constant 1;
            massTotal       2000000;
            SOI             0;
            duration        0.00001;
        }
    }

    dispersionModel none;

    patchInteractionModel none;

    surfaceFilmModel none;

    collisionModel none;

    patchInteractionModel standardWallInteraction;

    standardWallInteractionCoeffs
    {
        type        rebound;    // stick, escape
        e           0.9;        // optional - elasticity coeff
        mu          0.09;       // optional - restitution coeff
        UrMax       1e-4;
    }

    stochasticCollisionModel none;
}


cloudFunctions
{}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/kinematicparcelfoam/">kinematicParcelFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
