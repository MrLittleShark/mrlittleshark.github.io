---
title: "mdEquilibrationDict"
layout: reference
description: "分子动力学预平衡阶段的控制参数。"
dictionary: true
cms_slug: "dictionary-mdequilibrationdict"
---

<p>分子动力学预平衡阶段的控制参数。</p><p>位置：<code>system/mdEquilibrationDict</code></p><h2>配置实例</h2><p>discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater 中的 mdEquilibrationDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      mdEquilibrationDict;
}

targetTemperature  298;</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater</summary><p>周期水体系的初始排列需要经过动力学演化再进入采样阶段。本文件把平衡阶段的目标温度设为 298 K。</p>
<ul>
<li><code>targetTemperature 298</code> 是温度控制目标，与初始化文件中的 298 K 配合。</li>
<li>v2512 的 <code>mdEquilibrationFoam</code> 在写出时刻调用温度调整，因此 <code>controlDict</code> 中的写出频率也决定这种温度调整的间隔。</li>
<li>实现使用 \(\sqrt{T_{target}/T_{measured}}\) 同时缩放分子的速度和角动量；当前统计温度高于目标时，缩放系数小于 1。</li>
</ul>
<p>可以改变目标温度建立另一组平衡初态，也可比较不同写出间隔对达到平衡速度的影响。进入后续动力学计算前，观察温度、压力和能量统计是否稳定，并保存对应的分子状态。</p>
<p><a href="/assets/examples/v2512/mdequilibrationdict/1-mdEquilibrationDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater/system/mdEquilibrationDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mdEquilibrationDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

targetTemperature  298;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon</summary><p><code>periodicCubeArgon</code> 将高密度氩原子体系调节到 300 K，为后续统计或动力学计算准备初态。</p>
<ul>
<li><code>targetTemperature 300.0</code> 指定平衡目标温度，单位 K。</li>
<li>温度控制在求解器的写出时刻进行；改变 <code>writeInterval</code> 会同时改变数据输出与该平衡步骤的调用频率。</li>
<li>若测得温度为 330 K，速度缩放系数为 \(\sqrt{300/330}\approx0.9535\)。缩放速度降低动能，使体系向目标温度调整。</li>
</ul>
<p>可比较不同初始化晶格和密度下的平衡过程。温度达到目标后，继续观察压力与势能的变化，再确定用于后续计算的初始状态。</p>
<p><a href="/assets/examples/v2512/mdequilibrationdict/2-mdEquilibrationDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon/system/mdEquilibrationDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mdEquilibrationDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

targetTemperature  300.0;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/mdequilibrationfoam/">mdEquilibrationFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
