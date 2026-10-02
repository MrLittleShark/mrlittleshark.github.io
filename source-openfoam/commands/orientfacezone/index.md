---
title: "orientFaceZone · 根据外部参考点统一 faceZone 的定向标记"
layout: reference
description: "根据外部参考点统一 faceZone 的定向标记。"
cms_slug: "command-orientfacezone"
---

<p>根据外部参考点统一 faceZone 的定向标记。</p><h2>开始前</h2>
<p>已存在目标 faceZone；第二位置参数必须是网格外部参考点，用来确定面的外侧。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：统一闭合区域朝向</h2>
<pre><code class="language-bash">orientFaceZone shellFaces '(10 0 0)'
</code></pre>
<p>shellFaces 已包围目标区域，参考点(10,0,0)确在网格外；程序更新该zone的 flipMap 并报告翻转数量。</p>
<h2>示例 2：对另一侧外部点定向</h2>
<pre><code class="language-bash">orientFaceZone inletSection '(-10 0 0)'
</code></pre>
<p>入口截面附近的外部参考点位于负x方向，使定向与所选外侧对应；用于统一截面积分的符号约定。</p>
<h2>示例 3：处理多区域中的界面</h2>
<pre><code class="language-bash">orientFaceZone -region fluid interfaceFaces '(10 10 10)'
</code></pre>
<p>仅修改 fluid 的 interfaceFaces；参考点应位于该区域外，结果写入 fluid 的 faceZones。</p>
<h2>示例 4：生成 zone 后定向</h2>
<pre><code class="language-bash">topoSet -dict system/topoSet-interfaceDict
orientFaceZone interfaceFaces '(0 0 10)'
</code></pre>
<p>topoSet 字典先创建 interfaceFaces faceZone，再用外部参考点统一朝向，适合作为界面通量统计的前处理。</p>
<h2>示例 5：分区网格中同步定向</h2>
<pre><code class="language-bash">mpirun -np 4 orientFaceZone -parallel shellFaces '(10 0 0)'
</code></pre>
<p>已有4分区且耦合面两侧都进入zone；并行交换定向信息，使跨处理器的 flipMap 一致。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/orientFaceZone/orientFaceZone.C">源码与说明</a> · <a href="/assets/command-help/orientfacezone.txt">帮助文本</a></p>
