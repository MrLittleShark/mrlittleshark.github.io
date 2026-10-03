---
title: "PDRMesh · 按阻塞单元和阻塞面集合修改网格，并更新 PDR 算例的场数据"
layout: reference
description: "按阻塞单元和阻塞面集合修改网格，并更新 PDR 算例的场数据。"
cms_slug: "command-pdrmesh"
---

<p>按阻塞单元和阻塞面集合修改网格，并更新 PDR 算例的场数据。</p><h2>开始前</h2>
<p>已有 PDR 网格、system/PDRMeshDict、blockedCells 单元集及需要的面集；blockedFaces 的目标 patch 必须已存在。示例在案例副本执行。</p>
<h2>示例 1：移除阻塞单元并生成边界</h2>
<pre><code class="language-bash">PDRMesh
</code></pre>
<p>按 PDRMeshDict 的 blockedCells 删除阻塞区域，将暴露面放到指定 patch，结果写入后续时间。检查日志中的保留单元数和新边界面数。</p>
<h2>示例 2：指定阻塞单元集合</h2>
<pre><code class="language-bash">foamDictionary system/PDRMeshDict -entry blockedCells -set obstacleCells
PDRMesh
</code></pre>
<p>前提是 obstacleCells 已准备好。更换被排除的单元区域，可以比较不同障碍物布置对有效流体域的影响。</p>
<h2>示例 3：为阻塞面设置目标边界</h2>
<pre><code class="language-bash">foamDictionary system/PDRMeshDict -entry blockedFaces -set '((screenFaces screenWall))'
PDRMesh
</code></pre>
<p>把 screenFaces 中的阻塞面分配到已有 screenWall patch。检查两侧挡板面及由删除单元暴露的面是否得到正确分组。</p>
<h2>示例 4：设置其他暴露面的归属</h2>
<pre><code class="language-bash">foamDictionary system/PDRMeshDict -entry defaultPatch -set obstacleWall
PDRMesh -overwrite
</code></pre>
<p>未被 blockedFaces 等条目明确分配的暴露面进入 obstacleWall。-overwrite 把结果写回原网格位置，运行前使用可恢复的独立副本。</p>
<h2>示例 5：在分解网格上处理</h2>
<pre><code class="language-bash">mpirun -np 4 PDRMesh -parallel -overwrite
mpirun -np 4 checkMesh -parallel
</code></pre>
<p>前提是网格、集合及 PDR 设置已一致分解为四个子域。并行处理后检查跨处理器连接以及新生成边界。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/PDRMesh/PDRMesh.C">源码与说明</a> · <a href="/assets/command-help/pdrmesh.txt">帮助文本</a></p>
