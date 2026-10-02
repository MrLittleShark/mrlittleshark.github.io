---
title: "removeFaces · 输入为预先建立的 faceSet"
layout: reference
description: "输入为预先建立的 faceSet。"
cms_slug: "command-removefaces"
---

<p>输入为预先建立的 faceSet。</p><h2>开始前</h2>
<p>已有 faceSet，内含拟移除的内部面；移除这些面会合并相邻单元。使用案例副本并检查合并后单元形状。</p>
<h2>示例 1：合并指定内部面两侧的单元</h2>
<pre><code class="language-bash">removeFaces internalFaces
</code></pre>
<p>读取 internalFaces，执行内部面移除与单元合并，结果写入新的网格实例。检查单元数是否按预期减少。</p>
<h2>示例 2：从几何选区建立移除面集</h2>
<pre><code class="language-bash">topoSet -dict system/topoSet-removeFacesDict
removeFaces mergeFaces
</code></pre>
<p>前提是该 topoSet 字典生成只含目标内部面的 mergeFaces。先在可视化中检查选区，再合并这些面的相邻单元。</p>
<h2>示例 3：把修改限制在独立案例</h2>
<pre><code class="language-bash">removeFaces internalFaces -case ../mergeTest
checkMesh -case ../mergeTest -latestTime -allGeometry
</code></pre>
<p>使用 mergeTest 的面集和网格，检查生成的多面体体积、凹性及面质量。</p>
<h2>示例 4：将确认的修改写回原实例</h2>
<pre><code class="language-bash">removeFaces internalFaces -overwrite
checkMesh -constant -allTopology
</code></pre>
<p>适合已经在副本验证过的面集。更新原网格位置后，检查内部面与边界连接并核对已有场数据。</p>
<h2>示例 5：并行合并单元</h2>
<pre><code class="language-bash">mpirun -np 4 removeFaces internalFaces -parallel -overwrite
mpirun -np 4 checkMesh -parallel
</code></pre>
<p>网格和面集需已一致分解到四个子域。并行运行后检查处理器界面，确认跨分区连接保持一致。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/removeFaces/removeFaces.C">源码与说明</a> · <a href="/assets/command-help/removefaces.txt">帮助文本</a></p>
