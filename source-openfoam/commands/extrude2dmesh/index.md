---
title: "extrude2DMesh · 读取 system/extrude2DMeshDict"
layout: reference
description: "读取 system/extrude2DMeshDict。polyMesh2D 输入为仅含顶点和边的二维网格。"
cms_slug: "command-extrude2dmesh"
---

<p>读取 system/extrude2DMeshDict。polyMesh2D 输入为仅含顶点和边的二维网格。</p><h2>开始前</h2>
<p>已有二维输入及system/extrude2DMeshDict。位置参数只接受polyMesh2D或MeshedSurface，大小写按源码填写。</p>
<h2>示例 1：拉伸二维体网格</h2>
<pre><code class="language-bash">extrude2DMesh polyMesh2D
</code></pre>
<p>从polyMesh2D路径构造输入网格，按字典生成三维厚度方向单元，日志显示生成时间。</p>
<h2>示例 2：使用表面网格输入</h2>
<pre><code class="language-bash">extrude2DMesh MeshedSurface
</code></pre>
<p>已有该模式所需的MeshedSurface数据时，选择表面输入通路；字典仍控制拉伸模型和层数。</p>
<h2>示例 3：指定另一个算例</h2>
<pre><code class="language-bash">extrude2DMesh -case ../thinChannel polyMesh2D
</code></pre>
<p>在thinChannel中读取二维网格与拉伸字典，结果也写入该算例。</p>
<h2>示例 4：改变直线拉伸厚度</h2>
<pre><code class="language-bash">foamDictionary system/extrude2DMeshDict -entry linearDirectionCoeffs.thickness -set 0.02
extrude2DMesh polyMesh2D
</code></pre>
<p>前提extrudeModel为linearDirection；将厚度设为0.02m，并检查生成网格的包围盒。</p>
<h2>示例 5：增加三维分辨率</h2>
<pre><code class="language-bash">foamDictionary system/extrude2DMeshDict -entry nLayers -set 5
extrude2DMesh polyMesh2D
checkMesh -latestTime
</code></pre>
<p>把厚度方向改成5层后检查新网格；用于三维计算时，前后边界应采用相应物理类型。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: extrude2DMesh [OPTIONS] &lt;surfaceFormat&gt;
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

Create a 3D mesh from a 2D mesh by extruding with specified thickness

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/extrude2DMesh/extrude2DMeshApp.C">源码与说明</a> · <a href="/assets/command-help/extrude2dmesh.txt">帮助文本</a></p>
