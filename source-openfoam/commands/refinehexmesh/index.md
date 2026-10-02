---
title: "refineHexMesh · 待细化集合可通过 topoSet 建立"
layout: reference
description: "待细化集合可通过 topoSet 建立。"
cms_slug: "command-refinehexmesh"
---

<p>待细化集合可通过 topoSet 建立。</p><h2>开始前</h2>
<p>网格由可进行 2×2×2 细化的六面体构成，并已有目标 cellSet；按几何选集时可先使用 topoSet。</p>
<h2>示例 1：细化选定单元</h2>
<pre><code class="language-bash">refineHexMesh refineCells
</code></pre>
<p>将 refineCells 中的六面体细分，工具会根据相邻细化等级关系调整实际选区。查看日志中的选中与最终细化单元数。</p>
<h2>示例 2：缩小选集以满足等级约束</h2>
<pre><code class="language-bash">refineHexMesh refineCells -minSet
</code></pre>
<p>通过从原选集中删减单元来满足细化约束；默认处理倾向于扩大选集。适合希望细化尽量局限在指定区域的情况。</p>
<h2>示例 3：直接更新案例副本</h2>
<pre><code class="language-bash">refineHexMesh refineCells -overwrite
checkMesh -constant
</code></pre>
<p>将细化结果写回原网格位置。检查单元数、网格连接和物理场映射，再继续计算。</p>
<h2>示例 4：细化命名区域</h2>
<pre><code class="language-bash">refineHexMesh hotCells -region solid
</code></pre>
<p>读取 solid 区域及其 hotCells 集合，只处理该区域的网格。适合局部加密固体传热区，需检查区域接口的一致性。</p>
<h2>示例 5：并行细化</h2>
<pre><code class="language-bash">mpirun -np 4 refineHexMesh refineCells -parallel -overwrite
mpirun -np 4 checkMesh -parallel
</code></pre>
<p>前提是网格与 refineCells 已分解到四个子域。并行细化后检查子域连接和各进程单元数量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-minSet</code></td><td>从待细化 cellSet 中移除部分单元以满足 2:1 尺度比；默认方式是扩展集合。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/refineHexMesh/refineHexMesh.C">源码与说明</a> · <a href="/assets/command-help/refinehexmesh.txt">帮助文本</a></p>
