---
title: "foamToTetDualMesh · 把单元场和边界面场映射为已有 tetDualMesh 的点场"
layout: reference
description: "把单元场和边界面场映射为已有 tetDualMesh 的点场。"
cms_slug: "command-foamtotetdualmesh"
---

<p>把单元场和边界面场映射为已有 tetDualMesh 的点场。</p><h2>开始前</h2>
<p>算例中已有原 polyMesh、目标区域 tetDualMesh/polyMesh 及其 pointDualAddressing。该映射表的长度须等于目标点数，正值对应原单元编号加 1，负值对应原边界面编号取负再减 1，0 对应未映射点。以下处理的是配套的网格与字段。</p>
<h2>示例 1：映射初始时刻的场</h2>
<pre><code class="language-bash">foamToTetDualMesh -time 0
</code></pre>
<p>读取 0 目录内的体标量、体矢量及张量场，按 pointDualAddressing 写出 0/tetDualMesh 下的同名点场。例如单元压力 p 转成目标网格的 pointScalarField。</p>
<h2>示例 2：映射指定结果时刻</h2>
<pre><code class="language-bash">foamToTetDualMesh -time 0.5
</code></pre>
<p>-time 选择最接近 0.5 的已有时间。各目标点从对应原单元或边界面取得数值；映射表中为 0 的点写入零值。适合把某一计算结果交给使用对偶点数据的后处理。</p>
<h2>示例 3：处理另一算例的最终结果</h2>
<pre><code class="language-bash">foamToTetDualMesh -case ./dualView -latestTime
</code></pre>
<p>dualView 已包含两套匹配网格和寻址表。-case 指定目录，-latestTime 选最后一个结果时间；输出仍位于这个时间的 tetDualMesh 区域下，原单元场保留。</p>
<h2>示例 4：转换一组已有时间</h2>
<pre><code class="language-bash">for t in 0.1 0.2 0.3; do
    foamToTetDualMesh -time "$t"
done
</code></pre>
<p>三个时间均已存在，并共享有效的对偶寻址关系。工具每次只选择一个时间，因此用循环分别产生三个时间的点场；网格拓扑改变时，应为该时刻准备匹配的目标网格和映射表。</p>
<h2>示例 5：检查目标网格和转换后的场类型</h2>
<pre><code class="language-bash">checkMesh -region tetDualMesh -constant
foamToTetDualMesh -time 0.5
foamDictionary 0.5/tetDualMesh/p -entry FoamFile/class -value
</code></pre>
<p>此例的两套网格保存在 constant，且 0.5/p 已存在。先检查目标区域网格，再映射压力；最后应读到 pointScalarField，可继续检查点数和映射表是否一致。转换程序读取目标网格，仅写转换后的场。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-time &lt;value&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamToTetDualMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times
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
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times (currently ignored)
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;value&gt;     Select the nearest time to the specified value
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert polyMesh results to tetDualMesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamToTetDualMesh/foamToTetDualMesh.C">源码与说明</a> · <a href="/assets/command-help/foamtotetdualmesh.txt">帮助文本</a></p>
