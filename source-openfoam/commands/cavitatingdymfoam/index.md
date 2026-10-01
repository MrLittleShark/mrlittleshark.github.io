---
title: "cavitatingDyMFoam · 动网格均相平衡空化流动"
layout: reference
description: "动网格均相平衡空化流动。具体方程、物理假设和所需字段见下方源码与教程。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>动网格均相平衡空化流动。具体方程、物理假设和所需字段见下方源码与教程。</p><h2>v2512 源码中的用途</h2><p>Transient cavitation solver based on the homogeneous equilibrium model from which the compressibility of the liquid/vapour &#x27;mixture&#x27; is obtained, with optional mesh motion and mesh topology changes. Turbulence modelling is generic, i.e. laminar, RAS or LES may be selected.</p><h2>使用入口</h2><pre><code class="language-bash">cavitatingDyMFoam -help-full</code></pre><h2>使用条件与核对</h2><p>
源码说明：Transient cavitation solver based on the homogeneous equilibrium model from which the compressibility of the liquid/vapour &#x27;mixture&#x27; is obtained, with optional mesh motion and mesh topology changes. Turbulence modelling is generic, i.e. laminar, RAS or LES may be selected.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -decomposeParDict -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -hostRoots -info-switch -lib -listFunctionObjects -listRegisteredSwitches -listScalarBCs -listSwitches -listTurbulenceModels -listUnsetSwitches -listVectorBCs -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noFunctionObjects -opt-switch -parallel -postProcess -roots -world</p><p>关联配置：<a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/cavitatingdymfoam.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: cavitatingDyMFoam
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/multiphase/cavitatingFoam/cavitatingDyMFoam/cavitatingDyMFoam.C


Usage: cavitatingDyMFoam [OPTIONS]
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
  -listFunctionObjects
                    List functionObjects
  -listRegisteredSwitches
                    List switches registered for run-time modification (see
                    -listUnsetSwitches option)
  -listScalarBCs    List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)
  -listSwitches     List switches declared in libraries (see -listUnsetSwitches
                    option)
  -listTurbulenceModels
                    List turbulenceModels
  -listUnsetSwitches
                    Modifies switch listing to display values not set in
                    etc/controlDict
  -listVectorBCs    List vector field boundary conditions (fvPatchField&lt;vector&gt;)
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
  -postProcess      Execute functionObjects only
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Transient cavitation solver based on the homogeneous equilibrium model from
which the compressibility of the liquid/vapour &#x27;mixture&#x27; is obtained.
With optional mesh motion and mesh topology changes.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/multiphase/cavitatingFoam/cavitatingDyMFoam/cavitatingDyMFoam.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/multiphase/cavitatingFoam/cavitatingDyMFoam/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
