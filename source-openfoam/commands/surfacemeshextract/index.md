---
title: "surfaceMeshExtract · -patches 指定网格中已有的边界名称"
layout: reference
description: "-patches 指定网格中已有的边界名称。"
cms_slug: "command-surfacemeshextract"
---

<p>-patches 指定网格中已有的边界名称。</p><h2>开始前</h2>
<p>案例已有体网格和边界名称；含 faceZone 的示例还需先建立相应面区域。</p>
<h2>示例 1：提取全部边界</h2>
<pre><code class="language-bash">surfaceMeshExtract boundary.obj -constant
</code></pre>
<p>读取 constant 中的网格边界，输出表面文件。可在几何软件中查看计算域外形以及各边界的分区。</p>
<h2>示例 2：只提取壁面</h2>
<pre><code class="language-bash">surfaceMeshExtract walls.stl -patches '(walls)' -constant
</code></pre>
<p>仅提取名为 walls 的 patch。括号表示名称列表；将名称换成 constant/polyMesh/boundary 中的实际边界名。</p>
<h2>示例 3：按名称匹配并排除</h2>
<pre><code class="language-bash">surfaceMeshExtract body.obj -patches '("wall.*")' -exclude-patches '(wallAux)' -constant
</code></pre>
<p>先匹配 wall 开头的边界，再排除 wallAux。输出用于检查主要壁面，避免把辅助封口面一并导出。</p>
<h2>示例 4：提取内部面区域</h2>
<pre><code class="language-bash">surfaceMeshExtract interface.obj -faceZones '(interfaceZone)' -constant
</code></pre>
<p>把 interfaceZone 中的内部面也加入提取范围。适合查看耦合界面或风扇面的位置；需要该 faceZone 已存在。</p>
<h2>示例 5：提取末时刻移动边界</h2>
<pre><code class="language-bash">surfaceMeshExtract moved.obj -latestTime -patches '(movingWall)'
</code></pre>
<p>读取最新时间对应的网格位置，导出 movingWall。与初始位置的表面对比，可检查动网格位移方向和量级。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-exclude-patches &lt;wordRes&gt;</code></td><td>从 -patches 的选择中排除边界，例如 outlet 或 &#x27;(inlet &quot;.*Wall&quot;)&#x27;。</td></tr><tr><td><code>-excludeProcPatches</code></td><td>排除并行进程之间的边界。</td></tr><tr><td><code>-extractZonePoints</code></td><td>提取所选 faceZone 的点边界。</td></tr><tr><td><code>-faceZones &lt;wordRes&gt;</code></td><td>选择要提取的一个或多个 faceZone，例如 cells 或 &#x27;(slice &quot;mfp-.*&quot;)&#x27;。</td></tr><tr><td><code>-featureAngle &lt;angle&gt;</code></td><td>按特征角自动提取特征边、特征点，并放入独立的点边界。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-patches &lt;wordRes&gt;</code></td><td>选择要提取的边界，例如 top 或 &#x27;(front &quot;.*back&quot;)&#x27;。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（21 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-writeOBJ</code></td><td>将新增 pointPatch 的点写为 OBJ 文件。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshExtract/surfaceMeshExtract.C">源码与说明</a> · <a href="/assets/command-help/surfacemeshextract.txt">帮助文本</a></p>
