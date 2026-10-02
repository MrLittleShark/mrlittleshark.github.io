---
title: "setExprBoundaryFields · 用表达式设置边界场的数值或条目"
layout: reference
description: "用表达式设置边界场的数值或条目。"
cms_slug: "command-setexprboundaryfields"
---

<p>用表达式设置边界场的数值或条目。</p><h2>开始前</h2>
<p>已有场和system/setExprBoundaryFieldsDict；字典明确字段、边界、表达式及所需引用场。</p>
<h2>示例 1：先计算表达式预览</h2>
<pre><code class="language-bash">setExprBoundaryFields -dry-run -time 0
</code></pre>
<p>求值并检查字段、patch和表达式，保留原场，适合先定位字段名或表达式问题。</p>
<h2>示例 2：写入初始边界值</h2>
<pre><code class="language-bash">setExprBoundaryFields -time 0
</code></pre>
<p>按默认字典更新0时刻边界，适合空间变化的入口温度或速度分布。</p>
<h2>示例 3：保留被替换子条目</h2>
<pre><code class="language-bash">setExprBoundaryFields -backup -time 0
</code></pre>
<p>写新设置时把原子条目保留为.backup，便于比较表达式施加前后的边界内容。</p>
<h2>示例 4：预加载引用场</h2>
<pre><code class="language-bash">setExprBoundaryFields -load-fields '(U T)' -dict system/setExprBoundaryFields-inletDict -time 0
</code></pre>
<p>表达式引用U、T时先加载它们，按入口专用字典生成耦合分布。</p>
<h2>示例 5：批量处理一段时间</h2>
<pre><code class="language-bash">setExprBoundaryFields -time '0.1:0.5' -ascii
</code></pre>
<p>对已有时间区间逐次求值，并强制ASCII写出，方便检查每个时刻边界值的变化。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-ascii</code></td><td>以 ASCII 文本格式写出，覆盖 controlDict 的输出格式设置。</td></tr><tr><td><code>-backup</code></td><td>将原子条目保存为 .backup 备份。</td></tr><tr><td><code>-cache-fields</code></td><td>在多次调用之间缓存场数据。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 setExprBoundaryFieldsDict 文件。</td></tr><tr><td><code>-dry-run</code></td><td>计算表达式但暂不写入文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-load-fields &lt;wordList&gt;</code></td><td>指定预先加载的场，例如 T 或 &#x27;(p T U)&#x27;。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-withFunctionObjects</code></td><td>执行函数对象。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（19 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprBoundaryFields/setExprBoundaryFields.C">源码与说明</a> · <a href="/assets/command-help/setexprboundaryfields.txt">帮助文本</a></p>
