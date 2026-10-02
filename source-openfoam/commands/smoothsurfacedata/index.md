---
title: "smoothSurfaceData · 对外部表面标量数据进行中值滤波"
layout: reference
description: "对外部表面标量数据进行中值滤波。"
cms_slug: "command-smoothsurfacedata"
---

<p>对外部表面标量数据进行中值滤波。</p><h2>开始前</h2>
<p>输入为受支持的表面结果文件；默认读取EnSight，默认处理标量T。半径单位为米。</p>
<h2>示例 1：平滑表面温度</h2>
<pre><code class="language-bash">smoothSurfaceData surface.case -radius 0.002
</code></pre>
<p>输入EnSight表面结果含T；以2毫米邻域执行默认一次中值滤波，输出滤波后的表面数据。</p>
<h2>示例 2：改为处理压力</h2>
<pre><code class="language-bash">smoothSurfaceData surface.case -field p -radius 0.002
</code></pre>
<p>选择标量p，对局部压力尖峰进行中值过滤，几何仍取输入表面。</p>
<h2>示例 3：增加过滤遍数</h2>
<pre><code class="language-bash">smoothSurfaceData surface.case -field T -radius 0.002 -sweeps 3
</code></pre>
<p>连续执行3级中值滤波，抑制孤立异常值的同时也会改变较细的空间变化。</p>
<h2>示例 4：比较较大邻域</h2>
<pre><code class="language-bash">smoothSurfaceData coarseStudy.case -field T -radius 0.01 -sweeps 1
</code></pre>
<p>独立输入副本使用1厘米滤波半径，比较平滑尺度对温度梯度的影响。</p>
<h2>示例 5：明确格式并输出详细过程</h2>
<pre><code class="language-bash">smoothSurfaceData surface.case -read-format ensight -field T -radius 0.002 -sweeps 2 -verbose
</code></pre>
<p>显式选择EnSight读取器，执行两遍过滤并显示更多处理信息，便于核对字段和邻域构建。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-field &lt;name&gt;</code></td><td>指定要处理的标量场，默认为 T。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-radius &lt;m&gt;</code></td><td>指定滤波半径，单位为米。</td></tr><tr><td><code>-read-format &lt;type&gt;</code></td><td>指定输入格式，默认为 ensight。</td></tr><tr><td><code>-sweeps &lt;N&gt;</code></td><td>设置中值滤波的轮数。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/smoothSurfaceData/smoothSurfaceData.C">源码与说明</a> · <a href="/assets/command-help/smoothsurfacedata.txt">帮助文本</a></p>
