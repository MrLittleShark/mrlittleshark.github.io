---
title: "writeMorpherCPs · 写出体积 B 样条网格变形器的控制点"
layout: reference
description: "写出体积 B 样条网格变形器的控制点。"
cms_slug: "command-writemorphercps"
---

<p>写出体积 B 样条网格变形器的控制点。</p><h2>开始前</h2>
<p>constant/dynamicMeshDict 已含 volumetricBSplinesMotionSolverCoeffs 及各控制盒定义。</p>
<h2>示例 1：导出当前控制点布局</h2>
<pre><code class="language-bash">writeMorpherCPs
</code></pre>
<p>创建字典中每个B样条控制盒对象并写控制点，供查看设计变量在空间中的分布。</p>
<h2>示例 2：检查细化网格上的控制盒</h2>
<pre><code class="language-bash">writeMorpherCPs -case ./optimisation-fineMesh
</code></pre>
<p>细网格案例已有相同物理控制盒设置；输出控制点，比较控制盒与细化边界的相对位置。</p>
<h2>示例 3：比较另一套控制盒布置</h2>
<pre><code class="language-bash">cp -r shapeCase shapeCase-wideBox
# 在 shapeCase-wideBox/constant/dynamicMeshDict 中调整控制盒范围
writeMorpherCPs -case shapeCase-wideBox
</code></pre>
<p>在独立副本中修改既有控制盒的几何定义，再导出；检查设计区域是否覆盖待优化表面。</p>
<h2>示例 4：网格生成后导出控制点</h2>
<pre><code class="language-bash">blockMesh
writeMorpherCPs
</code></pre>
<p>blockMeshDict与变形器字典已配套；先生成当前设计几何网格，再输出控制点用于叠加检查。</p>
<h2>示例 5：与边界几何一起查看</h2>
<pre><code class="language-bash">writeMorpherCPs
foamToVTK -no-fields -no-internal -name VTK-designBoundary
</code></pre>
<p>导出控制点后，另外导出边界网格，在同一视图检查控制点密度与边界曲率、局部细节的对应。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: writeMorpherCPs [OPTIONS]
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
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/optimisation/writeMorpherCPs/writeMorpherCPs.C">源码与说明</a> · <a href="/assets/command-help/writemorphercps.txt">帮助文本</a></p>
