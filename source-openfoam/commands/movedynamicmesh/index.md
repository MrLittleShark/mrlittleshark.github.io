---
title: "moveDynamicMesh · 运行动态网格更新，检查运动和拓扑变化"
layout: reference
description: "运行动态网格更新，检查运动和拓扑变化。"
cms_slug: "command-movedynamicmesh"
---

<p>运行动态网格更新，检查运动和拓扑变化。</p><h2>开始前</h2>
<p>已有 constant/dynamicMeshDict、所需位移或运动场，以及 controlDict 时间设置；运动边界与运动求解器一致。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：单独运行网格运动</h2>
<pre><code class="language-bash">moveDynamicMesh
</code></pre>
<p>按 controlDict 推进时间并调用 dynamicFvMesh 更新，写出设置的运动网格时间，便于先检查运动轨迹。</p>
<h2>示例 2：限制运动试验长度</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry endTime -set 0.1
moveDynamicMesh
</code></pre>
<p>将试验终止时间设为 0.1，仅生成起始运动阶段；检查最早出现的大变形或局部挤压。</p>
<h2>示例 3：检查 AMI 接口</h2>
<pre><code class="language-bash">moveDynamicMesh -checkAMI
</code></pre>
<p>用于存在 AMI 接口的动态网格；额外检查插值权重并写接口 VTK 文件，观察相对运动中的覆盖情况。</p>
<h2>示例 4：检查指定运动区域</h2>
<pre><code class="language-bash">moveDynamicMesh -region rotor
</code></pre>
<p>案例已经为 rotor 区域提供动态网格设置；只推进该区域，输出它的运动网格。</p>
<h2>示例 5：并行运动预演</h2>
<pre><code class="language-bash">decomposePar
mpirun -np 4 moveDynamicMesh -parallel -checkAMI
</code></pre>
<p>decomposeParDict 设置 4 个子域；运动在分区网格上执行，检查并行边界和 AMI 随运动的变化，结果写入 processor 目录。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-checkAMI</code></td><td>Check AMI weights and write VTK files of the AMI patches Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/pipe">mesh/blockMesh/pipe</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/moveDynamicMesh/badMove">mesh/moveDynamicMesh/badMove</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/moveDynamicMesh/bendJunction">mesh/moveDynamicMesh/bendJunction</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/moveDynamicMesh/faceZoneBlock">mesh/moveDynamicMesh/faceZoneBlock</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/moveDynamicMesh/twistingColumn">mesh/moveDynamicMesh/twistingColumn</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: moveDynamicMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -checkAMI         Check AMI weights and write VTK files of the AMI patches
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
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Mesh motion and topological mesh changes utility

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/moveDynamicMesh/moveDynamicMesh.C">源码与说明</a> · <a href="/assets/command-help/movedynamicmesh.txt">帮助文本</a></p>
