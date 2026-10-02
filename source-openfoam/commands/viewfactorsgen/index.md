---
title: "viewFactorsGen · 计算表面间辐射视角因子及分布映射"
layout: reference
description: "计算表面间辐射视角因子及分布映射。"
cms_slug: "command-viewfactorsgen"
---

<p>计算表面间辐射视角因子及分布映射。</p><h2>开始前</h2>
<p>已有constant/viewFactorsDict、辐射边界和需要的faceAgglomerate结果。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：生成辐射交换数据</h2>
<pre><code class="language-bash">viewFactorsGen
</code></pre>
<p>按网格表面可见关系计算视角因子，写出后续viewFactor辐射模型需要的矩阵和映射数据。</p>
<h2>示例 2：写出视角因子矩阵诊断</h2>
<pre><code class="language-bash">foamDictionary constant/viewFactorsDict -entry writeViewFactorMatrix -set true
viewFactorsGen
</code></pre>
<p>开启矩阵输出选项，便于检查表面对之间的交换比例和结果分布。</p>
<h2>示例 3：导出可见射线</h2>
<pre><code class="language-bash">foamDictionary constant/viewFactorsDict -entry dumpRays -set true
viewFactorsGen
</code></pre>
<p>额外生成allVisibleFaces.obj等可见性诊断，适合检查遮挡与表面朝向。</p>
<h2>示例 4：针对命名区域计算</h2>
<pre><code class="language-bash">faceAgglomerate -region enclosure
viewFactorsGen -region enclosure
</code></pre>
<p>为enclosure生成聚合映射后计算其视角因子，适合多区域中的辐射腔体。</p>
<h2>示例 5：并行生成</h2>
<pre><code class="language-bash">mpirun -np 4 faceAgglomerate -parallel
mpirun -np 4 viewFactorsGen -parallel
</code></pre>
<p>网格已有4分区且viewFactorsDict一致；先聚合再计算，输出与各分区对应的交换数据。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/viewFactorsGen/viewFactorsGen.C">源码与说明</a> · <a href="/assets/command-help/viewfactorsgen.txt">帮助文本</a></p>
