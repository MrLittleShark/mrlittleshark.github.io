---
title: "dsmcInitialiseDict"
layout: reference
description: "设置 DSMC 初始粒子分布、物种数密度、温度和宏观速度。"
dictionary: true
cms_slug: "dictionary-dsmcinitialisedict"
---

<p>设置 DSMC 初始粒子分布、物种数密度、温度和宏观速度。</p><p>位置：<code>system/dsmcInitialiseDict</code></p><h2>配置实例</h2><p>discreteMethods/dsmcFoam/supersonicCorner 中的 dsmcInitialiseDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      dsmcInitialiseDict;
}

numberDensities
{
    Ar          1.0e20;
};

temperature     300;

velocity        (1936 0 0);</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · discreteMethods/dsmcFoam/supersonicCorner</summary><p><code>supersonicCorner</code> 先生成一团带整体来流速度的稀薄氩气，再通过 DSMC 追踪分子运动与统计碰撞。本文件供 <code>dsmcInitialise</code> 生成初始粒子云。</p>
<ul>
<li><code>numberDensities/Ar 1.0e20</code> 是氩原子数密度，单位为 m⁻³。配套 <code>dsmcProperties</code> 的 <code>typeIdList</code> 中必须存在 <code>Ar</code>。</li>
<li><code>temperature 300</code> 指定 300 K 的初始热运动温度。初始化在整体速度上叠加按温度采样的随机热速度。</li>
<li><code>velocity (1936 0 0)</code> 给出 x 方向 1936 m/s 的整体漂移速度，与角点附近的压缩流动相配合。</li>
<li>配套 <code>nEquivalentParticles 1.2e12</code> 表示一个模拟粒子代表的真实原子数。区域体积为 \(V\) 时，模拟粒子数量约为 \(nV/(1.2\times10^{12})\)。</li>
</ul>
<p>提高数密度会缩短平均自由程，也会改变合适的网格与时间步。单独提高统计分辨率时，可降低等效粒子数，并比较密度、温度和壁面统计量的波动。</p>
<p><a href="/assets/examples/v2512/dsmcinitialisedict/1-dsmcInitialiseDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/supersonicCorner/system/dsmcInitialiseDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/supersonicCorner">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      dsmcInitialiseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

numberDensities
{
    Ar          1.0e20;
};

temperature     300;

velocity        (1936 0 0);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · discreteMethods/dsmcFoam/freeSpacePeriodic</summary><p><code>freeSpacePeriodic</code> 在周期区域内初始化氮氧混合气，适合观察粒子穿过周期边界后的输运与碰撞统计。</p>
<ul>
<li><code>N2 0.777e20</code> 与 <code>O2 0.223e20</code> 相加为 \(10^{20}\,\mathrm{m^{-3}}\)，对应数量分数 77.7% 与 22.3%。质量分数还需乘各分子的质量后重新归一化。</li>
<li><code>temperature 300</code> 同时给出初始热运动尺度，<code>velocity (1950 0 0)</code> 给出共同的 x 向整体速度。</li>
<li>配套 <code>InflowBoundaryModel none</code> 表示没有额外入口注入；周期边界让现有分子离开一侧后从另一侧继续运动。</li>
<li>配套 <code>nEquivalentParticles 1e12</code> 控制抽样粒子数。总数密度保持不变时，减小这一权重会增加计算中的模拟粒子。</li>
</ul>
<p>把整体速度改为零，可以比较静止与平移参考状态下的温度统计。改变混合比例时保持总数密度一致，可单独研究分子质量与碰撞参数的影响。</p>
<p><a href="/assets/examples/v2512/dsmcinitialisedict/2-dsmcInitialiseDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/freeSpacePeriodic/system/dsmcInitialiseDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/freeSpacePeriodic">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      dsmcInitialiseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

numberDensities
{
    N2          0.777e20;
    O2          0.223e20;
};

temperature     300;

velocity        (1950 0 0);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · discreteMethods/dsmcFoam/wedge15Ma5</summary><p><code>wedge15Ma5</code> 初始化流向 15° 楔面的稀薄氮氧混合气。楔形几何使来流偏转，形成可研究的压缩区。</p>
<ul>
<li><code>N2 0.777e20</code>、<code>O2 0.223e20</code> 定义两种分子的初始数密度，总数密度为 \(10^{20}\,\mathrm{m^{-3}}\)。</li>
<li><code>temperature 300</code> 为初始温度，<code>velocity (1736 0 0)</code> 为整体来流速度；案例名称中的 <code>Ma5</code> 对应其约五倍声速的工况。</li>
<li>数密度、温度和漂移速度描述气体状态；粒子统计权重与碰撞模型继续在 <code>dsmcProperties</code> 中设置。</li>
</ul>
<p>保持楔角不变，分别改变速度和数密度，可以观察可压缩效应与稀薄效应的变化。统计壁面压力、滑移速度和温度时，使用相同的稳定后采样时长，便于比较不同工况。</p>
<p><a href="/assets/examples/v2512/dsmcinitialisedict/3-dsmcInitialiseDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/wedge15Ma5/system/dsmcInitialiseDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/wedge15Ma5">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      dsmcInitialiseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

numberDensities
{
    N2          0.777e20;
    O2          0.223e20;
};

temperature     300;

velocity        (1736 0 0);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/dsmcinitialise/">dsmcInitialise</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
