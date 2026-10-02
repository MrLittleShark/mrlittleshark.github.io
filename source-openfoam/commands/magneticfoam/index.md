---
title: "magneticFoam · 永磁体产生的磁场"
layout: reference
description: "永磁体产生的磁场。"
cms_slug: "command-magneticfoam"
---

<p>永磁体产生的磁场。</p><h2>开始前</h2>
<p><code>magneticFoam</code> 用于永磁体产生的磁场。以下操作使用已完成网格与初始化的串行算例 <code>baseCase</code>；将它换成自己的目录名。各例中的新目录用于保留不同设置，运行前使用尚未存在的目录名。</p>
<h2>示例 1：计算磁场</h2>
<pre><code class="language-bash">magneticFoam -case baseCase
</code></pre>
<p>准备网格、磁势 <code>psi</code>、磁体参数和 <code>fvSolution</code> 后运行。程序求解磁势，并写出磁场强度 <code>H</code> 与磁通密度 <code>B</code>；输出目录在起始时刻基础上推进一步。</p>
<h2>示例 2：只保存磁通密度</h2>
<pre><code class="language-bash">magneticFoam -case baseCase -noH
</code></pre>
<p><code>-noH</code> 省去 <code>H</code> 的写出，仍保存磁势和 <code>B</code>。只关心磁通密度分布时，可减少一个矢量场的存储。</p>
<h2>示例 3：只保存磁场强度</h2>
<pre><code class="language-bash">magneticFoam -case baseCase -noB
</code></pre>
<p><code>-noB</code> 省去 <code>B</code> 的写出，保留磁势和 <code>H</code>。这里改变的是输出选择，磁势方程和磁体设置保持原样。</p>
<h2>示例 4：计算磁场梯度作用项</h2>
<pre><code class="language-bash">magneticFoam -case baseCase -HdotGradH
</code></pre>
<p>额外生成 <code>HdotGradH</code>，其计算式为 <code>H &amp; fvc::grad(H)</code>，可用于分析顺磁颗粒受力所需的场量。实际颗粒力还需结合磁化率与体积等参数。</p>
<h2>示例 5：仅保留磁势与梯度作用项</h2>
<pre><code class="language-bash">magneticFoam -case baseCase -noH -noB -HdotGradH
</code></pre>
<p>三个选项组合后，程序仍在内存中计算构造梯度项所需的 <code>H</code>，最终只写磁势和 <code>HdotGradH</code>。适合只需要后者进行进一步受力计算的工作流程。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-HdotGradH</code></td><td>Write the paramagnetic particle force field</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dry-run</code></td><td>Check case set-up only using a single time step</td></tr><tr><td><code>-dry-run-write</code></td><td>Check case set-up and write only using a single time step Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-listScalarBCs</code></td><td>List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)</td></tr><tr><td><code>-listVectorBCs</code></td><td>List vector field boundary conditions (fvPatchField&lt;vector&gt;)</td></tr><tr><td><code>-noB</code></td><td>Do not write the magnetic flux density field Do not execute function objects</td></tr><tr><td><code>-noH</code></td><td>Do not write the magnetic field intensity field Set named OptimisationSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: magneticFoam [OPTIONS]
Options:
  -HdotGradH        Write the paramagnetic particle force field
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
  -noB              Do not write the magnetic flux density field
  -noFunctionObjects
                    Do not execute function objects
  -noH              Do not write the magnetic field intensity field
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Solver for the magnetic field generated by permanent magnets.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/electromagnetics/magneticFoam/magneticFoam.C">源码与说明</a> · <a href="/assets/command-help/magneticfoam.txt">帮助文本</a></p>
