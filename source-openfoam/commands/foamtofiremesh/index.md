---
title: "foamToFireMesh · -scale 指定长度缩放系数"
layout: reference
description: "-scale 指定长度缩放系数。"
cms_slug: "command-foamtofiremesh"
---

<p>-scale 指定长度缩放系数。</p><h2>开始前</h2>
<p>案例已有体网格；按时间导出示例需要相应网格时间目录。输出用于 AVL FIRE 格式交换。</p>
<h2>示例 1：导出初始网格</h2>
<pre><code class="language-bash">foamToFireMesh -constant
</code></pre>
<p>选择 constant 网格并转换为 FIRE 格式。转换日志给出实际写出的文件位置。</p>
<h2>示例 2：使用 ASCII 格式</h2>
<pre><code class="language-bash">foamToFireMesh -constant -ascii
</code></pre>
<p>以文本格式导出，便于排查交换文件问题。与二进制输出相比，文件通常更大。</p>
<h2>示例 3：转换为毫米坐标</h2>
<pre><code class="language-bash">foamToFireMesh -constant -scale 1000
</code></pre>
<p>输出坐标乘 1000，将米制网格改为毫米数值。接收软件应按毫米解释输出坐标。</p>
<h2>示例 4：导出最新变形网格</h2>
<pre><code class="language-bash">foamToFireMesh -latestTime
</code></pre>
<p>读取最新时间对应的几何。适用于动网格计算后将变形位置交给 FIRE 相关工具。</p>
<h2>示例 5：导出一组瞬态网格</h2>
<pre><code class="language-bash">foamToFireMesh -time '0.1:0.5' -ascii
</code></pre>
<p>遍历所选范围内已有的时间目录，导出相关网格。核对每个输出对应的时间，避免把静态网格重复文件误认为不同形状。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-ascii</code></td><td>以 ASCII 文本格式写出，替代二进制格式。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 1，即保持原尺寸。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamToFireMesh/foamToFireMesh.C">源码与说明</a> · <a href="/assets/command-help/foamtofiremesh.txt">帮助文本</a></p>
