---
title: "phaseProperties"
layout: reference
description: "描述相系统、各相模型以及相间动量、热量和质量交换。"
dictionary: true
cms_slug: "dictionary-phaseproperties"
---

<p>描述相系统、各相模型以及相间动量、热量和质量交换。</p><p>位置：<code>constant/water/phaseProperties</code></p><h2>配置实例</h2><p>verificationAndValidation/multiphase/StefanProblem/setups.orig/icoReactingMultiphaseInterFoam 中的 phaseProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      phaseChangeProperties;
}

type    massTransferMultiphaseSystem;

phases  (liquid gas);

liquid
{
    type            pureMovingPhaseModel;
}

gas
{
    type            pureMovingPhaseModel;
}

surfaceTension
(
    (gas and liquid)
    {
        type            constant;
        sigma           0.0;
    }
);

massTransferModel
(
    (liquid to gas)
    {
        type            Lee;
        C               1700;
        Tactivate       373.25;
    }
);</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>phases</td><td>相名称列表；这些名称会影响相分数、速度、热物性等字段或字典的命名。</td></tr><tr><td>sigma</td><td>常见为表面张力系数，但在电磁模型中可表示电导率；以模型与量纲为准。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · verificationAndValidation/multiphase/StefanProblem/setups.orig/icoReactingMultiphaseInterFoam</summary><p>这个 Stefan 算例使用 <code>icoReactingMultiphaseInterFoam</code> 计算液体向气体的相变，借助平面界面问题比较相变前沿的位置。</p>
<ul>
<li><code>type massTransferMultiphaseSystem</code> 启用相间质量交换；<code>phases (liquid gas)</code> 列出两相，均为 <code>pureMovingPhaseModel</code>。</li>
<li><code>surfaceTension</code> 中 <code>sigma 0.0</code> 去掉表面张力作用，使本例突出导热、潜热与相变前沿运动。</li>
<li><code>(liquid to gas)</code> 指定质量由液相转入气相；<code>Lee</code> 使用温度偏离激活温度的程度构造源项。</li>
<li><code>C 1700</code> 的量纲为 s⁻¹，<code>Tactivate 373.25</code> 为激活温度，单位 K。对于这里的正 <code>C</code>，高于激活温度的液相产生蒸发源项。</li>
</ul>
<p>可以先保持 <code>Tactivate</code> 与热物性不变，减小 <code>C</code> 比较界面响应，再做时间步和网格细化。验证指标可选界面位置、温度剖面及总潜热消耗。</p>
<p><a href="/assets/examples/v2512/phaseproperties/1-phaseProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/icoReactingMultiphaseInterFoam/constant/phaseProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/icoReactingMultiphaseInterFoam">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      phaseChangeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

type    massTransferMultiphaseSystem;

phases  (liquid gas);

liquid
{
    type            pureMovingPhaseModel;
}

gas
{
    type            pureMovingPhaseModel;
}

surfaceTension
(
    (gas and liquid)
    {
        type            constant;
        sigma           0.0;
    }
);

massTransferModel
(
    (liquid to gas)
    {
        type            Lee;
        C               1700;
        Tactivate       373.25;
    }
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/icoReactingMultiphaseInterFoam/evaporationMultiComponent</summary><p><code>evaporationMultiComponent</code> 将单组分液体蒸发到多组分气体中，因此两相采用不同的成分模型。</p>
<ul>
<li><code>liquid</code> 采用 <code>pureMovingPhaseModel</code>；<code>gas</code> 采用 <code>multiComponentMovingPhaseModel</code>，气相可同时含蒸气与其他组分。</li>
<li><code>species vapour.gas</code> 指定蒸发质量进入气相中的 <code>vapour</code> 组分。该名称需要与气相热物性及组分场对应。</li>
<li><code>Lee</code> 模型的 <code>C 100</code> 控制相变响应速度，<code>Tactivate 366</code> K 给出激活温度；正系数对应高温侧的液体蒸发。</li>
<li><code>sigma 0.07</code> N/m 为气液表面张力系数，会影响弯曲界面的压力跳跃及形态。</li>
</ul>
<p>修改环境气体组分时，保留蒸气接收组分与相变模型之间的对应关系。改变 <code>C</code> 可研究模型响应；改变表面张力则用于研究界面动力学。比较液体质量损失与气相蒸气增加量，可以检查相间质量交换。</p>
<p><a href="/assets/examples/v2512/phaseproperties/2-phaseProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/evaporationMultiComponent/constant/phaseProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/evaporationMultiComponent">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      phaseProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

type    massTransferMultiphaseSystem;

phases  (liquid gas);

liquid
{
    type            pureMovingPhaseModel;
}

gas
{
    type            multiComponentMovingPhaseModel;
}

surfaceTension
(
    (gas and liquid)
    {
        type            constant;
        sigma           0.07;
    }
);

massTransferModel
(
    (liquid to gas)
    {
        type            Lee;
        species         vapour.gas;
        C               100;
        Tactivate       366;
    }
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/icoReactingMultiphaseInterFoam/solidMelting2D</summary><p><code>solidMelting2D</code> 计算固体熔化后形成液体的过程，同时用阻力项抑制尚未熔化区域中的流动。</p>
<ul>
<li><code>phases (solid liquid)</code> 定义两相；固相为 <code>pureStaticSolidPhaseModel</code>，液相为 <code>pureMovingPhaseModel</code>。</li>
<li><code>(solid to liquid)</code> 的 <code>Lee</code> 模型使用 <code>Tactivate 302.78</code> K 与 <code>C 40</code> s⁻¹。温度超过激活值后，固相向液相转化。</li>
<li><code>interfacePorous</code> 选择 <code>VollerPrakash</code>，通过 <code>solidPhase alpha.solid</code> 读取固相分数。</li>
<li><code>Cu 1e7</code> 放大固相区域的阻力。源码中的系数与 \(C_u\alpha_s^2/[(1-\alpha_s)^3+10^{-3}]\) 成正比，固相分数越高，速度抑制越强。</li>
</ul>
<p>增大 <code>Cu</code> 可以进一步降低残余固区速度，同时会增强动量方程刚性。改变加热温度时，比较熔化前沿、液相对流与总焓变化；改变 <code>C</code> 时则观察相变响应速度。</p>
<p><a href="/assets/examples/v2512/phaseproperties/3-phaseProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/solidMelting2D/constant/phaseProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/solidMelting2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      phaseProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

type    massTransferMultiphaseSystem;

phases  (solid liquid);

liquid
{
    type            pureMovingPhaseModel;
}

solid
{
    type            pureStaticSolidPhaseModel;
}

interfacePorous
(
    (solid and liquid)
    {
        type            VollerPrakash;
        solidPhase      alpha.solid;
        Cu              1e7;
    }
);

massTransferModel
(
    (solid to liquid)
    {
        type            Lee;
        C               40;
        Tactivate       302.78;
    }
);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/reactingtwophaseeulerfoam/">reactingTwoPhaseEulerFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
