---
title: "redistributePar · 修改 decomposeParDict 后执行重分配，MPI 进程数取源分区数与目标分区数的较大"
layout: reference
description: "修改 decomposeParDict 后执行重分配，MPI 进程数取源分区数与目标分区数的较大值。"
cms_slug: "command-redistributepar"
---

<p>修改 decomposeParDict 后执行重分配，MPI 进程数取源分区数与目标分区数的较大值。</p><h2>用法</h2><pre><code class="language-bash">mpirun -np 8 redistributePar -parallel -overwrite</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">mpirun -np 8 redistributePar -parallel -overwrite -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-allRegions</td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-cellDist</td><td>写出单元所属子域，便于检查分区。</td></tr><tr><td>-constant</td><td>将 constant 目录加入选择。</td></tr><tr><td>-decompose</td><td>Decompose case Alternative decomposePar dictionary file</td></tr><tr><td>-dry-run</td><td>Test without writing the decomposition. Changes -cellDist to only write volScalarField. Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-newTimes</td><td>Only reconstruct new times (i.e. that do not exist already)</td></tr><tr><td>-no-finite-area</td><td>Suppress finiteArea mesh/field handling</td></tr><tr><td>-noZero</td><td>跳过 0 时刻。</td></tr><tr><td>-overwrite</td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-reconstruct</td><td>Reconstruct case</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-decomposepardict/">decomposeParDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: redistributePar [OPTIONS]
Options:
  -allRegions       Use all regions in regionProperties
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cellDist         Write cell distribution as a labelList - for use with
                    &#x27;manual&#x27; decomposition method or as a volScalarField for
                    post-processing.
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decompose        Decompose case
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Test without writing the decomposition. Changes -cellDist
                    to only write volScalarField.
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -newTimes         Only reconstruct new times (i.e. that do not exist already)
  -no-finite-area   Suppress finiteArea mesh/field handling
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times list, has precedence over
                    the -withZero option
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -reconstruct      Reconstruct case
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity. (Can be used multiple times)
  -withZero         Include &#x27;0/&#x27; dir in the times list
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Redistribute decomposed mesh and fields according to the decomposeParDict
settings.
Optionally run in decompose/reconstruct mode

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/redistributePar/loadOrCreateMesh.C">源码与说明</a> · <a href="/assets/command-help/redistributepar.txt">帮助文本</a></p>
