---
title: "gravitationalProperties"
layout: reference
description: "shallowWaterFoam 浅水教程中的重力与旋转参数。"
dictionary: true
cms_slug: "dictionary-gravitationalproperties"
---

<p>shallowWaterFoam 浅水教程中的重力与旋转参数。</p><p>位置：<code>constant/gravitationalProperties</code></p><h2>配置实例</h2><p>incompressible/shallowWaterFoam/squareBump 中的 gravitationalProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      gravitationalProperties;
}

g            g           [0 1 -2 0 0 0 0]  (0 0 -9.81);
rotating     true;
Omega        Omega       [0 0 -1 0 0 0 0]  (0 0 7.292e-5);</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>g</td><td>含显式量纲的重力加速度向量，垂向方向由其符号与坐标共同确定。</td></tr><tr><td>rotating</td><td>是否在浅水方程中考虑旋转效应。</td></tr><tr><td>Omega</td><td>旋转角速度向量，量纲为时间的负一次方；并非湍流比耗散率 omega。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/shallowWaterFoam/squareBump</summary><p>squareBump 用浅水方程计算自由液面的传播，同时可考虑旋转参考系中的科里奥利效应。</p>
<ul>
<li><code>g (0 0 -9.81)</code> 指定重力向下，大小为 9.81 m/s²。</li>
<li><code>rotating true</code> 开启旋转项。</li>
<li><code>Omega (0 0 7.292e-5)</code> 给出沿 z 轴的角速度，大小接近地球自转角速度，单位为 s⁻¹。</li>
</ul>
<p>研究旋转作用时可比较 rotating 为 true 和 false 的两组结果，保持初始水深扰动、网格和时间步一致。</p>
<p><a href="/assets/examples/v2512/gravitationalproperties/1-gravitationalProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/shallowWaterFoam/squareBump/constant/gravitationalProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/shallowWaterFoam/squareBump">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      gravitationalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

g            g           [0 1 -2 0 0 0 0]  (0 0 -9.81);
rotating     true;
Omega        Omega       [0 0 -1 0 0 0 0]  (0 0 7.292e-5);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/shallowwaterfoam/">shallowWaterFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
