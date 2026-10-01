---
title: "setExprBoundaryFields  按表达式设置边界场"
layout: reference
description: "读取边界表达式字典，-backup 保留原场。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>读取边界表达式字典，-backup 保留原场。</p><h2>v2512 源码中的用途</h2><p>Set boundary values using an expression</p><h2>使用入口</h2><pre><code class="language-bash">setExprBoundaryFields</code></pre><h2>使用条件与核对</h2><p>读取边界表达式字典，-backup 保留原场。 用法：setExprBoundaryFields [-dict 文件] 示例：setExprBoundaryFields
源码说明：Set boundary values using an expression
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-ascii -backup -cache-fields -case -debug-switch -decomposeParDict -dict -doc -doc-source -dry-run -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -latestTime -lib -load-fields -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noZero -opt-switch -parallel -region -roots -time -withFunctionObjects -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/setexprboundaryfields.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: setExprBoundaryFields
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprBoundaryFields/setExprBoundaryFields.C


Usage: setExprBoundaryFields [OPTIONS]
Options:
  -ascii            Write in ASCII format instead of the controlDict setting
  -backup           Preserve sub-entry as .backup
  -cache-fields     Cache fields between calls
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative dictionary for setExprBoundaryFieldsDict
  -dry-run          Evaluate but do not write
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
  -load-fields &lt;wordList&gt;
                    Specify field or fields to preload. Eg, &#x27;T&#x27; or &#x27;(p T U)&#x27;
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -withFunctionObjects
                    Execute functionObjects
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprBoundaryFields/setExprBoundaryFields.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprBoundaryFields/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
