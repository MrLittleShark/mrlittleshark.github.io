---
title: "rotateMesh · 按两个方向向量确定旋转，同时旋转网格与向量、张量场"
layout: reference
description: "按两个方向向量确定旋转，同时旋转网格与向量、张量场。"
cms_slug: "command-rotatemesh"
---

<p>按两个方向向量确定旋转，同时旋转网格与向量、张量场。</p><h2>开始前</h2>
<p>已有网格和要旋转的结果时间；from、to 是非零方向向量，二者确定刚体旋转。</p>
<h2>示例 1：把x方向转到y方向</h2>
<pre><code class="language-bash">rotateMesh '(1 0 0)' '(0 1 0)'
</code></pre>
<p>旋转网格，并同步处理所读向量、张量场的分量，适合改变整个案例的空间朝向。</p>
<h2>示例 2：仅处理最后时刻</h2>
<pre><code class="language-bash">rotateMesh '(0 0 1)' '(1 0 0)' -latestTime
</code></pre>
<p>选择最新结果，把原z方向转到x方向；输出该状态下经过一致旋转的几何和场。</p>
<h2>示例 3：旋转指定时间区间</h2>
<pre><code class="language-bash">rotateMesh '(1 0 0)' '(0 0 1)' -time '0.1:0.5'
</code></pre>
<p>仅处理0.1到0.5之间已有时间目录，便于统一一段动画数据的朝向。</p>
<h2>示例 4：旋转指定区域</h2>
<pre><code class="language-bash">rotateMesh '(1 0 0)' '(0 1 0)' -region fluid -time 0
</code></pre>
<p>只处理 fluid 的0时刻网格与场；适合区域输入数据的坐标系转换。</p>
<h2>示例 5：多区域一致旋转</h2>
<pre><code class="language-bash">rotateMesh '(1 0 0)' '(0 1 0)' -allRegions -constant
</code></pre>
<p>regionProperties 已登记各区域；所有区域按同一旋转变换处理，并将 constant 纳入选择，保持相对空间位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中的全部区域。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，例如 -region gas。</td></tr><tr><td><code>-regions &lt;wordRes&gt;</code></td><td>指定一个区域或按 regionProperties 匹配多个区域，例如 -regions gas 或 -regions &#x27;(gas &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/rotateMesh/rotateMesh.C">源码与说明</a> · <a href="/assets/command-help/rotatemesh.txt">帮助文本</a></p>
