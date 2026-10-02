---
title: "radiationProperties"
layout: reference
description: "选择辐射模型及吸收、发射、散射等子模型，为能量方程提供辐射热交换。"
dictionary: true
cms_slug: "dictionary-radiationproperties"
---

<p>选择辐射模型及吸收、发射、散射等子模型，为能量方程提供辐射热交换。</p><p>位置：<code>constant/radiationProperties</code></p><h2>radiationProperties 选择辐射换热模型</h2>
<p><code>radiationProperties</code> 描述辐射如何在介质和表面之间传递。它位于 <code>constant</code> 下；多区域算例中通常位于 <code>constant/&lt;区域名&gt;/radiationProperties</code>。求解器根据模型将辐射贡献加入能量方程。</p>
<h3>表面对表面的 viewFactor 模型</h3>
<p>下面是 v2512 多区域加热教程中使用的配置主体，放在文件头之后：</p>
<pre><code class="language-foam">radiation on;
radiationModel viewFactor;
viewFactorCoeffs
{
    smoothing true;
    constantEmissivity true;
}
solverFreq 3;
absorptionEmissionModel none;
scatterModel none;
sootModel none;
</code></pre>
<p><code>radiation on</code> 启用辐射，<code>viewFactor</code> 使用表面之间的角系数描述能量交换，适用于主要考虑表面辐射、介质自身参与较弱的设置。<code>constantEmissivity true</code> 允许采用恒定表面发射率的处理；具体壁面发射率和辐射边界仍由相关场及边界配置给出。</p>
<p><code>solverFreq 3</code> 指定辐射计算与流动迭代之间的调用频率，启动阶段还会进行必要初始化。辐射场变化较快时可先取 1，再比较降低计算频率对温度与热流的影响。</p>
<p><code>absorptionEmissionModel none</code>、<code>scatterModel none</code> 和 <code>sootModel none</code> 分别关闭体介质的相应吸收发射子模型、散射和烟炱模型。这组设置与表面辐射案例配套。</p>
<h3>角系数从哪里来</h3>
<p>角系数 \(F_{ij}\) 表示表面 \(i\) 发出的辐射中，到达表面 \(j\) 的比例。它由几何位置、遮挡和表面离散决定。封闭系统中，每个表面的各方向贡献满足相应的能量分配关系，互易关系为 \(A_iF_{ij}=A_jF_{ji}\)。</p>
<p>在完整多区域教程完成网格和相关预处理后，可对一个空气区域生成角系数：</p>
<pre><code class="language-bash">viewFactorsGen -region topAir
</code></pre>
<p><code>topAir</code> 对应实际区域名。教程同时提供角系数生成、壁面辐射场和必要的预处理字典；只增加 <code>radiationModel viewFactor</code> 尚未提供这些几何及边界数据。<code>smoothing</code> 用于所配置的角系数矩阵平滑处理，适合结合封闭表面的角系数收支检查。</p>
<h3>选择参与介质模型</h3>
<p>高温气体、烟气或有明显吸收的介质，可考虑 P1 或 fvDOM 等模型。P1 使用辐射传输的近似形式；fvDOM 将方向空间离散成多个方向，计算量通常随角度分辨率增加。它们需要相应吸收、发射和散射系数，模型选择应结合介质光学厚度与方向性需求。</p>
<p>热辐射与绝对温度的四次方有关。例如理想黑体净交换的量级为 \(\sigma(T_h^4-T_c^4)\)，其中 \(\sigma\approx5.67\times10^{-8}\,\mathrm{W/(m^2K^4)}\)。温度必须使用 K。开启辐射后可比较壁面辐射热流与导热、对流热流的量级，分析它对总能量收支的贡献。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · heatTransfer/chtMultiRegionSimpleFoam/multiRegionHeaterRadiation</summary><p>multiRegionHeaterRadiation 的 topAir 区使用视因子方法处理表面间辐射。</p>
<ul>
<li><code>radiation on</code>、<code>radiationModel viewFactor</code> 启用表面辐射模型，视因子描述各表面互相可见的程度。</li>
<li><code>constantEmissivity true</code> 按固定发射率处理，表面参数要与边界辐射配置对应。</li>
<li><code>smoothing true</code> 启用视因子模型的平滑处理，<code>solverFreq 3</code> 使辐射求解隔若干求解步更新。</li>
<li><code>absorptionEmissionModel none</code>、<code>scatterModel none</code>、<code>sootModel none</code> 表示这里没有附加气体吸收、散射或烟炱子模型。</li>
</ul>
<p>几何遮挡改变后需要重建视因子；壁面涂层变化则应检查表面发射率。</p>
<p><a href="/assets/examples/v2512/radiationproperties/authored-multiRegionHeater-viewFactor-radiationProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/multiRegionHeaterRadiation/constant/topAir/radiationProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/multiRegionHeaterRadiation">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      radiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

