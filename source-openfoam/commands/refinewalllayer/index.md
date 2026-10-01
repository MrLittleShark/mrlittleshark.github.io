---
title: "refineWallLayer  细化近壁网格"
layout: reference
description: "输入比例指定边的细分位置。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>输入比例指定边的细分位置。</p><h2>v2512 源码中的用途</h2><p>Refine cells next to specified patches. Arguments: 1: List of patch names or regular expressions 2: The size of the refined cells as a fraction of the edge-length. Examples: Split the near-wall cells of patch Wall in the middle refineWallLayer &quot;(Wall)&quot; 0.5 Split the near-wall cells of patches Wall1 and Wall2 in the middle refineWallLayer &quot;(Wall1 Wall2)&quot; 0.5 Split the near-wall cells of all patches with names beginning with wall with the near-wall cells 10% of the thickness of the original cells refineWallLayer &#x27;(&quot;Wall.*&quot;)&#x27; 0.1</p><h2>使用入口</h2><pre><code class="language-bash">refineWallLayer &#x27;(walls)&#x27; 0.3 -overwrite</code></pre><h2>使用条件与核对</h2><p>输入比例指定边的细分位置。 用法：refineWallLayer patch列表 边比例 [选项] 示例：refineWallLayer &#x27;(walls)&#x27; 0.3 -overwrite
源码说明：Refine cells next to specified patches. Arguments: 1: List of patch names or regular expressions 2: The size of the refined cells as a fraction of the edge-length. Examples: Split the near-wall cells of patch Wall in the middle refineWallLayer &quot;(Wall)&quot; 0.5 Split the near-wall cells of patches Wall1 and Wall2 in the middle refineWallLayer &quot;(Wall1 Wall2)&quot; 0.5 Split the near-wall cells of all patches with names beginning with wall with the near-wall cells 10% of the thickness of the original cells refineWallLayer &#x27;(&quot;Wall.*&quot;)&#x27; 0.1
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -decomposeParDict -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -opt-switch -overwrite -parallel -roots -useSet -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/refinewalllayer.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: refineWallLayer
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/refineWallLayer/refineWallLayer.C


Usage: refineWallLayer [OPTIONS] &lt;patches&gt; &lt;edgeFraction&gt;
Arguments:
  &lt;patches&gt;         The list of patch names or regex - Eg, &#x27;(top &quot;Wall.&quot;)&#x27;
  &lt;edgeFraction&gt;    The size of the refined cells as a fraction of the
                    edge-length on a (0,1) interval
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
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -useSet &lt;name&gt;    Restrict cells to refine based on specified cellSet name
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Refine cells next to specified patches.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/refineWallLayer/refineWallLayer.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/refineWallLayer/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
