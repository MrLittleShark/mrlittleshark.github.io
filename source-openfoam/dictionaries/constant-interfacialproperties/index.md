---
title: "interfacialProperties"
layout: reference
description: "multiphaseEulerFoam/mixerVessel2D 教程保留的相间阻力与换热配置，示例包含 SchillerNaumann、RanzMarshall、相间混合选择与小相分数控制。"
dictionary: true
cms_slug: "dictionary-interfacialproperties"
---

<p>multiphaseEulerFoam/mixerVessel2D 教程保留的相间阻力与换热配置，示例包含 SchillerNaumann、RanzMarshall、相间混合选择与小相分数控制。</p><p>位置：<code>constant/interfacialProperties</code></p><h2>配置实例</h2><p>multiphase/multiphaseEulerFoam/mixerVessel2D 中的 interfacialProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      interfacialProperties;
}

dragModel1          SchillerNaumann;
dragModel2          SchillerNaumann;

heatTransferModel1  RanzMarshall;
heatTransferModel2  RanzMarshall;

dispersedPhase      both;
dragPhase           blended;

residualSlip        1e-2;
minInterfaceAlpha   1e-3;</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/multiphaseEulerFoam/mixerVessel2D</summary><p><code>mixerVessel2D</code> 的此文件保留了旧式两相接口写法。v2512 的配套 <code>multiphaseEulerFoam</code> 通过 <code>multiphaseSystem</code> 读取 <code>constant/transportProperties</code>；实际相间模型应在那个文件中的相对表里调整。</p>
<ul>
<li>这里的 <code>dragModel1/2 SchillerNaumann</code> 表达两侧分散相均采用球形分散物阻力关联式的意图；<code>dragPhase blended</code> 表达两种分散状态的混合处理。</li>
<li><code>heatTransferModel1/2 RanzMarshall</code> 是分散颗粒换热关联式的名称。当前求解流程应以实际读取的模型字典为准，原文件适合用于理解旧式参数组织。</li>
<li>配套 <code>transportProperties</code> 明确列出 <code>(air water)</code>、<code>(air oil)</code> 等相对，每组 <code>drag</code> 选择 <code>type blended</code>，其内部各相再选择 <code>SchillerNaumann</code>。</li>
<li>在有效的 <code>drag</code> 子字典中，<code>residualSlip 1e-2</code> 是 0.01 m/s 的滑移速度下限，<code>residualPhaseFraction 1e-2</code> 是相分数正则化参数；原文件的 <code>minInterfaceAlpha</code> 没有对应到当前这条读取路径。</li>
</ul>
<p>要比较搅拌中空气与水的滑移，可进入 <code>transportProperties/drag</code> 修改该相对的阻力设置，并检查气泡直径模型。增加一种流体时，还要补齐它与其他相之间需要的模型配置。</p>
<p><a href="/assets/examples/v2512/interfacialproperties/1-interfacialProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/multiphaseEulerFoam/mixerVessel2D/constant/interfacialProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/multiphaseEulerFoam/mixerVessel2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      interfacialProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dragModel1          SchillerNaumann;
dragModel2          SchillerNaumann;

heatTransferModel1  RanzMarshall;
heatTransferModel2  RanzMarshall;

dispersedPhase      both;
dragPhase           blended;

residualSlip        1e-2;
minInterfaceAlpha   1e-3;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/multiphaseeulerfoam/">multiphaseEulerFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
