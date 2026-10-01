---
title: "transformPoints  对体网格进行平移旋转和缩放"
layout: reference
description: "示例将毫米坐标换算为米。外部源项位置和参考点需同步换算。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>示例将毫米坐标换算为米。外部源项位置和参考点需同步换算。</p><h2>v2512 源码中的用途</h2><p>Transforms the mesh points in the polyMesh directory according to the translate, rotate and scale options.</p><h2>使用入口</h2><pre><code class="language-bash">transformPoints -scale &#x27;(0.001 0.001 0.001)&#x27;</code></pre><h2>使用条件与核对</h2><p>示例将毫米坐标换算为米。外部源项位置和参考点需同步换算。 用法：transformPoints 变换选项 示例：transformPoints -scale &#x27;(0.001 0.001 0.001)&#x27;
源码说明：Transforms the mesh points in the polyMesh directory according to the translate, rotate and scale options.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-allRegions -auto-centre -case -centre -cylToCart -debug-switch -decomposeParDict -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noFunctionObjects -opt-switch -parallel -recentre -region -regions -rollPitchYaw -roots -rotate -rotate-angle -rotate-x -rotate-y -rotate-z -rotateFields -scale -time -translate -world -yawPitchRoll</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/transformpoints.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: transformPoints
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/transformPoints/transformPoints.C


Usage: transformPoints [OPTIONS]
Options:
  -allRegions       Use all regions in regionProperties
  -auto-centre      Use bounding box centre as centre for rotations
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -centre &lt;point&gt;   Use specified &lt;point&gt; as centre for rotations
  -cylToCart &lt;(originVec axisVec directionVec)&gt;
                    Tranform cylindrical coordinates to cartesian coordinates
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
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
  -recentre         Recentre the bounding box before other operations
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -rollPitchYaw &lt;vector&gt;
                    Rotate by &#x27;(roll pitch yaw)&#x27; degrees
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -rotate &lt;(vectorA vectorB)&gt;
                    Rotate from &lt;vectorA&gt; to &lt;vectorB&gt; - eg, &#x27;((1 0 0) (0 0 1))&#x27;
  -rotate-angle &lt;(vector angle)&gt;
                    Rotate &lt;angle&gt; degrees about &lt;vector&gt; - eg, &#x27;((1 0 0) 45)&#x27;
  -rotate-x &lt;deg&gt;   Rotate (degrees) about x-axis
  -rotate-y &lt;deg&gt;   Rotate (degrees) about y-axis
  -rotate-z &lt;deg&gt;   Rotate (degrees) about z-axis
  -rotateFields     Read and transform vector and tensor fields too
  -scale &lt;scalar | vector&gt;
                    Scale by the specified amount - Eg, for uniform [mm] to [m]
                    scaling use either &#x27;(0.001 0.001 0.001)&#x27; or simply &#x27;0.001&#x27;
  -time &lt;time&gt;      Specify the time to search from and apply the
                    transformation (default is latest)
  -translate &lt;vector&gt;
                    Translate by specified &lt;vector&gt; before rotations
  -world &lt;name&gt;     Name of the local world for parallel communication
  -yawPitchRoll &lt;vector&gt;
                    Rotate by &#x27;(yaw pitch roll)&#x27; degrees
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Transform (translate / rotate / scale) mesh points.
Note: roll=rotate about x, pitch=rotate about y, yaw=rotate about z

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/transformPoints/transformPoints.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/transformPoints/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
