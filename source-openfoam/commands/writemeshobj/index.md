---
title: "writeMeshObj · -cell、-face、-point 和 -cellSet 等选项指定诊断对象"
layout: reference
description: "-cell、-face、-point 和 -cellSet 等选项指定诊断对象。"
cms_slug: "command-writemeshobj"
---

<p>-cell、-face、-point 和 -cellSet 等选项指定诊断对象。</p><h2>开始前</h2>
<p>案例已有网格；按编号查看时编号从 0 开始，使用集合选取时需先创建对应 cellSet 或 faceSet。</p>
<h2>示例 1：导出单个单元</h2>
<pre><code class="language-bash">writeMeshObj -cell 0 -constant
</code></pre>
<p>把编号 0 的单元写为 OBJ 几何。终端报告输出文件，可用 ParaView 查看该单元的面、边连接。</p>
<h2>示例 2：检查指定网格面</h2>
<pre><code class="language-bash">writeMeshObj -face 100 -constant
</code></pre>
<p>导出面 100，适合结合 checkMesh 报告定位问题面。前提是网格中确实存在该面编号。</p>
<h2>示例 3：检查一个点的邻域</h2>
<pre><code class="language-bash">writeMeshObj -point 25 -constant
</code></pre>
<p>导出与点 25 相关的几何信息，用于查看局部连接。适合定位重复点、异常边或局部网格畸变。</p>
<h2>示例 4：查看问题单元集合</h2>
<pre><code class="language-bash">writeMeshObj -cellSet badCells -constant
</code></pre>
<p>将已存在的 badCells 单元集合导出。可从检查结果或 topoSet 建立集合，集中查看质量不佳区域。</p>
<h2>示例 5：导出边界的面与边</h2>
<pre><code class="language-bash">writeMeshObj -patchFaces -patchEdges -latestTime
</code></pre>
<p>将最新网格的 patch 面和边写为 OBJ。适合查看动网格最终边界形状以及各 patch 的连接情况。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-cell &lt;cellId&gt;</code></td><td>写出指定单元的点。</td></tr><tr><td><code>-cellSet &lt;name&gt;</code></td><td>写出指定 cellSet 中各单元的点。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-face &lt;faceId&gt;</code></td><td>写出指定的面。</td></tr><tr><td><code>-faceSet &lt;name&gt;</code></td><td>写出指定 faceSet 中各面的点。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-patchEdges</code></td><td>写出边界的外围边。</td></tr><tr><td><code>-patchFaces</code></td><td>写出边界上各面的边。</td></tr><tr><td><code>-point &lt;pointId&gt;</code></td><td>写出指定的点。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（20 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/writeMeshObj/writeMeshObj.C">源码与说明</a> · <a href="/assets/command-help/writemeshobj.txt">帮助文本</a></p>
