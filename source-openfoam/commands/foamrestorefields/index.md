---
title: "foamRestoreFields  恢复备份或转换后的场"
layout: reference
description: "从已有备份恢复，method 按命令帮助指定。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>从已有备份恢复，method 按命令帮助指定。</p><h2>v2512 源码中的用途</h2><p>Adjust (restore) field names by removing the ending. The fields are selected automatically or can be specified as optional command arguments. The operation &#x27;mean&#x27; renames files ending with &#x27;Mean&#x27; and makes a backup of existing names, using the &#x27;.orig&#x27; ending. The operation &#x27;orig&#x27; renames files ending with &#x27;.orig&#x27;.</p><h2>使用入口</h2><pre><code class="language-bash">foamRestoreFields U p</code></pre><h2>使用条件与核对</h2><p>从已有备份恢复，method 按命令帮助指定。 用法：foamRestoreFields [选项] 场名列表 示例：foamRestoreFields U p
源码说明：Adjust (restore) field names by removing the ending. The fields are selected automatically or can be specified as optional command arguments. The operation &#x27;mean&#x27; renames files ending with &#x27;Mean&#x27; and makes a backup of existing names, using the &#x27;.orig&#x27; ending. The operation &#x27;orig&#x27; renames files ending with &#x27;.orig&#x27;.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-allRegions -case -constant -debug-switch -decomposeParDict -doc -doc-source -dry-run -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -latestTime -lib -method -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noZero -opt-switch -parallel -processor -region -regions -roots -time -verbose -withZero -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamrestorefields.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: foamRestoreFields
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamRestoreFields/foamRestoreFields.C


Usage: foamRestoreFields [OPTIONS] [&lt;fieldName ... fieldName&gt;]
Options:
  -allRegions       Use all regions in regionProperties
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Report action without moving/renaming
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
  -method &lt;name&gt;    The restore method (mean|orig) [MANDATORY]. With &lt;mean&gt;
                    renames files ending with &#x27;Mean&#x27; (with backup of existing
                    as &#x27;.orig&#x27;). With &lt;orig&gt; renames files ending with &#x27;.orig&#x27;
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times list, has precedence over
                    the -withZero option
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -processor        In serial mode use times from processor0/ directory, but
                    operate on processor\d+ directories
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -withZero         Include &#x27;0/&#x27; dir in the times list
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Restore field names by removing the ending. Fields are selected automatically
or can be specified as optional command arguments

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamRestoreFields/foamRestoreFields.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamRestoreFields/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
