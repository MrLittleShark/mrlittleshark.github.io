---
title: "flattenMesh · 把二维笛卡尔网格的前后顶点校正到两个平面"
layout: reference
description: "把二维笛卡尔网格的前后顶点校正到两个平面。"
cms_slug: "command-flattenmesh"
---

<p>把二维笛卡尔网格的前后顶点校正到两个平面。</p><h2>开始前</h2>
<p>网格已有正确的二维 empty 边界，前后面沿同一坐标方向；程序直接重写所读 points。</p>
<h2>示例 1：校正轻微不共面的顶点</h2>
<pre><code class="language-bash">flattenMesh
</code></pre>
<p>程序识别二维法向，把两侧顶点分别放到包围盒的两个端平面，输出修正后的 points 路径。</p>
<h2>示例 2：在案例副本上比较几何</h2>
<pre><code class="language-bash">cp -r planarCase planarCase-flat
flattenMesh -case planarCase-flat
</code></pre>
<p>输入 planarCase 为现有薄层二维网格；结果写在独立副本，便于并排查看前后面平整程度。</p>
<h2>示例 3：和网格检查连续使用</h2>
<pre><code class="language-bash">flattenMesh
checkMesh -allGeometry
</code></pre>
<p>完成平面校正后检查几何，重点观察二维方向、面平面性和单元体积。拓扑仍来自原网格。</p>
<h2>示例 4：处理导入的二维网格</h2>
<pre><code class="language-bash">fluentMeshToFoam channel.msh
flattenMesh
checkMesh
</code></pre>
<p>channel.msh 已按薄层二维方式生成并含可识别的 empty 边界；导入后校正坐标舍入误差，再检查网格。</p>
<h2>示例 5：导出校正后的几何</h2>
<pre><code class="language-bash">flattenMesh
foamToVTK -no-fields -name VTK-flat
</code></pre>
<p>将校正后的网格导出到 VTK-flat，关闭场输出；可在 ParaView 中检查前后平面和薄层厚度。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/flattenMesh/flattenMesh.C">源码与说明</a> · <a href="/assets/command-help/flattenmesh.txt">帮助文本</a></p>
