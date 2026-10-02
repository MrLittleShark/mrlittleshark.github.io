---
title: "PDRMesh · 输入包括 blockedCells、blockedFaces 等集合"
layout: reference
description: "输入包括 blockedCells、blockedFaces 等集合。"
cms_slug: "command-pdrmesh"
---

<p>输入包括 blockedCells、blockedFaces 等集合。</p><h2>开始前</h2>
<p>已有 PDR 网格、system/PDRMeshDict、blockedCells 单元集及需要的面集；blockedFaces 的目标 patch 必须已存在。示例在案例副本执行。</p>
<h2>示例 1：移除阻塞单元并生成边界</h2>
<pre><code class="language-bash">PDRMesh
</code></pre>
<p>按 PDRMeshDict 的 blockedCells 删除阻塞区域，将暴露面放到指定 patch，结果写入后续时间。检查日志中的保留单元数和新边界面数。</p>
<h2>示例 2：指定阻塞单元集合</h2>
<pre><code class="language-bash">foamDictionary system/PDRMeshDict -entry blockedCells -set obstacleCells
PDRMesh
</code></pre>
<p>前提是 obstacleCells 已准备好。更换被排除的单元区域，可以比较不同障碍物布置对有效流体域的影响。</p>
<h2>示例 3：为阻塞面设置目标边界</h2>
<pre><code class="language-bash">foamDictionary system/PDRMeshDict -entry blockedFaces -set '((screenFaces screenWall))'
PDRMesh
</code></pre>
<p>把 screenFaces 中的阻塞面分配到已有 screenWall patch。检查两侧挡板面及由删除单元暴露的面是否得到正确分组。</p>
<h2>示例 4：设置其他暴露面的归属</h2>
<pre><code class="language-bash">foamDictionary system/PDRMeshDict -entry defaultPatch -set obstacleWall
PDRMesh -overwrite
</code></pre>
<p>未被 blockedFaces 等条目明确分配的暴露面进入 obstacleWall。-overwrite 把结果写回原网格位置，运行前使用可恢复的独立副本。</p>
<h2>示例 5：在分解网格上处理</h2>
<pre><code class="language-bash">mpirun -np 4 PDRMesh -parallel -overwrite
mpirun -np 4 checkMesh -parallel
</code></pre>
<p>前提是网格、集合及 PDR 设置已一致分解为四个子域。并行处理后检查跨处理器连接以及新生成边界。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: PDRMesh [OPTIONS]
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
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Mesh and field preparation utility for PDR type simulations.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/PDRMesh/PDRMesh.C">源码与说明</a> · <a href="/assets/command-help/pdrmesh.txt">帮助文本</a></p>
