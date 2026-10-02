---
title: "interPhaseChangeFoam · 含空化等相变的不可压缩两相 VOF 输运"
layout: reference
description: "含空化等相变的不可压缩两相 VOF 输运。"
cms_slug: "command-interphasechangefoam"
---

<p>含空化等相变的不可压缩两相 VOF 输运。</p><h2>开始前</h2>
<p><code>interPhaseChangeFoam</code> 用于含空化等相变的不可压缩两相 VOF 输运。以下操作使用已完成网格与初始化的串行算例 <code>baseCase</code>；将它换成自己的目录名。各例中的新目录用于保留不同设置，运行前使用尚未存在的目录名。 配套输入可从<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interPhaseChangeFoam/cavitatingBullet">官方 <code>multiphase/interPhaseChangeFoam/cavitatingBullet</code> 算例</a>取得；先按该算例的 <code>Allrun</code> 完成网格和初始场准备。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：运行准备好的算例</h2>
<pre><code class="language-bash">interPhaseChangeFoam -case baseCase &gt; baseCase/log.interPhaseChangeFoam 2&gt;&amp;1
tail -n 20 baseCase/log.interPhaseChangeFoam
</code></pre>
<p><code>-case baseCase</code> 指定算例；<code>&gt; ... 2&gt;&amp;1</code> 将正常输出和报错都保存到日志。程序按 <code>controlDict</code> 的起止设置求解含空化等相变的不可压缩两相 VOF 输运，结果场，例如 <code>p_rgh</code>、<code>U</code>、<code>rho</code>、<code>p</code>写入相应时间目录。日志末尾可查看计算进度和执行时间。</p>
<h2>示例 2：先做一段短程计算</h2>
<pre><code class="language-bash">foamCloneCase baseCase short-study
foamDictionary short-study/system/controlDict -entry startFrom -set startTime
foamDictionary short-study/system/controlDict -entry stopAt -set endTime
t0=$(foamDictionary short-study/system/controlDict -entry startTime -value)
dt=$(foamDictionary short-study/system/controlDict -entry deltaT -value)
end=$(awk -v t="$t0" -v dt="$dt" 'BEGIN {printf "%.12g", t+5*dt}')
foamDictionary short-study/system/controlDict -entry endTime -set "$end"
interPhaseChangeFoam -case short-study &gt; short-study/log.interPhaseChangeFoam 2&gt;&amp;1
</code></pre>
<p>先复制输入，再把结束值设为起始值加 <code>5 × deltaT</code>。这样可用一段较短的计算检查含空化等相变的不可压缩两相 VOF 输运的初始化和求解过程；原算例设置保留在 <code>baseCase</code>。若算例启用了自适应时间步，实际步数随步长调整而变化；这里控制的是结束时刻。</p>
<h2>示例 3：每十步保存一次结果</h2>
<pre><code class="language-bash">foamCloneCase baseCase output-study
foamDictionary output-study/system/controlDict -entry startFrom -set startTime
foamDictionary output-study/system/controlDict -entry writeControl -set timeStep
foamDictionary output-study/system/controlDict -entry writeInterval -set 10
interPhaseChangeFoam -case output-study &gt; output-study/log.interPhaseChangeFoam 2&gt;&amp;1
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
interPhaseChangeFoam -case baseCase &gt; baseCase/log.restart 2&gt;&amp;1
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
mpirun -np 2 interPhaseChangeFoam -case parallel-study -parallel &gt; parallel-study/log.parallel 2&gt;&amp;1
reconstructPar -case parallel-study -latestTime
</code></pre>
<p>在新副本中用官方模板替换分区字典，将网格分成两个子域；<code>-np 2</code> 与 <code>numberOfSubdomains 2</code> 保持一致。求解器的 <code>-parallel</code> 选项使每个进程读取自己的子域数据，最后合并最新场。可在相同网格和计算区间内比较串行与并行耗时。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dry-run</code></td><td>Check case set-up only using a single time step</td></tr><tr><td><code>-dry-run-write</code></td><td>Check case set-up and write only using a single time step Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-listFvOptions</code></td><td>List fvOptions List switches registered for run-time modification (see -listUnsetSwitches option)</td></tr><tr><td><code>-listScalarBCs</code></td><td>List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)</td></tr><tr><td><code>-listVectorBCs</code></td><td>List vector field boundary conditions (fvPatchField&lt;vector&gt;)</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-postProcess</code></td><td>Execute functionObjects only Subprocess root directories for distributed running</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interPhaseChangeFoam/cavitatingBullet">multiphase/interPhaseChangeFoam/cavitatingBullet</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/multiphase/interPhaseChangeFoam/cavitatingBullet&quot; interPhaseChangeFoam-study
cd interPhaseChangeFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: interPhaseChangeFoam [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Check case set-up only using a single time step
  -dry-run-write    Check case set-up and write only using a single time step
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -listFunctionObjects
                    List functionObjects
  -listFvOptions    List fvOptions
  -listRegisteredSwitches
                    List switches registered for run-time modification (see
                    -listUnsetSwitches option)
  -listScalarBCs    List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)
  -listSwitches     List switches declared in libraries (see -listUnsetSwitches
                    option)
  -listTurbulenceModels
                    List turbulenceModels
  -listUnsetSwitches
                    Modifies switch listing to display values not set in
                    etc/controlDict
  -listVectorBCs    List vector field boundary conditions (fvPatchField&lt;vector&gt;)
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -postProcess      Execute functionObjects only
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Solver for two incompressible, isothermal immiscible fluids with phase-change.
Uses VOF (volume of fluid) phase-fraction based interface capturing.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/multiphase/interPhaseChangeFoam/interPhaseChangeFoam.C">源码与说明</a> · <a href="/assets/command-help/interphasechangefoam.txt">帮助文本</a></p>
