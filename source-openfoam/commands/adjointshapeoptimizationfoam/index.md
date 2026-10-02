---
title: "adjointShapeOptimizationFoam · 不可压缩流动的伴随形状优化"
layout: reference
description: "不可压缩流动的伴随形状优化。"
cms_slug: "command-adjointshapeoptimizationfoam"
---

<p>不可压缩流动的伴随形状优化。</p><h2>用法</h2><pre><code class="language-bash">adjointShapeOptimizationFoam -help-full</code></pre><h2>运行计算</h2><pre><code class="language-bash">adjointShapeOptimizationFoam &gt; log.adjointShapeOptimizationFoam 2&gt;&amp;1
tail -n 20 log.adjointShapeOptimizationFoam</code></pre><p>在已经准备好网格、物性和初始场的算例目录运行。第一行把终端输出保存到日志，计算结束后，第二行显示日志最后 20 行。计算结果按 controlDict 的设置写入时间目录。</p><h2>指定算例目录</h2><pre><code class="language-bash">adjointShapeOptimizationFoam -help-full -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-dry-run</td><td>Check case set-up only using a single time step</td></tr><tr><td>-dry-run-write</td><td>Check case set-up and write only using a single time step Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-listFvOptions</td><td>List fvOptions List switches registered for run-time modification (see -listUnsetSwitches option)</td></tr><tr><td>-listScalarBCs</td><td>List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)</td></tr><tr><td>-listVectorBCs</td><td>List vector field boundary conditions (fvPatchField&lt;vector&gt;)</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-postProcess</td><td>Execute functionObjects only Subprocess root directories for distributed running</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointShapeOptimizationFoam/pitzDaily">incompressible/adjointShapeOptimizationFoam/pitzDaily</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/incompressible/adjointShapeOptimizationFoam/pitzDaily&quot; adjointShapeOptimizationFoam-study
cd adjointShapeOptimizationFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: adjointShapeOptimizationFoam [OPTIONS]
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

Steady-state solver for incompressible, turbulent flow of non-Newtonian fluids
with duct shape optimisation by applying &#x27;blockage&#x27; in regions causing pressure
loss

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/incompressible/adjointShapeOptimizationFoam/adjointOutletPressure/adjointOutletPressureFvPatchScalarField.C">源码与说明</a> · <a href="/assets/command-help/adjointshapeoptimizationfoam.txt">帮助文本</a></p>
