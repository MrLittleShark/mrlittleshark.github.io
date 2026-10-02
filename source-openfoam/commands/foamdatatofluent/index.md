---
title: "foamDataToFluent · 按映射字典把场数据导出为 Fluent 数据文件"
layout: reference
description: "按映射字典把场数据导出为 Fluent 数据文件。"
cms_slug: "command-foamdatatofluent"
---

<p>按映射字典把场数据导出为 Fluent 数据文件。</p><h2>开始前</h2>
<p>已有匹配的OpenFOAM网格和字段，以及system/foamDataToFluentDict；Fluent端使用与之对应的网格。</p>
<h2>示例 1：转换已有结果</h2>
<pre><code class="language-bash">foamDataToFluent
</code></pre>
<p>读取字段映射规则并转换选中的时间，输出Fluent可读取的数据文件。</p>
<h2>示例 2：只转换最后时刻</h2>
<pre><code class="language-bash">foamDataToFluent -latestTime
</code></pre>
<p>仅写最新结果，适合把最终解传给对应Fluent网格继续分析。</p>
<h2>示例 3：转换明确时刻</h2>
<pre><code class="language-bash">foamDataToFluent -time 1
</code></pre>
<p>选择已有时间1，便于把同一物理时刻的解在不同后处理软件中对照。</p>
<h2>示例 4：转换一段瞬态结果</h2>
<pre><code class="language-bash">foamDataToFluent -time '0.1:0.5' -noZero
</code></pre>
<p>导出0.1到0.5的已有结果并排除初值，输出可用于瞬态场对比。</p>
<h2>示例 5：并行计算后再转换</h2>
<pre><code class="language-bash">reconstructPar -latestTime
foamDataToFluent -latestTime
</code></pre>
<p>先把processor场重构成完整场，再按Fluent映射规则导出，保证字段对应完整网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamDataToFluent/writeFluentScalarField.C">源码与说明</a> · <a href="/assets/command-help/foamdatatofluent.txt">帮助文本</a></p>
