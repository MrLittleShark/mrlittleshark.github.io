---
title: "overPotentialFoam · 重叠网格势流初始化"
layout: reference
description: "重叠网格势流初始化。"
cms_slug: "command-overpotentialfoam"
---

<p>重叠网格势流初始化。</p><h2>开始前</h2>
<p><code>overPotentialFoam</code> 用于重叠网格势流初始化。以下操作使用已完成网格与初始化的串行算例 <code>baseCase</code>；将它换成自己的目录名。各例中的新目录用于保留不同设置，运行前使用尚未存在的目录名。 重叠网格算例还需要 <code>zoneID</code>、overset 边界和相应的插值设置。 配套输入可从<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/basic/overPotentialFoam/cylinder/cylinderAndBackground">官方 <code>basic/overPotentialFoam/cylinder/cylinderAndBackground</code> 算例</a>取得；先按该算例的 <code>Allrun</code> 完成网格和初始场准备。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：求解速度势并初始化速度</h2>
<pre><code class="language-bash">overPotentialFoam -case baseCase
</code></pre>
<p>在已经准备好的重叠网格的势流算例中求解速度势，重建并写出 <code>U</code>。这个程序完成一次势流初始化；输出位于当前选定的时间目录。</p>
<h2>示例 2：先更新速度边界</h2>
<pre><code class="language-bash">overPotentialFoam -case baseCase -initialiseUBCs
</code></pre>
<p><code>-initialiseUBCs</code> 在求解前计算 <code>U</code> 的边界值。入口等边界使用需要更新的条件时，可用这一选项使初始化速度与边界设置配合。</p>
<h2>示例 3：同时保存速度势和面通量</h2>
<pre><code class="language-bash">overPotentialFoam -case baseCase -writePhi -writephi
</code></pre>
<p><code>Phi</code> 是速度势，<code>phi</code> 是体积面通量，两个选项区分大小写。保存后可比较势函数、速度和面通量之间的关系。</p>
<h2>示例 4：计算并保存 Euler 压力</h2>
<pre><code class="language-bash">overPotentialFoam -case baseCase -initialiseUBCs -writep
</code></pre>
<p><code>-writep</code> 由势流速度计算并写出 Euler 压力场。此结果适合势流初始化及相应假设下的压力分布分析；后续黏性求解器会继续更新压力。</p>
<h2>示例 5：在两个子域上初始化</h2>
<pre><code class="language-bash">foamCloneCase baseCase parallel-study
foamDictionary parallel-study/system/controlDict -entry startFrom -set startTime
foamGetDict -case parallel-study -force decomposeParDict
foamDictionary parallel-study/system/decomposeParDict -entry numberOfSubdomains -set 2
foamDictionary parallel-study/system/decomposeParDict -entry method -set scotch
t0=$(foamDictionary parallel-study/system/controlDict -entry startTime -value)
decomposePar -case parallel-study -time "$t0"
mpirun -np 2 overPotentialFoam -case parallel-study -parallel -writePhi -writephi &gt; parallel-study/log.parallel 2&gt;&amp;1
reconstructPar -case parallel-study -time "$t0"
</code></pre>
<p>先按初始时刻分解完整的势流输入，再由两个进程完成初始化。<code>-writePhi -writephi</code> 让分区目录同时保存势与通量，最后重建相应场供检查或后续计算使用。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dry-run</code></td><td>通过一个时间步检查算例设置。</td></tr><tr><td><code>-dry-run-write</code></td><td>用一个时间步检查算例设置，并写出结果。</td></tr><tr><td><code>-initialiseUBCs</code></td><td>初始化 U 的边界条件。</td></tr><tr><td><code>-listFunctionObjects</code></td><td>列出可用的函数对象。</td></tr><tr><td><code>-listScalarBCs</code></td><td>列出标量场的边界条件类型，即 fvPatchField&lt;scalar&gt;。</td></tr><tr><td><code>-listVectorBCs</code></td><td>列出向量场的边界条件类型，即 fvPatchField&lt;vector&gt;。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-pName &lt;pName&gt;</code></td><td>指定压力场名称。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-withFunctionObjects</code></td><td>执行函数对象。</td></tr><tr><td><code>-writePhi</code></td><td>写出最终的速度势 Phi。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/basic/overPotentialFoam/cylinder/cylinderAndBackground">basic/overPotentialFoam/cylinder/cylinderAndBackground</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/basic/overPotentialFoam/cylinder/cylinderAndBackground&quot; overPotentialFoam-study
cd overPotentialFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details class="command-more-options"><summary>更多参数（23 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-listRegisteredSwitches</code></td><td>列出已注册、支持运行时修改的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listSwitches</code></td><td>列出库中声明的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listUnsetSwitches</code></td><td>将开关列表限定为 etc/controlDict 尚未设置的项。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-writep</code></td><td>计算并写出欧拉压力场。</td></tr><tr><td><code>-writephi</code></td><td>写出最终的体积通量场 phi。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/basic/potentialFoam/overPotentialFoam/overPotentialFoam.C">源码与说明</a> · <a href="/assets/command-help/overpotentialfoam.txt">帮助文本</a></p>
