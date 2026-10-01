---
title: "combinePatchFaces  合并近共面的边界面"
layout: reference
description: "通过 concaveAngle 及质量约束控制合并。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>通过 concaveAngle 及质量约束控制合并。</p><h2>v2512 源码中的用途</h2><p>Checks for multiple patch faces on the same cell and combines them. Multiple patch faces can result from e.g. removal of refined neighbouring cells, leaving 4 exposed faces with same owner. Rules for merging: - only boundary faces (since multiple internal faces between two cells not allowed anyway) - faces have to have same owner - faces have to be connected via edge which are not features (so angle between them &lt; feature angle) - outside of faces has to be single loop - outside of face should not be (or just slightly) concave (so angle between consecutive edges &lt; concaveangle E.g. to allow all faces on same patch to be merged: combinePatchFaces 180 -concaveAngle 90</p><h2>使用入口</h2><pre><code class="language-bash">combinePatchFaces 5 -overwrite</code></pre><h2>使用条件与核对</h2><p>通过 concaveAngle 及质量约束控制合并。 用法：combinePatchFaces 特征角 [选项] 示例：combinePatchFaces 5 -overwrite
源码说明：Checks for multiple patch faces on the same cell and combines them. Multiple patch faces can result from e.g. removal of refined neighbouring cells, leaving 4 exposed faces with same owner. Rules for merging: - only boundary faces (since multiple internal faces between two cells not allowed anyway) - faces have to have same owner - faces have to be connected via edge which are not features (so angle between them &lt; feature angle) - outside of faces has to be single loop - outside of face should not be (or just slightly) concave (so angle between consecutive edges &lt; concaveangle E.g. to allow all faces on same patch to be merged: combinePatchFaces 180 -concaveAngle 90
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -concaveAngle -debug-switch -decomposeParDict -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -lib -meshQuality -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -opt-switch -overwrite -parallel -roots -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/combinepatchfaces.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: combinePatchFaces
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/combinePatchFaces/combinePatchFaces.C


Usage: combinePatchFaces [OPTIONS] &lt;featureAngle&gt;
Arguments:
  &lt;featureAngle&gt;    in degrees [0-180]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -concaveAngle &lt;degrees&gt;
                    Specify concave angle [0..180] (default: 30 degrees)
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
  -meshQuality      Read user-defined mesh quality criteria from
                    system/meshQualityDict
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Checks for multiple patch faces on the same cell and combines them.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/combinePatchFaces/combinePatchFaces.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/combinePatchFaces/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
