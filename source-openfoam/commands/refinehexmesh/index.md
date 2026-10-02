---
title: "refineHexMesh · 待细化集合可通过 topoSet 建立"
layout: reference
description: "待细化集合可通过 topoSet 建立。"
cms_slug: "command-refinehexmesh"
---

<p>待细化集合可通过 topoSet 建立。</p><h2>开始前</h2>
<p>网格由可进行 2×2×2 细化的六面体构成，并已有目标 cellSet；按几何选集时可先使用 topoSet。</p>
<h2>示例 1：细化选定单元</h2>
<pre><code class="language-bash">refineHexMesh refineCells
</code></pre>
<p>将 refineCells 中的六面体细分，工具会根据相邻细化等级关系调整实际选区。查看日志中的选中与最终细化单元数。</p>
<h2>示例 2：缩小选集以满足等级约束</h2>
<pre><code class="language-bash">refineHexMesh refineCells -minSet
</code></pre>
<p>通过从原选集中删减单元来满足细化约束；默认处理倾向于扩大选集。适合希望细化尽量局限在指定区域的情况。</p>
<h2>示例 3：直接更新案例副本</h2>
<pre><code class="language-bash">refineHexMesh refineCells -overwrite
checkMesh -constant
</code></pre>
<p>将细化结果写回原网格位置。检查单元数、网格连接和物理场映射，再继续计算。</p>
<h2>示例 4：细化命名区域</h2>
<pre><code class="language-bash">refineHexMesh hotCells -region solid
</code></pre>
<p>读取 solid 区域及其 hotCells 集合，只处理该区域的网格。适合局部加密固体传热区，需检查区域接口的一致性。</p>
<h2>示例 5：并行细化</h2>
<pre><code class="language-bash">mpirun -np 4 refineHexMesh refineCells -parallel -overwrite
mpirun -np 4 checkMesh -parallel
</code></pre>
<p>前提是网格与 refineCells 已分解到四个子域。并行细化后检查子域连接和各进程单元数量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-minSet</code></td><td>Remove cells from input cellSet to keep to 2:1 ratio (default is to extend set)</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: refineHexMesh [OPTIONS] &lt;cellSet&gt;
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
  -minSet           Remove cells from input cellSet to keep to 2:1 ratio
                    (default is to extend set)
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
  -region &lt;name&gt;    Specify mesh region (default: region0)
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

Refine a hex mesh by 2x2x2 cell splitting for the specified cellSet

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/refineHexMesh/refineHexMesh.C">源码与说明</a> · <a href="/assets/command-help/refinehexmesh.txt">帮助文本</a></p>
