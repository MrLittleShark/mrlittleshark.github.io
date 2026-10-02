---
title: "foamSearch · 在多个算例中查找字典条目，汇总不同取值及出现次数"
layout: reference
description: "在多个算例中查找字典条目，汇总不同取值及出现次数。"
cms_slug: "command-foamsearch"
---

<p>在多个算例中查找字典条目，汇总不同取值及出现次数。</p><h2>开始前</h2>
<p>加载 OpenFOAM v2512 环境后即可使用。<code>foamSearch</code> 读取字典文件；查询官方教程时使用 <code>$FOAM_TUTORIALS</code>，查询自己的算例时换成对应目录。命令的三个位置参数依次是搜索目录、条目路径和文件名。</p>
<h2>示例 1：查询当前算例的时间离散格式</h2>
<pre><code class="language-bash">cd "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity"
foamSearch ddtSchemes.default fvSchemes
</code></pre>
<p>输出示例：</p>
<pre><code class="language-text">default         Euler;
</code></pre>
<p>省略搜索目录时，从当前目录向下查找 <code>fvSchemes</code>。<code>ddtSchemes.default</code> 指向 <code>ddtSchemes</code> 子字典中的 <code>default</code>；方腔教程使用 <code>Euler</code>，输出包含 <code>default Euler;</code>。这里查询的是时间导数的离散格式。</p>
<h2>示例 2：比较所有教程的时间离散格式</h2>
<pre><code class="language-bash">foamSearch "$FOAM_TUTORIALS" ddtSchemes.default fvSchemes
</code></pre>
<p>输出示例：</p>
<pre><code class="language-text">default         backward;
default         backward 1;
default         CrankNicolson 0.5;
default         CrankNicolson 0.9;
default         Euler;
default         localEuler;
default         none;
default         steadyState;
</code></pre>
<p>增加第一个参数后，搜索范围扩展到整个教程目录。程序逐个读取 <code>fvSchemes</code>，将找到的条目排序、去重，例如 <code>Euler</code>、<code>backward</code> 和 <code>steadyState</code>。相同内容只显示一次；标准输出汇总取值，处理文件数量写到错误输出。</p>
<h2>示例 3：只查询不可压缩算例的压力求解器</h2>
<pre><code class="language-bash">foamSearch "$FOAM_TUTORIALS/incompressible" solvers.p.solver fvSolution
</code></pre>
<p>输出示例：</p>
<pre><code class="language-text">solver          GAMG;
solver          PBiCGStab;
solver          PCG;
solver          smoothSolver;
</code></pre>
<p><code>solvers.p.solver</code> 依次进入 <code>solvers</code>、<code>p</code>，读取其中的 <code>solver</code>，例如 <code>PCG</code> 或 <code>GAMG</code>。最后一个参数改为 <code>fvSolution</code>，因为线性求解器配置保存在该文件中。这个查询针对名为 <code>p</code> 的条目；<code>p_rgh</code> 等字段可以替换路径中的字段名继续查找。</p>
<h2>示例 4：统计每种配置出现的次数</h2>
<pre><code class="language-bash">foamSearch -count "$FOAM_TUTORIALS" ddtSchemes.default fvSchemes
</code></pre>
<p>输出示例：</p>
<pre><code class="language-text">19 default         backward;
      2 default         backward 1;
      2 default         CrankNicolson 0.5;
      1 default         CrankNicolson 0.9;
    335 default         Euler;
      9 default         localEuler;
     43 default         none;
    171 default         steadyState;
</code></pre>
<p><code>-count</code> 放在位置参数前，在每一条去重结果前添加次数。对于这里的单行条目，次数表示多少份字典返回了相同设置，例如一行 <code>12 default Euler;</code> 表示该条目出现 12 次。具体数量随教程内容变化，可用于了解某种格式在教程中的使用情况。</p>
<h2>示例 5：按出现次数排序并保存结果</h2>
<pre><code class="language-bash">foamSearch -count "$FOAM_TUTORIALS/incompressible" \
    relaxationFactors.equations.U fvSolution \
    2&gt; foamSearch-progress.log | sort -nr &gt; U-relaxation-counts.txt
cat U-relaxation-counts.txt
</code></pre>
<p>查询路径指向速度方程的松弛因子。<code>sort -nr</code> 按行首数字降序排列，使最常见的设置排在前面；<code>&gt;</code> 保存汇总表，<code>2&gt;</code> 单独保存处理进度。将输出与具体教程的流动模型和迭代设置一起阅读，可以理解不同松弛因子的使用背景。</p>
<h2>示例 6：一次比较压力、速度和湍流方程的求解器</h2>
<pre><code class="language-bash">for field in p U k omega; do
    printf '\n--- %s ---\n' "$field"
    foamSearch -count "$FOAM_TUTORIALS/incompressible" \
        "solvers.${field}.solver" fvSolution
done
</code></pre>
<p>循环依次把 <code>field</code> 替换成四个字段名。双引号让变量展开后仍作为完整条目路径传入。输出按字段分组，可比较压力方程与速度、湍流方程的线性求解器选择。若某个查询没有结果，进入对应教程查看 <code>solvers</code> 中实际使用的字段名、正则表达式或引用关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-c | -count</code></td><td>在每行前面显示该配置的出现次数。</td></tr><tr><td><code>-help</code></td><td>显示帮助。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSearch">源码与说明</a> · <a href="/assets/command-help/foamsearch.txt">帮助文本</a></p>
