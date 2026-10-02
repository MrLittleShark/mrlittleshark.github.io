---
title: "surfaceRedistributePar · 示例采用 4 个进程，并读取 constant/triSurface/body.stl"
layout: reference
description: "示例采用 4 个进程，并读取 constant/triSurface/body.stl。分配方式包括 follow、independent、distributed 和 frozen；follow 按网格包围盒划分。"
cms_slug: "command-surfaceredistributepar"
---

<p>示例采用 4 个进程，并读取 constant/triSurface/body.stl。分配方式包括 follow、independent、distributed 和 frozen；follow 按网格包围盒划分。</p><h2>开始前</h2>
<p>准备已分解的体网格、system/decomposeParDict 和 constant/triSurface/body.stl；MPI 进程数应等于子域数。操作写入分区表面，宜在案例副本内进行。</p>
<h2>示例 1：按两个网格子域分配表面</h2>
<pre><code class="language-bash">mpirun -np 2 surfaceRedistributePar body.stl follow -parallel
</code></pre>
<p>follow 按各进程网格边界框分配相交三角面。完成后各进程拥有其局部网格需要查询的表面部分。</p>
<h2>示例 2：在四个子域使用同一流程</h2>
<pre><code class="language-bash">mpirun -np 4 surfaceRedistributePar body.stl follow -parallel
</code></pre>
<p>适用于已分为四个子域的案例。比较各进程报告的表面规模，可判断几何在当前网格分区中的负载分布。</p>
<h2>示例 3：保留网格之外的三角面</h2>
<pre><code class="language-bash">mpirun -np 2 surfaceRedistributePar body.stl follow -keepNonMapped -parallel
</code></pre>
<p>保留没有映射到当前网格边界框的表面三角形。适合后续网格范围还会扩展、需要保留完整几何的工作流程。</p>
<h2>示例 4：按表面独立分配</h2>
<pre><code class="language-bash">mpirun -np 2 surfaceRedistributePar body.stl independent -parallel
</code></pre>
<p>独立确定表面的分布，而不是逐步跟随体网格边界框。对照 follow 的各进程三角面数，评估所选分配方式的负载。</p>
<h2>示例 5：重新分配已有分区表面</h2>
<pre><code class="language-bash">mpirun -np 2 surfaceRedistributePar body.stl follow -parallel -case ../redistributedCase
</code></pre>
<p>目标案例需已经完成体网格重新分区。工具可读取已有分区表面，并使其分布跟随新网格，供后续并行几何查询使用。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-keepNonMapped</code></td><td>保留网格包围范围以外的表面。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceRedistributePar/surfaceRedistributePar.C">源码与说明</a> · <a href="/assets/command-help/surfaceredistributepar.txt">帮助文本</a></p>
