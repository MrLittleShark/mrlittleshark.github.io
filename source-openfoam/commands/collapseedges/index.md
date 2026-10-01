---
title: "collapseEdges  按字典折叠短边和低质量面"
layout: reference
description: "读取 collapseDict 或指定字典，折叠操作可改变网格拓扑。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>读取 collapseDict 或指定字典，折叠操作可改变网格拓扑。</p><h2>v2512 源码中的用途</h2><p>Collapses short edges and combines edges that are in line. - collapse short edges. Length of edges to collapse provided as argument. - merge two edges if they are in line. Maximum angle provided as argument. - remove unused points. - collapse faces: - with small areas to a single point - that have a high aspect ratio (i.e. sliver face) to a single edge Optionally checks the resulting mesh for bad faces and reduces the desired face length factor for those faces attached to the bad faces. When collapsing an edge with one point on the boundary it will leave the boundary point intact. When both points inside it chooses random. When both points on boundary random again.</p><h2>使用入口</h2><pre><code class="language-bash">collapseEdges</code></pre><h2>使用条件与核对</h2><p>读取 collapseDict 或指定字典，折叠操作可改变网格拓扑。 用法：collapseEdges [-dict 文件] 示例：collapseEdges
源码说明：Collapses short edges and combines edges that are in line. - collapse short edges. Length of edges to collapse provided as argument. - merge two edges if they are in line. Maximum angle provided as argument. - remove unused points. - collapse faces: - with small areas to a single point - that have a high aspect ratio (i.e. sliver face) to a single edge Optionally checks the resulting mesh for bad faces and reduces the desired face length factor for those faces attached to the bad faces. When collapsing an edge with one point on the boundary it will leave the boundary point intact. When both points inside it chooses random. When both points on boundary random again.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -collapseFaceSet -collapseFaces -constant -debug-switch -decomposeParDict -dict -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -latestTime -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noZero -opt-switch -overwrite -parallel -roots -time -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/collapseedges.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: collapseEdges
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/collapseEdges/collapseEdges.C


Usage: collapseEdges [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -collapseFaceSet &lt;faceSet&gt;
                    Collapse faces that are in the supplied face set
  -collapseFaces    Collapse small and sliver faces as well as small edges
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative collapseDict
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
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
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Collapses small edges to a point.
Optionally collapse small faces to a point and thin faces to an edge.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/collapseEdges/collapseEdges.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/collapseEdges/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
