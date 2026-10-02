---
title: "parcelInjectionProperties"
layout: reference
description: "颗粒注入位置与物性分布的配置或数据。"
dictionary: true
cms_slug: "dictionary-parcelinjectionproperties"
---

<p>颗粒注入位置与物性分布的配置或数据。</p><p>位置：<code>constant/parcelInjectionProperties</code></p><h2>配置实例</h2><p>lagrangian/reactingParcelFoam/rivuletPanel 中的 parcelInjectionProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      parcelInjectionProperties;
}

// (x y z) (u v w) d rho mDot T cp (Y0..Y2) (Yg0..YgN) (Yl0..YlN) (Ys0..YsN)
(
    (0.050 0.025 0.09) (0 0 -5) 0.001 1000 0.002 300 4200 (1)
);</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/reactingParcelFoam/rivuletPanel</summary><p><code>rivuletPanel</code> 保留了一行表格式注入数据。每行描述一个注入位置的状态，读取它的云注入模型决定使用时刻与计算包数量。</p>
<ul>
<li><code>(0.050 0.025 0.09)</code> 是位置，单位 m；<code>(0 0 -5)</code> 给出沿负 z 方向的 5 m/s 初速度。</li>
<li><code>0.001</code> 是 1 mm 粒径，<code>1000</code> kg/m³ 是密度，<code>0.002</code> kg/s 是此注入位置的质量流率。</li>
<li><code>300</code> K 与 <code>4200</code> J/(kg·K) 分别为温度与比热，末尾 <code>(1)</code> 是单组分质量分数列表。</li>
<li>本例的 <code>reactingCloud1Properties</code> 设置 <code>active no</code>，这张表当前是保留数据；启用时应配合读取这种单组分数据格式的注入模型。</li>
</ul>
<p>将流率改为 <code>0.004</code> 会把该位置的名义供液量加倍；改变速度方向可移动撞击位置。增加表格行时，检查各位置都落在网格内部，并逐行累计总流量。</p>
<p><a href="/assets/examples/v2512/parcelinjectionproperties/1-parcelInjectionProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/rivuletPanel/constant/parcelInjectionProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/rivuletPanel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      parcelInjectionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// (x y z) (u v w) d rho mDot T cp (Y0..Y2) (Yg0..YgN) (Yl0..YlN) (Ys0..YsN)
(
    (0.050 0.025 0.09) (0 0 -5) 0.001 1000 0.002 300 4200 (1)
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · lagrangian/reactingParcelFoam/splashPanel</summary><p><code>splashPanel</code> 用这行数据描述朝平板运动的液滴流，便于控制撞击速度、粒径和供液量。</p>
<ul>
<li>注入位置为 <code>(0.050 0.025 0.09)</code> m，速度 <code>(0 0 -5)</code> m/s，使液滴朝负 z 方向运动。</li>
<li>粒径为 <code>0.001</code> m、密度为 <code>1000</code> kg/m³，质量流率为 <code>0.002</code> kg/s。计算包的生成频率由读取此表的云注入模型继续设置。</li>
<li><code>300</code> K、<code>4200</code> J/(kg·K) 给出注入温度与比热。</li>
<li><code>(0 1 0)</code> 按气、液、固顺序表示纯液相；后面的 <code>()</code>、<code>(1)</code>、<code>()</code> 分别是各相内部组分列表，液相只有一种组分。</li>
</ul>
<p>改变粒径会同时改变单滴质量和撞击 Weber 数；改变速度会改变撞击动能。保持总供液量相同时，可分别比较粒径与速度对液膜累积和飞溅的影响。</p>
<p><a href="/assets/examples/v2512/parcelinjectionproperties/2-parcelInjectionProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/splashPanel/constant/parcelInjectionProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/splashPanel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      parcelInjectionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// (x y z) (u v w) d rho mDot T cp (Y0..Y2) (Yg0..YgN) (Yl0..YlN) (Ys0..YsN)
(
    (0.050 0.025 0.09) (0 0 -5) 0.001 1000 0.002 300 4200 (0 1 0) () (1) ()
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/reactingParcelFoam/cylinder</summary><p><code>cylinder</code> 沿 z 方向布置三个注入位置，让液滴从圆柱上方落向不同的轴向截面。</p>
<ul>
<li>三个位置的 x、y 坐标均为 <code>(0 1.95)</code> m，z 分别为 <code>-0.2</code>、<code>0</code>、<code>0.2</code> m；初速度均为 <code>(0 -5 0)</code> m/s。</li>
<li>每个注入位置的粒径为 1 mm，密度为 1000 kg/m³，质量流率为 0.002 kg/s；若三处同时按此表工作，总流率为 0.006 kg/s。</li>
<li>三处温度均为 300 K，比热为 4200 J/(kg·K)，因此这里主要比较位置差异引起的覆盖范围。</li>
<li><code>(0 1 0) () (1) ()</code> 表示纯液相、液相内为单组分，与所选云的组分顺序配合。</li>
</ul>
<p>扩大 z 向间距可改变轴向润湿分布，调整 y 向初速度可改变撞击强度。新增注入位置时，同时检查总流量和圆柱端部边界，便于解释膜厚沿轴向的变化。</p>
<p><a href="/assets/examples/v2512/parcelinjectionproperties/3-parcelInjectionProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/cylinder/constant/parcelInjectionProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/cylinder">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      parcelInjectionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// (x y z) (u v w) d rho mDot T Cp (Y0..Y2) (Yg0..YgN) (Yl0..YlN) (Ys0..YsN)
(
    (0 1.95 -0.2) (0 -5 0) 0.001 1000 0.002 300 4200 (0 1 0) () (1) ()
    (0 1.95    0) (0 -5 0) 0.001 1000 0.002 300 4200 (0 1 0) () (1) ()
    (0 1.95  0.2) (0 -5 0) 0.001 1000 0.002 300 4200 (0 1 0) () (1) ()
);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/reactingparcelfoam/">reactingParcelFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
