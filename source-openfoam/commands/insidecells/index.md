---
title: "insideCells · 按单元中心是否位于封闭表面内部创建 cellSet"
layout: reference
description: "按单元中心是否位于封闭表面内部创建 cellSet。"
cms_slug: "command-insidecells"
---

<p>按单元中心是否位于封闭表面内部创建 cellSet。</p><h2>开始前</h2>
<p>已生成体网格；输入曲面必须封闭、单连通，曲面与网格使用同一坐标和单位。</p>
<h2>示例 1：选出球体内的单元</h2>
<pre><code class="language-bash">insideCells constant/triSurface/sphere.stl sphereCells
</code></pre>
<p>第一个参数是封闭曲面，第二个是输出 cellSet 名；中心位于球内的单元写入 sphereCells。</p>
<h2>示例 2：检查选区位置</h2>
<pre><code class="language-bash">insideCells constant/triSurface/solid.stl solidCells
foamToVTK -cellSet solidCells -no-fields
</code></pre>
<p>先创建选区，再仅导出这些单元的几何，检查曲面与网格是否对齐。</p>
<h2>示例 3：将选区变成体区域</h2>
<pre><code class="language-bash">insideCells constant/triSurface/heater.stl heater
setsToZones -noFlipMap
</code></pre>
<p>建立 heater cellSet，再生成同名 cellZone，供体积热源或多孔区模型引用；-noFlipMap 简化可能同时存在的 faceSet 转换。</p>
<h2>示例 4：从曲面内提取子网格</h2>
<pre><code class="language-bash">insideCells constant/triSurface/core.stl coreCells
subsetMesh coreCells -resultTime 1
</code></pre>
<p>先选 coreCells，再把所选单元组成子网格并写到时间 1。新增切割面默认进入 oldInternalFaces。</p>
<h2>示例 5：选择另一个案例中的物体</h2>
<pre><code class="language-bash">insideCells -case ./fineMesh ./geometry/body.stl bodyCells
</code></pre>
<p>fineMesh 是已有细网格案例；曲面路径按当前工作目录提供，-case 指定 cellSet 写入的目标案例，用于网格细化后的同一几何选区。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/insideCells/insideCells.C">源码与说明</a> · <a href="/assets/command-help/insidecells.txt">帮助文本</a></p>
