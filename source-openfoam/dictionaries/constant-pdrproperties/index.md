---
title: "PDRProperties"
layout: reference
description: "PDR 燃烧或障碍物模型的物性与模型控制参数。"
dictionary: true
cms_slug: "dictionary-pdrproperties"
---

<p>PDR 燃烧或障碍物模型的物性与模型控制参数。</p><p>位置：<code>constant/PDRProperties</code></p><h2>配置实例</h2><p>preProcessing/PDRsetFields/simplePipeCage 中的 PDRProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      PDRProperties;
}

PDRDragModel basic;

basicCoeffs
{
    drag     on;
    Csu      0.5;
    Csk      0.05;
}

XiModel transport;

transportCoeffs
{
    XiShapeCoef 1;
}

XiEqModel instability;

instabilityCoeffs
{
    XiEqIn 2.5;

    XiEqModel basicSubGrid;

    basicSubGridCoeffs
    {
        XiEqModel SCOPEBlend;

        SCOPEBlendCoeffs
        {
            XiEqModelL
            {
                XiEqModel       Gulder;

                GulderCoeffs
                {
                    XiEqCoef   0.62;
                    uPrimeCoef      1.0;
                    subGridSchelkin true;
                }
            }

            XiEqModelH
            {
                XiEqModel       SCOPEXiEq;

                SCOPEXiEqCoeffs
                {
                    XiEqCoef   1.6;
                    XiEqExp    0.33333;
                    lCoef      0.336;
                    uPrimeCoef      1.0;
                    subGridSchelkin true;
                }
            }
        }
    }
}

XiGModel instabilityG;

instabilityGCoeffs
{
    lambdaIn        lambdaIn   [0 1 0 0 0 0 0] 0.6;
    GIn             GIn        [0 0 -1 0 0 0 0] 1.917;

    XiGModel basicSubGridG;

    basicSubGridGCoeffs
    {
        k1 0.5;

        XiGModel KTS;

        KTSCoeffs
        {
             GEtaCoef   0.28;
        }
    }
}</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · preProcessing/PDRsetFields/simplePipeCage</summary><p>simplePipeCage 用管架障碍物展示 PDR 场初始化。PDRProperties 提供阻力模型以及预混火焰褶皱模型的选择。</p>
<ul>
<li><code>PDRDragModel basic</code> 与 <code>drag on</code> 启用基本阻力模型，<code>Csu 0.5</code>、<code>Csk 0.05</code> 是该模型的闭合系数。</li>
<li><code>XiModel transport</code> 求解火焰褶皱因子 Xi 的输运，<code>XiShapeCoef 1</code> 控制对应模型项。</li>
<li><code>XiEqModel instability</code> 内嵌 basicSubGrid 与 SCOPEBlend；后者分别给出低、高湍流强度条件下的模型选择与系数。阅读时从每一级 <code>XiEqModel</code> 向内追踪实际选中的子字典。</li>
<li><code>XiGModel instabilityG</code> 的 <code>lambdaIn 0.6</code> 带长度量纲，<code>GIn 1.917</code> 带逆时间量纲，用于不稳定性相关的生成模型。</li>
</ul>
<p>这些系数与障碍物尺度、燃料及标定条件有关。调整管架几何时先更新几何生成的 PDR 场，再比较压力上升和火焰传播速度。</p>
<p><a href="/assets/examples/v2512/pdrproperties/1-PDRProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/PDRsetFields/simplePipeCage/constant/PDRProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/PDRsetFields/simplePipeCage">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      PDRProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

PDRDragModel basic;

basicCoeffs
{
    drag     on;
    Csu      0.5;
    Csk      0.05;
}

XiModel transport;

transportCoeffs
{
    XiShapeCoef 1;
}

XiEqModel instability;

