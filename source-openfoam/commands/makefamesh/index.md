---
title: "makeFaMesh · v2512 的常用字典位置为 system/finite-area/faMeshDefiniti"
layout: reference
description: "v2512 的常用字典位置为 system/finite-area/faMeshDefinition。"
cms_slug: "command-makefamesh"
---

<p>v2512 的常用字典位置为 system/finite-area/faMeshDefinition。</p><h2>开始前</h2>
<p>已有体网格及与其patch匹配的faMeshDefinition；命名面积区域还需对应区域配置。</p>
<h2>示例 1：先构造但不保存</h2>
<pre><code class="language-bash">makeFaMesh -dry-run
</code></pre>
<p>读取定义并尝试构造面积网格，先检查边界选择和连接关系，暂不写网格。</p>
<h2>示例 2：生成默认面积网格</h2>
<pre><code class="language-bash">makeFaMesh
</code></pre>
<p>从定义选定的体网格边界面创建有限面积网格，供液膜或壳体模型使用。</p>
<h2>示例 3：使用另一份定义</h2>
<pre><code class="language-bash">makeFaMesh -dict system/faMeshDefinition.test
</code></pre>
<p>已准备该完整定义时选择它，适合对照不同patch组合；字典路径由-dict明确指定。</p>
<h2>示例 4：生成命名区域并输出图形</h2>
<pre><code class="language-bash">makeFaMesh -area-region film -write-vtk -write-edges-obj
</code></pre>
<p>生成film面积网格，同时导出面与边的可视化数据，检查薄膜边界是否闭合。</p>
<h2>示例 5：在分区网格上生成</h2>
<pre><code class="language-bash">mpirun -np 4 makeFaMesh -parallel -area-region film -no-fields
</code></pre>
<p>4个体网格分区已经存在；生成面积网格及分区寻址，-no-fields暂不分解面积场。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allAreas</code></td><td>选择有限面积 regionProperties 中的全部区域。</td></tr><tr><td><code>-area-region &lt;name&gt;</code></td><td>指定有限面积网格区域，例如 -area-region shell。</td></tr><tr><td><code>-area-regions &lt;wordRes&gt;</code></td><td>选择有限面积区域，例如 -area-regions film；也可按 regionProperties 中的名称匹配，如 -area-regions &#x27;(film &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 faMeshDefinition 文件。</td></tr><tr><td><code>-dry-run</code></td><td>创建网格但暂不写入文件。</td></tr><tr><td><code>-empty-patch &lt;name&gt;</code></td><td>为默认的 empty 边界指定名称。</td></tr><tr><td><code>-no-decompose</code></td><td>并行运行时跳过 procAddressing 生成和场分解。</td></tr><tr><td><code>-no-fields</code></td><td>并行运行时跳过场分解。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-write-edges-obj</code></td><td>将网格边写为 OBJ 文件，每个进程各输出一份。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（20 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-write-vtk</code></td><td>将网格写为 VTP（VTK）文件，便于显示或调试。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/finiteArea/makeFaMesh/makeFaMesh.C">源码与说明</a> · <a href="/assets/command-help/makefamesh.txt">帮助文本</a></p>
