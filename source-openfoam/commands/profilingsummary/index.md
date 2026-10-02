---
title: "profilingSummary · 汇总各处理器的性能剖析记录"
layout: reference
description: "汇总各处理器的性能剖析记录。"
cms_slug: "command-profilingsummary"
---

<p>汇总各处理器的性能剖析记录。</p><h2>开始前</h2>
<p>计算时已启用并写出profiling数据；工具读取对应时间中的记录，汇总调用数、耗时及可用内存信息。</p>
<h2>示例 1：汇总最新性能记录</h2>
<pre><code class="language-bash">profilingSummary -latestTime
</code></pre>
<p>选最后保存的profiling记录，对各处理器统计做汇总，写入postProcessing/profiling。</p>
<h2>示例 2：汇总指定时刻</h2>
<pre><code class="language-bash">profilingSummary -time 100
</code></pre>
<p>时间100已有性能记录时，生成该阶段的摘要，便于定位计算成本。</p>
<h2>示例 3：比较多个阶段</h2>
<pre><code class="language-bash">profilingSummary -time '100,200,300'
</code></pre>
<p>分别汇总三个时刻，比较网格更新、压力求解等模块的耗时变化。</p>
<h2>示例 4：忽略初始阶段</h2>
<pre><code class="language-bash">profilingSummary -time '200:500' -noZero
</code></pre>
<p>只整理后期时间段，适合分析进入稳定工作状态后的并行负载。</p>
<h2>示例 5：比较另一并行规模</h2>
<pre><code class="language-bash">profilingSummary -case ./run-16cores -latestTime
</code></pre>
<p>run-16cores已保存16核案例的profiling数据；与其他规模的摘要比较最大、平均、最小耗时，检查负载差异。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>排除 0/ 目录；此选项优先于 -withZero。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-withZero</code></td><td>将 0/ 目录加入时间选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/profilingSummary/profilingSummary.C">源码与说明</a> · <a href="/assets/command-help/profilingsummary.txt">帮助文本</a></p>
