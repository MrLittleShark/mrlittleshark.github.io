---
title: "constant/kinematicCloudProperties · kinematicCloudProperties"
layout: reference
description: "运动学颗粒云的离散相控制文件，包含载体耦合、积分格式、注入方式、阻力与碰撞等子模型。每个 parcel 可代表多个真实颗粒，检查质量流率时必须同时检查 parcel 数与代表颗粒数。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>运动学颗粒云的离散相控制文件，包含载体耦合、积分格式、注入方式、阻力与碰撞等子模型。每个 parcel 可代表多个真实颗粒，检查质量流率时必须同时检查 parcel 数与代表颗粒数。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>solution</td><td>颗粒云的求解控制，包含稳态/瞬态、载体耦合、源项与时间积分等。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>coupled</td><td>是否向连续相反馈颗粒源项。</td></tr><tr><td>transient</td><td>选择瞬态或稳态颗粒云控制方式，必须与求解器匹配。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>constantProperties</td><td>单个颗粒或材料的基本属性，例如密度、温度和热容；具体键由云类型决定。</td></tr><tr><td>subModels</td><td>颗粒云注入、力、传热、碰撞和相变等子模型集合。</td></tr><tr><td>particleForces</td><td>作用于颗粒的力模型列表，例如阻力和重力，实际可选模型由云类型决定。</td></tr><tr><td>injectionModels</td><td>注入时间、位置、流量与粒径分布等设置；需要同时满足总注入质量与统计分辨率要求。</td></tr><tr><td>patchInteractionModel</td><td>颗粒与边界接触时的反弹、粘附或逸出处理。</td></tr><tr><td>surfaceFilmModel</td><td>表面液膜模型选择，需与液膜区域和主流体耦合条件配套。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>cloudFunctions</td><td>颗粒云附加监测或后处理功能。</td></tr><tr><td>mu</td><td>通常表示动力黏度，也可能在特定模型中表示其他系数；必须结合量纲和源码语境确认。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>e</td><td>optional - elasticity coeff</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · lagrangian/kinematicParcelFoam/drippingChair</h3><p>原始路径：<code>tutorials/lagrangian/kinematicParcelFoam/drippingChair/constant/kinematicCloudProperties</code>；求解器：<code>kinematicParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/drippingChair/constant/kinematicCloudProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/kinematiccloudproperties/1-kinematicCloudProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/drippingChair">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · lagrangian/kinematicParcelFoam/windshield</h3><p>原始路径：<code>tutorials/lagrangian/kinematicParcelFoam/windshield/constant/kinematicCloudProperties</code>；求解器：<code>kinematicParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/windshield/constant/kinematicCloudProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/kinematiccloudproperties/2-kinematicCloudProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/windshield">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · lagrangian/uncoupledKinematicParcelDyMFoam/rotor2DAMI</h3><p>原始路径：<code>tutorials/lagrangian/uncoupledKinematicParcelDyMFoam/rotor2DAMI/constant/kinematicCloudProperties</code>；求解器：<code>uncoupledKinematicParcelDyMFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/uncoupledKinematicParcelDyMFoam/rotor2DAMI/constant/kinematicCloudProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/kinematiccloudproperties/3-kinematicCloudProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/uncoupledKinematicParcelDyMFoam/rotor2DAMI">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/kinematicparcelfoam/">kinematicParcelFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/kinematicCloudProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/kinematicCloudProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
