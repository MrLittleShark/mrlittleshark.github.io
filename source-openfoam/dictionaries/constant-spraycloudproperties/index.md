---
title: "constant/sprayCloudProperties · sprayCloudProperties"
layout: reference
description: "喷雾颗粒云的注入、雾化、破碎、碰撞、蒸发和传热子模型配置。喷嘴流量、喷射锥角、粒径分布与 parcel 数需要分别检查；提高 parcel 数主要改善统计分辨率。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>喷雾颗粒云的注入、雾化、破碎、碰撞、蒸发和传热子模型配置。喷嘴流量、喷射锥角、粒径分布与 parcel 数需要分别检查；提高 parcel 数主要改善统计分辨率。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>solution</td><td>颗粒云的求解控制，包含稳态/瞬态、载体耦合、源项与时间积分等。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>radiation</td><td>辐射计算开关，需与模型、壁面辐射条件及能量方程配合。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr><tr><td>Cp</td><td>定压比热容，单位通常为焦耳每千克每开尔文。</td></tr><tr><td>kappa</td><td>热导率或模型特定参数，需结合量纲确认；不要与湍动能 k 混淆。</td></tr><tr><td>constantProperties</td><td>单个颗粒或材料的基本属性，例如密度、温度和热容；具体键由云类型决定。</td></tr><tr><td>subModels</td><td>颗粒云注入、力、传热、碰撞和相变等子模型集合。</td></tr><tr><td>particleForces</td><td>作用于颗粒的力模型列表，例如阻力和重力，实际可选模型由云类型决定。</td></tr><tr><td>injectionModels</td><td>注入时间、位置、流量与粒径分布等设置；需要同时满足总注入质量与统计分辨率要求。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patchInteractionModel</td><td>颗粒与边界接触时的反弹、粘附或逸出处理。</td></tr><tr><td>surfaceFilmModel</td><td>表面液膜模型选择，需与液膜区域和主流体耦合条件配套。</td></tr><tr><td>atomizationModel</td><td>雾化子模型，处理喷嘴出口附近的液体破碎起始过程。</td></tr><tr><td>breakupModel</td><td>后续液滴破碎模型，与初始雾化模型有不同职责。</td></tr><tr><td>phases</td><td>相名称列表；这些名称会影响相分数、速度、热物性等字段或字典的命名。</td></tr><tr><td>cloudFunctions</td><td>颗粒云附加监测或后处理功能。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>rho0</td><td>Place holders for rho0 and Cp0 reset from liquid properties using T0</td></tr><tr><td>massTotal</td><td>Placeholder only when using applyDistributionMassTotal</td></tr><tr><td>breakupModel</td><td>ReitzKHRT;</td></tr><tr><td>resampleSize</td><td>optional</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · multiphase/interFoam/laminar/vofToLagrangian/lagrangianParticleInjection</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianParticleInjection/constant/sprayCloudProperties</code>；求解器：<code>sprayFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianParticleInjection/constant/sprayCloudProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/spraycloudproperties/1-sprayCloudProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianParticleInjection">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      sprayCloudProperties;
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
            rho             explicit 1;
            U               explicit 1;
            Yi              explicit 1;
            h               explicit 1;
            radiation       explicit 1;
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
    }

    integrationSchemes
    {
        U               Euler;
        T               analytical;
    }
}


constantProperties
{
    T0              293;

    // Place holders for rho0 and Cp0
    // - reset from liquid properties using T0
    rho0            1000;
    Cp0             4187;

    constantVolume  false;
}


