---
title: "refinementLevel · 用于贴体变形前的网格"
layout: reference
description: "用于贴体变形前的网格。"
cms_slug: "command-refinementlevel"
---

<p>用于贴体变形前的网格。</p><h2>开始前</h2>
<p>用于经过 2×2×2 笛卡尔细化且尚未贴体变形的网格。程序按单元体积分类，写出级别场及相关集合。</p>
<h2>示例 1：识别体积对应的细化级别</h2>
<pre><code class="language-bash">refinementLevel
</code></pre>
<p>按体积分组生成 vol0、vol1 等 cellSet，以及用于显示的 refinementLevel 场。较小单元对应更高细化级别。</p>
<h2>示例 2：处理已有级别文件的案例</h2>
<pre><code class="language-bash">refinementLevel -readLevel
</code></pre>
<p>允许读取已经存在的 refinementLevel 标签文件继续处理；程序仍按当前体积分箱计算级别。适合检查已有细化状态与当前网格的对应关系。</p>
<h2>示例 3：在独立未贴体网格中检查</h2>
<pre><code class="language-bash">refinementLevel -case ../castellatedCase
</code></pre>
<p>指定只完成笛卡尔细化的案例。查看终端的体积组和每组单元数，判断目标区域细化是否达到预期。</p>
<h2>示例 4：使用建议集合继续细化</h2>
<pre><code class="language-bash">refinementLevel
refineHexMesh refCells
</code></pre>
<p>当工具明确报告写出非空 refCells 时执行第二步。该集合标出需要继续细化以改善相邻等级过渡的单元，之后重新检查等级关系。</p>
<h2>示例 5：并行检查细化等级</h2>
<pre><code class="language-bash">mpirun -np 4 refinementLevel -parallel
</code></pre>
<p>在已分解的未贴体网格上运行，写出各子域的级别信息。比较各进程报告，检查局部细化分布及跨子域的过渡区域。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-readLevel</code></td><td>Read level from refinementLevel file Subprocess root directories for distributed running</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: refinementLevel [OPTIONS]
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
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -readLevel        Read level from refinementLevel file
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Attempt to determine refinement levels of a refined cartesian mesh.
Run BEFORE snapping!

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/refinementLevel/refinementLevel.C">源码与说明</a> · <a href="/assets/command-help/refinementlevel.txt">帮助文本</a></p>
