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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-geometry</code></td><td>对六面体也采用几何切割。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-set &lt;name&gt;</code></td><td>仅拆分指定 cellSet 中的单元。</td></tr><tr><td><code>-tol &lt;scalar&gt;</code></td><td>设置边吸附容差，默认为 0.2。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/splitCells/splitCells.C">源码与说明</a> · <a href="/assets/command-help/splitcells.txt">帮助文本</a></p>
