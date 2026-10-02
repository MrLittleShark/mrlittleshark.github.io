---
title: "moveEngineMesh · 按发动机曲轴转角设置推进发动机网格运动"
layout: reference
description: "按发动机曲轴转角设置推进发动机网格运动。"
cms_slug: "command-moveenginemesh"
---

<p>按发动机曲轴转角设置推进发动机网格运动。</p><h2>开始前</h2>
<p>已有 engineGeometry、发动机网格运动配置和初始网格；controlDict 的时间设置与 engineTime 的转角约定匹配。</p>
<h2>示例 1：检查完整活塞运动</h2>
<pre><code class="language-bash">moveEngineMesh
</code></pre>
<p>程序按发动机时间循环更新网格，日志以 CA-deg 显示曲轴转角，结果时间保存运动几何。</p>
<h2>示例 2：只检查起始转角段</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry endTime -set 10
moveEngineMesh
</code></pre>
<p>在以曲轴转角为用户时间、起始角小于10的案例中，将终止角设为10度，集中观察这一段活塞运动。</p>
<h2>示例 3：减小转角步长</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry deltaT -set 0.25
moveEngineMesh
</code></pre>
<p>本案例时间步以曲轴角计时；0.25度提供更密的运动状态，可比较单步变形与质量变化。</p>
<h2>示例 4：比较另一发动机几何</h2>
<pre><code class="language-bash">moveEngineMesh -case ./engine-longStroke
</code></pre>
<p>engine-longStroke 已有独立的行程和运动参数；生成该几何的运动序列，和基准案例比较活塞位置。</p>
<h2>示例 5：检查运动末态网格</h2>
<pre><code class="language-bash">moveEngineMesh
checkMesh -latestTime
</code></pre>
<p>先完成运动，再检查最后保存状态的体积和质量，适合检查接近上止点的狭小空间。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/moveEngineMesh/moveEngineMesh.C">源码与说明</a> · <a href="/assets/command-help/moveenginemesh.txt">帮助文本</a></p>
