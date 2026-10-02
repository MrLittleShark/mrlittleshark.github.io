---
title: "thermophysicalProperties"
layout: reference
description: "定义热力学类型、状态方程、热容、输运性质和能量变量。"
dictionary: true
cms_slug: "dictionary-thermophysicalproperties"
---

<p>定义热力学类型、状态方程、热容、输运性质和能量变量。</p><p>位置：<code>constant/thermophysicalProperties</code></p><h2>thermophysicalProperties 组合热物性模型</h2>
<p><code>constant/thermophysicalProperties</code> 定义密度、比热、黏度和能量变量如何计算。它将热力学模型、状态方程和输运模型组合成求解器需要的物性系统。</p>
<p>下面从 <code>buoyantPimpleFoam/hotRoom</code> 提取理想气体物性配置，放在 <code>FoamFile</code> 文件头之后：</p>
<pre><code class="language-foam">thermoType
{
    type            heRhoThermo;
    mixture         pureMixture;
    transport       const;
    thermo          hConst;
    equationOfState perfectGas;
    specie          specie;
    energy          sensibleEnthalpy;
}
mixture
{
    specie
    {
        molWeight 28.9;
    }
    thermodynamics
    {
        Cp 1000;
        Hf 0;
    }
    transport
    {
        mu 1.8e-5;
        Pr 0.7;
    }
}
</code></pre>
<h3>模型名称怎样组合</h3>
<table>
<thead>
<tr>
<th>条目</th>
<th>本例设置</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td><code>type</code></td>
<td><code>heRhoThermo</code></td>
<td>密度形式的热物性包</td>
</tr>
<tr>
<td><code>mixture</code></td>
<td><code>pureMixture</code></td>
<td>单一组成、均匀混合物</td>
</tr>
<tr>
<td><code>transport</code></td>
<td><code>const</code></td>
<td>常数黏度及 Prandtl 数</td>
</tr>
<tr>
<td><code>thermo</code></td>
<td><code>hConst</code></td>
<td>常数定压比热模型</td>
</tr>
<tr>
<td><code>equationOfState</code></td>
<td><code>perfectGas</code></td>
<td>理想气体状态方程</td>
</tr>
<tr>
<td><code>energy</code></td>
<td><code>sensibleEnthalpy</code></td>
<td>以显焓为能量变量</td>
</tr>
</tbody></table>
<p>这些选项需要形成受支持的组合，并与求解器所需热物性类型一致。若使用求解内能的完整案例，其 <code>energy</code> 和对应方程也会相应变化。</p>
<h3>数值与单位</h3>
<p><code>molWeight 28.9</code> 的单位为 kg/kmol；<code>Cp 1000</code> 的单位为 J/(kg K)；<code>mu 1.8e-5</code> 为动力黏度，单位为 Pa s；<code>Pr</code> 是无量纲 Prandtl 数。<code>Hf</code> 是该模型的形成焓参数。</p>
<p>理想气体满足 \(\rho=p/(RT)\)，其中 \(R=R_u/M\)，\(R_u\approx8314.46\,\mathrm{J/(kmol\,K)}\)。本例 \(M=28.9\,\mathrm{kg/kmol}\)，所以 \(R\approx287.70\,\mathrm{J/(kg\,K)}\)。取 100000 Pa 和 300 K，密度约为 \(1.159\,\mathrm{kg/m^3}\)。</p>
<p>常数输运模型的导热系数可由 \(k=\mu C_p/Pr\) 计算，本例约为 \(0.0257\,\mathrm{W/(m\,K)}\)。这也说明温度传热不仅取决于 <code>Cp</code>，还与黏度及 <code>Pr</code> 共同相关。</p>
<p>温度场使用 K，理想气体密度由热力学绝对压力计算。封闭不可压缩系统的压力基准通常在 <code>fvSolution</code> 中通过 <code>pRefCell/pRefValue</code> 等控制；它用于确定压力常数，与本例状态方程中的绝对压力含义不同。</p>
<h3>扩展与排查</h3>
<p>温度范围很宽时，可选择温度相关的输运和比热模型，并提供对应系数。变化后的 \(\mu(T)\) 和 \(C_p(T)\) 会影响动量、导热及温度与能量的转换，适合先在简单边界条件下检查物性曲线。</p>
<p>启动时输出的模型组合和密度范围很有参考价值。若出现非物理温度或密度，先检查压力、温度初值及单位，再检查所选状态方程。多区域算例为各区域分别保存该文件，流体和固体使用各自的物性类型。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · heatTransfer/buoyantPimpleFoam/hotRoom</summary><p>hotRoom 的热浮力计算需要温度、压力与密度相互联系。本文件给空气选择热物性模型。</p>
<ul>
<li><code>heRhoThermo</code>、<code>pureMixture</code> 使用单组分密度型热力学包，能量变量为 <code>sensibleEnthalpy</code>。</li>
<li><code>perfectGas</code> 按理想气体关系计算密度，<code>molWeight 28.9</code> 给出分子量；<code>pRef 100000</code> 提供压力参考。</li>
<li><code>hConst</code> 与 <code>Cp 1000</code> 使用恒定比热，<code>Hf 0</code> 给定焓参考。</li>
<li><code>transport const</code>、<code>mu 1.8e-05</code>、<code>Pr 0.7</code> 使用恒定动力黏度和 Prandtl 数，单位分别为 Pa·s 和无量纲。</li>
</ul>
<p>更换气体时同步修改分子量、比热和输运参数；温度跨度较大时可比较温度相关物性模型。</p>
<p><a href="/assets/examples/v2512/thermophysicalproperties/authored-hotRoom-thermophysicalProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantPimpleFoam/hotRoom/constant/thermophysicalProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantPimpleFoam/hotRoom">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      thermophysicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

