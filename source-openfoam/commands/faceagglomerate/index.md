---
title: "faceAgglomerate  聚合辐射边界面并输出映射"
layout: reference
description: "用于视角因子计算的前处理。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>用于视角因子计算的前处理。</p><h2>v2512 源码中的用途</h2><p>Agglomerate boundary faces using the pairPatchAgglomeration algorithm. It writes a map from the fine to coarse grid. SeeAlso pairPatchAgglomeration.H</p><h2>使用入口</h2><pre><code class="language-bash">faceAgglomerate</code></pre><h2>使用条件与核对</h2><p>用于视角因子计算的前处理。 用法：faceAgglomerate [-dict 文件] 示例：faceAgglomerate
源码说明：Agglomerate boundary faces using the pairPatchAgglomeration algorithm. It writes a map from the fine to coarse grid. SeeAlso pairPatchAgglomeration.H
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -decomposeParDict -dict -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -hostRoots -info-switch -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noFunctionObjects -opt-switch -parallel -region -roots -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/faceagglomerate.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: faceAgglomerate
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/faceAgglomerate/faceAgglomerate.C


Usage: faceAgglomerate [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative viewFactorsDict
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
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Agglomerate boundary faces using the pairPatchAgglomeration algorithm. Writes a
map of fine to coarse grid.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/faceAgglomerate/faceAgglomerate.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/faceAgglomerate/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
