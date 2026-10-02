---
title: "tetgenToFoam · 按前缀读取配套的 node、ele 和 face 等文件"
layout: reference
description: "按前缀读取配套的 node、ele 和 face 等文件。"
cms_slug: "command-tetgentofoam"
---

<p>按前缀读取配套的 node、ele 和 face 等文件。</p><h2>开始前</h2>
<p>准备 TetGen 同名前缀的 .node、.ele 和 .face 文件；边界标记用于建立表面分区。</p>
<h2>示例 1：按前缀导入</h2>
<pre><code class="language-bash">tetgenToFoam mesh.1
</code></pre>
<p>读取 mesh.1.node、mesh.1.ele 和 mesh.1.face，建立四面体网格。检查边界标记对应的 patch 数量。</p>
<h2>示例 2：仅使用节点与单元文件</h2>
<pre><code class="language-bash">tetgenToFoam mesh.1 -noFaceFile
</code></pre>
<p>适用于没有 .face 文件的输入。网格仍可由节点和单元建立，所需边界分区需要后续按几何重新配置。</p>
<h2>示例 3：检查四面体质量</h2>
<pre><code class="language-bash">tetgenToFoam mesh.1
checkMesh -constant -allGeometry -allTopology
</code></pre>
<p>检查转换后的单元体积、非正交性和边界连接，确认输入中的四面体能够用于预期离散格式。</p>
<h2>示例 4：将毫米坐标换算为米</h2>
<pre><code class="language-bash">tetgenToFoam mesh-mm.1
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>TetGen 文件中的坐标数值被直接读取，转换后统一缩放。通过边界框检查实际长度。</p>
<h2>示例 5：为缺失标记的网格划分边界</h2>
<pre><code class="language-bash">tetgenToFoam mesh.1 -noFaceFile
autoPatch 45 -overwrite
</code></pre>
<p>根据外表面的折角建立边界分区。之后在可视化中确认各区位置，再使用 createPatchDict 整理为入口、出口和壁面。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFaceFile</code></td><td>跳过 .face 文件中的边界信息。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/tetgenToFoam/tetgenToFoam.C">源码与说明</a> · <a href="/assets/command-help/tetgentofoam.txt">帮助文本</a></p>
