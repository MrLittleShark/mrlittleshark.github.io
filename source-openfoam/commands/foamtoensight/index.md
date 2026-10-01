---
title: "foamToEnsight  导出 EnSight 数据集"
layout: reference
description: "选项可控制区域、粒子及场数据的输出范围。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>选项可控制区域、粒子及场数据的输出范围。</p><h2>使用入口</h2><pre><code class="language-bash">foamToEnsight -latestTime -fields &#x27;(U p)&#x27;</code></pre><h2>使用条件与核对</h2><p>选项可控制区域、粒子及场数据的输出范围。 用法：foamToEnsight [选项] 示例：foamToEnsight -latestTime -fields &#x27;(U p)&#x27;
源码说明：
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-allAreas -allRegions -area-region -area-regions -ascii -case -cellZones -constant -debug-switch -decomposeParDict -doc -doc-source -exclude-fields -exclude-patches -faceZones -fields -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -index -info-switch -latestTime -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -name -nearCellValue -no-boundary -no-cellZones -no-fields -no-finite-area -no-internal -no-lagrangian -no-libs -no-mesh -no-overwrite -no-point-data -noFunctionObjects -noZero -nodeValues -opt-switch -parallel -patches -region -regions -roots -time -verbose -width -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamtoensight.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: foamToEnsight
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamToEnsight/readFields.C


Usage: foamToEnsight [OPTIONS]
Options:
  -allAreas         Use all regions in finite-area regionProperties
  -allRegions       Use all regions in regionProperties
  -area-region &lt;name&gt;
                    Specify area-mesh region. Eg, -area-region shell
  -area-regions &lt;wordRes&gt;
                    Use specified area region. Eg, -area-regions film
                    Or from regionProperties.  Eg, -area-regions &#x27;(film
                    &quot;solid.*&quot;)&#x27;
  -ascii            Write in ASCII format instead of &#x27;C Binary&#x27;
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cellZones &lt;wordRes&gt;
                    Specify single or multiple cellZones to write
                    Eg, &#x27;cells&#x27; or &#x27;( slice &quot;mfp-.*&quot; )&#x27;.
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -exclude-fields &lt;wordRes&gt;
                    Exclude single or multiple fields
  -exclude-patches &lt;wordRes&gt;
                    Exclude single or multiple patches from writing
                    Eg, &#x27;outlet&#x27; or &#x27;( inlet &quot;.*Wall&quot; )&#x27;
  -faceZones &lt;wordRes&gt;
                    Specify single or multiple faceZones to write
                    Eg, &#x27;cells&#x27; or &#x27;( slice &quot;mfp-.*&quot; )&#x27;.
  -fields &lt;wordRes&gt;
                    Specify single or multiple fields to write (all by default)
                    Eg, &#x27;T&#x27; or &#x27;( &quot;U.*&quot; )&#x27;
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -index &lt;start&gt;    Starting index for consecutive number of Ensight data/
                    files. Ignore the time index contained in the uniform/time
                    file.
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
  -name &lt;subdir&gt;    Sub-directory name for Ensight output (default: &#x27;EnSight&#x27;)
  -nearCellValue    Use zero-gradient cell values on patches
  -no-boundary      Suppress writing any patches
  -no-cellZones     Suppress writing any cellZones
  -no-fields        Suppress conversion of fields
  -no-finite-area   Suppress output of finite-area mesh/fields
  -no-internal      Suppress writing the internal mesh
  -no-lagrangian    Suppress writing lagrangian positions and fields
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-mesh          Suppress writing the geometry. Can be useful for converting
                    partial results for a static geometry
  -no-overwrite     Suppress removal of existing EnSight output directory
  -no-point-data    Suppress conversion of pointFields, disable -nodeValues
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -nodeValues       Force interpolation of values to nodes
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -patches &lt;wordRes&gt;
                    Specify single patch or multiple patches to write
                    Eg, &#x27;inlet&#x27; or &#x27;(outlet &quot;inlet.*&quot;)&#x27;
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -width &lt;n&gt;        Width of Ensight data subdir
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Translate OpenFOAM data to Ensight format with individual parts for cellZones,
unzoned cells and patches

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamToEnsight/readFields.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamToEnsight/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
