---
title: "constant/coalCloud1Properties · coalCloud1Properties"
layout: reference
description: "名为 coalCloud1 的煤颗粒云配置，关联干燥、挥发、焦炭反应、辐射与传热模型。煤的组分定义、热值和颗粒注入质量需要一致。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>名为 coalCloud1 的煤颗粒云配置，关联干燥、挥发、焦炭反应、辐射与传热模型。煤的组分定义、热值和颗粒注入质量需要一致。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>solution</td><td>颗粒云的求解控制，包含稳态/瞬态、载体耦合、源项与时间积分等。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>radiation</td><td>辐射计算开关，需与模型、壁面辐射条件及能量方程配合。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr><tr><td>Cp</td><td>定压比热容，单位通常为焦耳每千克每开尔文。</td></tr><tr><td>kappa</td><td>热导率或模型特定参数，需结合量纲确认；不要与湍动能 k 混淆。</td></tr><tr><td>constantProperties</td><td>单个颗粒或材料的基本属性，例如密度、温度和热容；具体键由云类型决定。</td></tr><tr><td>subModels</td><td>颗粒云注入、力、传热、碰撞和相变等子模型集合。</td></tr><tr><td>particleForces</td><td>作用于颗粒的力模型列表，例如阻力和重力，实际可选模型由云类型决定。</td></tr><tr><td>injectionModels</td><td>注入时间、位置、流量与粒径分布等设置；需要同时满足总注入质量与统计分辨率要求。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patchInteractionModel</td><td>颗粒与边界接触时的反弹、粘附或逸出处理。</td></tr><tr><td>surfaceFilmModel</td><td>表面液膜模型选择，需与液膜区域和主流体耦合条件配套。</td></tr><tr><td>mu</td><td>通常表示动力黏度，也可能在特定模型中表示其他系数；必须结合量纲和源码语境确认。</td></tr><tr><td>phases</td><td>相名称列表；这些名称会影响相分数、速度、热物性等字段或字典的命名。</td></tr><tr><td>E</td><td>线弹性材料的杨氏模量，通常以压力为单位。</td></tr><tr><td>cloudFunctions</td><td>颗粒云附加监测或后处理功能。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 1 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><p>该文件族在本次固定版本源码中仅选到一份不同的完整配置；不重复同一个文件充当多个案例。</p><h3>示例 1 · lagrangian/coalChemistryFoam/simplifiedSiwek</h3><p>原始路径：<code>tutorials/lagrangian/coalChemistryFoam/simplifiedSiwek/constant/coalCloud1Properties</code>；求解器：<code>coalChemistryFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/coalChemistryFoam/simplifiedSiwek/constant/coalCloud1Properties">查看固定版本源码</a> · <a href="/assets/examples/v2512/coalcloud1properties/1-coalCloud1Properties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/coalChemistryFoam/simplifiedSiwek">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/coalchemistryfoam/">coalChemistryFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/coalCloud1Properties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/coalCloud1Properties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
