---
title: "SRFProperties"
layout: reference
description: "为单旋转参考系模型设置旋转中心、轴向和转速。SRF 求解器通常求解相对速度 Urel。"
dictionary: true
cms_slug: "dictionary-srfproperties"
---

<p>为单旋转参考系模型设置旋转中心、轴向和转速。SRF 求解器通常求解相对速度 Urel。</p><p>位置：<code>constant/SRFProperties</code></p><h2>SRFProperties 定义单一旋转参考系</h2>
<p>SRF（Single Rotating Frame）在整个计算域使用同一个旋转参考系。<code>SRFSimpleFoam</code> 以相对速度 <code>Urel</code> 求解流动，适合可以在统一旋转坐标系中描述的稳态问题。</p>
<p>以下是 <code>constant/SRFProperties</code> 的配置主体，取自 v2512 的 <code>SRFSimpleFoam/mixer</code>：</p>
<pre><code class="language-foam">SRFModel rpm;
origin (0 0 0);
axis (0 0 1);
rpmCoeffs
{
    rpm 1000;
}
</code></pre>
<p><code>SRFModel rpm</code> 选择按每分钟转数给定转速的模型，<code>rpm 1000</code> 就是 1000 r/min。<code>origin</code> 和 <code>axis</code> 分别定义转轴的位置及方向。程序将转速转换为角速度向量，用于旋转坐标系的惯性项。</p>
<h3>相对速度与绝对速度</h3>
<p>二者满足</p>
<p>\[
\mathbf U_{\mathrm{abs}}=\mathbf U_{\mathrm{rel}}+
\boldsymbol\Omega\times(\mathbf r-\mathbf r_0).
\]</p>
<p>在半径 0.1 m、转速 1000 r/min 处，参考系切向速度约为 10.47 m/s。随参考系一起旋转的壁面相对速度为零；绝对静止的外壁，在旋转系中具有方向相反的切向速度。</p>
<p>这一区别也体现在 <code>0/Urel</code> 的边界条件中。下面是一个绝对静止外壁的片段，应放入该场的 <code>boundaryField</code>，patch 名按实际网格调整：</p>
<pre><code class="language-foam">outerWall
{
    type SRFVelocity;
    inletValue uniform (0 0 0);
    relative no;
    value uniform (0 0 0);
}
</code></pre>
<p><code>relative no</code> 表示 <code>inletValue</code> 用绝对坐标系解释，边界条件负责转换为相对速度。最后的 <code>value</code> 提供初始化值，随后由边界条件更新。与转子一起旋转的壁面，则可在相对速度场中采用 <code>noSlip</code>。</p>
<h3>与 MRF 的配置差别</h3>
<p>SRF 使用全域单一参考系，文件中直接给出 <code>SRFModel</code>、转轴和 <code>rpmCoeffs</code>。MRF 将参考系作用于指定 <code>cellZone</code>，可在一个域内定义多个旋转区域，因此其配置采用 <code>MRF1 { cellZone ...; omega ...; }</code> 的结构。</p>
<p>选择 SRF 后，还需要使用支持 <code>Urel</code> 的求解器及完整场文件。后处理时区分相对速度与绝对速度，叶轮附近流线、入口速度和外壁运动应在同一坐标系下解释。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/SRFSimpleFoam/mixer</summary><p>SRFSimpleFoam 的 mixer 算例在单一旋转参考系中求稳态流动。</p>
<ul>
<li><code>SRFModel rpm</code> 选择用转每分钟输入转速的模型。</li>
<li><code>origin (0 0 0)</code>、<code>axis (0 0 1)</code> 定义转轴。</li>
<li><code>rpmCoeffs/rpm 1000</code> 对应约 104.72 rad/s，单位与 MRF 的 omega 写法不同。</li>
</ul>
<p>改变转速时修改 rpm，并结合求解器使用的相对速度和壁面条件解释输出。</p>
<p><a href="/assets/examples/v2512/srfproperties/1-SRFProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/SRFSimpleFoam/mixer/constant/SRFProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/SRFSimpleFoam/mixer">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      SRFProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

SRFModel        rpm;

origin          (0 0 0);
axis            (0 0 1);

rpmCoeffs
{
    rpm         1000;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/SRFPimpleFoam/rotor2D</summary><p>SRFPimpleFoam 的 rotor2D 用单一旋转参考系计算非定常流动。</p>
<ul>
<li>模型为 <code>rpm</code>，转轴通过原点并沿 z。</li>
<li><code>rpm 60</code> 表示每分钟 60 转，即每秒一转。</li>
<li>旋转参考系的速度变量需与相对速度边界条件保持一致。</li>
</ul>
<p>提高转速时检查时间分辨率，并按实际边界是否随转子运动设置速度条件。</p>
<p><a href="/assets/examples/v2512/srfproperties/2-SRFProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/SRFPimpleFoam/rotor2D/constant/SRFProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/SRFPimpleFoam/rotor2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      SRFProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

SRFModel        rpm;

origin          (0 0 0);
axis            (0 0 1);

rpmCoeffs
{
    rpm             60;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/srfsimplefoam/">SRFSimpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
