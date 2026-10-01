---
title: "lumpedPointMovement  测试集中点运动及响应文件"
layout: reference
description: "采用对应耦合模型配置。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>采用对应耦合模型配置。</p><h2>v2512 源码中的用途</h2><p>This utility can be used to produce VTK files to visualize the response points/rotations and the corresponding movement of the building surfaces. Uses the tabulated responses from the specified file. Optionally, it can also be used to a dummy responder for the externalFileCoupler logic, which makes it useful as a debugging facility as well demonstrating how an external application could communicate with the lumpedPointMovement point-patch boundary condition.</p><h2>使用入口</h2><pre><code class="language-bash">lumpedPointMovement response.dat</code></pre><h2>使用条件与核对</h2><p>采用对应耦合模型配置。 用法：lumpedPointMovement 响应文件 [选项] 示例：lumpedPointMovement response.dat
源码说明：This utility can be used to produce VTK files to visualize the response points/rotations and the corresponding movement of the building surfaces. Uses the tabulated responses from the specified file. Optionally, it can also be used to a dummy responder for the externalFileCoupler logic, which makes it useful as a debugging facility as well demonstrating how an external application could communicate with the lumpedPointMovement point-patch boundary condition.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -decomposeParDict -doc -doc-source -dry-run -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -lib -max -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -opt-switch -parallel -removeLock -roots -scale -slave -span -visual-length -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/lumpedpointmovement.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: lumpedPointMovement
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lumped/lumpedPointMovement/lumpedPointMovement.C


Usage: lumpedPointMovement [OPTIONS] &lt;responseFile&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Test movement without a mesh
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
  -max &lt;N&gt;          Maximum number of outputs
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -removeLock       Remove lock-file on termination of slave
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -scale &lt;factor&gt;   Relaxation/scaling factor for movement (default: 1)
  -slave            Invoke as a slave responder for testing
  -span &lt;N&gt;         Increment each input by N (default: 1)
  -visual-length &lt;len&gt;
                    Visualization length for planes (visualized as triangles)
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Visualize lumpedPoint movements or provide a slave responder for diagnostic
purposes.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lumped/lumpedPointMovement/lumpedPointMovement.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lumped/lumpedPointMovement/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
