---
title: "refineWallLayer · 输入比例指定边的细分位置"
layout: reference
description: "输入比例指定边的细分位置。"
cms_slug: "command-refinewalllayer"
---

<p>输入比例指定边的细分位置。</p><h2>开始前</h2>
<p>已有包含指定壁面 patch 的网格；edgeFraction 决定沿壁面相连边切分的位置，取 0–1 之间的比例。</p>
<h2>示例 1：细化一个壁面附近的单元</h2>
<pre><code class="language-bash">refineWallLayer '(walls)' 0.5
</code></pre>
<p>对 walls 相邻的单元按一半比例切分，形成更细的近壁层。输出后检查壁面法向的单元尺寸。</p>
<h2>示例 2：获得更薄的第一层</h2>
<pre><code class="language-bash">refineWallLayer '(walls)' 0.2
</code></pre>
<p>将壁面附近切分比例设为 0.2，得到较薄的靠壁部分。与 0.5 的独立副本比较第一层高度和网格质量。</p>
<h2>示例 3：同时选择多组壁面</h2>
<pre><code class="language-bash">refineWallLayer '(upperWall lowerWall)' 0.3
</code></pre>
<p>同时处理上下壁面。两侧边界名称应与 boundary 文件一致，检查狭窄区域是否产生互相影响的切分。</p>
<h2>示例 4：把处理限制到单元集合</h2>
<pre><code class="language-bash">refineWallLayer '(walls)' 0.25 -useSet nearWallCells
</code></pre>
<p>仅在指定壁面附近且属于 nearWallCells 的单元中进行操作。适合局部壁面加密，保留其余区域原有分辨率。</p>
<h2>示例 5：在副本更新并检查</h2>
<pre><code class="language-bash">refineWallLayer '(walls)' 0.2 -overwrite
checkMesh -constant -allGeometry
</code></pre>
<p>更新原网格后检查近壁单元的长宽比、体积与非正交性。第一层高度仍需结合雷诺数、壁面模型及目标 y⁺ 估算。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-useSet &lt;name&gt;</code></td><td>Restrict cells to refine based on specified cellSet name</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: refineWallLayer [OPTIONS] &lt;patches&gt; &lt;edgeFraction&gt;
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
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/refineWallLayer/refineWallLayer.C">源码与说明</a> · <a href="/assets/command-help/refinewalllayer.txt">帮助文本</a></p>