subModels
{
    particleForces
    {
        sphereDrag;
    }

    injectionModels
    {
        model1
        {
            type            injectedParticleInjection;
            SOI             0;
            massTotal       6.0e-6;
            parcelBasisType fixed;
            nParticle       1;
            cloud           eulerianParticleCloud;
            positionOffset  (-0.025 2 -0.025);
        }
    }

    dispersionModel none;

    patchInteractionModel standardWallInteraction;

    heatTransferModel RanzMarshall;

    compositionModel singlePhaseMixture;

    phaseChangeModel none;

    surfaceFilmModel none;

    atomizationModel none;

    breakupModel    ReitzDiwakar;

    stochasticCollisionModel none;

    radiation       off;

    standardWallInteractionCoeffs
    {
        type            rebound;
    }

    RanzMarshallCoeffs
    {
        BirdCorrection  true;
    }

    singlePhaseMixtureCoeffs
    {
        phases
        (
            liquid
            {
                H2O             1;
            }
        );
    }

    ReitzDiwakarCoeffs
    {
        solveOscillationEq yes;
        Cbag            6;
        Cb              0.785;
        Cstrip          0.5;
        Cs              10;
    }

    TABCoeffs
    {
        y0              0;
        yDot0           0;
        Cmu             10;
        Comega          8;
        WeCrit          12;
    }
}


cloudFunctions
{}


// ************************************************************************* //</code></pre><h3>示例 2 · multiphase/interFoam/laminar/vofToLagrangian/lagrangianDistributionInjection</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianDistributionInjection/constant/sprayCloudProperties</code>；求解器：<code>sprayFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianDistributionInjection/constant/sprayCloudProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/spraycloudproperties/2-sprayCloudProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianDistributionInjection">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      sprayCloudProperties;
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
            rho             explicit 1;
            U               explicit 1;
            Yi              explicit 1;
            h               explicit 1;
            radiation       explicit 1;
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
    }

    integrationSchemes
    {
        U               Euler;
        T               analytical;
    }
}


constantProperties
{
    T0              293;

    // Place holders for rho0 and Cp0
    // - reset from liquid properties using T0
    rho0            1000;
    Cp0             4187;

    constantVolume  false;
}


subModels
{
    particleForces
    {
        sphereDrag;
    }

    injectionModels
    {
        model1
        {
            type            injectedParticleDistributionInjection;
            SOI             0;
            parcelBasisType mass;
            cloud           eulerianParticleCloud;
            positionOffset  (-0.025 2 -0.025);
            binWidth        0.1e-3;
            parcelsPerInjector 500;
            resampleSize    100;                    // optional
            applyDistributionMassTotal yes;

            // Placeholder only when using applyDistributionMassTotal
            massTotal       0;
        }
    }

    dispersionModel none;

    patchInteractionModel standardWallInteraction;

    heatTransferModel RanzMarshall;

    compositionModel singlePhaseMixture;

    phaseChangeModel none;

    surfaceFilmModel none;

    atomizationModel none;

    breakupModel    ReitzDiwakar;

    stochasticCollisionModel none;

    radiation       off;

    standardWallInteractionCoeffs
    {
        type            rebound;
    }

    RanzMarshallCoeffs
    {
        BirdCorrection  true;
    }

    singlePhaseMixtureCoeffs
    {
        phases
        (
            liquid
            {
                H2O             1;
            }
        );
    }

    ReitzDiwakarCoeffs
    {
        solveOscillationEq yes;
        Cbag            6;
        Cb              0.785;
        Cstrip          0.5;
        Cs              10;
    }

    TABCoeffs
    {
        y0              0;
        yDot0           0;
        Cmu             10;
        Comega          8;
        WeCrit          12;
    }
}


cloudFunctions
{}


// ************************************************************************* //</code></pre><h3>示例 3 · lagrangian/sprayFoam/aachenBomb</h3><p>原始路径：<code>tutorials/lagrangian/sprayFoam/aachenBomb/constant/sprayCloudProperties</code>；求解器：<code>sprayFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb/constant/sprayCloudProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/spraycloudproperties/3-sprayCloudProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      sprayCloudProperties;
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
            rho             explicit 1;
            U               explicit 1;
            Yi              explicit 1;
            h               explicit 1;
            radiation       explicit 1;
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
    }

    integrationSchemes
    {
        U               Euler;
        T               analytical;
    }
}


