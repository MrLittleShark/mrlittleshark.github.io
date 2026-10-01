---
title: "constant/transportProperties · transportProperties"
layout: reference
description: "不可压缩牛顿流体的配置如下。求解器可直接读取 nu，也可通过 transportModel 创建输运模型，相应条目采用该求解器的配置结构。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>不可压缩牛顿流体的配置如下。求解器可直接读取 nu，也可通过 transportModel 创建输运模型，相应条目采用该求解器的配置结构。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>constant/transportProperties</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>transportModel</code> · <code>nu</code> · <code>rho</code> · <code>phases</code> · <code>sigma</code></p><h2>关联命令</h2><p><a href="/commands/?q=icoFoam">icoFoam</a> · <a href="/commands/?q=interFoam">interFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary constant/transportProperties -keywords
icoFoam -help</code></pre><h2>9.5 constant/transportProperties</h2><p>不可压缩牛顿流体的配置如下。求解器可直接读取 nu，也可通过 transportModel 创建输运模型，相应条目采用该求解器的配置结构。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object transportProperties;
}
transportModel Newtonian;
nu [0 2 -1 0 0 0 0] 1e-6;</code></pre>
<p>nu 为运动黏度，mu 为动力黏度，两者满足 \(\mu = \rho*\nu\)。powerLaw、BirdCarreau 等非牛顿模型采用各自的系数字典，参数定义见对应模型源码和教程。</p>
<p>不可压缩 VOF 的两相物性配置如下。</p>
<pre><code class="language-openfoam">phases (water air);
water { transportModel Newtonian; nu 1e-6; rho 1000; }
air   { transportModel Newtonian; nu 1.5e-5; rho 1.2; }
sigma 0.072;</code></pre>
<p>rho 表示相密度，sigma 表示表面张力系数。示例数值为常温条件下的近似示例。可压缩多相模型通常分别设置各相热物性。</p>
<h2>18.1 transportProperties（物性）</h2><p>单相不可压</p>
<pre><code class="language-openfoam">transportModel  Newtonian;
nu              [0 2 -1 0 0 0 0] 1e-05;      // 运动粘度 m²/s
// 新版也可以简写（量纲由程序推断）：nu 1e-05;</code></pre>
<p>非牛顿流体可选 CrossPowerLaw、BirdCarreau、HerschelBulkley、powerLaw，各自再跟一个系数子字典。</p>
<p>两相（interFoam）</p>
<pre><code class="language-openfoam">phases (water air);

water { transportModel Newtonian; nu 1e-06; rho 1000; }
air   { transportModel Newtonian; nu 1.48e-05; rho 1; }

sigma  0.07;          // 表面张力系数 N/m</code></pre>
<p>laplacianFoam</p>
<pre><code class="language-openfoam">DT              [0 2 -1 0 0 0 0] 4e-05;      // 扩散系数</code></pre><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>nu</td><td>运动黏度，SI 单位为平方米每秒；它与动力黏度相差一个密度因子。</td></tr><tr><td>phases</td><td>相名称列表；这些名称会影响相分数、速度、热物性等字段或字典的命名。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>sigma</td><td>常见为表面张力系数，但在电磁模型中可表示电导率；以模型与量纲为准。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>transportModel</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/icoFoam/cavity/cavity</h3><p>原始路径：<code>tutorials/incompressible/icoFoam/cavity/cavity/constant/transportProperties</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/constant/transportProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/transportproperties/1-transportProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/nonNewtonianIcoFoam/offsetCylinder</h3><p>原始路径：<code>tutorials/incompressible/nonNewtonianIcoFoam/offsetCylinder/constant/transportProperties</code>；求解器：<code>nonNewtonianIcoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/nonNewtonianIcoFoam/offsetCylinder/constant/transportProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/transportproperties/2-transportProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/nonNewtonianIcoFoam/offsetCylinder">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · multiphase/interFoam/laminar/damBreak/damBreak</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/damBreak/damBreak/constant/transportProperties</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/constant/transportProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/transportproperties/3-transportProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/interfoam/">interFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/transportProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/transportProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
