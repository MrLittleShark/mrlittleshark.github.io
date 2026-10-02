---
title: "MRFProperties"
layout: reference
description: "在指定 cellZone 内设置旋转参考系，常用于固定网格上的叶轮流动近似。"
dictionary: true
cms_slug: "dictionary-mrfproperties"
---

<p>在指定 cellZone 内设置旋转参考系，常用于固定网格上的叶轮流动近似。</p><p>位置：<code>constant/MRFProperties</code></p><figure class="wolf-figure"><img src="/assets/wolf/wolf-dynamic-mrf-configuration.png" alt="MRF 的旋转区和壁面参考系" loading="lazy"><figcaption><strong>MRF 的旋转区和壁面参考系</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 154</small></figcaption></figure><h2>MRFProperties 定义旋转参考系区域</h2>
<p>MRF（Multiple Reference Frame）在指定体积区域中采用旋转参考系处理动量方程，常用于搅拌器和旋转机械的稳态近似。网格几何在计算中保持静止，区域内的旋转效应通过方程和通量处理体现。</p>
<p>以下配置主体放在 <code>constant/MRFProperties</code> 的文件头之后：</p>
<pre><code class="language-foam">MRF1
{
    cellZone rotor;
    active yes;
    nonRotatingPatches ();
    origin (0 0 0);
    axis (0 0 1);
    omega 104.72;
}
</code></pre>
<p><code>MRF1</code> 是区域名称，可以自定；<code>rotor</code> 必须是已有 <code>cellZone</code>。<code>origin</code> 定义转轴经过的点，单位为 m；<code>axis</code> 给出轴方向；<code>omega</code> 是角速度，单位为 rad/s，正方向按右手定则。</p>
<p>转速与角速度满足 \(\omega=2\pi n/60\)。1000 r/min 对应约 104.72 rad/s。将转速数值 1000 直接填进 <code>omega</code> 会改变实际转速。</p>
<h3>nonRotatingPatches 怎么填</h3>
<p>MRF 区域中的边界通常按区域旋转处理。若固定外壁也落在旋转单元区域的边界上，需要把对应 patch 名加入 <code>nonRotatingPatches</code>，例如：</p>
<pre><code class="language-foam">nonRotatingPatches (stationaryWall);
</code></pre>
<p>名称与网格 <code>boundary</code> 文件一致。叶轮壁面随参考系旋转，固定机壳保持绝对静止；这一区分决定壁面速度与流体相对运动。若固定壁面在旋转区之外，则由其所在区域的普通边界设置处理。</p>
<h3>确认旋转区域</h3>
<p>建立 <code>cellZone</code> 后，在 ParaView 中显示相应区域，检查它是否覆盖叶轮附近的流体，并与静止区域形成合理划分。运行时日志会列出 MRF 区域，几何上的 <code>rotor</code> 分区与文件名中的文字本身没有自动关联，关键是网格中的实际区域名称。</p>
<p>可在文件中添加多个类似 <code>MRF1</code> 的对象，分别指定单元区、转轴和角速度。区域定义和物理分区应一致，避免同一单元被不合理地重复赋予不同旋转状态。</p>
<h3>什么时候改用动网格</h3>
<p>MRF 适合在固定相对位置上估计平均流动、压升或扭矩。若需要计算叶片通过频率、转子与定子相对位置变化或运动引起的瞬态作用，可使用实际旋转网格和 AMI 接口，相关运动写在 <code>dynamicMeshDict</code> 中。</p>
<p>v2512 的 <code>simpleFoam/mixerVessel2D</code> 提供 MRF 示例。比较不同转速时，同时记录流量、压差和力矩，比只观察速度云图更便于理解运行特性。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/simpleFoam/rotatingCylinders</summary><p>rotatingCylinders 采用 MRF 旋转参考系处理转动区域，网格点保持原位。</p>
<ul>
<li><code>cellZone all</code> 选定作用区域，<code>active yes</code> 启用它。</li>
<li><code>origin (0 0 0)</code>、<code>axis (0 0 1)</code> 给出 z 轴转动中心。</li>
<li><code>omega 100</code> 的单位为 rad/s。</li>
<li><code>nonRotatingPatches (outerWall)</code> 指明外壁不随该参考系转动。</li>
</ul>
<p>改变转速时修改 omega；外壁和内壁的实际运动还需与速度边界条件一起核对。</p>
<p><a href="/assets/examples/v2512/mrfproperties/1-MRFProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/rotatingCylinders/constant/MRFProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/rotatingCylinders">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      MRFProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

MRF1
{
    cellZone    all;
    active      yes;

    nonRotatingPatches (outerWall);

    origin    (0 0 0);
    axis      (0 0 1);
    omega     100;
}

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet</summary><p>cpuCabinet 在 domain0 流体区内用 MRF 近似风扇区域的转动。</p>
<ul>
<li><code>cellZone v_MRF</code> 指定局部旋转区，<code>active true</code> 启用。</li>
<li>转轴通过 (−0.01,0.04,−0.06)，<code>axis (1 0 0)</code> 沿 x。</li>
<li><code>omega 209.44</code> 约对应 2000 rpm。</li>
<li><code>nonRotatingPatches ()</code> 未另外列出保持静止的边界。</li>
</ul>
<p>移动风扇位置时同步更新 cellZone 和轴心；转速变化后比较流量、压降与散热效果。</p>
<p><a href="/assets/examples/v2512/mrfproperties/2-MRFProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet/constant/domain0/MRFProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      MRFProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

VC_1
{
    cellZone        v_MRF;
    active          true;
    nonRotatingPatches ();
    origin          (-0.01 0.04 -0.06);
    axis            (1 0 0);
    omega           209.44;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/simpleFoam/mixerVessel2D</summary><p>mixerVessel2D 使用 MRF 近似搅拌转子对流体的作用。</p>
<ul>
<li><code>cellZone rotor</code> 选择旋转单元区。</li>
<li>转轴经过原点，方向为 <code>(0 0 1)</code>。</li>
<li><code>omega 104.72</code> 约为 1000 rpm，<code>active yes</code> 开启该区域。</li>
<li><code>nonRotatingPatches ()</code> 没有附加静止边界清单。</li>
</ul>
<p>需要解析转子相位随时间的变化时，应评估真实动网格方案；MRF 参数变化主要改变参考系中的旋转作用。</p>
<p><a href="/assets/examples/v2512/mrfproperties/3-MRFProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/mixerVessel2D/constant/MRFProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/mixerVessel2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      MRFProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

MRF1
{
    cellZone    rotor;
    active      yes;

    // Fixed patches (by default they &#x27;move&#x27; with the MRF zone)
    nonRotatingPatches ();

    origin    (0 0 0);
    axis      (0 0 1);
    omega     104.72;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/pimplefoam/">pimpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
