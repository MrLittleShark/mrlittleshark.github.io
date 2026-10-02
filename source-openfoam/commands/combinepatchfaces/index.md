---
title: "combinePatchFaces · 通过 concaveAngle 及质量约束控制合并"
layout: reference
description: "通过 concaveAngle 及质量约束控制合并。"
cms_slug: "command-combinepatchfaces"
---

<p>通过 concaveAngle 及质量约束控制合并。</p><h2>开始前</h2>
<p>网格某些单元在同一 patch 上有多个近共面的边界面；工具将符合角度与凸凹条件的面合并。示例应在独立案例副本比较。</p>
<h2>示例 1：合并近共面的边界面</h2>
<pre><code class="language-bash">combinePatchFaces 5
</code></pre>
<p>以 5° 特征角判断可合并面，写出修改后的网格。适合整理几乎共面的碎面，检查边界面数变化。</p>
<h2>示例 2：提高允许折角</h2>
<pre><code class="language-bash">combinePatchFaces 20
</code></pre>
<p>允许更大的夹角参与合并，简化程度通常提高。比较外形与网格质量，确认曲面细节仍满足所需分辨率。</p>
<h2>示例 3：限制允许的凹角</h2>
<pre><code class="language-bash">combinePatchFaces 10 -concaveAngle 15
</code></pre>
<p>同时使用 10° 特征角和 15° 凹角参数，控制形成多边形面的几何形状。检查输出面是否出现不适合的凹形结构。</p>
<h2>示例 4：启用网格质量约束</h2>
<pre><code class="language-bash">combinePatchFaces 10 -meshQuality
</code></pre>
<p>读取 system/meshQualityDict 中的质量约束来检查合并操作。该字典应已配置完整，适合在面简化时保留明确质量条件。</p>
<h2>示例 5：在分解网格中合并</h2>
<pre><code class="language-bash">mpirun -np 4 combinePatchFaces 10 -parallel -overwrite
mpirun -np 4 checkMesh -parallel
</code></pre>
<p>四个子域均使用同一角度设置，直接更新分区网格。完成后检查处理器边界和新面质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-meshQuality</code></td><td>Read user-defined mesh quality criteria from system/meshQualityDict</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: combinePatchFaces [OPTIONS] &lt;featureAngle&gt;
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
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/combinePatchFaces/combinePatchFaces.C">源码与说明</a> · <a href="/assets/command-help/combinepatchfaces.txt">帮助文本</a></p>
