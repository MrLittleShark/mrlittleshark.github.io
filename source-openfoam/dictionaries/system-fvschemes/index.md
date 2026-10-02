---
title: "fvSchemes"
layout: reference
description: "选择时间导数、梯度、散度、拉普拉斯项和面插值的离散格式。"
dictionary: true
cms_slug: "dictionary-fvschemes"
---

<p>选择时间导数、梯度、散度、拉普拉斯项和面插值的离散格式。</p><p>位置：<code>system/fvSchemes</code></p><figure class="wolf-figure"><img src="/assets/wolf/wolf-advection-profile-errors.png" alt="一维输运中的格式误差曲线" loading="lazy"><figcaption><strong>一维输运中的格式误差曲线</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 157</small></figcaption></figure><h2>fvSchemes 决定方程怎样离散</h2>
<p><code>system/fvSchemes</code> 为时间导数、梯度、对流和扩散分别选择数值格式。求解器负责建立哪些方程，字典负责指定这些算子的离散方法。</p>
<p>以下是均匀正交方腔可用的一组设置，放在 <code>FoamFile</code> 文件头之后：</p>
<pre><code class="language-foam">ddtSchemes
{
    default Euler;
}
gradSchemes
{
    default Gauss linear;
}
divSchemes
{
    default none;
    div(phi,U) Gauss linear;
}
laplacianSchemes
{
    default Gauss linear orthogonal;
}
interpolationSchemes
{
    default linear;
}
snGradSchemes
{
    default orthogonal;
}
</code></pre>
<table>
<thead>
<tr>
<th>子字典</th>
<th>对应计算</th>
<th>本例的含义</th>
</tr>
</thead>
<tbody><tr>
<td><code>ddtSchemes</code></td>
<td>时间导数</td>
<td><code>Euler</code>：一阶隐式时间离散</td>
</tr>
<tr>
<td><code>gradSchemes</code></td>
<td>单元梯度</td>
<td><code>Gauss linear</code>：面插值后进行 Gauss 求和</td>
</tr>
<tr>
<td><code>divSchemes</code></td>
<td>散度，常用于对流</td>
<td><code>div(phi,U)</code>：速度对流项</td>
</tr>
<tr>
<td><code>laplacianSchemes</code></td>
<td>扩散型算子</td>
<td>面系数线性插值，加正交法向梯度</td>
</tr>
<tr>
<td><code>interpolationSchemes</code></td>
<td>单元场到面场插值</td>
<td>默认线性插值</td>
</tr>
<tr>
<td><code>snGradSchemes</code></td>
<td>面法向梯度</td>
<td>使用正交中心差分</td>
</tr>
</tbody></table>
<p><code>default</code> 指定该类算子的默认方法；写出 <code>grad(U)</code> 或 <code>div(phi,T)</code> 等专门条目后，对应算子使用专门设置。<code>divSchemes/default none</code> 让漏写的对流项显式报错，便于确认每个方程采用什么格式。</p>
<h3>对流格式怎么替换</h3>
<p>下面三行是可替换的选择，在同一个字典中保留其中一行：</p>
<pre><code class="language-foam">// 迎风
 div(phi,U) Gauss upwind;
// 线性迎风
 div(phi,U) Gauss linearUpwind grad(U);
// 受限制的线性插值
 div(phi,U) Gauss limitedLinearV 1;
</code></pre>
<p><code>upwind</code> 取上游值，通常较稳健但数值扩散明显。<code>linearUpwind</code> 利用上游梯度改善面值，<code>grad(U)</code> 指向梯度设置。<code>limitedLinearV</code> 对向量场施加限制；标量温度可使用 <code>div(phi,T) Gauss limitedLinear 1;</code>。</p>
<p>修改键名时与求解器源码对应。例如 <code>fvm::div(phi,T)</code> 查找 <code>div(phi,T)</code>，修改 <code>div(phi,U)</code> 对这个标量方程没有作用。</p>
<h3>非正交网格的扩散项</h3>
<p>对于非正交网格，通常将两个法向梯度设置一起调整为：</p>
<pre><code class="language-foam">laplacianSchemes
{
    default Gauss linear corrected;
}
snGradSchemes
{
    default corrected;
}
</code></pre>
<p><code>corrected</code> 通过重建梯度补充中心连线与面法向之间的差别。修正项较大时，可以研究受限修正并改善网格。增加 <code>fvSolution</code> 的非正交校正次数，则让显式修正使用更新后的场。</p>
<h3>稳态与瞬态</h3>
<p>稳态求解使用 <code>steadyState</code>；瞬态可选择 <code>Euler</code>、<code>backward</code> 或带偏心参数的 <code>CrankNicolson</code>。对流格式、时间格式和步长分别影响误差。比较时保留其他参数，先看峰值、积分量和剖面，再决定是否需要进一步细化网格或减小时间步。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/icoFoam/cavity/cavity</summary><p>方腔使用单一、正交的六面体块网格。<code>fvSchemes</code> 把连续方程中的时间导数、对流项和扩散项分别对应到离散格式。</p>
<ul>
<li><code>ddtSchemes/default Euler</code> 使用一阶隐式时间离散，配合 <code>controlDict</code> 的 0.005 s 步长推进非定常流动。</li>
<li><code>div(phi,U) Gauss linear</code> 用高斯积分与线性面插值离散速度对流；本例低 Reynolds 数且网格规整，适合观察中心插值的基本行为。</li>
<li><code>gradSchemes</code> 中的 <code>Gauss linear</code> 计算压力等场的梯度，<code>interpolationSchemes/default linear</code> 提供默认面插值。</li>
<li><code>laplacianSchemes/default Gauss linear orthogonal</code> 和 <code>snGradSchemes/default orthogonal</code> 使用正交网格对应的法向梯度处理。</li>
<li><code>divSchemes/default none</code> 要求为实际使用的对流项明确给出格式，漏项时会报告缺少配置。</li>
</ul>
<p>若将网格改为明显非正交网格，应检查 Laplacian 与法向梯度修正方式。改变时间精度时，同时比较时间步；空间格式、时间格式和步长共同决定离散误差。</p>
<p><a href="/assets/examples/v2512/fvschemes/1-fvSchemes.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/fvSchemes">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvSchemes;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

