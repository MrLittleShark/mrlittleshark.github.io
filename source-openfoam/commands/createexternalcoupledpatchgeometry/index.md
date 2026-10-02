---
title: "createExternalCoupledPatchGeometry · 导出外部耦合patch组的几何信息"
layout: reference
description: "导出外部耦合patch组的几何信息。"
cms_slug: "command-createexternalcoupledpatchgeometry"
---

<p>导出外部耦合patch组的几何信息。</p><h2>开始前</h2>
<p>网格已有用于外部耦合的patch组；位置参数是组名，输出供外部程序按面顺序交换数据。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：导出耦合壁面组</h2>
<pre><code class="language-bash">createExternalCoupledPatchGeometry coupledWalls
</code></pre>
<p>coupledWalls 是已存在的patch组；生成该组的几何数据，供外部传热或结构程序读取。</p>
<h2>示例 2：指定通信目录</h2>
<pre><code class="language-bash">createExternalCoupledPatchGeometry coupledWalls -commsDir exchange
</code></pre>
<p>把通信几何输出到exchange，而非默认comms，便于与外部程序统一路径。</p>
<h2>示例 3：导出流体区域接口</h2>
<pre><code class="language-bash">createExternalCoupledPatchGeometry coupledWalls -region fluid
</code></pre>
<p>从fluid区域读取同名patch组，输出该区域的接口几何。</p>
<h2>示例 4：同时导出多个区域</h2>
<pre><code class="language-bash">createExternalCoupledPatchGeometry coupledWalls -regions '(fluid solid)' -commsDir exchange
</code></pre>
<p>两个区域均配置目标组时，批量输出接口几何，区域信息用于区分对应面。</p>
<h2>示例 5：网格分区后导出接口</h2>
<pre><code class="language-bash">mpirun -np 4 createExternalCoupledPatchGeometry coupledWalls -parallel -commsDir exchange
</code></pre>
<p>已有4分区网格和一致组名；按并行案例的接口布局生成几何，供外部耦合按相同面组织交换数据。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-commsDir &lt;dir&gt;</code></td><td>指定通信目录，默认为 comms。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域。</td></tr><tr><td><code>-regions &lt;(name1 .. nameN)&gt;</code></td><td>指定多个网格区域。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/createExternalCoupledPatchGeometry/createExternalCoupledPatchGeometry.C">源码与说明</a> · <a href="/assets/command-help/createexternalcoupledpatchgeometry.txt">帮助文本</a></p>
