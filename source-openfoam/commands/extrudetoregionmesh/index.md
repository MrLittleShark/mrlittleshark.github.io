---
title: "extrudeToRegionMesh · 将选定面集挤出为独立网格区域，用于薄层、液膜等模型"
layout: reference
description: "将选定面集挤出为独立网格区域，用于薄层、液膜等模型。"
cms_slug: "command-extrudetoregionmesh"
---

<p>将选定面集挤出为独立网格区域，用于薄层、液膜等模型。</p><h2>开始前</h2>
<p>已有faceZone或faceSet以及system/extrudeToRegionMeshDict；字典给出新region名、源面、厚度、层数和映射方式。</p>
<h2>示例 1：生成壁膜区域</h2>
<pre><code class="language-bash">extrudeToRegionMesh
</code></pre>
<p>按默认定义从源面拉伸出新区域，例如wallFilmRegion，输出新的区域网格及界面设置。</p>
<h2>示例 2：选择固体板方案</h2>
<pre><code class="language-bash">extrudeToRegionMesh -dict system/extrudeToRegionMeshDict.panel
</code></pre>
<p>在完整panel定义中指定region panelRegion，生成固体板区域，适合共轭传热或热解模型。</p>
<h2>示例 3：加密厚度方向</h2>
<pre><code class="language-bash">foamDictionary system/extrudeToRegionMeshDict -entry nLayers -set 8
extrudeToRegionMesh
</code></pre>
<p>同一源面、同一厚度下生成8层；线性均匀拉伸且expansionRatio=1时每层厚度为总厚度的1/8。</p>
<h2>示例 4：从指定体区域拉伸</h2>
<pre><code class="language-bash">extrudeToRegionMesh -region air -dict system/extrudeToRegionMeshDict.panel
</code></pre>
<p>源面位于air区域时选择该体网格，避免在默认区域查找同名faceZone。</p>
<h2>示例 5：建立并检查新区域</h2>
<pre><code class="language-bash">extrudeToRegionMesh
checkMesh -region panelRegion
</code></pre>
<p>字典中的region必须为panelRegion；检查生成区域的单元体积、厚度及耦合面，确认它可供后续区域求解。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 extrudeToRegionMeshDict 文件。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/extrude/extrudeToRegionMesh/extrudeToRegionMesh.C">源码与说明</a> · <a href="/assets/command-help/extrudetoregionmesh.txt">帮助文本</a></p>
