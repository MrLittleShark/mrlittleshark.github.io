---
title: "thermodynamicProperties"
layout: reference
description: "特定教程中的热力学材料数据或附加参数。"
dictionary: true
cms_slug: "dictionary-thermodynamicproperties"
---

<p>特定教程中的热力学材料数据或附加参数。</p><p>位置：<code>constant/thermodynamicProperties</code></p><h2>配置实例</h2><p>compressible/sonicLiquidFoam/decompressionTank 中的 thermodynamicProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      thermodynamicProperties;
}

rho0            1000;

p0              100000;

psi             4.54e-07;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>pSat</td><td>饱和蒸气压，须与压力场的基准与量纲一致。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · compressible/sonicLiquidFoam/decompressionTank</summary><p><code>decompressionTank</code> 研究可压缩液体的卸压过程。<code>sonicLiquidFoam</code> 用线性压力—密度关系描述液体压缩性。</p>
<ul>
<li><code>rho0 1000</code> kg/m³ 是参考密度，<code>p0 100000</code> Pa 是对应参考压力。</li>
<li><code>psi 4.54e-07</code> 表示 \(\partial\rho/\partial p\)，量纲为 s²/m²。求解器构造 \(\rho=\rho_0+\psi(p-p_0)\)。</li>
<li>压力增加 \(10^6\) Pa 时，按这组参数密度增加 0.454 kg/m³。参考态附近的声速为 \(c=1/\sqrt{\psi}\)，约 1484 m/s。</li>
</ul>
<p>改变液体材料时，应成套更新参考密度与压缩系数。提高卸压速度后，要根据声传播时间尺度选择时间步，并比较压力波到达时刻、峰值与质量收支。</p>
<p><a href="/assets/examples/v2512/thermodynamicproperties/1-thermodynamicProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/sonicLiquidFoam/decompressionTank/constant/thermodynamicProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/sonicLiquidFoam/decompressionTank">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      thermodynamicProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

rho0            1000;

p0              100000;

psi             4.54e-07;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/cavitatingFoam/LES/throttle</summary><p><code>cavitatingFoam</code> 的 <code>throttle</code> 算例用压力相关的液汽混合物描述节流处的空化。本文件给出两相的线性压缩性与饱和参考状态。</p>
<ul>
<li><code>barotropicCompressibilityModel linear</code> 按汽相分数线性混合两相压缩系数；<code>psiv 2.5e-06</code> 与 <code>psil 5e-07</code> 的量纲均为 s²/m²。</li>
<li><code>pSat 4500</code> Pa 是饱和参考压力；<code>rholSat 830</code> kg/m³ 是该压力下的液体密度。</li>
<li>源码由 <code>psiv*pSat</code> 得到饱和汽相密度，本例为 0.01125 kg/m³；液相密度截距为 <code>rholSat-pSat*psil</code>。</li>
<li><code>rhoMin 0.001</code> kg/m³ 是密度下限，供密度重建时截断使用。</li>
</ul>
<p>更换液体或温度工况时，应一起更新饱和压力、饱和液体密度和压缩系数。可通过压差扫描比较汽相体积、流量和空化区长度；数值下限的影响则通过保持物性不变、单独调整 <code>rhoMin</code> 检查。</p>
<p><a href="/assets/examples/v2512/thermodynamicproperties/2-thermodynamicProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/cavitatingFoam/LES/throttle/constant/thermodynamicProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/cavitatingFoam/LES/throttle">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      thermodynamicProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

barotropicCompressibilityModel linear;

psiv            2.5e-06;

rholSat         830;

psil            5e-07;

pSat            4500;

rhoMin          0.001;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/foamdictionary/">foamDictionary</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
