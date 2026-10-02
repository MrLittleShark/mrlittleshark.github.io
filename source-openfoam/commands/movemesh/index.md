---
title: "moveMesh · 用 motionSolver 推进网格运动"
layout: reference
description: "用 motionSolver 推进网格运动。"
cms_slug: "command-movemesh"
---

<p>用 motionSolver 推进网格运动。</p><h2>开始前</h2>
<p>已有 motionSolver 所需字典和运动场；controlDict 给出基础时间设置。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：按案例设置运动</h2>
<pre><code class="language-bash">moveMesh
</code></pre>
<p>读取运动求解器，逐步计算顶点位置并写结果，适合独立检查给定位移或速度边界。</p>
<h2>示例 2：快速检查短时间运动</h2>
<pre><code class="language-bash">moveMesh -endTime 0.02
</code></pre>
<p>-endTime 临时覆盖终止时间，在已知起始时间小于0.02的案例中只预演初始阶段。</p>
<h2>示例 3：采用更细时间步</h2>
<pre><code class="language-bash">moveMesh -deltaT 0.001 -endTime 0.1
</code></pre>
<p>每步0.001秒，运行至0.1秒；更密的几何状态便于观察运动边界与内部网格响应。</p>
<h2>示例 4：比较较大的运动步长</h2>
<pre><code class="language-bash">moveMesh -case ./motion-coarseStep -deltaT 0.01 -endTime 0.1
</code></pre>
<p>在同一初态的独立副本上把时间步增大到0.01，比较最终顶点位置和中间网格质量。</p>
<h2>示例 5：并行推进运动</h2>
<pre><code class="language-bash">decomposePar
mpirun -np 4 moveMesh -parallel -deltaT 0.001 -endTime 0.1
</code></pre>
<p>已有4分区设置，运动求解在各分区执行并交换边界数据，输出 processor 目录下的运动网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-deltaT &lt;time&gt;</code></td><td>覆盖 deltaT 设置，例如用于加速运动测试。</td></tr><tr><td><code>-endTime &lt;time&gt;</code></td><td>覆盖 endTime 设置，例如用于缩短测试。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/moveMesh/moveMesh.C">源码与说明</a> · <a href="/assets/command-help/movemesh.txt">帮助文本</a></p>
