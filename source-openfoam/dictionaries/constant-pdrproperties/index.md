---
title: "constant/PDRProperties · PDRProperties"
layout: reference
description: "PDR 燃烧或障碍物模型的物性与模型控制参数。PDR 将未解析障碍物对流动与火焰的影响表示为模型项，必须保持障碍物预处理、阻力数据和求解器模型一致。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>PDR 燃烧或障碍物模型的物性与模型控制参数。PDR 将未解析障碍物对流动与火焰的影响表示为模型项，必须保持障碍物预处理、阻力数据和求解器模型一致。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>PDRDragModel</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>StSmoothCoef</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>schelkin</td><td>No smooth if &gt;100</td></tr><tr><td>gulderCoef</td><td>this value is not usssed 1.0.</td></tr><tr><td>gMaCoef</td><td>not used</td></tr><tr><td>gMaCoef1</td><td>not used</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 2 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · preProcessing/PDRsetFields/simplePipeCage</h3><p>原始路径：<code>tutorials/preProcessing/PDRsetFields/simplePipeCage/constant/PDRProperties</code>；求解器：<code>PDRFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/PDRsetFields/simplePipeCage/constant/PDRProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/pdrproperties/1-PDRProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/PDRsetFields/simplePipeCage">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · combustion/PDRFoam/pipeLattice</h3><p>原始路径：<code>tutorials/combustion/PDRFoam/pipeLattice/constant/PDRProperties</code>；求解器：<code>PDRFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/PDRFoam/pipeLattice/constant/PDRProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/pdrproperties/2-PDRProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/PDRFoam/pipeLattice">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    &#36;schelkin;
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
    &#36;transportTwoEqsCoeffs;
    &#36;k3Coeffs;
}

transportFourEqsCoeffs
{
    &#36;transportTwoEqsCoeffs;
    &#36;k3Coeffs;
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
        &#36;schelkin;
        gulderCoef  1.0; //this value is not usssed 1.0.
        kaCoef      0.25;
        lowK0       0.1;
        lowKg       0.0;
        gMaCoef     0.032; //not used
        gMaCoef1    0.0;  // not used
        &#36;BLMcoeffs;
    }

    BLMXiEqCoeffs
    {
        &#36;schelkin;
        gulderCoef  0.31;
        kaCoef      0.25;
        lowK1       0.02;
        lowK2       0.05;
        &#36;BLMcoeffs;
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
                &#36;schelkin;
                XiEqCoef    0.62;
            }
        }

        XiEqModelH
        {
            XiEqModel       SCOPEXiEq;

            SCOPEXiEqCoeffs
            {
                &#36;schelkin;
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/pdrfoam/">PDRFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/PDRProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/PDRProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
