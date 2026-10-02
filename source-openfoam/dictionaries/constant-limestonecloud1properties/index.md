---
title: "limestoneCloud1Properties"
layout: reference
description: "名为 limestoneCloud1 的石灰石颗粒云配置，用于对应反应颗粒教程。"
dictionary: true
cms_slug: "dictionary-limestonecloud1properties"
---

<p>名为 limestoneCloud1 的石灰石颗粒云配置，用于对应反应颗粒教程。</p><p>位置：<code>constant/limestoneCloud1Properties</code></p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>solution</td><td>颗粒云的求解控制，包含稳态/瞬态、载体耦合、源项与时间积分等。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>radiation</td><td>辐射计算开关，需与模型、壁面辐射条件及能量方程配合。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>Cp</td><td>定压比热容，单位通常为焦耳每千克每开尔文。</td></tr><tr><td>kappa</td><td>热导率或模型特定参数，需结合量纲确认；不要与湍动能 k 混淆。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr><tr><td>constantProperties</td><td>单个颗粒或材料的基本属性，例如密度、温度和热容；具体键由云类型决定。</td></tr><tr><td>subModels</td><td>颗粒云注入、力、传热、碰撞和相变等子模型集合。</td></tr><tr><td>particleForces</td><td>作用于颗粒的力模型列表，例如阻力和重力，实际可选模型由云类型决定。</td></tr><tr><td>injectionModels</td><td>注入时间、位置、流量与粒径分布等设置；需要同时满足总注入质量与统计分辨率要求。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patchInteractionModel</td><td>颗粒与边界接触时的反弹、粘附或逸出处理。</td></tr><tr><td>surfaceFilmModel</td><td>表面液膜模型选择，需与液膜区域和主流体耦合条件配套。</td></tr><tr><td>mu</td><td>通常表示动力黏度，也可能在特定模型中表示其他系数；必须结合量纲和源码语境确认。</td></tr><tr><td>cloudFunctions</td><td>颗粒云附加监测或后处理功能。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/coalChemistryFoam/simplifiedSiwek</summary><p><code>simplifiedSiwek</code> 中的石灰石颗粒云用于描述随煤粉加入的另一类颗粒，主要参与运动、吸热与辐射交换。</p>
<ul>
<li><code>parcelTypeId 2</code> 区分这类颗粒；<code>rho0 2500</code> kg/m³、<code>T0 300</code> K、<code>Cp0 900</code> J/(kg·K) 给出初始材料性质。</li>
<li><code>manualInjection</code> 从 <code>limestonePositions</code> 读取位置，总质量为 <code>0.0001</code> kg，初速度为零。Rosin–Rammler 粒径范围为 5–565 μm，<code>lambda 48 μm</code>、<code>n 0.5</code> 控制分布。</li>
<li><code>sphereDrag</code>、<code>gravity</code> 与 <code>stochasticDispersionRAS</code> 分别处理阻力、重力和 RAS 湍流弥散。</li>
<li><code>RanzMarshall</code> 提供换热，<code>BirdCorrection false</code> 关闭相应质量传递修正；本文件的子模型没有加入分解反应。</li>
<li><code>radiation on</code> 参与辐射换热，<code>cloudFunctions/particleDose1</code> 从 <code>G</code> 读取辐射场并累计颗粒所受辐射剂量。</li>
</ul>
<p>增大石灰石总质量可增加体系中的热容量，改变粒径则会改变升温时间与表面积。可比较颗粒温度分布、气相温度和辐射剂量；若研究煅烧，还需另行配置分解反应及产物成分。</p>
<p><a href="/assets/examples/v2512/limestonecloud1properties/1-limestoneCloud1Properties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/coalChemistryFoam/simplifiedSiwek/constant/limestoneCloud1Properties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/coalChemistryFoam/simplifiedSiwek">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      limestoneCloud1Properties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solution
{
    active          true;
    coupled         true;
    transient       yes;
    cellValueSourceCorrection on;
    maxCo           0.3;

    sourceTerms
    {
        schemes
        {
            U               explicit 1;
            h               explicit 1;
            radiation       explicit 1;
        }
    }

    interpolationSchemes
    {
        rho             cell;
        thermo:mu       cell;
        U               cellPoint;
        Cp              cell;
        kappa           cell;
        T               cell;
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
    parcelTypeId    2;

    rho0            2500;
    T0              300;
    Cp0             900;

    epsilon0        1;
    f0              0.5;
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
            positionsFile   &quot;limestonePositions&quot;;
            U0              (0 0 0);
            sizeDistribution
            {
                type        RosinRammler;
                RosinRammlerDistribution
                {
                    minValue        5e-06;
                    maxValue        0.000565;
                    lambda          4.8e-05;
                    n               0.5;
                }
            }
        }
    }

    dispersionModel stochasticDispersionRAS;

    patchInteractionModel standardWallInteraction;

    heatTransferModel RanzMarshall;

    stochasticCollisionModel none;

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
        BirdCorrection  false;
    }
}


cloudFunctions
{
    particleDose1
    {
        type            particleDose;
        GName           G;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/coalchemistryfoam/">coalChemistryFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
