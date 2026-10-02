---
title: "sprayCloudProperties"
layout: reference
description: "喷雾颗粒云的注入、雾化、破碎、碰撞、蒸发和传热子模型配置。"
dictionary: true
cms_slug: "dictionary-spraycloudproperties"
---

<p>喷雾颗粒云的注入、雾化、破碎、碰撞、蒸发和传热子模型配置。</p><p>位置：<code>constant/sprayCloudProperties</code></p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>solution</td><td>颗粒云的求解控制，包含稳态/瞬态、载体耦合、源项与时间积分等。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>radiation</td><td>辐射计算开关，需与模型、壁面辐射条件及能量方程配合。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr><tr><td>Cp</td><td>定压比热容，单位通常为焦耳每千克每开尔文。</td></tr><tr><td>kappa</td><td>热导率或模型特定参数，需结合量纲确认；不要与湍动能 k 混淆。</td></tr><tr><td>constantProperties</td><td>单个颗粒或材料的基本属性，例如密度、温度和热容；具体键由云类型决定。</td></tr><tr><td>subModels</td><td>颗粒云注入、力、传热、碰撞和相变等子模型集合。</td></tr><tr><td>particleForces</td><td>作用于颗粒的力模型列表，例如阻力和重力，实际可选模型由云类型决定。</td></tr><tr><td>injectionModels</td><td>注入时间、位置、流量与粒径分布等设置；需要同时满足总注入质量与统计分辨率要求。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patchInteractionModel</td><td>颗粒与边界接触时的反弹、粘附或逸出处理。</td></tr><tr><td>surfaceFilmModel</td><td>表面液膜模型选择，需与液膜区域和主流体耦合条件配套。</td></tr><tr><td>atomizationModel</td><td>雾化子模型，处理喷嘴出口附近的液体破碎起始过程。</td></tr><tr><td>breakupModel</td><td>后续液滴破碎模型，与初始雾化模型有不同职责。</td></tr><tr><td>phases</td><td>相名称列表；这些名称会影响相分数、速度、热物性等字段或字典的命名。</td></tr><tr><td>cloudFunctions</td><td>颗粒云附加监测或后处理功能。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/interFoam/laminar/vofToLagrangian/lagrangianParticleInjection</summary><p>这个 <code>vofToLagrangian</code> 后续算例把前一阶段识别出的液滴记录重新注入喷雾计算，实现从界面分辨计算到离散液滴跟踪的衔接。</p>
<ul>
<li><code>injectedParticleInjection</code> 读取 <code>eulerianParticleCloud</code>，直接使用记录中的注入时刻、位置、直径和速度；<code>positionOffset (-0.025 2 -0.025)</code> 将位置平移到后续网格。</li>
<li><code>parcelBasisType fixed</code>、<code>nParticle 1</code> 使每个注入包对应一滴。此模型从导入直径计算总体积并重算注入质量，文件中的 <code>massTotal 6.0e-6</code> 会被这一步覆盖。</li>
<li><code>coupled true</code> 开启与连续相交换，<code>maxCo 0.3</code> 控制颗粒子步，速度积分用 <code>Euler</code>，温度积分用 <code>analytical</code>。</li>
<li>液相成分是 <code>H2O 1</code>，初始温度 <code>T0 293</code> K。<code>rho0</code> 与 <code>Cp0</code> 是占位值，随后由液体物性按初温更新。</li>
<li><code>ReitzDiwakar</code> 处理二次破碎，<code>phaseChangeModel none</code> 关闭蒸发；<code>RanzMarshall</code> 仍负责液滴换热。</li>
</ul>
<p>改变位置偏移前，先比较两套网格的坐标原点。导入后可核对液滴个数、总体积和质量，再研究破碎导致的粒径变化；需要蒸发时再配置水的相变模型。</p>
<p><a href="/assets/examples/v2512/spraycloudproperties/1-sprayCloudProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianParticleInjection/constant/sprayCloudProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianParticleInjection">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/interFoam/laminar/vofToLagrangian/lagrangianDistributionInjection</summary><p>此例把界面分辨阶段得到的液滴记录转为统计分布，再重新采样注入，适合用较少的计算包延续喷雾计算。</p>
<ul>
<li><code>injectedParticleDistributionInjection</code> 从 <code>eulerianParticleCloud</code> 建立统计注入器，<code>positionOffset (-0.025 2 -0.025)</code> 完成坐标平移。</li>
<li><code>binWidth 0.1e-3</code> 给粒径直方图设置 0.1 mm 的分箱宽度；更细的分箱能保留更多分布细节，也需要足够的原始样本。</li>
<li><code>parcelsPerInjector 500</code> 控制各注入器的计算包数量；<code>resampleSize 100</code> 为位置和速度数据建立重采样样本。</li>
<li><code>applyDistributionMassTotal yes</code> 从原分布的总体积与液体密度确定注入总质量，因此 <code>massTotal 0</code> 在这里是占位项。</li>
<li>水滴使用 <code>ReitzDiwakar</code> 二次破碎与 <code>RanzMarshall</code> 换热，蒸发关闭。粒径和位置统计变化可以与直接逐滴注入的算例对照。</li>
</ul>
<p>可分别改变分箱宽度和计算包数量，比较总质量、Sauter 平均直径及喷雾贯穿长度。先保持质量一致，再判断统计压缩对结果的影响。</p>
<p><a href="/assets/examples/v2512/spraycloudproperties/2-sprayCloudProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianDistributionInjection/constant/sprayCloudProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianDistributionInjection">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/sprayFoam/aachenBomb</summary><p><code>aachenBomb</code> 在容器内喷入正庚烷，计算液滴运动、破碎、换热及蒸发。</p>
<ul>
<li><code>coneNozzleInjection</code> 从直径 <code>1.9e-4</code> m 的圆形喷孔注入，方向为负 y；<code>thetaInner 0</code>、<code>thetaOuter 10</code> 是相对喷射轴的角度范围，最大半角为 10°。</li>
<li><code>massTotal 6.0e-6</code> kg 与 <code>duration 1.25e-3</code> s 给出总喷油量和持续时间；<code>flowRateProfile table</code> 给出时间分布形状，<code>Cd 0.9</code> 用于流率与出口速度关系。</li>
<li><code>parcelsPerSecond 20000000</code> 控制抽样数量。Rosin–Rammler 直径范围为 1–150 μm，<code>lambda 150 μm</code>、<code>n 3</code> 控制分布形状。</li>
<li><code>T0 320</code> K 是初始液滴温度，<code>C7H16 1</code> 是纯正庚烷。<code>liquidEvaporationBoil</code> 与 <code>activeLiquids (C7H16)</code> 开启该液体的蒸发/沸腾计算。</li>
<li>当前破碎模型为 <code>ReitzDiwakar</code>，块注释中的 <code>ReitzKHRTCoeffs</code> 是备用设置。<code>cloudFunctions</code> 输出 Weber、Reynolds、Nusselt 数和换热系数，便于理解局部破碎与换热条件。</li>
</ul>
<p>改变喷孔直径时要重新检查喷射速度和动量流率。改变容器温度时，可比较液相贯穿距离、蒸发质量与液滴温度；比较破碎模型时保留同一注入分布与喷油量。</p>
<p><a href="/assets/examples/v2512/spraycloudproperties/3-sprayCloudProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb/constant/sprayCloudProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/sprayfoam/">sprayFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
