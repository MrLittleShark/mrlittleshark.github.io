---
title: "redistributePar  并行重分区或重构网格和场"
layout: reference
description: "修改 decomposeParDict 后执行重分配，MPI 进程数取源分区数与目标分区数的较大值。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>修改 decomposeParDict 后执行重分配，MPI 进程数取源分区数与目标分区数的较大值。</p><h2>使用入口</h2><pre><code class="language-bash">mpirun -np 8 redistributePar -parallel -overwrite</code></pre><h2>使用条件与核对</h2><p>修改 decomposeParDict 后执行重分配，MPI 进程数取源分区数与目标分区数的较大值。 用法：redistributePar [选项] 示例：mpirun -np 8 redistributePar -parallel -overwrite MPI 程序采用 mpirun -np N 应用 -parallel 启动，其中 N 为进程数。例如，执行 mpirun -np 4 pimpleFoam -parallel 前，将 numberOfSubdomains 设为 4，并运行 decomposePar。
源码说明：
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-allRegions -case -cellDist -constant -debug-switch -decompose -decomposeParDict -doc -doc-source -dry-run -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -latestTime -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -newTimes -no-finite-area -no-libs -noZero -opt-switch -overwrite -parallel -reconstruct -region -regions -roots -time -verbose -withZero -world</p><p>关联配置：<a href="/dictionaries/system-decomposepardict/">decomposeParDict</a></p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/redistributepar.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: redistributePar
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/redistributePar/loadOrCreateMesh.C


Usage: redistributePar [OPTIONS]
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
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/redistributePar/loadOrCreateMesh.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/redistributePar/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
