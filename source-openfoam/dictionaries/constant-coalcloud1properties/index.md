---
title: "coalCloud1Properties"
layout: reference
description: "名为 coalCloud1 的煤颗粒云配置，关联干燥、挥发、焦炭反应、辐射与传热模型。"
dictionary: true
cms_slug: "dictionary-coalcloud1properties"
---

<p>名为 coalCloud1 的煤颗粒云配置，关联干燥、挥发、焦炭反应、辐射与传热模型。</p><p>位置：<code>constant/coalCloud1Properties</code></p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>solution</td><td>颗粒云的求解控制，包含稳态/瞬态、载体耦合、源项与时间积分等。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>radiation</td><td>辐射计算开关，需与模型、壁面辐射条件及能量方程配合。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr><tr><td>Cp</td><td>定压比热容，单位通常为焦耳每千克每开尔文。</td></tr><tr><td>kappa</td><td>热导率或模型特定参数，需结合量纲确认；不要与湍动能 k 混淆。</td></tr><tr><td>constantProperties</td><td>单个颗粒或材料的基本属性，例如密度、温度和热容；具体键由云类型决定。</td></tr><tr><td>subModels</td><td>颗粒云注入、力、传热、碰撞和相变等子模型集合。</td></tr><tr><td>particleForces</td><td>作用于颗粒的力模型列表，例如阻力和重力，实际可选模型由云类型决定。</td></tr><tr><td>injectionModels</td><td>注入时间、位置、流量与粒径分布等设置；需要同时满足总注入质量与统计分辨率要求。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patchInteractionModel</td><td>颗粒与边界接触时的反弹、粘附或逸出处理。</td></tr><tr><td>surfaceFilmModel</td><td>表面液膜模型选择，需与液膜区域和主流体耦合条件配套。</td></tr><tr><td>mu</td><td>通常表示动力黏度，也可能在特定模型中表示其他系数；必须结合量纲和源码语境确认。</td></tr><tr><td>phases</td><td>相名称列表；这些名称会影响相分数、速度、热物性等字段或字典的命名。</td></tr><tr><td>E</td><td>线弹性材料的杨氏模量，通常以压力为单位。</td></tr><tr><td>cloudFunctions</td><td>颗粒云附加监测或后处理功能。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/coalChemistryFoam/simplifiedSiwek</summary><p><code>simplifiedSiwek</code> 把煤粉作为具有挥发分、含水量、固定碳和灰分的反应颗粒云，计算加热、挥发分析出与表面氧化。</p>
<ul>
<li><code>coupled true</code> 使煤粉向连续相交换质量、动量、组分、焓和辐射贡献，各源项采用 <code>semiImplicit 1</code>；<code>maxCo 0.3</code> 控制跟踪子步。</li>
<li><code>manualInjection</code> 从 <code>coalCloud1Positions</code> 读取位置，总质量为 <code>0.0001</code> kg，初速度为 <code>(0 -10 0)</code> m/s。粒径分布范围为 5–500 μm。</li>
<li>初始总质量分数为 <code>YGasTot0 0.211</code>、<code>YLiquidTot0 0.026</code>、<code>YSolidTot0 0.763</code>，三者相加为 1。气相挥发分含 CH4、H2、CO2，液相为水，固相含碳与灰分。</li>
<li><code>TDevol 400</code> K 与 <code>constantRateDevolatilisation</code> 配置挥发分析出；<code>volatileData</code> 为三种挥发组分分别设置速率常数 12，<code>residualCoeff 0.001</code> 控制残余挥发分判定。</li>
<li><code>COxidationKineticDiffusionLimitedRate</code> 联合考虑表面反应动力学与扩散供氧；<code>C1</code>、<code>C2</code>、<code>E</code> 应作为该反应关联式的一组参数使用。</li>
<li><code>RanzMarshall</code> 计算换热，<code>liquidEvaporation</code> 处理水分蒸发，<code>radiation on</code> 加入辐射交换。<code>constantVolume true</code> 为质量变化采用固定颗粒体积的设置。</li>
</ul>
<p>可分别改变煤粉直径、含水量和挥发分比例，观察升温、失重和气相产物。改变组分比例后，先重新归一化各级质量分数，再比较初始煤粉质量与残余灰分、气体释放量。</p>
<p><a href="/assets/examples/v2512/coalcloud1properties/1-coalCloud1Properties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/coalChemistryFoam/simplifiedSiwek/constant/coalCloud1Properties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/coalChemistryFoam/simplifiedSiwek">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      coalCloud1Properties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solution
{
    active          true;
    transient       yes;
    coupled         true;
    cellValueSourceCorrection on;
    maxCo           0.3;

    sourceTerms
    {
        schemes
        {
            rho             semiImplicit 1;
            U               semiImplicit 1;
            Yi              semiImplicit 1;
            h               semiImplicit 1;
            radiation       semiImplicit 1;
        }
    }

    interpolationSchemes
    {
        rho             cell;
        U               cellPoint;
        thermo:mu       cell;
        T               cell;
        Cp              cell;
        kappa           cell;
        p               cell;
        G               cell;
    }

    integrationSchemes
    {
        U               Euler;
        T               analytical;
    }
}

constantProperties
{
    rho0            1000;
    T0              300;
    Cp0             4187;
    epsilon0        1;
    f0              0.5;

    TDevol          400;
    LDevol          0;
    hRetentionCoeff 1;

    constantVolume  true;
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
        model1
        {
            type            manualInjection;
            massTotal       0.0001;
            parcelBasisType mass;
            SOI             0;
            positionsFile   &quot;coalCloud1Positions&quot;;
            U0              (0 -10 0);
            sizeDistribution
            {
                type        RosinRammler;
                RosinRammlerDistribution
                {
                    minValue        5e-06;
                    maxValue        0.0005;
                    lambda          5e-05;
                    n               0.5;
                }
            }
        }
    }

    dispersionModel stochasticDispersionRAS;

    patchInteractionModel standardWallInteraction;

    heatTransferModel RanzMarshall;

    compositionModel singleMixtureFraction;

    phaseChangeModel liquidEvaporation;

    devolatilisationModel constantRateDevolatilisation;

    stochasticCollisionModel none;

    surfaceReactionModel COxidationKineticDiffusionLimitedRate;

    surfaceFilmModel none;

    radiation       on;

    standardWallInteractionCoeffs
    {
        type            rebound;
        e               1;
        mu              0;
    }

    RanzMarshallCoeffs
    {
        BirdCorrection  true;
    }

    singleMixtureFractionCoeffs
    {
        phases
        (
            gas
            {
                CH4             0.604;
                H2              0.099;
                CO2             0.297;
            }
            liquid
            {
                H2O             1;
            }
            solid
            {
                ash             0.136304;
                C               0.863696;
            }
        );
        YGasTot0        0.211;
        YLiquidTot0     0.026;
        YSolidTot0      0.763;
    }

    liquidEvaporationCoeffs
    {
        enthalpyTransfer enthalpyDifference;

        activeLiquids
        (
            H2O
        );
    }

    constantRateDevolatilisationCoeffs
    {
        volatileData
        (
            (CH4            12)
            (H2             12)
            (CO2            12)
        );
        residualCoeff   0.001;
    }

    COxidationKineticDiffusionLimitedRateCoeffs
    {
        Sb              1;
        C1              5.0E-12;
        C2              0.002;
        E               7.9E+07;
    }
}


cloudFunctions
{}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/coalchemistryfoam/">coalChemistryFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
