---
title: "system/decomposeParDict · decomposeParDict"
layout: reference
description: "numberOfSubdomains 指定分区数，与求解阶段 mpirun -np 的进程数一致。scotch 采用图分割，simple 按坐标规则划分，hierarchical 按指定方向依次划分，manual 使用给定的处理器映射，multiLevel 组合多级分解方法。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>numberOfSubdomains 指定分区数，与求解阶段 mpirun -np 的进程数一致。scotch 采用图分割，simple 按坐标规则划分，hierarchical 按指定方向依次划分，manual 使用给定的处理器映射，multiLevel 组合多级分解方法。</p><figure><img src="/assets/diagrams/reference-6.svg" alt="并行计算配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/decomposeParDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>numberOfSubdomains</code> · <code>method</code> · <code>scotch</code> · <code>simpleCoeffs</code> · <code>hierarchicalCoeffs</code> · <code>regions</code> · <code>constraints</code></p><h2>关联命令</h2><p><a href="/commands/?q=decomposePar">decomposePar</a> · <a href="/commands/?q=redistributePar">redistributePar</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/decomposeParDict -keywords
decomposePar -help</code></pre><h2>8.4 system/decomposeParDict</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object decomposeParDict;
}
numberOfSubdomains 4;
method scotch;</code></pre>
<p>numberOfSubdomains 指定分区数，与求解阶段 mpirun -np 的进程数一致。scotch 采用图分割，simple 按坐标规则划分，hierarchical 按指定方向依次划分，manual 使用给定的处理器映射，multiLevel 组合多级分解方法。</p>
<pre><code class="language-openfoam">// 用 simple 替换上面的 method 时，加入以下系数
method simple;
simpleCoeffs
{
    n (2 2 1);
    delta 0.001;
}</code></pre>
<p>示例中 n 的三个分量乘积为 4。hierarchicalCoeffs 还通过 order 指定划分顺序，如 xyz。多区域算例可在 regions 子字典中分别设置方法和子域数。constraints 用于保持挡板、面区域及指定连接关系，约束范围同时影响负载均衡。</p>
<h2>17.1 decomposeParDict（并行分区）</h2><pre><code class="language-openfoam">numberOfSubdomains  8;          // 必须等于 mpirun -np 的数字

method              scotch;     // 分区算法

// 各算法的参数（只需写你用的那个）
simpleCoeffs    { n (2 2 2); delta 0.001; }        // 按 x/y/z 均分
hierarchicalCoeffs { n (2 2 2); delta 0.001; order xyz; }
manualCoeffs    { dataFile &quot;decompositionData&quot;; }</code></pre>
<div class="table-scroll"><table>
<tr><th>method</th><th>说明</th><th>何时用</th></tr>
<tr><td>scotch</td><td>自动最小化交界面，默认首选</td><td>绝大多数情况</td></tr>
<tr><td>hierarchical</td><td>按指定顺序在 x/y/z 上依次均分</td><td>规则区域、想控制分区形状</td></tr>
<tr><td>simple</td><td>直接三向均分</td><td>简单几何</td></tr>
<tr><td>kahip / metis</td><td>其他图分区库</td><td>有装才有</td></tr>
<tr><td>multiLevel</td><td>多级分区（跨节点/节点内分别优化）</td><td>大规模集群</td></tr>
<tr><td>structured</td><td>沿某方向不切（保持结构）</td><td>边界层方向不切分</td></tr>
<tr><td>manual</td><td>读文件指定每个单元归谁</td><td>特殊需求</td></tr>
</table></div>
<p>约束条件（保证某些面不被切开）：</p>
<pre><code class="language-openfoam">constraints
{
    baffles       { type preserveBaffles; }
    cyclics       { type preservePatches; patches (cyc1 cyc2); }
    faces         { type singleProcessorFaceSets; sets ((f0 -1)); }
}</code></pre>
<p>n (2 2 2) 的乘积必须等于 numberOfSubdomains，写不一致会直接报错。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>numberOfSubdomains</td><td>并行分区数，通常须与 MPI 进程数一致。</td></tr><tr><td>method</td><td>所采用的分区、插值或模型方法；含义由该字典的读取程序决定。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/pimpleFoam/laminar/filmPanel0</h3><p>原始路径：<code>tutorials/incompressible/pimpleFoam/laminar/filmPanel0/system/decomposeParDict</code>；求解器：<code>pimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/filmPanel0/system/decomposeParDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/decomposepardict/1-decomposeParDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/filmPanel0">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      decomposeParDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

numberOfSubdomains 12;

method  scotch;

// ************************************************************************* //</code></pre><h3>示例 2 · combustion/fireFoam/LES/compartmentFire</h3><p>原始路径：<code>tutorials/combustion/fireFoam/LES/compartmentFire/system/decomposeParDict</code>；求解器：<code>fireFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/compartmentFire/system/decomposeParDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/decomposepardict/2-decomposeParDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/compartmentFire">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      decomposeParDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

numberOfSubdomains 8;

method      scotch;


// ************************************************************************* //</code></pre><h3>示例 3 · incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses-mass-uniformity-SQP-extraVars/reEval</h3><p>原始路径：<code>tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses-mass-uniformity-SQP-extraVars/reEval/system/decomposeParDict</code>；求解器：<code>adjointOptimisationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses-mass-uniformity-SQP-extraVars/reEval/system/decomposeParDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/decomposepardict/3-decomposeParDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses-mass-uniformity-SQP-extraVars/reEval">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      decomposeParDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

numberOfSubdomains 4;
method          scotch;

// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/decomposepar/">decomposePar</a> · <a href="/commands/redistributepar/">redistributePar</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/decomposeParDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/decomposeParDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>分区数与 MPI 进程数不同</td><td>核对 numberOfSubdomains 与 mpirun -np，修改分区数后重新分解。</td></tr><tr><td>串并行结果差异过大</td><td>保持网格、初值、时间步与收敛准则一致，并检查各进程日志与整体守恒。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
