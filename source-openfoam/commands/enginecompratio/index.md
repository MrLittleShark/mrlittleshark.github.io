---
title: "engineCompRatio · 用发动机运动网格的最大、最小体积计算几何压缩比"
layout: reference
description: "用发动机运动网格的最大、最小体积计算几何压缩比。"
cms_slug: "command-enginecompratio"
---

<p>用发动机运动网格的最大、最小体积计算几何压缩比。</p><h2>开始前</h2>
<p>已有发动机网格、engineGeometry和对应engineMesh模型；工具会把网格移动到下止点与上止点位置计算体积。</p>
<h2>示例 1：计算几何压缩比</h2>
<pre><code class="language-bash">engineCompRatio
</code></pre>
<p>日志输出Vmax、Vmin和Vmax/Vmin，可直接核对案例几何压缩比。</p>
<h2>示例 2：比较较大余隙</h2>
<pre><code class="language-bash">foamDictionary constant/engineGeometry -entry clearance -set '[0 1 0 0 0 0 0] 0.002'
engineCompRatio
</code></pre>
<p>在与该余隙一致的发动机几何副本中设置2毫米clearance，再计算上止点体积和压缩比。</p>
<h2>示例 3：比较另一活塞行程</h2>
<pre><code class="language-bash">engineCompRatio -case ./engine-longStroke
</code></pre>
<p>该副本的初始网格和stroke参数已成套更新；比较行程变化后的扫气体积与压缩比。</p>
<h2>示例 4：网格重建后重新核查</h2>
<pre><code class="language-bash">blockMesh -case ./engine-refined
engineCompRatio -case ./engine-refined
</code></pre>
<p>engine-refined已配置相同物理几何的细网格；比较数值体积得到的压缩比随分辨率的变化。</p>
<h2>示例 5：运动预演与压缩比配套检查</h2>
<pre><code class="language-bash">moveEngineMesh -case ./engine-preview
engineCompRatio -case ./engine-reference
</code></pre>
<p>两个独立案例使用相同初始几何；前者查看运动全过程，后者由原始参考网格计算止点体积，便于核对活塞运动模型。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/engineCompRatio/engineCompRatio.C">源码与说明</a> · <a href="/assets/command-help/enginecompratio.txt">帮助文本</a></p>
