---
title: "netgenNeutralToFoam · 转换后检查边界划分"
layout: reference
description: "转换后检查边界划分。"
cms_slug: "command-netgenneutraltofoam"
---

<p>转换后检查边界划分。</p><h2>开始前</h2>
<p>准备 NETGEN Neutral 格式文件；边界标签随输入读取，转换后需根据几何位置核对各 patch。</p>
<h2>示例 1：导入四面体网格</h2>
<pre><code class="language-bash">netgenNeutralToFoam mesh.neu
</code></pre>
<p>读取顶点、四面体以及表面三角形，生成 OpenFOAM 网格。日志给出各边界分区的面数。</p>
<h2>示例 2：检查边界面连接</h2>
<pre><code class="language-bash">netgenNeutralToFoam mesh.neu
checkMesh -constant -allTopology
</code></pre>
<p>检查边界三角形是否与体单元正确相连。若转换器提示某些边界面没有相邻单元，应回到输入网格核对表面数据。</p>
<h2>示例 3：换算毫米坐标</h2>
<pre><code class="language-bash">netgenNeutralToFoam mesh-mm.neu
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>将转换后的全网格统一缩放为米，再通过 bounding box 核对模型尺寸。</p>
<h2>示例 4：整理编号式边界名称</h2>
<pre><code class="language-bash">netgenNeutralToFoam mesh.neu
createPatch -overwrite
</code></pre>
<p>前提是根据转换输出的 patch 编号配置 createPatchDict。把实际入口、出口和壁面改为有物理意义的名称，方便配置场文件。</p>
<h2>示例 5：在指定案例导出外表面</h2>
<pre><code class="language-bash">netgenNeutralToFoam /data/mesh.neu -case ../netgenCase
foamToSurface netgen-boundary.obj -case ../netgenCase -constant
</code></pre>
<p>将网格转换到 netgenCase，并导出边界用于与 NETGEN 原模型对比。检查孔洞、几何尺度及各边界的位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/netgenNeutralToFoam/netgenNeutralToFoam.C">源码与说明</a> · <a href="/assets/command-help/netgenneutraltofoam.txt">帮助文本</a></p>
