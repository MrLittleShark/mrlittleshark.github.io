---
title: "temporalInterpolate · 在已有时间之间插值字段，增加可视化时间帧"
layout: reference
description: "在已有时间之间插值字段，增加可视化时间帧。"
cms_slug: "command-temporalinterpolate"
---

<p>在已有时间之间插值字段，增加可视化时间帧。</p><h2>开始前</h2>
<p>已有至少两个时间的相同字段，网格拓扑与字段寻址保持相容；插值结果用于时间数据重采样。</p>
<h2>示例 1：在相邻时刻增加中间帧</h2>
<pre><code class="language-bash">temporalInterpolate -time '0:1' -divisions 1
</code></pre>
<p>对所选已有时刻的每个相邻间隔插入1个中间时间，默认使用线性插值。</p>
<h2>示例 2：每个间隔增加三帧</h2>
<pre><code class="language-bash">temporalInterpolate -time '0:1' -divisions 3
</code></pre>
<p>原间隔被分成4段，写3个内部时刻，适合让动画变化更连续。</p>
<h2>示例 3：只插值速度与压力</h2>
<pre><code class="language-bash">temporalInterpolate -time '0:1' -fields '(U p)' -divisions 3
</code></pre>
<p>只创建U、p的中间数据，减少输出量，其余字段保留原时间分辨率。</p>
<h2>示例 4：采用样条时间插值</h2>
<pre><code class="language-bash">temporalInterpolate -time '0:2' -fields '(T)' -interpolationType spline -divisions 2
</code></pre>
<p>存在足够相邻温度快照时用样条方式，每间隔增加2帧；比较温度变化是否出现插值过冲。</p>
<h2>示例 5：插值多区域中的流体数据</h2>
<pre><code class="language-bash">temporalInterpolate -region fluid -time '0.1:0.5' -fields '(U)' -divisions 4
</code></pre>
<p>只给fluid速度添加时间帧，再用相同区域导出动画，保持其他区域数据不变。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-divisions &lt;integer&gt;</code></td><td>设置相邻时刻间插入的时间分段数，默认为 1。</td></tr><tr><td><code>-fields &lt;wordRes&gt;</code></td><td>指定要插值的场，例如 U 或 &#x27;(U T p &quot;Y.*&quot;)&#x27;。</td></tr><tr><td><code>-interpolationType &lt;word&gt;</code></td><td>指定时间插值方式：linear 为线性插值，spline 为样条插值。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/temporalInterpolate/temporalInterpolate.C">源码与说明</a> · <a href="/assets/command-help/temporalinterpolate.txt">帮助文本</a></p>
