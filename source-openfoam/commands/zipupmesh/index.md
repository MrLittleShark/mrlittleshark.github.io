---
title: "zipUpMesh · 补齐含悬挂顶点的面连接，使多面体单元表面闭合"
layout: reference
description: "补齐含悬挂顶点的面连接，使多面体单元表面闭合。"
cms_slug: "command-zipupmesh"
---

<p>补齐含悬挂顶点的面连接，使多面体单元表面闭合。</p><h2>开始前</h2>
<p>输入网格的几何形状有效，但部分面边连接存在悬挂顶点；程序会更新网格拓扑。</p>
<h2>示例 1：修补悬挂顶点连接</h2>
<pre><code class="language-bash">zipUpMesh
</code></pre>
<p>读取网格并补齐单元面之间的边点连接，输出修补后的网格和处理统计。</p>
<h2>示例 2：修补后检查拓扑</h2>
<pre><code class="language-bash">zipUpMesh
checkMesh -allTopology
</code></pre>
<p>重点检查面连接和单元闭合，观察修补后原先的拓扑问题是否消失。</p>
<h2>示例 3：单独处理指定区域</h2>
<pre><code class="language-bash">zipUpMesh -region fluid
checkMesh -region fluid -allTopology
</code></pre>
<p>多区域案例只修补fluid，便于把问题定位到某个区域而保留其他区域的拓扑。</p>
<h2>示例 4：在独立副本上比较修补结果</h2>
<pre><code class="language-bash">cp -r importedMesh importedMesh-zipped
zipUpMesh -case importedMesh-zipped
checkMesh -case importedMesh-zipped
</code></pre>
<p>保留导入原网格，在副本中修补，再比较两份网格的连接与质量报告。</p>
<h2>示例 5：导出修补后的几何</h2>
<pre><code class="language-bash">zipUpMesh
foamToVTK -no-fields -name VTK-zipped
</code></pre>
<p>修补后仅转换网格几何，在ParaView中检查原先悬挂顶点附近的面是否闭合。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/zipUpMesh/zipUpMesh.C">源码与说明</a> · <a href="/assets/command-help/zipupmesh.txt">帮助文本</a></p>
