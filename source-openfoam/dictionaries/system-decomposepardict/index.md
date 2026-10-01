---
title: "system/decomposeParDict"
layout: "reference"
description: "numberOfSubdomains 指定分区数，与求解阶段 mpirun -np 的进程数一致。scotch 采用图分割，simple 按坐标规则划分，hierarchical 按指定方向依次划分，manual 使用给定的处理器映射，multiLevel 组合多级分解方法。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/decomposeParDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>numberOfSubdomains</code> · <code>method</code> · <code>scotch</code> · <code>simpleCoeffs</code> · <code>hierarchicalCoeffs</code> · <code>regions</code> · <code>constraints</code></p><h2>关联命令</h2><p><a href="/commands/?q=decomposePar">decomposePar</a> · <a href="/commands/?q=redistributePar">redistributePar</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/decomposeParDict -keywords
decomposePar -help</code></pre><h2>8.4 system/decomposeParDict</h2><pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object decomposeParDict;
}
numberOfSubdomains 4;
method scotch;</code></pre>
<p>numberOfSubdomains 指定分区数，与求解阶段 mpirun -np 的进程数一致。scotch 采用图分割，simple 按坐标规则划分，hierarchical 按指定方向依次划分，manual 使用给定的处理器映射，multiLevel 组合多级分解方法。</p>
<pre><code>// 用 simple 替换上面的 method 时，加入以下系数
method simple;
simpleCoeffs
{
    n (2 2 1);
    delta 0.001;
}</code></pre>
<p>示例中 n 的三个分量乘积为 4。hierarchicalCoeffs 还通过 order 指定划分顺序，如 xyz。多区域算例可在 regions 子字典中分别设置方法和子域数。constraints 用于保持挡板、面区域及指定连接关系，约束范围同时影响负载均衡。</p>
<h2>17.1 decomposeParDict（并行分区）</h2><pre><code>numberOfSubdomains  8;          // 必须等于 mpirun -np 的数字

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
<pre><code>constraints
{
    baffles       { type preserveBaffles; }
    cyclics       { type preservePatches; patches (cyc1 cyc2); }
    faces         { type singleProcessorFaceSets; sets ((f0 -1)); }
}</code></pre>
<p>n (2 2 2) 的乘积必须等于 numberOfSubdomains，写不一致会直接报错。</p>
{% endraw %}