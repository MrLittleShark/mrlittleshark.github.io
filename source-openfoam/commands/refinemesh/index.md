---
title: "refineMesh · 沿指定方向细化全域或选定单元"
layout: reference
description: "沿指定方向细化全域或选定单元。"
cms_slug: "command-refinemesh"
---

<p>沿指定方向细化全域或选定单元。</p><h2>开始前</h2>
<p>已有网格；局部或定向细化需要 system/refineMeshDict 及其引用的cellSet。</p>
<h2>示例 1：全域细化</h2>
<pre><code class="language-bash">refineMesh -all
</code></pre>
<p>选择所有单元细化，生成新的网格时间；检查细化前后单元数量与最小尺寸。</p>
<h2>示例 2：按默认字典局部细化</h2>
<pre><code class="language-bash">refineMesh
</code></pre>
<p>读取 refineMeshDict 的选区和方向，对指定单元做定向细化，适合局部提高分辨率。</p>
<h2>示例 3：先选区再细化</h2>
<pre><code class="language-bash">topoSet -dict system/topoSet-wakeDict
refineMesh -dict system/refineMesh-wakeDict -overwrite
</code></pre>
<p>两个字典约定同一个尾流 cellSet；先选尾流单元，再按指定方向细化并更新当前网格。</p>
<h2>示例 4：细化多区域中的流体</h2>
<pre><code class="language-bash">refineMesh -region fluid -all -overwrite
</code></pre>
<p>只细化 fluid 区域的全部单元，适合独立检查流体网格分辨率变化。</p>
<h2>示例 5：连续两级全域细化</h2>
<pre><code class="language-bash">refineMesh -all -overwrite
refineMesh -all -overwrite
checkMesh
</code></pre>
<p>第二次读取第一次细化后的网格，获得两级细化结果；单元数和所需内存会随细化明显增加，最终检查质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-all</code></td><td>Refine all cells</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-refinemeshdict/">refineMeshDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/refineMesh/refineFieldDirs">mesh/refineMesh/refineFieldDirs</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: refineMesh [OPTIONS]
Options:
  -all              Refine all cells
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative refineMeshDict
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

Refine cells in multiple directions

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/refineMesh/refineMesh.C">源码与说明</a> · <a href="/assets/command-help/refinemesh.txt">帮助文本</a></p>
