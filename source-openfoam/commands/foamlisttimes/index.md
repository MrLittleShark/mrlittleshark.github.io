---
title: "foamListTimes · 列出符合条件的案例时间目录"
layout: reference
description: "列出符合条件的案例时间目录。"
cms_slug: "command-foamlisttimes"
---

<p>列出符合条件的案例时间目录。</p><h2>开始前</h2>
<p>已有案例或processor结果；以下实例只列目录，不执行删除。</p>
<h2>示例 1：列出计算结果时间</h2>
<pre><code class="language-bash">foamListTimes
</code></pre>
<p>输出标准时间选择范围内的数值目录，可用于了解已保存的结果时刻。</p>
<h2>示例 2：包含初始0目录</h2>
<pre><code class="language-bash">foamListTimes -withZero
</code></pre>
<p>把0纳入结果列表，适合检查初场和输出时间是否齐全。</p>
<h2>示例 3：查找最新结果</h2>
<pre><code class="language-bash">foamListTimes -latestTime
</code></pre>
<p>输出最后一个可用数值时刻，常用于后处理脚本选择最终状态。</p>
<h2>示例 4：筛选指定范围</h2>
<pre><code class="language-bash">foamListTimes -time '0.1:0.5,1:2' -noZero
</code></pre>
<p>只列两个时间区间内的目录，方便决定重构、转换或动画的处理范围。</p>
<h2>示例 5：查看并行输出时刻</h2>
<pre><code class="language-bash">foamListTimes -processor -latestTime
</code></pre>
<p>从processor0读取时间列表，确定并行计算已写出的最新时刻，再决定是否重构。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>排除 0/ 目录；此选项优先于 -withZero。</td></tr><tr><td><code>-processor</code></td><td>从 processor0/ 目录读取时间列表。</td></tr><tr><td><code>-rm</code></td><td>删除选中的时间目录。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-verbose</code></td><td>显示删除时间目录的进度。</td></tr><tr><td><code>-withZero</code></td><td>将 0/ 目录加入时间选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamListTimes/foamListTimes.C">源码与说明</a> · <a href="/assets/command-help/foamlisttimes.txt">帮助文本</a></p>
