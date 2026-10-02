---
title: "subsetMesh · 按 cellSet 或 cellZone 提取子网格并映射场"
layout: reference
description: "按 cellSet 或 cellZone 提取子网格并映射场。"
cms_slug: "command-subsetmesh"
---

<p>按 cellSet 或 cellZone 提取子网格并映射场。</p><h2>开始前</h2>
<p>已有目标cellSet/cellZone；切割后暴露的内部面需要合适的边界patch。</p>
<h2>示例 1：按单元集合提取</h2>
<pre><code class="language-bash">subsetMesh coreCells
</code></pre>
<p>保留 coreCells 中的单元，新增切割面默认进入 oldInternalFaces，并写新网格时间。</p>
<h2>示例 2：指定切割边界名称</h2>
<pre><code class="language-bash">subsetMesh coreCells -patch cutBoundary -overwrite
</code></pre>
<p>cutBoundary 是已准备的目标patch；暴露内部面归入此边界，结果写回当前网格。</p>
<h2>示例 3：按cellZone提取</h2>
<pre><code class="language-bash">subsetMesh -zone rotor -resultTime 2
</code></pre>
<p>把 rotor 解释为cellZone名称，并将子网格写到时间2，便于和原网格分开查看。</p>
<h2>示例 4：合并选择多个zone</h2>
<pre><code class="language-bash">subsetMesh -zone '(fluid "channel.*")' -resultTime 3
</code></pre>
<p>选择 fluid 及匹配 channel.* 的zone，保留它们包含的单元，用于提取相关连通部件。</p>
<h2>示例 5：把切割面分配给最近边界</h2>
<pre><code class="language-bash">subsetMesh coreCells -patches '(inlet outlet walls)' -exclude-patches outlet -overwrite
</code></pre>
<p>已有这些patch时，在候选边界中按最近位置分配暴露面，并排除outlet，减少手工整理切割面的工作。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-exclude-patches &lt;wordRes&gt;</code></td><td>从 -patches 选择中排除一个或多个边界。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-patch &lt;name&gt;</code></td><td>将暴露出的内部面归入指定边界，替代默认的 oldInternalFaces。</td></tr><tr><td><code>-patches &lt;wordRes&gt;</code></td><td>将暴露出的内部面归入候选边界中最近的一个。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-resultTime &lt;time&gt;</code></td><td>指定合并后网格的输出时间目录。</td></tr><tr><td><code>-zone</code></td><td>按 cellZone 选取子网格；位置参数可使用名称列表或正则表达式。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/floatingBody/floatingBody">multiphase/overInterDyMFoam/floatingBody/floatingBody</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/floatingBodyWithSpring/floatingBody">multiphase/overInterDyMFoam/floatingBodyWithSpring/floatingBody</a></li></ul><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/subsetMesh/subsetMesh.C">源码与说明</a> · <a href="/assets/command-help/subsetmesh.txt">帮助文本</a></p>
