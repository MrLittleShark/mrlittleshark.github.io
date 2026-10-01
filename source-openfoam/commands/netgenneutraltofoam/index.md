---
title: "netgenNeutralToFoam  导入 Netgen 中性网格"
layout: reference
description: "转换后检查边界划分。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>转换后检查边界划分。</p><h2>v2512 源码中的用途</h2><p>Convert a neutral file format (Netgen v4.4) to OpenFOAM. Example: 9 1.000000 1.000000 1.000000 0.000000 1.000000 1.000000 0.000000 0.000000 1.000000 1.000000 0.000000 1.000000 0.000000 1.000000 0.000000 1.000000 1.000000 0.000000 1.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.500000 0.500000 0.500000 12 1 7 8 9 3 1 5 9 6 8 1 5 9 2 1 1 4 9 7 6 1 7 8 6 9 1 4 6 1 9 1 5 9 8 2 1 4 1 2 9 1 1 6 5 9 1 2 3 4 9 1 8 9 3 2 1 4 9 3 7 12 1 1 2 4 1 3 4 2 2 5 6 8 2 7 8 6 3 1 4 6 3 7 6 4 5 2 1 5 5 6 5 1 5 3 2 8 5 5 8 2 6 4 3 7 6 8 7 3 NOTE: - reverse order of boundary faces using geometric test. (not very space efficient) - order of tet vertices only tested on one file. - all patch/cell/vertex numbers offset by one.</p><h2>使用入口</h2><pre><code class="language-bash">netgenNeutralToFoam mesh.neutral</code></pre><h2>使用条件与核对</h2><p>转换后检查边界划分。 用法：netgenNeutralToFoam 中性网格文件 示例：netgenNeutralToFoam mesh.neutral
源码说明：Convert a neutral file format (Netgen v4.4) to OpenFOAM. Example: 9 1.000000 1.000000 1.000000 0.000000 1.000000 1.000000 0.000000 0.000000 1.000000 1.000000 0.000000 1.000000 0.000000 1.000000 0.000000 1.000000 1.000000 0.000000 1.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.500000 0.500000 0.500000 12 1 7 8 9 3 1 5 9 6 8 1 5 9 2 1 1 4 9 7 6 1 7 8 6 9 1 4 6 1 9 1 5 9 8 2 1 4 1 2 9 1 1 6 5 9 1 2 3 4 9 1 8 9 3 2 1 4 9 3 7 12 1 1 2 4 1 3 4 2 2 5 6 8 2 7 8 6 3 1 4 6 3 7 6 4 5 2 1 5 5 6 5 1 5 3 2 8 5 5 8 2 6 4 3 7 6 8 7 3 NOTE: - reverse order of boundary faces using geometric test. (not very space efficient) - order of tet vertices only tested on one file. - all patch/cell/vertex numbers offset by one.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -decomposeParDict -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -hostRoots -info-switch -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noFunctionObjects -opt-switch -parallel -roots -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/netgenneutraltofoam.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: netgenNeutralToFoam
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/netgenNeutralToFoam/netgenNeutralToFoam.C


Usage: netgenNeutralToFoam [OPTIONS] &lt;Neutral file&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
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
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert a neutral file format (Netgen v4.4) to OpenFOAM

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/netgenNeutralToFoam/netgenNeutralToFoam.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/netgenNeutralToFoam/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
