---
title: "transportProperties"
layout: reference
description: "配置运动黏度、输运模型或两相物性；具体结构由求解器读取的模型决定。"
dictionary: true
cms_slug: "dictionary-transportproperties"
---

<p>配置运动黏度、输运模型或两相物性；具体结构由求解器读取的模型决定。</p><p>位置：<code>constant/transportProperties</code></p><h2>transportProperties 保存不可压缩物性</h2>
<p><code>constant/transportProperties</code> 常用于不可压缩求解器中的黏度或标量扩散系数。字段名称和模型结构取决于求解器读取的物性类。</p>
<h3>牛顿流体</h3>
<p>采用 <code>singlePhaseTransportModel</code> 的不可压缩求解器，例如 <code>simpleFoam</code>，可在标准文件头之后使用：</p>
<pre><code class="language-foam">transportModel Newtonian;
nu [0 2 -1 0 0 0 0] 1e-6;
</code></pre>
<p><code>Newtonian</code> 指定牛顿黏性模型，<code>nu</code> 是运动黏度，单位为 \(\mathrm{m^2/s}\)。七个量纲指数依次表示质量、长度、时间、温度、物质的量、电流和发光强度。</p>
<p>动力黏度 \(\mu\) 与运动黏度的关系为 \(\nu=\mu/\rho\)。例如 \(\mu=0.001\,\mathrm{Pa\,s}\)、\(\rho=1000\,\mathrm{kg/m^3}\) 时，\(\nu=10^{-6}\,\mathrm{m^2/s}\)。将动力黏度的数值直接填进 <code>nu</code> 会使黏性尺度改变三个数量级。</p>
<p>基础 <code>icoFoam</code> 直接读取 <code>nu</code>，其方腔文件只需对应黏度条目。对固定速度和长度，黏度越小，雷诺数 \(Re=UL/\nu\) 越大，网格与时间分辨率需求也可能提高。</p>
<h3>标量扩散</h3>
<p><code>laplacianFoam</code> 和 <code>scalarTransportFoam</code> 使用 <code>DT</code>，其主体配置可写为：</p>
<pre><code class="language-foam">DT [0 2 -1 0 0 0 0] 1e-5;
</code></pre>
<p>若 <code>T</code> 表示温度，<code>DT</code> 是热扩散率 \(k/(\rho c_p)\)；如果是一般被动标量，它是相应的扩散系数。在 <code>scalarTransportFoam</code> 中设 <code>DT=0</code> 可研究纯对流；在 <code>laplacianFoam</code> 中增大 <code>DT</code> 会加快温度扩散。</p>
<p>对于两端固定温度的均匀一维杆，稳态温度直线与常数 <code>DT</code> 的大小无关；达到稳态的时间尺度约为 \(L^2/DT\)。因此，改变 <code>DT</code> 后要分别看稳态分布与瞬态演化。</p>
<h3>扩展到非牛顿流体</h3>
<p>非牛顿模型使有效运动黏度随剪切率等量变化。修改时需要同时指定 <code>transportModel</code> 和所选模型的系数子字典，并检查系数的单位及上下限。可从 v2512 中使用相同模型的完整教程出发，避免将牛顿流体的单一 <code>nu</code> 当作全部输入。</p>
<p>查看当前值可运行：</p>
<pre><code class="language-bash">foamDictionary constant/transportProperties -entry nu -value
</code></pre>
<p>对于标量例子，将 <code>nu</code> 换成 <code>DT</code>。修改物性后同时记录雷诺数或扩散时间尺度，能更直接理解流场为何变化。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/icoFoam/cavity/cavity</summary><p>方腔只有一个牛顿流体，<code>icoFoam</code> 直接从这里读取运动黏度。</p>
<ul>
<li><code>nu 0.01</code> 的单位为 \(\mathrm{m^2/s}\)，用于动量方程中的黏性扩散。</li>
<li>配套顶盖速度为 1 m/s、腔长为 0.1 m，因此 \(Re=UL/\nu=10\)，黏性作用明显，适合观察层流回流结构。</li>
<li>这个短字典采用求解器已知的参数量纲；运动黏度与动力黏度的关系为 \(\mu=\rho\nu\)。</li>
</ul>
<p>想考察较高 Reynolds 数，可减小 <code>nu</code>，同时检查网格和时间步是否能够解析更薄的剪切层。例如改成 <code>0.001</code>，其余条件不变时 \(Re=100\)。</p>
<p><a href="/assets/examples/v2512/transportproperties/1-transportProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/constant/transportProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      transportProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

nu              0.01;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/nonNewtonianIcoFoam/offsetCylinder</summary><p>偏置圆柱算例选择 CrossPowerLaw 描述剪切率相关运动黏度。</p>
<ul>
<li><code>transportModel CrossPowerLaw</code> 决定当前生效的模型，读取 CrossPowerLawCoeffs。</li>
<li><code>nu0 0.01</code>、<code>nuInf 10</code> 分别给定低剪切率与高剪切率极限黏度，单位 m²/s；本组数值表现为随剪切变化显著增黏。</li>
<li><code>m 0.4</code>、<code>n 3</code> 控制过渡尺度和曲线形状，需要结合模型关系读取。</li>
<li>BirdCarreauCoeffs 虽然也在文件中，当前未被 transportModel 选中。</li>
</ul>
<p>拟合新材料时先对照黏度—剪切率数据确定系数，再检查算例剪切率是否落在拟合范围。</p>
<p><a href="/assets/examples/v2512/transportproperties/2-transportProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/nonNewtonianIcoFoam/offsetCylinder/constant/transportProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/nonNewtonianIcoFoam/offsetCylinder">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      transportProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

transportModel  CrossPowerLaw;

CrossPowerLawCoeffs
{
    nu0         0.01;
    nuInf       10;
    m           0.4;
    n           3;
}

BirdCarreauCoeffs
{
    nu0         1e-06;
    nuInf       1e-06;
    k           0;
    n           1;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interFoam/laminar/damBreak/damBreak</summary><p>溃坝中的水、空气都按不可压缩牛顿流体处理，但密度和黏度分别给定；体积分数用于计算混合物性质。</p>
<ul>
<li><code>phases (water air)</code> 声明两相名称，需与 <code>alpha.water</code> 等字段和配套模型一致。</li>
<li>水的 <code>nu 1e-6</code>、<code>rho 1000</code> 分别是运动黏度 \(10^{-6}\,\mathrm{m^2/s}\) 和密度 \(1000\,\mathrm{kg/m^3}\)。</li>
<li>空气的 <code>nu 1.48e-5</code>、<code>rho 1</code> 使用同样单位。两相的密度差进入重力与压力作用，影响水柱塌落。</li>
<li>两个 <code>transportModel Newtonian</code> 表示黏度按常数牛顿流体模型处理。</li>
<li><code>sigma 0.07</code> 是界面张力系数，单位 N/m，用于界面曲率产生的表面张力。</li>
</ul>
<p>更换为油水等流体组合时，应成组修改两相名称、密度、运动黏度和界面张力，并对应更新初始体积分数字段。尺度减小时，界面张力相对于重力的影响会增强。</p>
<p><a href="/assets/examples/v2512/transportproperties/3-transportProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/constant/transportProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      transportProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

phases          (water air);

water
{
    transportModel  Newtonian;
    nu              1e-06;
    rho             1000;
}

air
{
    transportModel  Newtonian;
    nu              1.48e-05;
    rho             1;
}

sigma            0.07;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/interfoam/">interFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