thermoType
{
    type            heRhoThermo;
    mixture         pureMixture;
    transport       const;
    thermo          hConst;
    equationOfState perfectGas;
    specie          specie;
    energy          sensibleEnthalpy;
}

pRef            100000;

mixture
{
    specie
    {
        molWeight       28.9;
    }
    thermodynamics
    {
        Cp              1000;
        Hf              0;
    }
    transport
    {
        mu              1.8e-05;
        Pr              0.7;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · heatTransfer/chtMultiRegionFoam/multiRegionHeater</summary><p>这个文件属于 multiRegionHeater 的 heater 固体区，控制固体储热与导热，空气区另有自己的物性。</p>
<ul>
<li><code>heSolidThermo</code> 与 <code>constIso</code> 选择固体、各向同性恒定导热模型。</li>
<li><code>kappa 80</code> 是导热系数，单位 W/(m·K)，决定相同温差下的传热强度。</li>
<li><code>Cp 450</code>、<code>rho 8000</code> 分别给出比热 J/(kg·K) 和密度 kg/m³，乘积决定单位体积的热容量。</li>
<li><code>rhoConst</code> 保持密度不变，<code>sensibleEnthalpy</code> 以显焓表达能量。</li>
</ul>
<p>更换加热体材料时成组修改 kappa、Cp、rho；多区域耦合边界仍需在各区温度文件中设置。</p>
<p><a href="/assets/examples/v2512/thermophysicalproperties/authored-multiRegionHeater-solid-thermophysicalProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/multiRegionHeater/constant/heater/thermophysicalProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/multiRegionHeater">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      thermophysicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

thermoType
{
    type            heSolidThermo;
    mixture         pureMixture;
    transport       constIso;
    thermo          hConst;
    equationOfState rhoConst;
    specie          specie;
    energy          sensibleEnthalpy;
}

mixture
{
    specie
    {
        molWeight   50;
    }
    transport
    {
        kappa   80;
    }
    thermodynamics
    {
        Hf      0;
        Cp      450;
    }
    equationOfState
    {
        rho     8000;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interCondensatingEvaporatingFoam/condensatingVessel</summary><p>冷凝容器在此给出固定饱和温度，供相变模型判断温度相对于饱和状态的位置。</p>
<ul>
<li><code>TSat 367</code> 表示饱和温度为 367 K。</li>
<li>本文件只有这一项，液相与气相的其他热物性需结合配套相属性文件读取。</li>
<li>温度与 TSat 的差值会参与相变源项，因此初始温度和壁温应与之对应。</li>
</ul>
<p>改变工况压力或材料后，应检查固定饱和温度假设是否仍适用，并同步调整相变参数。</p>
<p><a href="/assets/examples/v2512/thermophysicalproperties/1-thermophysicalProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interCondensatingEvaporatingFoam/condensatingVessel/constant/thermophysicalProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interCondensatingEvaporatingFoam/condensatingVessel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      thermophysicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

TSat             367;   // saturation temperature


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 4 · multiphase/compressibleInterDyMFoam/laminar/sloshingTank2D</summary><p>可压缩晃荡水箱在这份总配置中列出两相，并给出压力下限和界面张力。</p>
<ul>
<li><code>phases (water air)</code> 定义相名称，各相热物性与场名需保持对应。</li>
<li><code>pMin 1000</code> 给出压力下限 1000 Pa，用于相关压力处理。</li>
<li><code>sigma 0</code> 在这个算例中忽略界面张力，主要观察晃荡及可压缩效应。</li>
</ul>
<p>研究毛细尺度运动时应恢复合适的 sigma，并检查网格与时间步是否解析界面张力效应。</p>
<p><a href="/assets/examples/v2512/thermophysicalproperties/2-thermophysicalProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/compressibleInterDyMFoam/laminar/sloshingTank2D/constant/thermophysicalProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/compressibleInterDyMFoam/laminar/sloshingTank2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      thermophysicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

phases          (water air);

pMin            1000;

sigma           0;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 5 · multiphase/compressibleInterFoam/laminar/depthCharge3D</summary><p>depthCharge3D 使用水和空气两相描述气体区与周围液体的压力运动。</p>
<ul>
<li><code>phases (water air)</code> 规定两相名称。</li>
<li><code>pMin 10000</code> 设置 10000 Pa 的压力下限；应与预期压力范围和相热物性一致。</li>
<li><code>sigma 0.07</code> 设置界面张力为 0.07 N/m。</li>
</ul>
<p>改变初始气体压力或尺寸时，同时检查两相状态方程、压力范围与界面分辨率。</p>
<p><a href="/assets/examples/v2512/thermophysicalproperties/3-thermophysicalProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/depthCharge3D/constant/thermophysicalProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/depthCharge3D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      thermophysicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

phases          (water air);

pMin            10000;

sigma           0.07;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/rhopimplefoam/">rhoPimpleFoam</a> · <a href="/commands/chtmultiregionfoam/">chtMultiRegionFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
