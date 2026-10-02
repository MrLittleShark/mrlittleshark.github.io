---
title: "RASProperties"
layout: reference
description: "v2512 源码中保留的特定教程文件名。"
dictionary: true
cms_slug: "dictionary-rasproperties"
---

<p>v2512 源码中保留的特定教程文件名。</p><p>位置：<code>constant/RASProperties</code></p><h2>配置实例</h2><p>incompressible/overSimpleFoam/aeroFoil/background_overset 中的 RASProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      RASProperties;
}

RASModel        kOmegaSST;

turbulence      on;

printCoeffs     on;</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/overSimpleFoam/aeroFoil/background_overset</summary><p>翼型重叠网格算例的背景区域采用 k–ω SST 湍流模型。该模型组合近壁 k–ω 描述和外部剪切流处理。</p>
<ul>
<li><code>RASModel kOmegaSST</code> 选择模型，需要相应的 k、omega 和 nut 场。</li>
<li><code>turbulence on</code> 启用湍流输运，<code>printCoeffs on</code> 在日志中打印使用的模型系数，便于与修改值核对。</li>
<li>该字典属于 background_overset 区域；另一个网格区域的设置应与其物理模型协调。</li>
</ul>
<p>改变来流速度或湍流条件时同步修改 k、omega 的入口值，并检查壁面 y⁺ 与所用壁面处理是否匹配。</p>
<p><a href="/assets/examples/v2512/rasproperties/1-RASProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/overSimpleFoam/aeroFoil/background_overset/constant/RASProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/overSimpleFoam/aeroFoil/background_overset">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      RASProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

RASModel        kOmegaSST;

turbulence      on;

printCoeffs     on;

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/foamdictionary/">foamDictionary</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
