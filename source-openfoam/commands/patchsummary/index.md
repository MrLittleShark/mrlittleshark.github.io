---
title: "patchSummary · 列出各边界patch上的字段边界条件"
layout: reference
description: "列出各边界patch上的字段边界条件。"
cms_slug: "command-patchsummary"
---

<p>列出各边界patch上的字段边界条件。</p><h2>开始前</h2>
<p>已有网格和所选时间的场；适合检查边界名称与各字段的类型是否一致。</p>
<h2>示例 1：查看初始边界条件</h2>
<pre><code class="language-bash">patchSummary -time 0
</code></pre>
<p>读取0时刻字段，汇总各patch采用的边界类型，适合求解前检查。</p>
<h2>示例 2：逐patch展开显示</h2>
<pre><code class="language-bash">patchSummary -time 0 -expand
</code></pre>
<p>关闭相同条件的合并展示，逐个列出patch，便于定位某一小边界。</p>
<h2>示例 3：检查最新重启状态</h2>
<pre><code class="language-bash">patchSummary -latestTime
</code></pre>
<p>查看最新结果场的边界类型，确认重启文件与预期边界设置一致。</p>
<h2>示例 4：比较多个时刻</h2>
<pre><code class="language-bash">patchSummary -time '0,1,2' -expand
</code></pre>
<p>三个时间均存在时，逐时刻列出边界条件，检查中途修改或重启是否改变了字段设置。</p>
<h2>示例 5：检查多区域流体边界</h2>
<pre><code class="language-bash">patchSummary -region fluid -latestTime -expand
</code></pre>
<p>仅查看fluid的最新场，便于把流固界面、入口和壁面条件分开核对。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-expand</code></td><td>逐个列出边界，保留各边界的独立信息。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/patchSummary/patchSummary.C">源码与说明</a> · <a href="/assets/command-help/patchsummary.txt">帮助文本</a></p>
