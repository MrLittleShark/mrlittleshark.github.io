---
title: "0/epsilon · epsilon"
layout: reference
description: "入口湍流量可由湍流强度 I、速度大小 U 和长度尺度 L 估算：k = 1.5*(I*U)^2，epsilon = Cmu^0.75*k^1.5/L，omega = sqrt(k)/(Cmu^0.25*L)。常用 Cmu = 0.09，湍流强度 5% 对应 I = 0.05。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>入口湍流量可由湍流强度 I、速度大小 U 和长度尺度 L 估算：k = 1.5*(I*U)^2，epsilon = Cmu^0.75*k^1.5/L，omega = sqrt(k)/(Cmu^0.25*L)。常用 Cmu = 0.09，湍流强度 5% 对应 I = 0.05。</p><figure><img src="/assets/diagrams/reference-2.svg" alt="初始场配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>0/epsilon</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dimensions</code> · <code>internalField</code> · <code>boundaryField</code> · <code>epsilonWallFunction</code></p><h2>关联命令</h2><p><a href="/commands/?q=simpleFoam">simpleFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary 0/epsilon -keywords
simpleFoam -help</code></pre><h2>9.4 湍流场与热扩散场</h2><div class="table-scroll"><table>
<tr><th>字段</th><th>量纲</th><th>常见边界与设置</th></tr>
<tr><td>k</td><td>[0 2 -2 0 0 0 0]</td><td>入口固定湍动能；壁面可配 kqRWallFunction</td></tr>
<tr><td>epsilon</td><td>[0 2 -3 0 0 0 0]</td><td>k epsilon 模型使用；壁面 epsilonWallFunction</td></tr>
<tr><td>omega</td><td>[0 0 -1 0 0 0 0]</td><td>k omega 模型使用；壁面 omegaWallFunction</td></tr>
<tr><td>nut</td><td>[0 2 -1 0 0 0 0]</td><td>湍动黏度，由模型给定；壁面可用 nutkWallFunction 等</td></tr>
<tr><td>alphat</td><td>由热模型定义，常见可压缩形式为 [1 -1 -1 0 0 0 0]</td><td>量纲按所用热模型确定</td></tr>
</table></div>
<p>入口湍流量可由湍流强度 I、速度大小 U 和长度尺度 L 估算：\(k=1.5(IU)^2\)，\(\varepsilon=\frac{C_\mu^{0.75}k^{1.5}}{L}\)，\(\omega=\frac{\sqrt{k}}{C_\mu^{0.25}L}\)。常用 \(C_\mu = 0.09\)，湍流强度 5% 对应 \(I = 0.05\)。</p>
<p>近壁处理方式应与网格设计一致。采用壁面函数或直接解析近壁区域时，分别据其要求确定第一层网格厚度及目标 y+。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>dimensions</td><td>七个指数依次表示质量、长度、时间、温度、物质量、电流、发光强度。量纲错误常在矩阵组装或赋值时暴露。</td></tr><tr><td>internalField</td><td>初始内部场，可使用 uniform 或 nonuniform。uniform 不表示求解过程始终空间均匀。</td></tr><tr><td>boundaryField</td><td>按网格 patch 名称设置边界条件；名称必须与 polyMesh/boundary 一致，类型还受网格边界类型约束。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/simpleFoam/pitzDailyExptInlet</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/pitzDailyExptInlet/constant/boundaryData/inlet/0/epsilon</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDailyExptInlet/constant/boundaryData/inlet/0/epsilon">查看固定版本源码</a> · <a href="/assets/examples/v2512/epsilon/1-epsilon.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDailyExptInlet">查看配套目录</a></p><pre><code class="language-openfoam">// Data on points
70
(

//minz
9813.84
9813.84
7231.83
1260.68
1260.68
253.433
253.433
76.6694
76.6694
30.8982
16.0868
16.0868
10.4406
7.39238
4.6135
3.0542
2.39951
2.24094
2.3504
2.93787
3.6326
3.15933
2.71282
2.72062
3.09416
4.18748
7.30754
14.5872
29.1787
73.9208
490.641
3622.84
5549.75
6430.47
6327.27

// maxz
9813.84
9813.84
7231.83
1260.68
1260.68
253.433
253.433
76.6694
76.6694
30.8982
16.0868
16.0868
10.4406
7.39238
4.6135
3.0542
2.39951
2.24094
2.3504
2.93787
3.6326
3.15933
2.71282
2.72062
3.09416
4.18748
7.30754
14.5872
29.1787
73.9208
490.641
3622.84
5549.75
6430.47
6327.27
)

// ************************************************************************* //</code></pre><h3>示例 2 · heatTransfer/chtMultiRegionFoam/externalCoupledHeater</h3><p>原始路径：<code>tutorials/heatTransfer/chtMultiRegionFoam/externalCoupledHeater/0.orig/epsilon</code>；求解器：<code>chtMultiRegionFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/externalCoupledHeater/0.orig/epsilon">查看固定版本源码</a> · <a href="/assets/examples/v2512/epsilon/2-epsilon.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/externalCoupledHeater">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      epsilon;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -3 0 0 0 0];

internalField   uniform 0.01;

boundaryField
{
    &quot;.*&quot;
    {
        type            calculated;
        value           &#36;internalField;
    }
}


// ************************************************************************* //</code></pre><h3>示例 3 · lagrangian/sprayFoam/aachenBomb</h3><p>原始路径：<code>tutorials/lagrangian/sprayFoam/aachenBomb/0.orig/epsilon</code>；求解器：<code>sprayFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb/0.orig/epsilon">查看固定版本源码</a> · <a href="/assets/examples/v2512/epsilon/3-epsilon.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      epsilon;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -3 0 0 0 0];

internalField   uniform 90;

boundaryField
{
    walls
    {
        type            epsilonWallFunction;
        value           uniform 90;
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/simplefoam/">simpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/boundaryData/inlet/0/epsilon&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/boundaryData/inlet/0/epsilon&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown patchField / patch type mismatch</td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
