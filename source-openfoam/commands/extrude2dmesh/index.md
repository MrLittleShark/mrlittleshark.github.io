---
title: "extrude2DMesh · 将二维网格沿厚度方向挤出为三维体网格"
layout: reference
description: "将二维网格沿厚度方向挤出为三维体网格。"
cms_slug: "command-extrude2dmesh"
---

<p>将二维网格沿厚度方向挤出为三维体网格。</p><h2>开始前</h2>
<p>已有二维输入及system/extrude2DMeshDict。位置参数只接受polyMesh2D或MeshedSurface，大小写按源码填写。</p>
<h2>示例 1：拉伸二维体网格</h2>
<pre><code class="language-bash">extrude2DMesh polyMesh2D
</code></pre>
<p>从polyMesh2D路径构造输入网格，按字典生成三维厚度方向单元，日志显示生成时间。</p>
<h2>示例 2：使用表面网格输入</h2>
<pre><code class="language-bash">extrude2DMesh MeshedSurface
</code></pre>
<p>已有该模式所需的MeshedSurface数据时，选择表面输入通路；字典仍控制拉伸模型和层数。</p>
<h2>示例 3：指定另一个算例</h2>
<pre><code class="language-bash">extrude2DMesh -case ../thinChannel polyMesh2D
</code></pre>
<p>在thinChannel中读取二维网格与拉伸字典，结果也写入该算例。</p>
<h2>示例 4：改变直线拉伸厚度</h2>
<pre><code class="language-bash">foamDictionary system/extrude2DMeshDict -entry linearDirectionCoeffs.thickness -set 0.02
extrude2DMesh polyMesh2D
</code></pre>
<p>前提extrudeModel为linearDirection；将厚度设为0.02m，并检查生成网格的包围盒。</p>
<h2>示例 5：增加三维分辨率</h2>
<pre><code class="language-bash">foamDictionary system/extrude2DMeshDict -entry nLayers -set 5
extrude2DMesh polyMesh2D
checkMesh -latestTime
</code></pre>
<p>把厚度方向改成5层后检查新网格；用于三维计算时，前后边界应采用相应物理类型。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/extrude2DMesh/extrude2DMeshApp.C">源码与说明</a> · <a href="/assets/command-help/extrude2dmesh.txt">帮助文本</a></p>
