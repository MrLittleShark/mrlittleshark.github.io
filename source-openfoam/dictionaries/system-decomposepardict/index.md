---
title: "decomposeParDict"
layout: reference
description: "设置并行分区数、分区方法和约束，供 decomposePar 分解网格与场。"
dictionary: true
cms_slug: "dictionary-decomposepardict"
---

<p>设置并行分区数、分区方法和约束，供 decomposePar 分解网格与场。</p><p>位置：<code>system/decomposeParDict</code></p><h2>配置实例</h2><pre><code class="language-openfoam">FoamFile
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
manualCoeffs    { dataFile "decompositionData"; }</code></pre>
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
<p>n (2 2 2) 的乘积必须等于 numberOfSubdomains，写不一致会直接报错。</p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>numberOfSubdomains</td><td>并行分区数，通常须与 MPI 进程数一致。</td></tr><tr><td>method</td><td>所采用的分区、插值或模型方法；含义由该字典的读取程序决定。</td></tr><tr><td>regions</td><td>几何选择区域或多区域列表；在不同字典中结构不同，不能只复制键名。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/laminar/filmPanel0</summary><p>filmPanel0 的并行计算把网格分给 12 个进程。</p>
<ul>
<li><code>numberOfSubdomains 12</code> 指定子域数，运行 MPI 时的进程数需与之匹配。</li>
<li><code>method scotch</code> 根据网格连接自动分区，目标是平衡工作量并控制子域接口。</li>
<li>薄层或局部加密网格应查看每个分区的单元数量与接口分布。</li>
</ul>
<p>换电脑或进程数后先修改子域数并重新分解，再启动对应数量的进程。</p>
<p><a href="/assets/examples/v2512/decomposepardict/1-decomposeParDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/filmPanel0/system/decomposeParDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/filmPanel0">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · combustion/fireFoam/LES/compartmentFire</summary><p>compartmentFire 使用 8 个并行子域计算燃烧室流动。</p>
<ul>
<li><code>numberOfSubdomains 8</code> 对应八个计算分区。</li>
<li><code>method scotch</code> 根据拓扑自动划分，不需要在本字典手工指定各坐标方向份数。</li>
<li>火源、颗粒和辐射等局部任务可能使计算负载与单元数不完全一致，可结合每步耗时判断平衡。</li>
</ul>
<p>调整进程数后重新分解，并比较通信开销与单步时间是否确有改善。</p>
<p><a href="/assets/examples/v2512/decomposepardict/2-decomposeParDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/compartmentFire/system/decomposeParDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/compartmentFire">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses-mass-uniformity-SQP-extraVars/reEval</summary><p>拓扑优化中的 reEval 阶段把当前设计的流场复算分成 4 个子域。</p>
<ul>
<li><code>numberOfSubdomains 4</code> 决定分区数量。</li>
<li><code>method scotch</code> 自动划分网格连接，适用于当前三维区域。</li>
<li>复算目录的分区应与它自身的网格及字段对应，不能直接混用另一轮优化的 processor 结果。</li>
</ul>
<p>改变网格或并行规模后重新分解，再比较同一设计的目标函数和流动结果。</p>
<p><a href="/assets/examples/v2512/decomposepardict/3-decomposeParDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses-mass-uniformity-SQP-extraVars/reEval/system/decomposeParDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses-mass-uniformity-SQP-extraVars/reEval">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/decomposepar/">decomposePar</a> · <a href="/commands/redistributepar/">redistributePar</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>分区数与 MPI 进程数不同</td><td>核对 numberOfSubdomains 与 mpirun -np，修改分区数后重新分解。</td></tr><tr><td>串并行结果差异过大</td><td>保持网格、初值、时间步与收敛准则一致，并检查各进程日志与整体守恒。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
