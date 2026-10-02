---
title: "blockMesh · 读取 blockMeshDict，生成由六面体块组成的网格"
layout: reference
description: "读取 blockMeshDict，生成由六面体块组成的网格。"
cms_slug: "command-blockmesh"
---

<p>读取 blockMeshDict，生成由六面体块组成的网格。</p><h2>开始前</h2>
<p>准备system/blockMeshDict；新网格会写入选定算例，已有网格的比较请使用独立副本。</p>
<h2>示例 1：生成方腔网格</h2>
<pre><code class="language-bash">blockMesh
checkMesh -constant
</code></pre>
<p>读取默认字典生成constant/polyMesh，再检查单元数、体积和边界；20×20×1块应得到400单元。</p>
<h2>示例 2：预览块拓扑</h2>
<pre><code class="language-bash">blockMesh -write-vtk
</code></pre>
<p>导出块拓扑VTU后退出，适合在实际细分前检查顶点连接与块的位置。</p>
<h2>示例 3：预览块边和中心</h2>
<pre><code class="language-bash">blockMesh -write-obj
</code></pre>
<p>导出块边及中心OBJ后退出，可排查弧线、边连接或顶点编号问题。</p>
<h2>示例 4：选择另一套划分</h2>
<pre><code class="language-bash">blockMesh -dict system/blockMeshDict.fine -time 1
</code></pre>
<p>用完整fine字典生成时间1的网格，便于与constant基准比较单元数量和分辨率。</p>
<h2>示例 5：创建命名区域及集合</h2>
<pre><code class="language-bash">blockMesh -region fluid -dict system/fluid/blockMeshDict -sets
</code></pre>
<p>为fluid区域生成网格；字典中命名的cellZones同时写成cellSets，便于后续集合操作。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 blockMeshDict 文件。</td></tr><tr><td><code>-merge-points</code></td><td>按点的几何位置合并网格，替代按拓扑关系合并；这是 v1912 及更早版本的默认方式。</td></tr><tr><td><code>-no-clean</code></td><td>保留 polyMesh/ 目录及已有文件。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-sets</code></td><td>将 cellZone 同时写为 cellSet，便于后续处理。</td></tr><tr><td><code>-time &lt;time&gt;</code></td><td>指定网格写入的时间目录，默认为 constant。</td></tr><tr><td><code>-verbose</code></td><td>显示详细输出；可重复使用。</td></tr><tr><td><code>-write-obj</code></td><td>将块的边与中心写为 OBJ 文件并退出。</td></tr><tr><td><code>-write-vtk</code></td><td>将块拓扑写为 VTU 文件并退出。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-blockmeshdict/">blockMeshDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/sphere">mesh/blockMesh/sphere</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/sphere7">mesh/blockMesh/sphere7</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/mergePairs">mesh/blockMesh/mergePairs</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/spheroidProjected">mesh/blockMesh/spheroidProjected</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/spheroid7Projected">mesh/blockMesh/spheroid7Projected</a></li></ul><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/blockMesh/blockMesh.C">源码与说明</a> · <a href="/assets/command-help/blockmesh.txt">帮助文本</a></p>