constantProperties
{
    T0              320;

    // place holders for rho0 and Cp0
    // - reset from liquid properties using T0
    rho0            1000;
    Cp0             4187;

    constantVolume  false;
}


subModels
{
    particleForces
    {
        sphereDrag;
    }

    injectionModels
    {
        model1
        {
            type            coneNozzleInjection;
            SOI             0;
            massTotal       6.0e-6;
            parcelBasisType mass;
            injectionMethod disc;
            flowType        flowRateAndDischarge;
            outerDiameter   1.9e-4;
            innerDiameter   0;
            duration        1.25e-3;
            position        (0 0.0995 0);
            direction       (0 -1 0);
            parcelsPerSecond 20000000;
            flowRateProfile table
            (
                (0              0.1272)
                (4.16667e-05    6.1634)
                (8.33333e-05    9.4778)
                (0.000125       9.5806)
                (0.000166667    9.4184)
                (0.000208333    9.0926)
                (0.00025        8.7011)
                (0.000291667    8.2239)
                (0.000333333    8.0401)
                (0.000375       8.8450)
                (0.000416667    8.9174)
                (0.000458333    8.8688)
                (0.0005         8.8882)
                (0.000541667    8.6923)
                (0.000583333    8.0014)
                (0.000625       7.2582)
                (0.000666667    7.2757)
                (0.000708333    6.9680)
                (0.00075        6.7608)
                (0.000791667    6.6502)
                (0.000833333    6.7695)
                (0.000875       5.5774)
                (0.000916667    4.8649)
                (0.000958333    5.0805)
                (0.001          4.9547)
                (0.00104167     4.5613)
                (0.00108333     4.4536)
                (0.001125       5.2651)
                (0.00116667     5.2560)
                (0.00120833     5.1737)
                (0.00125        3.9213)
                (0.001251       0.0000)
                (1000           0.0000)
            );

            Cd              constant 0.9;

            thetaInner      constant 0.0;
            thetaOuter      constant 10.0;

            sizeDistribution
            {
                type        RosinRammler;

                RosinRammlerDistribution
                {
                    minValue        1e-06;
                    maxValue        0.00015;
                    lambda          0.00015;
                    n               3;
                }
            }
        }
    }

    dispersionModel none;

    patchInteractionModel standardWallInteraction;

    heatTransferModel RanzMarshall;

    compositionModel singlePhaseMixture;

    phaseChangeModel liquidEvaporationBoil;

    surfaceFilmModel none;

    atomizationModel none;

    breakupModel    ReitzDiwakar; // ReitzKHRT;

    stochasticCollisionModel none;

    radiation       off;

    standardWallInteractionCoeffs
    {
        type            rebound;
    }

    RanzMarshallCoeffs
    {
        BirdCorrection  true;
    }

    singlePhaseMixtureCoeffs
    {
        phases
        (
            liquid
            {
                C7H16               1;
            }
        );
    }

    liquidEvaporationBoilCoeffs
    {
        enthalpyTransfer enthalpyDifference;

        activeLiquids    ( C7H16 );
    }

    ReitzDiwakarCoeffs
    {
        solveOscillationEq yes;
        Cbag            6;
        Cb              0.785;
        Cstrip          0.5;
        Cs              10;
    }

/*
    ReitzKHRTCoeffs
    {
        solveOscillationEq yes;
        B0              0.61;
        B1              40;
        Ctau            1;
        CRT             0.1;
        msLimit         0.2;
        WeberLimit      6;
    }
*/
    TABCoeffs
    {
        y0              0;
        yDot0           0;
        Cmu             10;
        Comega          8;
        WeCrit          12;
    }
}


cloudFunctions
{
    WeberNumber1
    {
        type    WeberNumber;
    }

    ReynoldsNumber1
    {
        type    ReynoldsNumber;
    }

    NusseltNumber1
    {
        type    NusseltNumber;
    }

    HeatTransferCoeff1
    {
        type    HeatTransferCoeff;
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/sprayfoam/">sprayFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/sprayCloudProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/sprayCloudProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
