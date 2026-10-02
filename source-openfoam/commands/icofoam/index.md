---
title: "icoFoam · 使用 PISO 算法求解不可压缩瞬态层流"
layout: reference
description: "使用 PISO 算法求解不可压缩瞬态层流。"
cms_slug: "command-icofoam"
---

<p>使用 PISO 算法求解不可压缩瞬态层流。</p><h2>开始前</h2>
<p><code>icoFoam</code> 使用 PISO 算法计算不可压缩牛顿流体的瞬态层流。下面先建立顶盖驱动方腔算例 <code>baseCase</code>，再分别练习短程计算、结果写出、续算和并行。新目录名应尚未使用。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：从官方方腔算例开始</h2>
<pre><code class="language-bash">cp -a "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" baseCase
blockMesh -case baseCase
icoFoam -case baseCase &gt; baseCase/log.icoFoam 2&gt;&amp;1
tail -n 20 baseCase/log.icoFoam
</code></pre>
<p>方腔顶部壁面沿 x 方向运动，其余壁面静止；<code>icoFoam</code> 求解腔内速度 <code>U</code> 和运动压力 <code>p</code>。官方设置从 0 s 算到 0.5 s，时间步为 0.005 s，每 20 步保存一次，即 0.1 s 保存一次。<code>blockMesh</code> 先生成网格，后面的命令才开始求解；结果写在 <code>baseCase/0.1</code>、<code>0.2</code> 等目录。</p>
<h2>示例 2：先做一段短程计算</h2>
<pre><code class="language-bash">foamCloneCase baseCase short-study
foamDictionary short-study/system/controlDict -entry startFrom -set startTime
foamDictionary short-study/system/controlDict -entry stopAt -set endTime
t0=$(foamDictionary short-study/system/controlDict -entry startTime -value)
dt=$(foamDictionary short-study/system/controlDict -entry deltaT -value)
end=$(awk -v t="$t0" -v dt="$dt" 'BEGIN {printf "%.12g", t+5*dt}')
foamDictionary short-study/system/controlDict -entry endTime -set "$end"
icoFoam -case short-study &gt; short-study/log.icoFoam 2&gt;&amp;1
</code></pre>
<p>先复制输入，再把结束值设为起始值加 <code>5 × deltaT</code>。这样可用一段较短的计算检查使用 PISO 算法求解不可压缩瞬态层流的初始化和求解过程；原算例设置保留在 <code>baseCase</code>。若算例启用了自适应时间步，实际步数随步长调整而变化；这里控制的是结束时刻。</p>
<h2>示例 3：每十步保存一次结果</h2>
<pre><code class="language-bash">foamCloneCase baseCase output-study
foamDictionary output-study/system/controlDict -entry startFrom -set startTime
foamDictionary output-study/system/controlDict -entry writeControl -set timeStep
foamDictionary output-study/system/controlDict -entry writeInterval -set 10
icoFoam -case output-study &gt; output-study/log.icoFoam 2&gt;&amp;1
foamListTimes -case output-study
</code></pre>
<p><code>writeControl timeStep</code> 按步数安排写出，<code>writeInterval 10</code> 表示每 10 个时间步保存一次。两项设置改变结果保存频率；<code>deltaT</code>、离散格式和线性求解容差继续沿用原算例。最后列出实际生成的结果时刻，便于核对输出间隔。</p>
<h2>示例 4：从已保存结果继续计算</h2>
<pre><code class="language-bash">last=$(foamListTimes -case baseCase -latestTime)
dt=$(foamDictionary baseCase/system/controlDict -entry deltaT -value)
end=$(awk -v t="$last" -v dt="$dt" 'BEGIN {printf "%.12g", t+20*dt}')
foamDictionary baseCase/system/controlDict -entry startFrom -set latestTime
foamDictionary baseCase/system/controlDict -entry stopAt -set endTime
foamDictionary baseCase/system/controlDict -entry endTime -set "$end"
icoFoam -case baseCase &gt; baseCase/log.restart 2&gt;&amp;1
</code></pre>
<p>在示例 1 已保存完整结果的基础上运行。<code>latestTime</code> 读取最近保存的网格、场和模型状态；结束值由最近目录名加 <code>20 × deltaT</code> 得到。这个例子会修改 <code>baseCase/system/controlDict</code>，日志单独保存为 <code>log.restart</code>，便于比较续算前后的过程。</p>
<h2>示例 5：改为两进程并行计算</h2>
<pre><code class="language-bash">foamCloneCase baseCase parallel-study
foamDictionary parallel-study/system/controlDict -entry startFrom -set startTime
foamGetDict -case parallel-study -force decomposeParDict
foamDictionary parallel-study/system/decomposeParDict -entry numberOfSubdomains -set 2
foamDictionary parallel-study/system/decomposeParDict -entry method -set scotch
t0=$(foamDictionary parallel-study/system/controlDict -entry startTime -value)
decomposePar -case parallel-study -time "$t0"
mpirun -np 2 icoFoam -case parallel-study -parallel &gt; parallel-study/log.parallel 2&gt;&amp;1
reconstructPar -case parallel-study -latestTime
</code></pre>
<p>在新副本中用官方模板替换分区字典，将网格分成两个子域；<code>-np 2</code> 与 <code>numberOfSubdomains 2</code> 保持一致。求解器的 <code>-parallel</code> 选项使每个进程读取自己的子域数据，最后合并最新场。可在相同网格和计算区间内比较串行与并行耗时。</p>
<h2>示例 6：减半时间步并保持相同输出时刻</h2>
<pre><code class="language-bash">foamCloneCase baseCase half-step-study
foamDictionary half-step-study/system/controlDict -entry startFrom -set startTime
foamDictionary half-step-study/system/controlDict -entry endTime -set 0.5
foamDictionary half-step-study/system/controlDict -entry deltaT -set 0.0025
foamDictionary half-step-study/system/controlDict -entry writeControl -set timeStep
foamDictionary half-step-study/system/controlDict -entry writeInterval -set 40
icoFoam -case half-step-study &gt; half-step-study/log.icoFoam 2&gt;&amp;1
</code></pre>
<p>将 0.005 s 减半为 0.0025 s，同时把保存间隔改为 40 步，使两次计算都在 0.1、0.2、…、0.5 s 输出。这样可在同一物理时刻比较中心线速度和涡心位置，观察时间步变化对解的影响。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dry-run</code></td><td>通过一个时间步检查算例设置。</td></tr><tr><td><code>-dry-run-write</code></td><td>用一个时间步检查算例设置，并写出结果。</td></tr><tr><td><code>-listFunctionObjects</code></td><td>列出可用的函数对象。</td></tr><tr><td><code>-listScalarBCs</code></td><td>列出标量场的边界条件类型，即 fvPatchField&lt;scalar&gt;。</td></tr><tr><td><code>-listVectorBCs</code></td><td>列出向量场的边界条件类型，即 fvPatchField&lt;vector&gt;。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-postProcess</code></td><td>仅执行函数对象后处理。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">incompressible/icoFoam/cavity/cavity</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavityGrade">incompressible/icoFoam/cavity/cavityGrade</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavityClipped">incompressible/icoFoam/cavity/cavityClipped</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/parallel/cavity">mesh/parallel/cavity</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/IO/cavity_parProfiling">IO/cavity_parProfiling</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity&quot; icoFoam-study
cd icoFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details class="command-more-options"><summary>更多参数（19 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-listRegisteredSwitches</code></td><td>列出已注册、支持运行时修改的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listSwitches</code></td><td>列出库中声明的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listUnsetSwitches</code></td><td>将开关列表限定为 etc/controlDict 尚未设置的项。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/incompressible/icoFoam/icoFoam.C">源码与说明</a> · <a href="/assets/command-help/icofoam.txt">帮助文本</a></p>
