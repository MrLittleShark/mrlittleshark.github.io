---
title: "potentialFoam · 求解势流方程，常用于初始化速度与通量"
layout: reference
description: "求解势流方程，常用于初始化速度与通量。"
cms_slug: "command-potentialfoam"
---

<p>求解势流方程，常用于初始化速度与通量。</p><h2>在配套算例中运行</h2>
<pre><code class="language-bash">potentialFoam &gt; log.potentialFoam 2&gt;&amp;1
tail -n 20 log.potentialFoam
</code></pre>
<p>先完成配套算例的网格和初始化步骤。<code>&gt;</code> 将标准输出写入日志，<code>2&gt;&amp;1</code> 将错误输出写到同一文件。计算结束后，<code>tail -n 20</code> 显示日志末尾。计算过程中查看日志时，在第二个终端执行 <code>tail -f log.potentialFoam</code>。</p>
<h2>选择算例目录</h2>
<pre><code class="language-bash">potentialFoam -case ../myCase
</code></pre>
<p><code>myCase</code> 应是为该求解器准备好的算例。网格位于 <code>constant/polyMesh</code>，时间与写出设置位于 <code>system/controlDict</code>。</p>
<h2>查看支持的选项</h2>
<pre><code class="language-bash">potentialFoam -help-full
</code></pre>
<p><code>-initialiseUBCs</code> 初始化速度边界，<code>-writep</code> 写出压力，<code>-writePhi</code> 写出势函数，<code>-writephi</code> 写出面通量；大小写分别代表不同字段。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-dry-run</td><td>Check case set-up only using a single time step</td></tr><tr><td>-dry-run-write</td><td>Check case set-up and write only using a single time step Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-initialiseUBCs</td><td>Initialise U boundary conditions</td></tr><tr><td>-listScalarBCs</td><td>List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)</td></tr><tr><td>-listVectorBCs</td><td>List vector field boundary conditions (fvPatchField&lt;vector&gt;)</td></tr><tr><td>-pName &lt;pName&gt;</td><td>Name of the pressure field</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-writePhi</td><td>Write the final velocity potential field</td></tr><tr><td>-writep</td><td>Calculate and write the Euler pressure field</td></tr><tr><td>-writephi</td><td>Write the final volumetric flux field</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/basic/potentialFoam/cylinder">basic/potentialFoam/cylinder</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/basic/potentialFoam/pitzDaily">basic/potentialFoam/pitzDaily</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/basic/potentialFoam/cylinder&quot; potentialFoam-study
cd potentialFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: potentialFoam [OPTIONS]
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

Potential flow solver which solves for the velocity potential

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/basic/potentialFoam/potentialFoam.C">源码与说明</a> · <a href="/assets/command-help/potentialfoam.txt">帮助文本</a></p>