radiation       on;

radiationModel  viewFactor;

viewFactorCoeffs
{
    smoothing true; //Smooth view factor matrix (use when in a close surface
                    //to force Sum(Fij = 1)
    constantEmissivity true; //constant emissivity on surfaces.
}

// Number of flow iterations per radiation iteration
solverFreq 3;

absorptionEmissionModel none;

scatterModel    none;

sootModel       none;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · heatTransfer/buoyantSimpleFoam/hotRadiationRoom</summary><p>hotRadiationRoom 用 P1 近似描述参与辐射介质中的辐射输运。</p>
<ul>
<li><code>radiation on</code>、<code>radiationModel P1</code> 开启 P1 辐射模型，<code>solverFreq 1</code> 每个求解步更新。</li>
<li><code>constantAbsorptionEmission</code> 采用恒定吸收与发射系数。</li>
<li><code>absorptivity 0.5</code>、<code>emissivity 0.5</code> 的量纲都是 m⁻¹，描述体介质的吸收、发射能力，含义不同于无量纲壁面发射率。</li>
<li><code>E 0</code> 不额外加入该模型的体辐射发射源；散射和烟炱模型均为 <code>none</code>。</li>
</ul>
<p>改变气体或介质厚度时应重新估计光学厚度与系数，选择适合该辐射条件的模型。</p>
<p><a href="/assets/examples/v2512/radiationproperties/authored-hotRadiationRoom-P1-radiationProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/hotRadiationRoom/constant/radiationProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/hotRadiationRoom">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      radiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

radiation on;

radiationModel  P1;

// Number of flow iterations per radiation iteration
solverFreq 1;

absorptionEmissionModel constantAbsorptionEmission;

constantAbsorptionEmissionCoeffs
{
    absorptivity    absorptivity    [0 -1 0 0 0 0 0] 0.5;
    emissivity      emissivity      [0 -1 0 0 0 0 0] 0.5;
    E               E               [1 -1 -3 0 0 0 0] 0;
}

scatterModel    none;

sootModel       none;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · heatTransfer/chtMultiRegionFoam/externalCoupledHeater</summary><p>externalCoupledHeater 的 heater 区在本配置中关闭辐射，只按配套导热及耦合条件处理热量。</p>
<ul>
<li><code>radiation off</code> 明确关闭辐射。</li>
<li><code>radiationModel none</code> 不创建有效辐射传热模型。</li>
<li>温度依然由能量方程和外部耦合条件决定，关闭辐射不等于恒温。</li>
</ul>
<p>启用辐射时需要一并选择模型及边界辐射属性，比较辐射与导热的相对贡献。</p>
<p><a href="/assets/examples/v2512/radiationproperties/1-radiationProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/externalCoupledHeater/constant/heater/radiationProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/externalCoupledHeater">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      radiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

radiation off;

radiationModel  none;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 4 · lagrangian/reactingParcelFoam/verticalChannel</summary><p>verticalChannel 的颗粒热流动在此不计算辐射。</p>
<ul>
<li><code>radiation off</code>、<code>radiationModel none</code> 是实际开关。</li>
<li><code>solverFreq 10</code> 是保留的辐射更新频率参数，在 none 模型下不会产生实际辐射求解。</li>
<li>颗粒和连续相的其他传热机制仍由其各自模型控制。</li>
</ul>
<p>需要辐射时先选择合适模型，再根据温度变化速度决定更新频率。</p>
<p><a href="/assets/examples/v2512/radiationproperties/2-radiationProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/verticalChannel/constant/radiationProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/verticalChannel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      radiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

radiation       off;

radiationModel  none;

solverFreq      10;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 5 · lagrangian/reactingParcelFoam/parcelInBox</summary><p>parcelInBox 的这份配置关闭连续相辐射模型。</p>
<ul>
<li><code>radiation off</code> 不计算辐射贡献。</li>
<li><code>radiationModel none</code> 与关闭状态一致。</li>
<li>箱内温度和颗粒热交换应从热物性、能量边界和云模型配置继续读取。</li>
</ul>
<p>研究高温辐射时补充模型与介质属性，再与关闭辐射的结果作同条件比较。</p>
<p><a href="/assets/examples/v2512/radiationproperties/3-radiationProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/parcelInBox/constant/radiationProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/parcelInBox">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      radiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

radiation       off;

radiationModel  none;

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/buoyantsimplefoam/">buoyantSimpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
