---
title: "checkFaMesh · 检查对象为有限面积网格"
layout: reference
description: "检查对象为有限面积网格。"
cms_slug: "command-checkfamesh"
---

<p>检查对象为有限面积网格。</p><h2>开始前</h2>
<p>已由 makeFaMesh 建立有限面积网格。area-region 指面积网格区域，region 指其所属体网格区域。</p>
<h2>示例 1：检查默认面积网格</h2>
<pre><code class="language-bash">checkFaMesh
</code></pre>
<p>读取默认有限面积网格，报告面、边及几何检查结果。</p>
<h2>示例 2：输出可视化网格</h2>
<pre><code class="language-bash">checkFaMesh -write-vtk
</code></pre>
<p>在检查时写出VTP网格，可在ParaView定位异常边或面。</p>
<h2>示例 3：检查指定薄膜区域</h2>
<pre><code class="language-bash">checkFaMesh -area-region film
</code></pre>
<p>已有名为film的面积网格时，仅检查它，便于排查多个面积区域中的问题。</p>
<h2>示例 4：检查所有面积区域</h2>
<pre><code class="language-bash">checkFaMesh -allAreas -write-vtk
</code></pre>
<p>按有限面积regionProperties逐个检查，并输出各区域可视化文件。</p>
<h2>示例 5：检查已分区网格</h2>
<pre><code class="language-bash">mpirun -np 4 checkFaMesh -parallel -area-region film
</code></pre>
<p>前提是4个分区中已有匹配的面积网格；检查并行分区及耦合边连接。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allAreas</code></td><td>选择有限面积 regionProperties 中的全部区域。</td></tr><tr><td><code>-area-region &lt;name&gt;</code></td><td>指定有限面积网格区域，例如 -area-region shell。</td></tr><tr><td><code>-area-regions &lt;wordRes&gt;</code></td><td>选择有限面积区域，例如 -area-regions film；也可按 regionProperties 中的名称匹配，如 -area-regions &#x27;(film &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-geometryOrder &lt;N&gt;</code></td><td>测试不同的几何计算阶次；此项为实验功能。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-write-vtk</code></td><td>将网格写为 VTP（VTK）文件，便于显示或调试。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/finiteArea/checkFaMesh/checkFaMesh.C">源码与说明</a> · <a href="/assets/command-help/checkfamesh.txt">帮助文本</a></p>
