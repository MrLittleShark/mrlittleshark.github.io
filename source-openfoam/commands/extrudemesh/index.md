---
title: "extrudeMesh · 读取 extrudeMeshDict"
layout: reference
description: "读取 extrudeMeshDict。"
cms_slug: "command-extrudemesh"
---

<p>读取 extrudeMeshDict。</p><h2>开始前</h2>
<p>已有待拉伸patch或字典指定的源表面，并准备system/extrudeMeshDict；其中确定源、方向、层数和厚度。</p>
<h2>示例 1：按默认字典拉伸</h2>
<pre><code class="language-bash">extrudeMesh
</code></pre>
<p>读取extrudeMeshDict，从所选源patch或表面生成拉伸网格，检查日志中的源面数与层数。</p>
<h2>示例 2：指定拉伸方案</h2>
<pre><code class="language-bash">extrudeMesh -dict system/extrudeMeshDict.thin
</code></pre>
<p>使用完整thin字典生成薄层网格，输出位置由拉伸方式与源/目标算例设置决定。</p>
<h2>示例 3：增加法向层数</h2>
<pre><code class="language-bash">foamDictionary system/extrudeMeshDict -entry nLayers -set 10
extrudeMesh
</code></pre>
<p>在已有法向拉伸配置中改为10层，比较层厚与厚度方向分辨率；总厚度仍由模型系数决定。</p>
<h2>示例 4：调整层厚增长</h2>
<pre><code class="language-bash">foamDictionary system/extrudeMeshDict -entry expansionRatio -set 1.2
extrudeMesh
</code></pre>
<p>在独立副本中让相邻层按1.2增长，适合从近壁细层向外过渡；检查最终层厚是否过大。</p>
<h2>示例 5：检查多区域源网格</h2>
<pre><code class="language-bash">extrudeMesh -region solid -dict system/extrudeMeshDict.solid
</code></pre>
<p>已准备solid区域及相应源patch的字典时，选择该源区域进行拉伸，核对输出区域连接与边界。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 extrudeMeshDict 文件。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-extrudemeshdict/">extrudeMeshDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/extrudeMesh/polyline">mesh/extrudeMesh/polyline</a></li></ul><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/extrude/extrudeMesh/extrudedMesh/extrudedMesh.C">源码与说明</a> · <a href="/assets/command-help/extrudemesh.txt">帮助文本</a></p>
