---
title: "foamyHexMesh · 根据几何表面和尺寸控制，生成以六面体为主的贴体网格"
layout: reference
description: "根据几何表面和尺寸控制，生成以六面体为主的贴体网格。"
cms_slug: "command-foamyhexmesh"
---

<p>根据几何表面和尺寸控制，生成以六面体为主的贴体网格。</p><h2>开始前</h2>
<p>准备完整foamyHexMeshDict与constant/triSurface几何；locationInMesh位于目标流体域，第三方依赖及程序已安装。</p>
<h2>示例 1：检查输入几何</h2>
<pre><code class="language-bash">foamyHexMesh -checkGeometry
</code></pre>
<p>读取字典中的全部表面并检查几何质量，先处理孔洞、交叉或区域选择问题。</p>
<h2>示例 2：生成Voronoi网格</h2>
<pre><code class="language-bash">foamyHexMesh
</code></pre>
<p>按尺寸、方向和表面贴合控制生成网格，日志显示初始点、贴合与平滑过程。</p>
<h2>示例 3：只做初始点贴合</h2>
<pre><code class="language-bash">foamyHexMesh -conformationOnly
</code></pre>
<p>已有合适初始点配置时，仅对初始点执行表面贴合，便于分离检查后续点运动的影响。</p>
<h2>示例 4：比较局部加密方案</h2>
<pre><code class="language-bash">foamyHexMesh -case ../foamyFine
</code></pre>
<p>fine副本已改变shapeControlFunctions的目标尺寸；单独生成后比较小间隙单元数和表面分辨率。</p>
<h2>示例 5：并行生成网格</h2>
<pre><code class="language-bash">mpirun -np 4 foamyHexMesh -parallel
</code></pre>
<p>按算例的并行准备流程设置4个分区及decomposeParDict，再并行运行，检查各进程分配与最终网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-checkGeometry</code></td><td>检查全部表面几何的质量。</td></tr><tr><td><code>-conformationOnly</code></td><td>仅使网格贴合初始点，保持点的位置固定。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/flange">mesh/foamyHexMesh/flange</a></li></ul><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/foamyMesh/foamyHexMesh/foamyHexMesh.C">源码与说明</a> · <a href="/assets/command-help/foamyhexmesh.txt">帮助文本</a></p>
