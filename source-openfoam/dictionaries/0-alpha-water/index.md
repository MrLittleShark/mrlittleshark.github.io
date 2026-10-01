---
title: "0/alpha.water · alpha.water"
layout: reference
description: "温度场 T 采用温度量纲，初值示例为 internalField uniform 300;。等温壁面使用 fixedValue，绝热壁面通常使用 zeroGradient。externalWallHeatFluxTemperature 可指定热通量或功率，并通过 mode、kappaMethod 等参数定义施加方式和导热率来源。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>温度场 T 采用温度量纲，初值示例为 internalField uniform 300;。等温壁面使用 fixedValue，绝热壁面通常使用 zeroGradient。externalWallHeatFluxTemperature 可指定热通量或功率，并通过 mode、kappaMethod 等参数定义施加方式和导热率来源。</p><figure><img src="/assets/diagrams/reference-2.svg" alt="初始场配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>0/alpha.water</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dimensions</code> · <code>internalField</code> · <code>boundaryField</code> · <code>inletOutlet</code> · <code>constantAlphaContactAngle</code> · <code>dynamicAlphaContactAngle</code> · <code>theta0</code> · <code>limit</code></p><h2>关联命令</h2><p><a href="/commands/?q=interFoam">interFoam</a> · <a href="/commands/?q=interIsoFoam">interIsoFoam</a> · <a href="/commands/?q=setFields">setFields</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary 0/alpha.water -keywords
interFoam -help</code></pre><h2>9.3 温度场与多相流场</h2><p>温度场 T 采用温度量纲，初值示例为 internalField uniform 300;。等温壁面使用 fixedValue，绝热壁面通常使用 zeroGradient。externalWallHeatFluxTemperature 可指定热通量或功率，并通过 mode、kappaMethod 等参数定义施加方式和导热率来源。</p>
<p>p_rgh 表示扣除静水压项后的压力，常见定义为 \(p_{\mathrm{rgh}}=p-\rho gh\)。参考高度和量纲由求解器确定，不可压缩 Boussinesq 模型可采用归一化形式。恢复实际压力时，应按该求解器的定义还原静水压项。</p>
<p>alpha.water 表示水相体积分数，为无量纲量，取值范围为 [0,1]；多相体系中各相体积分数之和为 1。入口可指定相分数，开放边界可采用 inletOutlet，壁面可采用 zeroGradient 或接触角条件。字段后缀 water 与 phases 中的相名对应。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>dimensions</td><td>七个指数依次表示质量、长度、时间、温度、物质量、电流、发光强度。量纲错误常在矩阵组装或赋值时暴露。</td></tr><tr><td>internalField</td><td>初始内部场，可使用 uniform 或 nonuniform。uniform 不表示求解过程始终空间均匀。</td></tr><tr><td>boundaryField</td><td>按网格 patch 名称设置边界条件；名称必须与 polyMesh/boundary 一致，类型还受网格边界类型约束。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · multiphase/interFoam/laminar/sloshingTank3D</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/sloshingTank3D/0.orig/alpha.water</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/sloshingTank3D/0.orig/alpha.water">查看固定版本源码</a> · <a href="/assets/examples/v2512/alpha-water/1-alpha.water.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/sloshingTank3D">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       volScalarField;
    object      alpha.water;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 0 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    walls
    {
        type            zeroGradient;
    }
}


// ************************************************************************* //</code></pre><h3>示例 2 · multiphase/interIsoFoam/sphereInReversedVortexFlow</h3><p>原始路径：<code>tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow/0.orig/alpha.water</code>；求解器：<code>interIsoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow/0.orig/alpha.water">查看固定版本源码</a> · <a href="/assets/examples/v2512/alpha-water/2-alpha.water.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       volScalarField;
    object      alpha.water;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 0 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    sides
    {
        type    fixedValue;
        value   uniform 0;
    }
}

// ************************************************************************* //</code></pre><h3>示例 3 · multiphase/compressibleInterFoam/laminar/waterCooler/fluid</h3><p>原始路径：<code>tutorials/multiphase/compressibleInterFoam/laminar/waterCooler/fluid/0.orig/alpha.water</code>；求解器：<code>compressibleInterFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/waterCooler/fluid/0.orig/alpha.water">查看固定版本源码</a> · <a href="/assets/examples/v2512/alpha-water/3-alpha.water.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/waterCooler/fluid">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       volScalarField;
    object      alpha.water;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 0 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    wall
    {
        type            zeroGradient;
    }

    defaultFaces
    {
        type            empty;
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/interfoam/">interFoam</a> · <a href="/commands/interisofoam/">interIsoFoam</a> · <a href="/commands/setfields/">setFields</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;0.orig/alpha.water&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;0.orig/alpha.water&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown patchField / patch type mismatch</td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
