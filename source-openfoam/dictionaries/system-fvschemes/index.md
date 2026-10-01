---
title: "system/fvSchemes · fvSchemes"
layout: reference
description: "下例给出不可压缩非稳态层流的离散设置。采用湍流模型或求解能量方程时，应补充相应方程的对流项。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>下例给出不可压缩非稳态层流的离散设置。采用湍流模型或求解能量方程时，应补充相应方程的对流项。</p><figure><img src="/assets/diagrams/reference-4.svg" alt="数值方法配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/fvSchemes</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>ddtSchemes</code> · <code>gradSchemes</code> · <code>divSchemes</code> · <code>laplacianSchemes</code> · <code>interpolationSchemes</code> · <code>snGradSchemes</code> · <code>fluxRequired</code> · <code>wallDist</code></p><h2>关联命令</h2><p><a href="/commands/?q=icoFoam">icoFoam</a> · <a href="/commands/?q=interFoam">interFoam</a> · <a href="/commands/?q=simpleFoam">simpleFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/fvSchemes -keywords
icoFoam -help</code></pre><h2>8.2 system/fvSchemes</h2><p>下例给出不可压缩非稳态层流的离散设置。采用湍流模型或求解能量方程时，应补充相应方程的对流项。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object fvSchemes;
}
ddtSchemes { default Euler; }
gradSchemes { default Gauss linear; }
divSchemes
{
    default none;
    div(phi,U) Gauss linearUpwind grad(U);
    div((nuEff*dev2(T(grad(U))))) Gauss linear;
}
laplacianSchemes { default Gauss linear corrected; }
interpolationSchemes { default linear; }
snGradSchemes { default corrected; }
wallDist { method meshWave; }</code></pre>
<div class="table-scroll"><table>
<tr><th>字典</th><th>控制对象</th><th>常用设置</th></tr>
<tr><td>ddtSchemes</td><td>时间导数</td><td>Euler 为一阶；backward 为二阶；CrankNicolson 0.9 为混合格式；steadyState 用于稳态</td></tr>
<tr><td>gradSchemes</td><td>梯度</td><td>Gauss linear、leastSquares、cellLimited Gauss linear 1</td></tr>
<tr><td>divSchemes</td><td>对流及显式散度</td><td>Gauss upwind 耗散较强；linearUpwind 阶数较高；limitedLinear 等限制格式按字段类型选择</td></tr>
<tr><td>laplacianSchemes</td><td>扩散项</td><td>常用 Gauss linear corrected；非正交程度较高时可采用 limited 修正</td></tr>
<tr><td>interpolationSchemes</td><td>面插值</td><td>linear 等</td></tr>
<tr><td>snGradSchemes</td><td>面法向梯度</td><td>corrected、uncorrected、limited 0.5 等</td></tr>
<tr><td>fluxRequired</td><td>指定需保留通量的场</td><td>按求解器要求标记 p 等场</td></tr>
<tr><td>wallDist</td><td>壁距算法</td><td>meshWave 等</td></tr>
<tr><td>default none</td><td>无默认格式</td><td>所需离散项必须显式配置，缺失时报告错误</td></tr>
</table></div>
<p>湍流方程可采用 div(phi,k) Gauss upwind; 和 div(phi,omega) Gauss upwind;，字段名称随模型确定。VOF 求解器的 div(phi,alpha)、div(phirb,alpha) 等条目采用其配套教程的定义。rhoCentralFoam 还需设置 fluxScheme 及变量重构格式。</p>
<h2>补充说明</h2><p>它管什么：每一项微分算子用什么数值格式离散。这是精度与稳定性的主要旋钮，也是初学者最容易被卡住的地方。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>method</td><td>所采用的分区、插值或模型方法；含义由该字典的读取程序决定。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>ddtSchemes</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/icoFoam/cavity/cavity</h3><p>原始路径：<code>tutorials/incompressible/icoFoam/cavity/cavity/system/fvSchemes</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/fvSchemes">查看固定版本源码</a> · <a href="/assets/examples/v2512/fvschemes/1-fvSchemes.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/simpleFoam/pitzDaily</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/pitzDaily/system/fvSchemes</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/system/fvSchemes">查看固定版本源码</a> · <a href="/assets/examples/v2512/fvschemes/2-fvSchemes.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    div(phi,k)      &#36;turbulence;
    div(phi,epsilon) &#36;turbulence;
    div(phi,omega)  &#36;turbulence;

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


// ************************************************************************* //</code></pre><h3>示例 3 · multiphase/interFoam/laminar/damBreak/damBreak</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system/fvSchemes</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system/fvSchemes">查看固定版本源码</a> · <a href="/assets/examples/v2512/fvschemes/3-fvSchemes.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/interfoam/">interFoam</a> · <a href="/commands/simplefoam/">simpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/fvSchemes&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/fvSchemes&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>找不到离散项或场求解器</td><td>把错误中的完整键名与 fvSchemes / fvSolution 对照，注意 div(phi,U) 等键的精确拼写。</td></tr><tr><td>残差下降但目标量漂移</td><td>同时监测守恒误差、力或流量，并分别检查时间步与网格敏感性。</td></tr><tr><td>非正交修正导致成本增加</td><td>优先改善网格；增加修正次数不是无条件提高精度的办法。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
