---
title: "particleTrackDict"
layout: reference
description: "粒子跟踪工具的轨迹筛选与输出控制。"
dictionary: true
cms_slug: "dictionary-particletrackdict"
---

<p>粒子跟踪工具的轨迹筛选与输出控制。</p><p>位置：<code>constant/particleTrackDict</code></p><h2>配置实例</h2><p>lagrangian/reactingHeterogenousParcelFoam/rectangularDuct 中的 particleTrackDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      particleTrackDict;
}

cloud           reactingCloud1Tracks;

fields
(
    d
    U
    T
);</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>cloud</td><td>要导出的轨迹云名称；示例为 reactingCloud1Tracks，应与已有 lagrangian 数据一致。</td></tr><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/reactingHeterogenousParcelFoam/rectangularDuct</summary><p>矩形管道算例保存了颗粒轨迹云 reactingCloud1Tracks，steadyParticleTracks 将它整理为可显示的轨迹及沿轨迹的数据。</p>
<ul>
<li><code>cloud reactingCloud1Tracks</code> 指定要读取的轨迹云名称，应与时间目录下 lagrangian 子目录对应。</li>
<li><code>fields (d U T)</code> 为每条轨迹附带粒径、速度和温度，便于观察颗粒沿管道的受热与运动。</li>
<li>这些值来自计算时保存的颗粒字段，字段名需要与云目录中的文件一致。</li>
</ul>
<p>希望比较组分或反应程度时，先让颗粒模型输出相应字段，再把字段名称加入列表。</p>
<p><a href="/assets/examples/v2512/particletrackdict/1-particleTrackDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingHeterogenousParcelFoam/rectangularDuct/constant/particleTrackDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingHeterogenousParcelFoam/rectangularDuct">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      particleTrackDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

cloud           reactingCloud1Tracks;

fields
(
    d
    U
    T
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · etc/caseDicts/annotated</summary><p>这个注释模板用于指定颗粒轨迹云和沿轨迹导出的字段。移植时需更新其中的云名称键。</p>
<ul>
<li><code>reactingCloud1Tracks</code> 是示例轨迹云名称，实际数据位于时间目录的 lagrangian 子目录中。</li>
<li>v2512 的 steadyParticleTracks 读取 <code>cloud</code>，因此将模板的 <code>cloudName reactingCloud1Tracks;</code> 改为 <code>cloud reactingCloud1Tracks;</code>。</li>
<li><code>fields (d U T)</code> 选择粒径、速度和温度，分别用于轨迹大小、速度方向和热状态的分析。</li>
</ul>
<p>先确认选定时间中存在该云及字段，再运行轨迹导出；其他云可通过更换 cloud 值处理。</p>
<p><a href="/assets/examples/v2512/particletrackdict/2-particleTrackDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/particleTrackDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      particleTrackDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

cloudName       reactingCloud1Tracks;

fields ( d U T );

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/particletracks/">particleTracks</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>未找到指定场或函数对象：<code>No field / No functionObject</code></td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
