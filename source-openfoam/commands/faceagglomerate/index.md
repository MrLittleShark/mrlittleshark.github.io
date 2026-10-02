---
title: "faceAgglomerate · 把边界细面聚合为粗面并写映射"
layout: reference
description: "把边界细面聚合为粗面并写映射。"
cms_slug: "command-faceagglomerate"
---

<p>把边界细面聚合为粗面并写映射。</p><h2>开始前</h2>
<p>已有边界网格和constant/viewFactorsDict，其中包含聚合参数与writeFacesAgglomeration。</p>
<h2>示例 1：生成细面到粗面映射</h2>
<pre><code class="language-bash">faceAgglomerate
</code></pre>
<p>读取默认viewFactorsDict，按pairPatchAgglomeration执行聚合，并写finalAgglom供视角因子计算使用。</p>
<h2>示例 2：写出可视化分组场</h2>
<pre><code class="language-bash">foamDictionary constant/viewFactorsDict -entry writeFacesAgglomeration -set true
faceAgglomerate
</code></pre>
<p>启用聚合可视化场，便于在ParaView中检查哪些细面归入同一粗面。</p>
<h2>示例 3：比较另一聚合设置</h2>
<pre><code class="language-bash">faceAgglomerate -dict constant/viewFactors-coarseDict
</code></pre>
<p>替代字典采用不同粗化参数；在副本中比较粗面数量与后续视角因子计算成本。</p>
<h2>示例 4：仅聚合指定区域</h2>
<pre><code class="language-bash">faceAgglomerate -region enclosure
</code></pre>
<p>只为enclosure区域生成映射，适合多区域辐射计算的几何预处理。</p>
<h2>示例 5：聚合后计算视角因子</h2>
<pre><code class="language-bash">faceAgglomerate
viewFactorsGen
</code></pre>
<p>使用viewFactorsGen流程的案例先创建finalAgglom，再计算粗面之间的辐射交换关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 viewFactorsDict 文件。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/faceAgglomerate/faceAgglomerate.C">源码与说明</a> · <a href="/assets/command-help/faceagglomerate.txt">帮助文本</a></p>
