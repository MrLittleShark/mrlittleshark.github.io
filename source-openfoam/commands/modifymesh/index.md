---
title: "modifyMesh · 按字典设置修改网格中的点、面和单元连接关系"
layout: reference
description: "按字典设置修改网格中的点、面和单元连接关系。"
cms_slug: "command-modifymesh"
---

<p>按字典设置修改网格中的点、面和单元连接关系。</p><h2>开始前</h2>
<p>准备 system/modifyMeshDict，含 pointsToMove、edgesToSplit、facesToTriangulate、edgesToCollapse、cellsToSplit 五个列表。下列坐标以 0–1 的单六面体为说明，每例从独立原始副本开始，先清空其他操作列表。</p>
<h2>示例 1：移动一个边界点</h2>
<pre><code class="language-bash">foamDictionary system/modifyMeshDict -entry pointsToMove -set '(((0 0 0) (-0.01 0 0)))'
modifyMesh
</code></pre>
<p>每个元素包含两个点：第一个定位原边界点，第二个给出新坐标。这里把原点沿负 x 移动 0.01，输出后检查相邻单元体积和面质量。</p>
<h2>示例 2：在边界边上插入切点</h2>
<pre><code class="language-bash">foamDictionary system/modifyMeshDict -entry edgesToSplit -set '(((0.5 0 0) (0.25 0 0)))'
modifyMesh
</code></pre>
<p>第一个点用于查找 x 轴上的边，第二个点是插入位置。在该边的四分之一处增加切点，检查相关边界面的顶点连接。</p>
<h2>示例 3：把边界面分解为三角面</h2>
<pre><code class="language-bash">foamDictionary system/modifyMeshDict -entry facesToTriangulate -set '(((0.5 0.5 0) (0.5 0.5 0)))'
modifyMesh
</code></pre>
<p>用底面中心定位边界面，并以同一位置作为分解中心。查看生成三角面的数量、方向和总面积。</p>
<h2>示例 4：将单元分为锥形子单元</h2>
<pre><code class="language-bash">foamDictionary system/modifyMeshDict -entry cellsToSplit -set '(((0.5 0.5 0.5) (0.5 0.5 0.5)))'
modifyMesh
</code></pre>
<p>第一个点定位目标单元，第二个指定内部公共顶点。单元按各面与内部顶点构成锥形子单元，检查子单元体积之和与原体积。</p>
<h2>示例 5：使用独立字典并检查结果</h2>
<pre><code class="language-bash">modifyMesh -dict system/modifyMesh-testDict
checkMesh -latestTime -allGeometry -allTopology
</code></pre>
<p>在该字典中明确选择一种修改操作，默认写到新的时间实例。对最新网格检查几何和拓扑，再决定是否把方案用于正式案例。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 modifyMeshDict 文件。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/modifyMesh/cellSplitter.C">源码与说明</a> · <a href="/assets/command-help/modifymesh.txt">帮助文本</a></p>
