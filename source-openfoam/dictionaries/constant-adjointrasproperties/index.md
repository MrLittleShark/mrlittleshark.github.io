---
title: "adjointRASProperties"
layout: reference
description: "伴随湍流模型的选择及其线性化控制。"
dictionary: true
cms_slug: "dictionary-adjointrasproperties"
---

<p>伴随湍流模型的选择及其线性化控制。</p><p>位置：<code>constant/adjointRASProperties</code></p><h2>配置实例</h2><p>incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/kOmegaSST/lift 中的 adjointRASProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      adjointTurbulenceProperties;
}

adjointRASModel adjointkOmegaSST;

adjointTurbulence on;</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/kOmegaSST/lift</summary><p>NACA0012 升力优化算例为 k–ω SST 流场选择对应的伴随湍流模型。伴随变量用于计算目标函数对设计变化的敏感度。</p>
<ul>
<li><code>adjointRASModel adjointkOmegaSST</code> 选择 SST 对应的伴随方程模型。</li>
<li><code>adjointTurbulence on</code> 将湍流模型相关的伴随贡献纳入计算。</li>
<li>该文件位于 lift 伴随问题的设置目录，应与同一工作点的原始流场模型及升力目标配置配套。</li>
</ul>
<p>切换原始湍流模型时同步选择匹配的伴随模型；先让原始流场收敛，再比较伴随残差和梯度分布。</p>
<p><a href="/assets/examples/v2512/adjointrasproperties/1-adjointRASProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/kOmegaSST/lift/constant/adjointRASProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/kOmegaSST/lift">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      adjointTurbulenceProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

adjointRASModel adjointkOmegaSST;

adjointTurbulence on;

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/adjointOptimisationFoam/sensitivityMaps/naca0012/turbulent/liftMinimumSetup</summary><p>这个 NACA0012 最小配置示例采用 Spalart–Allmaras 模型的伴随形式，用于升力相关的形状敏感度计算。</p>
<ul>
<li><code>adjointRASModel adjointSpalartAllmaras</code> 选择与原始 SA 湍流方程对应的伴随实现。</li>
<li><code>adjointTurbulence on</code> 启用伴随湍流贡献。</li>
<li>目标函数、工作点和优化更新分别由其他字典配置；这里负责模型的配对。</li>
</ul>
<p>改成 SST 时需要同时补齐原始 k、omega 场及对应伴随设置，避免只更换这一处名称而留下不匹配的场配置。</p>
<p><a href="/assets/examples/v2512/adjointrasproperties/2-adjointRASProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/naca0012/turbulent/liftMinimumSetup/constant/adjointRASProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/naca0012/turbulent/liftMinimumSetup">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      adjointTurbulenceProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

adjointRASModel adjointSpalartAllmaras;

adjointTurbulence on;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x</summary><p>层流拓扑优化算例仍通过统一的伴随湍流模型接口创建模型，因此这里使用 adjointLaminar。</p>
<ul>
<li><code>adjointRASModel adjointLaminar</code> 明确选择层流伴随实现。</li>
<li><code>adjointTurbulence on</code> 是该接口的开关；最终创建的是上面指定的层流模型。</li>
<li><code>printCoeffs off</code> 关闭模型系数打印，使优化日志更紧凑。</li>
</ul>
<p>扩展为湍流拓扑优化时，应同时处理原始湍流方程、伴随模型和近壁网格，不能只靠这个开关改变物理模型。</p>
<p><a href="/assets/examples/v2512/adjointrasproperties/3-adjointRASProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/constant/adjointRASProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      adjointRASProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

adjointRASModel        adjointLaminar;

adjointTurbulence      on;

printCoeffs     off;

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/adjointoptimisationfoam/">adjointOptimisationFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
