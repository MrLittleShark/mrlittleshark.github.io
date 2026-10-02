---
title: "cumulativeDisplacement · 计算各时刻网格点相对 constant 参考网格的位移及法向分量"
layout: reference
description: "计算各时刻网格点相对 constant 参考网格的位移及法向分量。"
cms_slug: "command-cumulativedisplacement"
---

<p>计算各时刻网格点相对 constant 参考网格的位移及法向分量。</p><h2>开始前</h2>
<p>constant保存初始points，各结果时刻点编号和点数与其相容；适合无重编号、无拓扑改变的形变序列。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：计算最终几何变化</h2>
<pre><code class="language-bash">cumulativeDisplacement -latestTime
</code></pre>
<p>生成点向量场displacement及边界点法向位移normalDisplacement，以constant网格为参考。</p>
<h2>示例 2：处理整个形变阶段</h2>
<pre><code class="language-bash">cumulativeDisplacement -time '0.1:1'
</code></pre>
<p>对区间内每个已有网格状态计算参考位移，便于观察变形如何随时间积累。</p>
<h2>示例 3：只处理某个区域</h2>
<pre><code class="language-bash">cumulativeDisplacement -region solid -latestTime
</code></pre>
<p>对solid区域网格计算位移，适合多区域中的结构形变检查。</p>
<h2>示例 4：计算分区网格的位移</h2>
<pre><code class="language-bash">mpirun -np 4 cumulativeDisplacement -parallel -latestTime
</code></pre>
<p>已有4分区且各时间点寻址一致；在分区上计算并同步边界点法向信息。</p>
<h2>示例 5：导出变形场</h2>
<pre><code class="language-bash">cumulativeDisplacement -latestTime
foamToVTK -latestTime -fields '(displacement normalDisplacement)' -name VTK-displacement
</code></pre>
<p>将生成的点场与网格一起导出，用法向位移检查表面局部鼓起或收缩，用向量场查看整体方向。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/optimisation/cumulativeDisplacement/cumulativeDisplacement.C">源码与说明</a> · <a href="/assets/command-help/cumulativedisplacement.txt">帮助文本</a></p>
