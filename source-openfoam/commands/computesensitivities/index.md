---
title: "computeSensitivities · 利用已有原始场与伴随场计算优化目标对设计变量的灵敏度"
layout: reference
description: "利用已有原始场与伴随场计算优化目标对设计变量的灵敏度。"
cms_slug: "command-computesensitivities"
---

<p>利用已有原始场与伴随场计算优化目标对设计变量的灵敏度。</p><h2>开始前</h2>
<p>已有完整optimisationDict、优化管理器、目标函数、设计变量，以及相同状态的原始和伴随解。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：计算当前设计灵敏度</h2>
<pre><code class="language-bash">computeSensitivities
</code></pre>
<p>读取优化设置，更新目标函数并计算相应设计变量的灵敏度，写出配置的结果场或设计导数。</p>
<h2>示例 2：使用最新收敛状态</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry startFrom -set latestTime
computeSensitivities
</code></pre>
<p>将读取状态设为最新结果；该时刻需有与目标匹配的原始和伴随场。</p>
<h2>示例 3：核对指定设计迭代</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry startFrom -set startTime
foamDictionary system/controlDict -entry startTime -set 20
computeSensitivities
</code></pre>
<p>时间20保存了完整设计状态时，重算该状态的目标和灵敏度，便于对照设计更新记录。</p>
<h2>示例 4：并行计算设计导数</h2>
<pre><code class="language-bash">mpirun -np 4 computeSensitivities -parallel
</code></pre>
<p>已有4分区原始和伴随解，按同一优化定义汇集各分区贡献，输出对应设计导数。</p>
<h2>示例 5：比较另一目标函数</h2>
<pre><code class="language-bash">computeSensitivities -case ./dragObjective
computeSensitivities -case ./pressureLossObjective
</code></pre>
<p>两案例各自已有对应目标的伴随解和配置；分别输出阻力目标与压降目标的灵敏度，比较设计区域的贡献差异。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/optimisation/computeSensitivities/computeSensitivities.C">源码与说明</a> · <a href="/assets/command-help/computesensitivities.txt">帮助文本</a></p>
