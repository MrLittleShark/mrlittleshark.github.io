---
title: "mechanicalProperties"
layout: reference
description: "固体力学中的密度、弹性模量与泊松比等材料参数。"
dictionary: true
cms_slug: "dictionary-mechanicalproperties"
---

<p>固体力学中的密度、弹性模量与泊松比等材料参数。</p><p>位置：<code>constant/mechanicalProperties</code></p><h2>配置实例</h2><p>stressAnalysis/solidDisplacementFoam/plateHole 中的 mechanicalProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      mechanicalProperties;
}

rho
{
    type        uniform;
    value       7854;
}

nu
{
    type        uniform;
    value       0.3;
}

E
{
    type        uniform;
    value       2e+11;
}

planeStress     yes;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>rho</td><td>固体密度，示例可以通过 uniform/value 子字典指定。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>nu</td><td>此文件中 nu 表示泊松比，不是流体运动黏度。</td></tr><tr><td>E</td><td>杨氏模量，压力单位。</td></tr><tr><td>planeStress</td><td>平面应力开关；关闭时的二维约束应结合求解器与几何解释。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · stressAnalysis/solidDisplacementFoam/plateHole</summary><p>plateHole 用线弹性模型计算带孔板在载荷下的位移与应力。mechanicalProperties 定义均匀材料参数。</p>
<ul>
<li><code>rho/value 7854</code> 设置密度为 7854 kg/m³。</li>
<li><code>E/value 2e11</code> 设置杨氏模量为 200 GPa，决定材料抵抗拉伸变形的刚度。</li>
<li>这里的 <code>nu/value 0.3</code> 是泊松比，表示单轴拉伸时横向与纵向应变之间的关系。</li>
<li><code>planeStress yes</code> 采用平面应力设置，适用于厚度较小、厚度方向应力可忽略的板问题。</li>
</ul>
<p>更换材料时成组修改 E、nu 和 rho；检查孔边应力集中时同时细化孔周网格。</p>
<p><a href="/assets/examples/v2512/mechanicalproperties/1-mechanicalProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/stressAnalysis/solidDisplacementFoam/plateHole/constant/mechanicalProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/stressAnalysis/solidDisplacementFoam/plateHole">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mechanicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

rho
{
    type        uniform;
    value       7854;
}

nu
{
    type        uniform;
    value       0.3;
}

E
{
    type        uniform;
    value       2e+11;
}

planeStress     yes;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · stressAnalysis/solidEquilibriumDisplacementFoam/beamEndLoad</summary><p>beamEndLoad 用端部载荷测试梁的弹性变形。材料常数与平面应力假设集中写在这里。</p>
<ul>
<li><code>rho 7854</code>、<code>E 2e11</code> 分别给出密度 7854 kg/m³ 和杨氏模量 200 GPa。</li>
<li><code>nu 0.0</code> 将泊松比设为零，简化横向收缩与纵向拉伸之间的耦合，便于这个演示问题的比较。</li>
<li><code>type uniform</code> 表示这些参数在整个材料域内一致，<code>planeStress yes</code> 选择平面应力关系。</li>
</ul>
<p>采用实际材料泊松比后重新比较梁端位移；改变梁厚时还应检查平面应力假设和载荷单位。</p>
<p><a href="/assets/examples/v2512/mechanicalproperties/2-mechanicalProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/stressAnalysis/solidEquilibriumDisplacementFoam/beamEndLoad/constant/mechanicalProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/stressAnalysis/solidEquilibriumDisplacementFoam/beamEndLoad">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mechanicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

rho
{
    type        uniform;
    value       7854;
}

nu
{
    type        uniform;
    value       0.0;
}

E
{
    type        uniform;
    value       2e+11;
}

planeStress     yes;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/soliddisplacementfoam/">solidDisplacementFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
