---
title: "snappyHexMesh  细化背景网格并生成贴体网格和边界层"
layout: reference
description: "输入包括背景网格及 constant/triSurface 中的表面。并行运行通过 mpirun 启动，并使用 -parallel。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>输入包括背景网格及 constant/triSurface 中的表面。并行运行通过 mpirun 启动，并使用 -parallel。</p><h2>v2512 源码中的用途</h2><p>Automatic split hex mesher. Refines and snaps to surface.</p><h2>使用入口</h2><pre><code class="language-bash">snappyHexMesh -overwrite</code></pre><h2>使用条件与核对</h2><p>输入包括背景网格及 constant/triSurface 中的表面。并行运行通过 mpirun 启动，并使用 -parallel。 用法：snappyHexMesh [-dict 文件] [-overwrite] 示例：snappyHexMesh -overwrite
源码说明：Automatic split hex mesher. Refines and snaps to surface.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -checkGeometry -debug-switch -decomposeParDict -dict -doc -doc-source -dry-run -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -opt-switch -outFile -overwrite -parallel -patches -profiling -region -roots -surfaceSimplify -world</p><p>关联配置：<a href="/dictionaries/system-snappyhexmeshdict/">snappyHexMeshDict</a> · <a href="/dictionaries/system-meshqualitydict/">meshQualityDict</a></p><h2>同版本官方教程</h2><p>以下链接直接指向 OpenFOAM-v2512 标签中的教程目录。先阅读 Allrun 确定网格生成、初始化和依赖，再在自己的工作目录运行。列出教程不表示本网站已执行它的全部计算。</p><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/refineMesh/cylinder">mesh/refineMesh/cylinder</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/flange">mesh/snappyHexMesh/flange</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/insidePoints">mesh/snappyHexMesh/insidePoints</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/gap_detection">mesh/snappyHexMesh/gap_detection</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/rotated_block">mesh/snappyHexMesh/rotated_block</a></li></ul><pre><code class="language-bash">mkdir -p &quot;&#36;FOAM_RUN&quot;
cd &quot;&#36;FOAM_RUN&quot;
# 先选择一个尚不存在的新目录；保留原教程
cp -r &quot;&#36;FOAM_TUTORIALS/mesh/refineMesh/cylinder&quot; ./snappyHexMesh-study
cd ./snappyHexMesh-study
ls
# 查看运行流程后，再决定执行哪些步骤
sed -n &#x27;1,200p&#x27; Allrun</code></pre><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/snappyhexmesh.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: snappyHexMesh
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/snappyHexMesh/snappyHexMesh.C


Usage: snappyHexMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -checkGeometry    Check all surface geometry for quality
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative snappyHexMeshDict
  -dry-run          Check case set-up only using a single time step
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
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -outFile &lt;file&gt;   Name of the file to save the simplified surface to
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -patches &lt;(patch0 .. patchN)&gt;
                    Only triangulate selected patches (wildcards supported)
  -profiling        Activate application-level profiling
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -surfaceSimplify &lt;boundBox&gt;
                    Simplify the surface using snappyHexMesh starting from a
                    boundBox
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Automatic split hex mesher. Refines and snaps to surface

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/snappyHexMesh/snappyHexMesh.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/snappyHexMesh/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
