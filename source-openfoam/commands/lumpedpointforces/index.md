---
title: "lumpedPointForces · 从压力场提取 lumped-point 运动区域的合力和力矩"
layout: reference
description: "从压力场提取 lumped-point 运动区域的合力和力矩。"
cms_slug: "command-lumpedpointforces"
---

<p>从压力场提取 lumped-point 运动区域的合力和力矩。</p><h2>开始前</h2>
<p>案例采用lumpedPoint边界及运动描述，所选时间已有p；压力积分区域与参考点设置完整。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：提取最终载荷</h2>
<pre><code class="language-bash">lumpedPointForces -latestTime
</code></pre>
<p>读取最新压力，按集中点控制区计算合力、力矩并打印，适合核对结构输入载荷。</p>
<h2>示例 2：输出载荷可视化</h2>
<pre><code class="language-bash">lumpedPointForces -latestTime -vtk
</code></pre>
<p>额外生成力和力矩的VTP几何及文件序列，便于查看各控制点的载荷方向。</p>
<h2>示例 3：提取整个载荷阶段</h2>
<pre><code class="language-bash">lumpedPointForces -time '0.1:1' -vtk
</code></pre>
<p>对区间内已有时刻计算，形成载荷随时间变化的可视化序列。</p>
<h2>示例 4：只处理指定流体区域</h2>
<pre><code class="language-bash">lumpedPointForces -region fluid -latestTime -vtk
</code></pre>
<p>多区域案例中从fluid的p与耦合边界提取载荷，结果对应该区域的控制点。</p>
<h2>示例 5：并行场的载荷积分</h2>
<pre><code class="language-bash">mpirun -np 4 lumpedPointForces -parallel -latestTime -vtk
</code></pre>
<p>已有4分区且lumped-point设置一致；归集各分区压力贡献，得到全局控制区合力和力矩。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-vtk</code></td><td>生成力数据的可视化文件。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lumped/lumpedPointForces/lumpedPointForces.C">源码与说明</a> · <a href="/assets/command-help/lumpedpointforces.txt">帮助文本</a></p>
