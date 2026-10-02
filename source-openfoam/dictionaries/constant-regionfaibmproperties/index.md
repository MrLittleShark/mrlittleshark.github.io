---
title: "regionFaIBMProperties"
layout: reference
description: "风挡颗粒/液膜教程中的有限面积区域运动表面配置。"
dictionary: true
cms_slug: "dictionary-regionfaibmproperties"
---

<p>风挡颗粒/液膜教程中的有限面积区域运动表面配置。</p><p>位置：<code>constant/regionFaIBMProperties</code></p><h2>配置实例</h2><p>lagrangian/kinematicParcelFoam/windshield 中的 regionFaIBMProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    location    &quot;constant&quot;;
    object      IBMProperties;
}

IBM1
{
    surface             &quot;&lt;constant&gt;/surface.obj&quot;;

    solidBodyMotionFunction rotatingMotion;

    origin              (0.5 0 0);
    axis                (0 0 1);
    omega               sine;
    frequency           0.5;
    amplitude           1;
    t0                 -1;

    // A scalar Function1
    scale               0.8;
    level               0;
}

IBM2
{
    surface             &quot;&lt;constant&gt;/surface_offset.obj&quot;;

    solidBodyMotionFunction rotatingMotion;

    origin              (0.65 0 0);
    axis                (0 0 1);
    omega               sine;
    frequency           0.5;
    amplitude           1;
    t0                 -1;

    // A scalar Function1
    scale               0.8;
    level               0;
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>surface</td><td>运动表面的几何路径，&lt;constant&gt; 在 OpenFOAM 文件查找机制中展开。</td></tr><tr><td>solidBodyMotionFunction</td><td>刚体运动函数，这些示例使用 rotatingMotion。</td></tr><tr><td>origin</td><td>局部坐标系、旋转或几何操作的参考原点。</td></tr><tr><td>axis</td><td>旋转轴或方向向量；需明确是否要求单位向量。</td></tr><tr><td>omega</td><td>角速度参数或湍流比耗散率场名，二者物理意义与量纲不同。</td></tr><tr><td>frequency</td><td>sine 函数的频率参数；与所定义函数的时间变量配合。</td></tr><tr><td>amplitude</td><td>sine 函数的振幅。</td></tr><tr><td>t0</td><td>时间函数参考起点，改变相位。</td></tr><tr><td>scale</td><td>此处属于对应区域对象的标量 Function1 设置，应按所用区域模型解释。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/kinematicParcelFoam/windshield</summary><p>windshield 用两个浸入边界表面表示摆动部件，regionFaIBMProperties 给它们指定几何和随时间变化的旋转运动。</p>
<ul>
<li>IBM1 与 IBM2 分别读取 surface.obj 和 surface_offset.obj，路径中的 <code>&lt;constant&gt;</code> 指向当前算例的 constant 目录。</li>
<li>两者均为 <code>rotatingMotion</code>，旋转轴为 <code>(0 0 1)</code>；旋转中心分别是 <code>(0.5 0 0)</code> 与 <code>(0.65 0 0)</code>。</li>
<li><code>omega sine</code> 将角速度设为正弦函数，<code>frequency 0.5</code> 对应 2 s 周期，<code>t0 -1</code> 设置时间偏移。</li>
<li><code>amplitude 1</code>、<code>scale 0.8</code>、<code>level 0</code> 给出正弦函数的幅值、缩放和基准，角速度随时间正负交替形成往复摆动。</li>
</ul>
<p>改变转轴位置时同步查看两个表面是否仍与目标部件重合，并比较一个周期内的最小间隙。</p>
<p><a href="/assets/examples/v2512/regionfaibmproperties/1-regionFaIBMProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/windshield/constant/regionFaIBMProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/windshield">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;constant&quot;;
    object      IBMProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

IBM1
{
    surface             &quot;&lt;constant&gt;/surface.obj&quot;;

    solidBodyMotionFunction rotatingMotion;

    origin              (0.5 0 0);
    axis                (0 0 1);
    omega               sine;
    frequency           0.5;
    amplitude           1;
    t0                 -1;

    // A scalar Function1
    scale               0.8;
    level               0;
}

IBM2
{
    surface             &quot;&lt;constant&gt;/surface_offset.obj&quot;;

    solidBodyMotionFunction rotatingMotion;

    origin              (0.65 0 0);
    axis                (0 0 1);
    omega               sine;
    frequency           0.5;
    amplitude           1;
    t0                 -1;

    // A scalar Function1
    scale               0.8;
    level               0;
}

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/kinematicparcelfoam/">kinematicParcelFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
