---
title: "0/p · p"
layout: reference
description: "下例给出与第 7 章二维通道网格对应的速度和压力场。内部初始速度等于入口速度，壁面采用无滑移条件，出口速度采用零梯度条件。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>下例给出与第 7 章二维通道网格对应的速度和压力场。内部初始速度等于入口速度，壁面采用无滑移条件，出口速度采用零梯度条件。</p><figure><img src="/assets/diagrams/reference-2.svg" alt="初始场配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>0/p</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dimensions</code> · <code>internalField</code> · <code>boundaryField</code> · <code>fixedValue</code> · <code>zeroGradient</code> · <code>totalPressure</code></p><h2>关联命令</h2><p><a href="/commands/?q=icoFoam">icoFoam</a> · <a href="/commands/?q=simpleFoam">simpleFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary 0/p -keywords
icoFoam -help</code></pre><h2>9.1 速度场与压力场</h2><p>下例给出与第 7 章二维通道网格对应的速度和压力场。内部初始速度等于入口速度，壁面采用无滑移条件，出口速度采用零梯度条件。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class volVectorField; object U;
}
dimensions [0 1 -1 0 0 0 0];
internalField uniform (1 0 0);
boundaryField
{
    inlet { type fixedValue; value uniform (1 0 0); }
    outlet { type zeroGradient; }
    walls { type noSlip; }
    frontAndBack { type empty; }
}
FoamFile
{
    version 2.0; format ascii;
    class volScalarField; object p;
}
dimensions [0 2 -2 0 0 0 0];
internalField uniform 0;
boundaryField
{
    inlet { type zeroGradient; }
    outlet { type fixedValue; value uniform 0; }
    walls { type zeroGradient; }
    frontAndBack { type empty; }
}</code></pre>
<p>本例 p 为运动学压力，适用于相应的不可压缩求解器。采用绝对压力的可压缩求解器时，dimensions 设为 [1 -1 -2 0 0 0 0]，压力值按状态方程设置，如 101325 Pa。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>dimensions</td><td>七个指数依次表示质量、长度、时间、温度、物质量、电流、发光强度。量纲错误常在矩阵组装或赋值时暴露。</td></tr><tr><td>internalField</td><td>初始内部场，可使用 uniform 或 nonuniform。uniform 不表示求解过程始终空间均匀。</td></tr><tr><td>boundaryField</td><td>按网格 patch 名称设置边界条件；名称必须与 polyMesh/boundary 一致，类型还受网格边界类型约束。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/icoFoam/cavity/cavity</h3><p>原始路径：<code>tutorials/incompressible/icoFoam/cavity/cavity/0/p</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/0/p">查看固定版本源码</a> · <a href="/assets/examples/v2512/p/1-p.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      p;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -2 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    movingWall
    {
        type            zeroGradient;
    }

    fixedWalls
    {
        type            zeroGradient;
    }

    frontAndBack
    {
        type            empty;
    }
}


// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/simpleFoam/pitzDaily</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/pitzDaily/0/p</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/0/p">查看固定版本源码</a> · <a href="/assets/examples/v2512/p/2-p.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      p;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -2 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    inlet
    {
        type            zeroGradient;
    }

    outlet
    {
        type            fixedValue;
        value           uniform 0;
    }

    upperWall
    {
        type            zeroGradient;
    }

    lowerWall
    {
        type            zeroGradient;
    }

    frontAndBack
    {
        type            empty;
    }
}


// ************************************************************************* //</code></pre><h3>示例 3 · compressible/rhoSimpleFoam/gasMixing/injectorPipe</h3><p>原始路径：<code>tutorials/compressible/rhoSimpleFoam/gasMixing/injectorPipe/0.orig/p</code>；求解器：<code>rhoSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoSimpleFoam/gasMixing/injectorPipe/0.orig/p">查看固定版本源码</a> · <a href="/assets/examples/v2512/p/3-p.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoSimpleFoam/gasMixing/injectorPipe">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      p;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -2 0 0 0 0];

internalField   uniform 1e5;

boundaryField
{
    #includeEtc &quot;caseDicts/setConstraintTypes&quot;

    outlet
    {
        type            fixedValue;
        value           &#36;internalField;
    }

    &quot;.*&quot;
    {
        type            zeroGradient;
    }
}


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/setConstraintTypes&quot;。下载单个文件不会自动取得这些依赖。</p><h2>配套命令与验证次序</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/simplefoam/">simpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;0/p&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;0/p&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown patchField / patch type mismatch</td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
