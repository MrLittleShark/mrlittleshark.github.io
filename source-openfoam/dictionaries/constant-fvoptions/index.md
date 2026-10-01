---
title: "constant/fvOptions · fvOptions"
layout: reference
description: "fvOptions 用于配置源项和约束，文件位置由求解器的读取路径确定，常见于 constant 或 system。下例在指定 cellZone 内施加速度方程源项，采用 sources 条目。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>fvOptions 用于配置源项和约束，文件位置由求解器的读取路径确定，常见于 constant 或 system。下例在指定 cellZone 内施加速度方程源项，采用 sources 条目。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>constant/fvOptions</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>active</code> · <code>selectionMode</code> · <code>cellZone</code> · <code>semiImplicitSource</code> · <code>scalarSemiImplicitSource</code> · <code>vectorSemiImplicitSource</code></p><h2>关联命令</h2><p><a href="/commands/?q=simpleFoam">simpleFoam</a> · <a href="/commands/?q=pimpleFoam">pimpleFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary constant/fvOptions -keywords
simpleFoam -help</code></pre><h2>9.9 constant/fvOptions</h2><p>fvOptions 用于配置源项和约束，文件位置由求解器的读取路径确定，常见于 constant 或 system。下例在指定 cellZone 内施加速度方程源项，采用 sources 条目。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object fvOptions;
}
drive
{
    type vectorSemiImplicitSource;
    active true;
    selectionMode cellZone;
    cellZone heater;
    volumeMode specific;
    sources
    {
        U ((0.1 0 0) 0);
    }
}</code></pre>
<p>半隐式源项写为 Su + Sp*字段，括号内依次给出显式项和隐式系数。specific 按单位体积定义，absolute 按所选体积的总量定义。源项量纲取决于控制方程；速度、动量以及以 h、e 或 T 为变量的能量方程应分别确定量纲和密度因子。</p>
<p>selectionMode 指定作用范围，可选 all、cellZone、cellSet 等；timeStart 和 duration 指定作用时间。常用类型包括 scalarSemiImplicitSource、vectorSemiImplicitSource、meanVelocityForce、explicitPorositySource、scalarFixedValueConstraint、limitTemperature 和 codedSource，其参数按对应模型设置。</p>
<h2>17.4 fvOptions（源项与区域模型）</h2><p>放在 system/fvOptions（或 constant/fvOptions）。它让你不改求解器就能加源项。</p>
<pre><code class="language-openfoam">momentumSource
{
    type            meanVelocityForce;      // 恒定流量驱动（周期性槽道流必用）
    active          yes;
    selectionMode   all;
    fields          (U);
    Ubar            (0.1335 0 0);
}

heatSource
{
    type            scalarSemiImplicitSource;
    active          yes;
    selectionMode   cellZone;
    cellZone        heater;
    volumeMode      absolute;               // absolute / specific
    sources         { h (500 0); }          // (显式部分 隐式部分)
}

porous
{
    type            explicitPorositySource;
    active          yes;
    selectionMode   cellZone;
    cellZone        porousZone;
    type            DarcyForchheimer;
    d   (5e7 -1000 -1000);
    f   (0 0 0);
    coordinateSystem { ... }
}

MRF1
{
    type            MRFSource;             // 旋转参考系（风机、搅拌器）
    selectionMode   cellZone;
    cellZone        rotor;
    origin          (0 0 0);
    axis            (0 0 1);
    omega           constant 104.72;       // rad/s
}</code></pre>
<p>常用类型还有：limitTemperature（限温，防发散）、limitVelocity、fixedTemperatureConstraint、buoyancyEnergy、radiation、solidificationMeltingSource（相变）、atmAmbientTurbSource（大气边界层）。</p>
<p>为什么它重要：初学者遇到”我要在某个区域加个热源/阻力/旋转”，第一反应常是去改求解器源码。用 fvOptions 一个字典就能解决，且不影响可维护性。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>radiation</td><td>辐射计算开关，需与模型、壁面辐射条件及能量方程配合。</td></tr><tr><td>libs</td><td>额外加载的共享库。函数对象或自定义边界未注册时，应检查库名与编译版本。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>viscousDissipation</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses</h3><p>原始路径：<code>tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses/system/fvOptions</code>；求解器：<code>adjointOptimisationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses/system/fvOptions">查看固定版本源码</a> · <a href="/assets/examples/v2512/fvoptions/1-fvOptions.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvOptions;
}
momSource
{
    type topOSource;
    names (U Ua);
    function BorrvallPetersson;
    b 100;
    interpolationField beta;
}</code></pre><h3>示例 2 · combustion/reactingFoam/RAS/SandiaD_LTS</h3><p>原始路径：<code>tutorials/combustion/reactingFoam/RAS/SandiaD_LTS/constant/fvOptions</code>；求解器：<code>reactingFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS/constant/fvOptions">查看固定版本源码</a> · <a href="/assets/examples/v2512/fvoptions/2-fvOptions.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvOptions;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

radiation
{
    type            radiation;
    libs (radiationModels);
}


// ************************************************************************* //</code></pre><h3>示例 3 · compressible/rhoPimpleFoam/RAS/TJunction</h3><p>原始路径：<code>tutorials/compressible/rhoPimpleFoam/RAS/TJunction/constant/fvOptions</code>；求解器：<code>rhoPimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunction/constant/fvOptions">查看固定版本源码</a> · <a href="/assets/examples/v2512/fvoptions/3-fvOptions.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunction">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvOptions;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

viscousDissipation
{
    type            viscousDissipation;
    enabled         true;
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/pimplefoam/">pimpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/fvOptions&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/fvOptions&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
