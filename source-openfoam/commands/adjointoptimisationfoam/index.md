---
title: "adjointOptimisationFoam · 伴随优化循环与设计变量更新"
layout: reference
description: "伴随优化循环与设计变量更新。"
cms_slug: "command-adjointoptimisationfoam"
---

<p>伴随优化循环与设计变量更新。</p><h2>开始前</h2>
<p><code>adjointOptimisationFoam</code> 用于伴随优化循环与设计变量更新。以下操作使用已完成网格与初始化的串行算例 <code>baseCase</code>；将它换成自己的目录名。各例中的新目录用于保留不同设置，运行前使用尚未存在的目录名。 配套输入可从<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/motorBike">官方 <code>incompressible/adjointOptimisationFoam/sensitivityMaps/motorBike</code> 算例</a>取得；先按该算例的 <code>Allrun</code> 完成网格和初始场准备。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：运行已配置的优化问题</h2>
<pre><code class="language-bash">adjointOptimisationFoam -case baseCase &gt; baseCase/log.optimisation 2&gt;&amp;1
</code></pre>
<p>算例需要配置 <code>system/optimisationDict</code>，其中选择原始问题、伴随问题、目标函数和设计变量。运行后查看日志中的优化循环及目标函数值。</p>
<h2>示例 2：在副本中保存更完整的过程输出</h2>
<pre><code class="language-bash">foamCloneCase baseCase history-study
foamDictionary history-study/system/controlDict -entry purgeWrite -set 0
adjointOptimisationFoam -case history-study &gt; history-study/log.optimisation 2&gt;&amp;1
</code></pre>
<p><code>purgeWrite 0</code> 保留求解器按输出设置写出的所有时间目录，可用于回看不同阶段的流场。优化器自己写出的目标函数、梯度和设计变量记录仍按优化配置保存。</p>
<h2>示例 3：提高保存结果的有效数字</h2>
<pre><code class="language-bash">foamCloneCase baseCase precision-study
foamDictionary precision-study/system/controlDict -entry writeFormat -set ascii
foamDictionary precision-study/system/controlDict -entry writePrecision -set 12
adjointOptimisationFoam -case precision-study &gt; precision-study/log.optimisation 2&gt;&amp;1
</code></pre>
<p>将流场文件保存为 12 位有效数字的文本，便于外部脚本读取和比较。伴随梯度的数值精度还取决于原始和伴随方程的收敛程度。</p>
<h2>示例 4：比较两份完整优化设置</h2>
<pre><code class="language-bash">foamCloneCase baseCase objective-study
cp optimisationDict.alternative objective-study/system/optimisationDict
adjointOptimisationFoam -case objective-study &gt; objective-study/log.optimisation 2&gt;&amp;1
</code></pre>
<p>提前准备一份与相同网格、边界和设计变量相容的 <code>optimisationDict.alternative</code>，例如只调整一个目标函数的权重。对比两次的目标值和设计变化，追踪该设置的影响。</p>
<h2>示例 5：并行运行优化问题</h2>
<pre><code class="language-bash">foamCloneCase baseCase parallel-study
foamDictionary parallel-study/system/controlDict -entry startFrom -set startTime
foamGetDict -case parallel-study -force decomposeParDict
foamDictionary parallel-study/system/decomposeParDict -entry numberOfSubdomains -set 2
foamDictionary parallel-study/system/decomposeParDict -entry method -set scotch
t0=$(foamDictionary parallel-study/system/controlDict -entry startTime -value)
decomposePar -case parallel-study -time "$t0"
mpirun -np 2 adjointOptimisationFoam -case parallel-study -parallel &gt; parallel-study/log.parallel 2&gt;&amp;1
reconstructPar -case parallel-study -latestTime
</code></pre>
<p>先将同一优化算例分为两个子域，再使用 <code>-parallel</code> 运行原始和伴随求解过程。分区后保留优化器的配置及设计变量定义，对比串行与并行的最终目标值和耗时。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-postProcess</code></td><td>仅执行函数对象后处理。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/motorBike">incompressible/adjointOptimisationFoam/sensitivityMaps/motorBike</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/motorBike">incompressible/adjointOptimisationFoam/shapeOptimisation/motorBike</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/sbend/laminar">incompressible/adjointOptimisationFoam/sensitivityMaps/sbend/laminar</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/naca0012/laminar/drag">incompressible/adjointOptimisationFoam/sensitivityMaps/naca0012/laminar/drag</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/naca0012/laminar/lift">incompressible/adjointOptimisationFoam/sensitivityMaps/naca0012/laminar/lift</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/incompressible/adjointOptimisationFoam/sensitivityMaps/motorBike&quot; adjointOptimisationFoam-study
cd adjointOptimisationFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/incompressible/adjointOptimisationFoam/adjointOptimisationFoam.C">源码与说明</a> · <a href="/assets/command-help/adjointoptimisationfoam.txt">帮助文本</a></p>
