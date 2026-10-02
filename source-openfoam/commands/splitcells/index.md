---
title: "splitCells · 用于网格单元的拓扑修复"
layout: reference
description: "用于网格单元的拓扑修复。"
cms_slug: "command-splitcells"
---

<p>用于网格单元的拓扑修复。</p><h2>开始前</h2>
<p>已有可进行平面切分的网格，按需要准备 cellSet。edgeAngle 以度给出，控制工具识别相关边的几何判据。</p>
<h2>示例 1：按角度判据分裂单元</h2>
<pre><code class="language-bash">splitCells 180
</code></pre>
<p>工具查找内部角超过给定阈值的单元，并尝试切分；这里使用 180°。查看日志中的候选和实际切分数量，再检查生成子单元的体积和形状。</p>
<h2>示例 2：只切分一个单元集合</h2>
<pre><code class="language-bash">splitCells 180 -set targetCells
</code></pre>
<p>将处理限制在已有 targetCells。适合对局部平面网格或问题区域进行试验，而保留其他区域的原单元。</p>
<h2>示例 3：对六面体使用几何切割</h2>
<pre><code class="language-bash">splitCells 180 -set targetCells -geometry
</code></pre>
<p>对六面体也启用几何切割方式，适用于希望按几何规则确定切面的位置。比较与默认处理的子单元形状。</p>
<h2>示例 4：调整切点贴合容差</h2>
<pre><code class="language-bash">splitCells 180 -set targetCells -geometry -tol 0.1
</code></pre>
<p>把边切点贴合容差从默认 0.2 改为 0.1。检查靠近已有顶点的切点如何处理，以及是否产生很短的新边。</p>
<h2>示例 5：更新副本并全面检查</h2>
<pre><code class="language-bash">splitCells 180 -set targetCells -overwrite
checkMesh -constant -allGeometry -allTopology
</code></pre>
<p>将已确认的局部分裂方案写回原网格实例。检查单元体积、内部连接和边界面，随后核对场数据与网格的一致性。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-geometry</code></td><td>Use geometric cut for hexes as well Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-set &lt;name&gt;</code></td><td>设置条目值，会修改文件。</td></tr><tr><td><code>-tol &lt;scalar&gt;</code></td><td>Edge snap tolerance (default 0.2)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: splitCells [OPTIONS] &lt;edgeAngle&gt;
Arguments:
  &lt;edgeAngle&gt;       in degrees [0-360]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -geometry         Use geometric cut for hexes as well
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -set &lt;name&gt;       Split cells from specified cellSet only
  -tol &lt;scalar&gt;     Edge snap tolerance (default 0.2)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Split cells with flat faces

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/splitCells/splitCells.C">源码与说明</a> · <a href="/assets/command-help/splitcells.txt">帮助文本</a></p>
