---
title: "checkFaMesh  检查有限面积网格"
layout: reference
description: "检查对象为有限面积网格。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>检查对象为有限面积网格。</p><h2>v2512 源码中的用途</h2><p>Check a finite-area mesh Original Authors Zeljko Tukovic, FAMENA Hrvoje Jasak, Wikki Ltd.</p><h2>使用入口</h2><pre><code class="language-bash">checkFaMesh</code></pre><h2>使用条件与核对</h2><p>检查对象为有限面积网格。 用法：checkFaMesh [选项] 示例：checkFaMesh
源码说明：Check a finite-area mesh Original Authors Zeljko Tukovic, FAMENA Hrvoje Jasak, Wikki Ltd.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-allAreas -area-region -area-regions -case -debug-switch -decomposeParDict -doc -doc-source -fileHandler -geometryOrder -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noFunctionObjects -opt-switch -parallel -region -roots -world -write-vtk</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/checkfamesh.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: checkFaMesh
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/finiteArea/checkFaMesh/checkFaMesh.C


Usage: checkFaMesh [OPTIONS]
Options:
  -allAreas         Use all regions in finite-area regionProperties
  -area-region &lt;name&gt;
                    Specify area-mesh region. Eg, -area-region shell
  -area-regions &lt;wordRes&gt;
                    Use specified area region. Eg, -area-regions film
                    Or from regionProperties.  Eg, -area-regions &#x27;(film
                    &quot;solid.*&quot;)&#x27;
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -geometryOrder &lt;N&gt;
                    Test different geometry order - experimental!!
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
  -write-vtk        Write mesh as a vtp (vtk) file for display or debugging
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Check a finite-area mesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/finiteArea/checkFaMesh/checkFaMesh.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/finiteArea/checkFaMesh/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