instabilityCoeffs
{
    XiEqIn 2.5;

    XiEqModel basicSubGrid;

    basicSubGridCoeffs
    {
        XiEqModel SCOPEBlend;

        SCOPEBlendCoeffs
        {
            XiEqModelL
            {
                XiEqModel       Gulder;

                GulderCoeffs
                {
                    XiEqCoef   0.62;
                    uPrimeCoef      1.0;
                    subGridSchelkin true;
                }
            }

            XiEqModelH
            {
                XiEqModel       SCOPEXiEq;

                SCOPEXiEqCoeffs
                {
                    XiEqCoef   1.6;
                    XiEqExp    0.33333;
                    lCoef      0.336;
                    uPrimeCoef      1.0;
                    subGridSchelkin true;
                }
            }
        }
    }
}

XiGModel instabilityG;

instabilityGCoeffs
{
    lambdaIn        lambdaIn   [0 1 0 0 0 0 0] 0.6;
    GIn             GIn        [0 0 -1 0 0 0 0] 1.917;

    XiGModel basicSubGridG;

    basicSubGridGCoeffs
    {
        k1 0.5;

        XiGModel KTS;

        KTSCoeffs
        {
             GEtaCoef   0.28;
        }
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · combustion/PDRFoam/pipeLattice</summary><p>pipeLattice 的预混火焰穿过管阵列。这个较长字典同时保留多种模型的系数，实际使用哪一组由各层模型名称决定。</p>
<ul>
<li><code>PDRDragModel basic</code> 选择障碍物阻力，<code>Csu 0.5</code>、<code>Csk 0.05</code> 参与其闭合。</li>
<li><code>XiModel transport</code> 启用 Xi 输运，所选 transportCoeffs 中 <code>XiShapeCoef 1</code>、<code>GEtaExp 0.28</code> 为模型系数。</li>
<li><code>XiEqModel instability</code> 的子字典继续选择 <code>XiEqModel Gulder</code>；此路径采用 <code>XiEqCoef 0.62</code>，同文件中 SCOPEBlend 等备用配置只有被选中后才参与计算。</li>
<li><code>XiGModel instabilityG</code> 使用 <code>lambdaIn 4.5e-3</code> m、<code>GIn 1.917</code> s⁻¹，内部选择 KTS 生成模型。</li>
<li><code>XpEqModel normBasicSubGrid</code> 与 <code>XpGModel normBasicSubGridG</code> 给出另一组亚网格火焰闭合，系数应按所选模型成组理解。</li>
</ul>
<p>比较模型时一次更换一个模型选择及其对应系数，并记录相同测点上的火焰到达时间与峰值压力。</p>
<p><a href="/assets/examples/v2512/pdrproperties/2-PDRProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/PDRFoam/pipeLattice/constant/PDRProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/PDRFoam/pipeLattice">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      PDRProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

StSmoothCoef    1000.0;

//No smooth if &gt;100

schelkin
{
    subGridSchelkin true;
    uPrimeCoef  1.0;
    lCoef       0.336;
    maxSchFac   100.0;
    nrCoef      0.1;
    nrExp       0.0;
    nrExp2      0.05;
}

PDRDragModel    basic;

basicCoeffs
{
    drag        on;
    Csu         0.5;
    Csk         0.05;
}

basicSchCoeffs
{
    drag        on;
    $schelkin;
    Csu         0.0;
    Csk         0.0;
}

XiModel         transport;

algebraicCoeffs
{
    XiShapeCoef 1;
    XpShapeCoef 1;
    CpfiDot     0.0;
    CpfiCross   0.0;
    GEtaExp     0.0;
    LOverCw     0.01;
}

transportTwoEqsCoeffs
{
    XiShapeCoef 1;
    XpShapeCoef 1;
    CpfiDot     0.0;
    CpfiCross   0.0;
    GEtaExp     0.0;
    LOverCw     0.01;
}

k3Coeffs
{
    k3Obs       10.0;
    k3Open      1.0;
}

transportThreeEqsCoeffs
{
    $transportTwoEqsCoeffs;
    $k3Coeffs;
}

transportFourEqsCoeffs
{
    $transportTwoEqsCoeffs;
    $k3Coeffs;
}

transportOneEqObsCoeffs
{
    XiShapeCoef 1;
    Cpfi        0.0;
    GEtaExp     0.0;
}

transportXp
{
}

transportCoeffs
{
    XiShapeCoef 1;
    GEtaExp     0.28;
}

fixedCoeffs
{
}


/*---------------------------------------------------------------------------*\
                          XiEqModel : Model for XiEq
\*---------------------------------------------------------------------------*/

XiEqModel       instability;

BLMcoeffs
{
    XiEqCoef    1.0;
    alphaCoefP  0.023;
    alphaCoefN  0.085;
    betaCoefP   -0.0103;
    betaCoefN   -0.0075;
    maLim       30.0;
    maLim1      7.0;
    quenchCoef  34.0;
    quenchExp   -1.8;
    quenchM     -4.0;
    quenchRate1 0.6;
    quenchRate2 0.14;
}

instability2XiEqCoeffs
{
    defaultCIn  12.6;
    XiEqInFade  1.0;

    XiEqModel   BLMgMaXiEq;

    BLMgMaXiEqCoeffs
    {
        $schelkin;
        gulderCoef  1.0; //this value is not usssed 1.0.
        kaCoef      0.25;
        lowK0       0.1;
        lowKg       0.0;
        gMaCoef     0.032; //not used
        gMaCoef1    0.0;  // not used
        $BLMcoeffs;
    }

    BLMXiEqCoeffs
    {
        $schelkin;
        gulderCoef  0.31;
        kaCoef      0.25;
        lowK1       0.02;
        lowK2       0.05;
        $BLMcoeffs;
     }
}

instabilityCoeffs
{

    XiEqIn      2.5;
    XiEqModel   Gulder;
    GulderCoeffs
    {
        uPrimeCoef      1.0;
        subGridSchelkin true;
        XiEqCoef        0.62;
    }

    SCOPEBlendCoeffs
    {
        XiEqModelL
        {
            XiEqModel   Gulder;

            GulderCoeffs
            {
                $schelkin;
                XiEqCoef    0.62;
            }
        }

        XiEqModelH
        {
            XiEqModel       SCOPEXiEq;

            SCOPEXiEqCoeffs
            {
                $schelkin;
                XiEqCoef    1.6;
                XiEqExp     0.33333;
            }
        }
    }
}


/*---------------------------------------------------------------------------*\
                     XiGModel : Model for generation of Xi
\*---------------------------------------------------------------------------*/

XiGModel            instabilityG;

instability2GCoeffs
{
    lambdaIn        0.0001;
    defaultCIn      10.0;
    GInMult         5.0;
    GInFade         4.0;

    XiGModel KTS;

    KTSCoeffs
    {
        GEtaCoef    0.28;
    }
}

instabilityGCoeffs
{
    lambdaIn        4.5e-3;
    GIn             1.917;

    XiGModel        KTS;
    KTSCoeffs
    {
         GEtaCoef   0.28;
    }
}


/*---------------------------------------------------------------------------*\
                          XpEqGModel : Model for XpEq
\*---------------------------------------------------------------------------*/

XpEqModel       normBasicSubGrid;

normBasicSubGridCoeffs
{
    Cxpe1       800.0;
    Cxpe2       40.0;
    Cxpe3       400.0;
    Cxpe4       1.0;
}

basicSubGridCoeffs
{
}


/*---------------------------------------------------------------------------*\
                     XpGModel : Model for generation of Xp
\*---------------------------------------------------------------------------*/

XpGModel        normBasicSubGridG;

normBasicSubGridGCoeffs
{
    k1          0.0;
    kb1         14.0;
    kbe         1.5;
    kbx         0.4;
    k2          1.0;
    LOverCw     0.01;
    Cxpe1       800.0;
    Cxpe2       40.0;
    Cxpe3       400.0;
    Cxpe4       1.0;
}

basicSubGridGCoeffs
{
    XpGModel    KTS;
    KTSCoeffs
    {
        GEtaCoef    0.28;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/pdrfoam/">PDRFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
