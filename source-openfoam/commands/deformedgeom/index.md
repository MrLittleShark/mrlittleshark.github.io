---
title: "deformedGeom · 用名为 U 的单元位移场生成变形网格"
layout: reference
description: "用名为 U 的单元位移场生成变形网格。"
cms_slug: "command-deformedgeom"
---

<p>用名为 U 的单元位移场生成变形网格。</p><h2>开始前</h2>
<p>时间目录中已有 volVectorField U，其物理意义为位移；程序将它插值到顶点，再乘位置参数 factor。各例使用同一未变形网格的独立副本。</p>
<h2>示例 1：显示实际位移</h2>
<pre><code class="language-bash">deformedGeom 1
</code></pre>
<p>系数 1 采用原位移幅值。程序遍历结果时间，在存在 U 的时刻写出变形网格，适合结构位移结果的几何显示。</p>
<h2>示例 2：放大微小变形</h2>
<pre><code class="language-bash">deformedGeom 20
</code></pre>
<p>顶点位移乘 20，便于观察很小的挠曲。所得几何用于放大显示，空间尺寸中的变形量已改变。</p>
<h2>示例 3：缩小显示幅度</h2>
<pre><code class="language-bash">deformedGeom 0.2
</code></pre>
<p>将位移缩到原来的五分之一；对大位移数据可先检查整体变形趋势，输出仍覆盖该副本的结果网格。</p>
<h2>示例 4：比较正反方向</h2>
<pre><code class="language-bash">deformedGeom -case ./reverseView -1
</code></pre>
<p>reverseView 中保存原网格与位移结果；负系数把每个顶点沿相反位移方向移动，适合检查位移符号约定。</p>
<h2>示例 5：检查放大后的网格质量</h2>
<pre><code class="language-bash">deformedGeom 5
checkMesh -latestTime
</code></pre>
<p>先生成五倍位移几何，再检查最后时刻的体积和质量指标；局部负体积能指出放大后发生穿越的位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/deformedGeom/deformedGeom.C">源码与说明</a> · <a href="/assets/command-help/deformedgeom.txt">帮助文本</a></p>
