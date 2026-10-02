---
title: "turbulenceProperties"
layout: reference
description: "选择层流、RAS 或 LES，并设置湍流模型及其系数。"
dictionary: true
cms_slug: "dictionary-turbulenceproperties"
---

<p>选择层流、RAS 或 LES，并设置湍流模型及其系数。</p><p>位置：<code>constant/turbulenceProperties</code></p><figure class="wolf-figure"><img src="/assets/wolf/wolf-turbulence-model-hierarchy.png" alt="RANS、LES 与 DNS 的解析范围" loading="lazy"><figcaption><strong>RANS、LES 与 DNS 的解析范围</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 26</small></figcaption></figure><h2>turbulenceProperties 选择层流或湍流模型</h2>
<p>在使用相应湍流模型接口的求解器中，<code>constant/turbulenceProperties</code> 选择层流、RANS 或 LES。模型改变后，需要的初始场、边界条件和离散方程也会变化。</p>
<h3>使用 k–epsilon 模型</h3>
<p>下面是 <code>simpleFoam/pitzDaily</code> 的配置主体：</p>
<pre><code class="language-foam">simulationType RAS;
RAS
{
    RASModel    kEpsilon;
    turbulence  on;
    printCoeffs on;
}
</code></pre>
<p><code>simulationType RAS</code> 选择雷诺平均模型族，<code>RASModel kEpsilon</code> 选择标准 \(k\)–\(\epsilon\) 模型。<code>turbulence on</code> 启用湍流计算，<code>printCoeffs on</code> 在启动时输出模型系数，方便了解默认设置。</p>
<p>\(k\) 是湍动能，单位为 \(\mathrm{m^2/s^2}\)；\(\epsilon\) 是耗散率，单位为 \(\mathrm{m^2/s^3}\)。相应算例需要 <code>0/k</code>、<code>0/epsilon</code> 和湍流运动黏度 <code>0/nut</code> 等输入，<code>fvSchemes</code> 和 <code>fvSolution</code> 也要配置相关方程。</p>
<h3>入口湍流量的量级</h3>
<p>已知平均速度 \(U\)、湍流强度 \(I\) 和长度尺度 \(\ell\)，常用估计为</p>
<p>\[
k=\frac32(UI)^2,\qquad
\epsilon=C_\mu^{3/4}\frac{k^{3/2}}{\ell}.
\]</p>
<p>例如 \(U=10\,\mathrm{m/s}\)、\(I=0.05\)、\(\ell=0.01\,\mathrm m\)，取 \(C_\mu=0.09\)，得到 \(k=0.375\,\mathrm{m^2/s^2}\)、\(\epsilon\approx3.77\,\mathrm{m^2/s^3}\)。长度尺度越小，对应的耗散率越高。</p>
<p>这些估计适合在缺少更详细入口数据时设置合理量级；有实验或上游计算剖面时，可直接采用对应分布。</p>
<h3>改为 kOmegaSST</h3>
<p>在同一个 <code>RAS</code> 子字典中替换模型名：</p>
<pre><code class="language-foam">RASModel kOmegaSST;
</code></pre>
<p>随后准备 <code>k</code>、<code>omega</code> 和 <code>nut</code> 的初始与边界条件，更新两份数值字典中对应场名。<code>omega</code> 的单位为 \(\mathrm{s^{-1}}\)。近壁单元高度与壁面处理共同影响结果，因此更换模型后应检查 \(y^+\) 和壁面条件。</p>
<h3>使用层流或 LES</h3>
<p>选择层流时，主体可简化为：</p>
<pre><code class="language-foam">simulationType laminar;
</code></pre>
<p>分子黏性仍由物性文件提供。LES 则使用 <code>simulationType LES</code> 和相应 <code>LES</code> 子字典，指定亚格子模型与滤波尺度模型。LES 还需要三维非定常网格、足够的时间分辨率和统计采样时长，计算目标通常是瞬态结构及其统计量。</p>
<p>参数调整可从默认系数开始。有物理或文献依据时再覆盖具体模型的系数，并将变化对应到压降、分离位置或壁面量，避免只根据残差曲线挑选模型。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/simpleFoam/pitzDaily</summary><p>pitzDaily 的后台阶剪切层按 RANS 平均流动建模。</p>
<ul>
<li><code>simulationType RAS</code> 选择雷诺平均湍流模型。</li>
<li><code>RASModel kEpsilon</code> 求解湍动能 k 和耗散率 epsilon，两者需要配套初值与边界条件。</li>
<li><code>turbulence on</code> 启用湍流贡献，<code>printCoeffs on</code> 在日志中打印模型系数。</li>
</ul>
<p>改成 kOmegaSST 等模型时同步准备对应字段、壁面条件和网格，而不只是替换模型名称。</p>
<p><a href="/assets/examples/v2512/turbulenceproperties/1-turbulenceProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/constant/turbulenceProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      turbulenceProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

simulationType      RAS;

RAS
{
    // Tested with kEpsilon, realizableKE, kOmega, kOmegaSST,
    // ShihQuadraticKE, LienCubicKE.
    RASModel        kEpsilon;

    turbulence      on;

    printCoeffs     on;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel</summary><p>surfaceMountedCube 的 initChannel 是入口流动准备阶段，尽管上层目录为 LES，这个具体阶段采用 RAS。</p>
<ul>
<li><code>simulationType RAS</code> 是本文件的实际选择。</li>
<li><code>RASModel LaunderSharmaKE</code> 使用低 Reynolds 数 k–epsilon 模型，需与近壁网格及边界设置配套。</li>
<li><code>turbulence on</code> 开启模型，<code>printCoeffs on</code> 输出系数供检查。</li>
</ul>
<p>切换到完整 LES 计算时使用 fullCase 的模型和初始场配置；阶段用途应由当前文件确认。</p>
<p><a href="/assets/examples/v2512/turbulenceproperties/2-turbulenceProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel/constant/turbulenceProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      turbulenceProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

simulationType      RAS;

RAS
{
    RASModel        LaunderSharmaKE;

    turbulence      on;

    printCoeffs     on;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · basic/simpleFoam/implicitAMI</summary><p>implicitAMI 示例在此选择层流模式，主要配置重点在网格接口而非湍流闭合。</p>
<ul>
<li><code>simulationType laminar</code> 让求解器按层流输运处理。</li>
<li>文件没有启用 RAS 或 LES 子模型，因此没有由本设置引入的湍流输运方程。</li>
<li>流体分子黏度仍由物性文件给出。</li>
</ul>
<p>增加流速或改变几何后，应结合 Reynolds 数和物理现象重新选择模型，并准备相应字段。</p>
<p><a href="/assets/examples/v2512/turbulenceproperties/3-turbulenceProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/basic/simpleFoam/implicitAMI/constant/turbulenceProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/basic/simpleFoam/implicitAMI">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      turbulenceProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

simulationType laminar;

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/pimplefoam/">pimpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