ddtSchemes
{
    default         Euler;
}

gradSchemes
{
    default         Gauss linear;
    grad(p)         Gauss linear;
}

divSchemes
{
    default         none;
    div(phi,U)      Gauss linear;
}

laplacianSchemes
{
    default         Gauss linear orthogonal;
}

interpolationSchemes
{
    default         linear;
}

snGradSchemes
{
    default         orthogonal;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/simpleFoam/pitzDaily</summary><p>后台阶流动包含剪切层与回流区，<code>pitzDaily</code> 为稳态速度和湍流输运选择不同的对流格式。</p>
<ul>
<li><code>ddtSchemes/default steadyState</code> 取消瞬态导数，配合 <code>simpleFoam</code> 求稳态解。</li>
<li><code>div(phi,U) bounded Gauss linearUpwind grad(U)</code> 用带梯度重构的迎风格式求速度对流；<code>grad(U)</code> 指定重构所用的梯度条目。</li>
<li><code>turbulence bounded Gauss limitedLinear 1</code> 为湍流变量提供受限格式，后面的 <code>div(phi,k)</code>、<code>div(phi,epsilon)</code> 等通过 <code>$turbulence</code> 复用它。</li>
<li><code>laplacianSchemes/default Gauss linear corrected</code> 与 <code>snGradSchemes/default corrected</code> 对非正交性作修正，适应多块网格的几何特征。</li>
<li><code>wallDist/method meshWave</code> 指定到壁面距离的计算方法，壁面距离会被有关湍流模型使用。</li>
</ul>
<p>加大入口速度或降低黏度后，剪切层会更难解析。可先比较网格细化和对流格式对回流长度的影响，再调整限制强度；求解残差很小仍可能伴随空间离散误差。</p>
<p><a href="/assets/examples/v2512/fvschemes/2-fvSchemes.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/system/fvSchemes">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvSchemes;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

ddtSchemes
{
    default         steadyState;
}

gradSchemes
{
    default         Gauss linear;
}

divSchemes
{
    default         none;

    div(phi,U)      bounded Gauss linearUpwind grad(U);

    turbulence      bounded Gauss limitedLinear 1;
    div(phi,k)      $turbulence;
    div(phi,epsilon) $turbulence;
    div(phi,omega)  $turbulence;

    div(nonlinearStress) Gauss linear;
    div((nuEff*dev2(T(grad(U))))) Gauss linear;
}

laplacianSchemes
{
    default         Gauss linear corrected;
}

interpolationSchemes
{
    default         linear;
}

snGradSchemes
{
    default         corrected;
}

wallDist
{
    method          meshWave;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interFoam/laminar/damBreak/damBreak</summary><p>溃坝的相分数决定水和空气的分布，动量方程还要使用随相分数变化的密度。本文件因此同时配置了动量输运和界面输运。</p>
<ul>
<li><code>ddtSchemes/default Euler</code> 采用一阶隐式时间格式，步长由 <code>controlDict</code> 的 Courant 限制调整。</li>
<li><code>div(rhoPhi,U) Gauss linearUpwind grad(U)</code> 用质量通量 <code>rhoPhi</code> 输运速度，体现两相密度不同。</li>
<li><code>div(phi,alpha) Gauss vanLeer</code> 用 van Leer 限制插值处理体积分数的对流，兼顾界面分辨率与变化区域的稳定性。</li>
<li><code>div(phirb,alpha) Gauss linear</code> 对应界面压缩通量项；压缩强度还由 <code>fvSolution</code> 中的 <code>cAlpha</code> 控制。</li>
<li><code>laplacianSchemes/default Gauss linear corrected</code> 与 <code>snGradSchemes/default corrected</code> 配合处理扩散项的非正交修正。</li>
</ul>
<p>界面过于弥散时，同时检查网格、时间步与压缩设置。比较时固定其他条件，并观察水体积和 <code>alpha.water</code> 的范围；只更换一个格式名称不足以判断整个界面算法的表现。</p>
<p><a href="/assets/examples/v2512/fvschemes/3-fvSchemes.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system/fvSchemes">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvSchemes;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

ddtSchemes
{
    default         Euler;
}

gradSchemes
{
    default         Gauss linear;
}

divSchemes
{
    div(rhoPhi,U)   Gauss linearUpwind grad(U);
    div(phi,alpha)  Gauss vanLeer;
    div(phirb,alpha) Gauss linear;
    div(((rho*nuEff)*dev2(T(grad(U))))) Gauss linear;
}

laplacianSchemes
{
    default         Gauss linear corrected;
}

interpolationSchemes
{
    default         linear;
}

snGradSchemes
{
    default         corrected;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/interfoam/">interFoam</a> · <a href="/commands/simplefoam/">simpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>找不到离散项或场求解器</td><td>把错误中的完整键名与 fvSchemes / fvSolution 对照，注意 div(phi,U) 等键的精确拼写。</td></tr><tr><td>残差下降但目标量漂移</td><td>同时监测守恒误差、力或流量，并分别检查时间步与网格敏感性。</td></tr><tr><td>非正交修正导致成本增加</td><td>优先改善网格；增加修正次数其作用随网格质量和解的光滑程度变化，可通过细化对比评估。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
