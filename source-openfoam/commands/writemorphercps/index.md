---
title: "writeMorpherCPs · 写出体积 B 样条网格变形器的控制点"
layout: reference
description: "写出体积 B 样条网格变形器的控制点。"
cms_slug: "command-writemorphercps"
---

<p>写出体积 B 样条网格变形器的控制点。</p><h2>开始前</h2>
<p>constant/dynamicMeshDict 已含 volumetricBSplinesMotionSolverCoeffs 及各控制盒定义。</p>
<h2>示例 1：导出当前控制点布局</h2>
<pre><code class="language-bash">writeMorpherCPs
</code></pre>
<p>创建字典中每个B样条控制盒对象并写控制点，供查看设计变量在空间中的分布。</p>
<h2>示例 2：检查细化网格上的控制盒</h2>
<pre><code class="language-bash">writeMorpherCPs -case ./optimisation-fineMesh
</code></pre>
<p>细网格案例已有相同物理控制盒设置；输出控制点，比较控制盒与细化边界的相对位置。</p>
<h2>示例 3：比较另一套控制盒布置</h2>
<pre><code class="language-bash">cp -r shapeCase shapeCase-wideBox
# 在 shapeCase-wideBox/constant/dynamicMeshDict 中调整控制盒范围
writeMorpherCPs -case shapeCase-wideBox
</code></pre>
<p>在独立副本中修改既有控制盒的几何定义，再导出；检查设计区域是否覆盖待优化表面。</p>
<h2>示例 4：网格生成后导出控制点</h2>
<pre><code class="language-bash">blockMesh
writeMorpherCPs
</code></pre>
<p>blockMeshDict与变形器字典已配套；先生成当前设计几何网格，再输出控制点用于叠加检查。</p>
<h2>示例 5：与边界几何一起查看</h2>
<pre><code class="language-bash">writeMorpherCPs
foamToVTK -no-fields -no-internal -name VTK-designBoundary
</code></pre>
<p>导出控制点后，另外导出边界网格，在同一视图检查控制点密度与边界曲率、局部细节的对应。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/optimisation/writeMorpherCPs/writeMorpherCPs.C">源码与说明</a> · <a href="/assets/command-help/writemorphercps.txt">帮助文本</a></p>
