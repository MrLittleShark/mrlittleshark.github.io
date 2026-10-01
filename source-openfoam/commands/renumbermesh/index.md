---
title: "renumberMesh  重排网格编号以降低矩阵带宽"
layout: reference
description: "-write-maps 输出新旧编号映射，供外部编号关联使用。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>-write-maps 输出新旧编号映射，供外部编号关联使用。</p><h2>v2512 源码中的用途</h2><p>Renumbers the cell list in order to reduce the bandwidth, reading and renumbering all fields from all the time directories. By default uses bandCompression (Cuthill-McKee) or the method specified by the -renumber-method option, but will read system/renumberMeshDict if -dict option is present</p><h2>使用入口</h2><pre><code class="language-bash">renumberMesh -overwrite</code></pre><h2>使用条件与核对</h2><p>-write-maps 输出新旧编号映射，供外部编号关联使用。 用法：renumberMesh [选项] 示例：renumberMesh -overwrite
源码说明：Renumbers the cell list in order to reduce the bandwidth, reading and renumbering all fields from all the time directories. By default uses bandCompression (Cuthill-McKee) or the method specified by the -renumber-method option, but will read system/renumberMeshDict if -dict option is present
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-allRegions -case -constant -debug-switch -decompose -decomposeParDict -dict -doc -doc-source -dry-run -fileHandler -frontWidth -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -latestTime -lib -list-renumber -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-fields -no-libs -noZero -opt-switch -overwrite -parallel -region -regions -renumber-coeffs -renumber-method -roots -time -verbose -world -write-maps</p><p>关联配置：<a href="/dictionaries/system-renumbermeshdict/">renumberMeshDict</a></p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/renumbermesh.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: renumberMesh
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/renumberMesh/renumberMesh.C


Usage: renumberMesh [OPTIONS]
Options:
  -allRegions       Use all regions in regionProperties
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decompose        Aggregate initially with a decomposition method (serial
                    only)
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative renumberMeshDict
  -dry-run          Test without writing. Changes -write-maps to write VTK
                    output.
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -frontWidth       Calculate the RMS of the front-width
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -list-renumber    List available renumbering methods
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-fields        Suppress renumbering of fields (eg, when they are only
                    uniform)
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times (currently ignored)
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -renumber-coeffs &lt;string-content&gt;
                    Specify renumber coefficients (dictionary content) as
                    string. eg, &#x27;reverse true;&#x27;
  -renumber-method &lt;name&gt;
                    Specify renumber method (default: CuthillMcKee) without
                    dictionary
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;value&gt;     Select the nearest time to the specified value
  -verbose          Additional verbosity (can be used multiple times)
  -world &lt;name&gt;     Name of the local world for parallel communication
  -write-maps       Write renumber mappings
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Renumber mesh cells to reduce the bandwidth. Use the -lib option or dictionary
&#x27;libs&#x27; entry to load additional libraries

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/renumberMesh/renumberMesh.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/renumberMesh/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
