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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dry-run</code></td><td>Check case set-up only using a single time step</td></tr><tr><td><code>-dry-run-write</code></td><td>Check case set-up and write only using a single time step Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-initialiseUBCs</code></td><td>Initialise U boundary conditions</td></tr><tr><td><code>-listScalarBCs</code></td><td>List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)</td></tr><tr><td><code>-listVectorBCs</code></td><td>List vector field boundary conditions (fvPatchField&lt;vector&gt;)</td></tr><tr><td><code>-pName &lt;pName&gt;</code></td><td>Name of the pressure field</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-writePhi</code></td><td>Write the final velocity potential field</td></tr><tr><td><code>-writep</code></td><td>Calculate and write the Euler pressure field</td></tr><tr><td><code>-writephi</code></td><td>Write the final volumetric flux field</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/basic/overPotentialFoam/cylinder/cylinderAndBackground">basic/overPotentialFoam/cylinder/cylinderAndBackground</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/basic/overPotentialFoam/cylinder/cylinderAndBackground&quot; overPotentialFoam-study
cd overPotentialFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: overPotentialFoam [OPTIONS]
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
  -initialiseUBCs   Initialise U boundary conditions
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -listFunctionObjects
                    List functionObjects
  -listRegisteredSwitches
                    List switches registered for run-time modification (see
                    -listUnsetSwitches option)
  -listScalarBCs    List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)
  -listSwitches     List switches declared in libraries (see -listUnsetSwitches
                    option)
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
  -pName &lt;pName&gt;    Name of the pressure field
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -withFunctionObjects
                    Execute functionObjects
  -world &lt;name&gt;     Name of the local world for parallel communication
  -writePhi         Write the final velocity potential field
  -writep           Calculate and write the Euler pressure field
  -writephi         Write the final volumetric flux field
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Overset potential flow solver which solves for the velocity potential

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/basic/potentialFoam/overPotentialFoam/overPotentialFoam.C">源码与说明</a> · <a href="/assets/command-help/overpotentialfoam.txt">帮助文本</a></p>
