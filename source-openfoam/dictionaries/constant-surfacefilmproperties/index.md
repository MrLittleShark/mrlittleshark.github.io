---
title: "surfaceFilmProperties"
layout: reference
description: "壁面液膜区域的模型与耦合参数，包括液膜热物性、相变、颗粒与壁面相互作用等。"
dictionary: true
cms_slug: "dictionary-surfacefilmproperties"
---

<p>壁面液膜区域的模型与耦合参数，包括液膜热物性、相变、颗粒与壁面相互作用等。</p><p>位置：<code>constant/surfaceFilmProperties</code></p><h2>配置实例</h2><p>combustion/fireFoam/LES/smallPoolFire3D 中的 surfaceFilmProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      surfaceFilmProperties;
}

surfaceFilmModel none;

region          none;

active          false;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>surfaceFilmModel</td><td>表面液膜模型选择，需与液膜区域和主流体耦合条件配套。</td></tr><tr><td>region</td><td>目标网格区域名称；多区域场与网格路径中应保持一致。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>injectionModels</td><td>注入时间、位置、流量与粒径分布等设置；需要同时满足总注入质量与统计分辨率要求。</td></tr><tr><td>radiationModel</td><td>辐射传输模型名称，例如 P1、fvDOM 或 viewFactor；不同模型需要不同附加文件。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · combustion/fireFoam/LES/smallPoolFire3D</summary><p><code>smallPoolFire3D</code> 的当前配置关闭表面液膜区域，池火计算由气相及配套边界模型组织。</p>
<ul>
<li><code>surfaceFilmModel none</code> 选择空液膜模型；<code>active false</code> 关闭液膜演化。</li>
<li><code>region none</code> 与这个关闭状态一致，当前无需读取名为液膜区域的网格与场。</li>
<li>要改变池火供燃料方式，应先检查气相边界和燃烧设置；本文件当前没有液膜厚度、流速或蒸发参数可调。</li>
</ul>
<p>若改成显式液膜供燃料的模型，需要建立膜区域、初始化膜厚与温度，并选择液膜传热和相变子模型。可以比较边界供给的燃料流率与液膜蒸发流率，明确两种建模方法的输入差别。</p>
<p><a href="/assets/examples/v2512/surfacefilmproperties/1-surfaceFilmProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/smallPoolFire3D/constant/surfaceFilmProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/smallPoolFire3D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFilmProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

surfaceFilmModel none;

region          none;

active          false;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · lagrangian/reactingParcelFoam/cylinder</summary><p><code>cylinder</code> 使用单层热液膜模型描述液滴落到圆柱表面后的铺展和沿壁面流动。</p>
<ul>
<li><code>thermoSingleLayer</code>、<code>active true</code> 开启膜的质量、动量和热过程；<code>region wallFilmRegion</code> 指向独立的薄层网格区域。</li>
<li><code>filmThermoModel liquid</code>、<code>liquid H2O</code>、<code>useReferenceValues no</code> 采用水的液体物性模型；<code>filmViscosityModel liquid</code> 同样从液体物性得到黏度。</li>
<li><code>deltaWet 1e-4</code> m 给出干湿判别的膜厚尺度，<code>hydrophilic no</code> 采用非强制亲水的润湿设置。</li>
<li><code>turbulence laminar</code> 与 <code>Cf 0.005</code> 配置层流膜内的摩擦处理；<code>thermocapillary</code> 根据表面张力梯度产生切向作用。</li>
<li>上下表面的常数换热系数均为 <code>c0 1e-8</code>，对应近似隔热的设置；蒸发、辐射和膜主动注入模型在此关闭。</li>
</ul>
<p>可改变 <code>deltaWet</code> 比较润湿面积的判定，再改变入射液滴流率观察膜厚。若研究壁面加热，应设置有物理依据的下表面换热系数与壁温，并观察膜温及表面张力梯度。</p>
<p><a href="/assets/examples/v2512/surfacefilmproperties/2-surfaceFilmProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/cylinder/constant/surfaceFilmProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/cylinder">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFilmProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

surfaceFilmModel thermoSingleLayer;

region          wallFilmRegion;

active          true;

thermoSingleLayerCoeffs
{
    filmThermoModel liquid;

    liquidCoeffs
    {
        useReferenceValues  no;
        liquid      H2O;
    }

    filmViscosityModel liquid;

    deltaWet    1e-4;

    hydrophilic no;

    turbulence  laminar;
    laminarCoeffs
    {
        Cf          0.005;
    }

    forces
    (
        thermocapillary
    );

    injectionModels ();

    phaseChangeModel none;

    radiationModel none;

    upperSurfaceModels
    {
        heatTransferModel constant;
        constantCoeffs
        {
            c0                1e-8;
        }
    }

    lowerSurfaceModels
    {
        heatTransferModel constant;
        constantCoeffs
        {
            c0                1e-8;
        }
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/reactingParcelFoam/splashPanel</summary><p><code>splashPanel</code> 将颗粒撞壁过程与平板液膜耦合，用膜区域记录液体的铺展和累积。</p>
<ul>
<li><code>thermoSingleLayer</code> 在 <code>wallFilmRegion</code> 上推进液膜，液体为 <code>H2O</code>，黏度与热物性通过液体模型求取。</li>
<li><code>deltaWet 2e-4</code> m 对应 0.2 mm 的润湿判别尺度，比圆柱示例的阈值更大；其影响体现在薄膜区域的干湿识别。</li>
<li><code>hydrophilic no</code>、<code>turbulence laminar</code> 和 <code>Cf 0.005</code> 分别控制润湿处理与膜内摩擦。</li>
<li><code>forces (thermocapillary)</code> 包含热毛细作用；上下表面 <code>c0 1e-8</code> 使该例的换热接近关闭。</li>
<li>膜自身的 <code>injectionModels</code> 为空，膜蒸发和辐射均关闭。液滴撞击、吸收或飞溅的判据需要与颗粒云端的膜相互作用模型一起阅读。</li>
</ul>
<p>提高注入速度可改变撞击动量，增加流量可提高膜内积液量。比较时分别记录入射颗粒、离开壁面的颗粒和液膜质量，并保持同一膜网格与干湿阈值。</p>
<p><a href="/assets/examples/v2512/surfacefilmproperties/3-surfaceFilmProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/splashPanel/constant/surfaceFilmProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/splashPanel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFilmProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

surfaceFilmModel thermoSingleLayer;

region          wallFilmRegion;

active          true;

thermoSingleLayerCoeffs
{
    filmThermoModel liquid;

    liquidCoeffs
    {
        useReferenceValues  no;
        liquid      H2O;
    }

    filmViscosityModel liquid;

    deltaWet    2e-4;
    hydrophilic no;

    turbulence  laminar;
    laminarCoeffs
    {
        Cf          0.005;
    }

    forces
    (
        thermocapillary
    );

    injectionModels
    ();

    phaseChangeModel none;

    radiationModel none;

    upperSurfaceModels
    {
        heatTransferModel constant;
        constantCoeffs
        {
            c0                1e-8;
        }
    }

    lowerSurfaceModels
    {
        heatTransferModel constant;
        constantCoeffs
        {
            c0                1e-8;
        }
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/reactingparcelfoam/">reactingParcelFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
