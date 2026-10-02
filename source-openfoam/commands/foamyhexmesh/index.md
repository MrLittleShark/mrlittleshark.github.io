---
title: "foamyHexMesh · 读取 foamyHexMeshDict 和相关几何，运行需具备对应编译依赖"
layout: reference
description: "读取 foamyHexMeshDict 和相关几何，运行需具备对应编译依赖。"
cms_slug: "command-foamyhexmesh"
---

<p>读取 foamyHexMeshDict 和相关几何，运行需具备对应编译依赖。</p><h2>开始前</h2>
<p>准备完整foamyHexMeshDict与constant/triSurface几何；locationInMesh位于目标流体域，第三方依赖及程序已安装。</p>
<h2>示例 1：检查输入几何</h2>
<pre><code class="language-bash">foamyHexMesh -checkGeometry
</code></pre>
<p>读取字典中的全部表面并检查几何质量，先处理孔洞、交叉或区域选择问题。</p>
<h2>示例 2：生成Voronoi网格</h2>
<pre><code class="language-bash">foamyHexMesh
</code></pre>
<p>按尺寸、方向和表面贴合控制生成网格，日志显示初始点、贴合与平滑过程。</p>
<h2>示例 3：只做初始点贴合</h2>
<pre><code class="language-bash">foamyHexMesh -conformationOnly
</code></pre>
<p>已有合适初始点配置时，仅对初始点执行表面贴合，便于分离检查后续点运动的影响。</p>
<h2>示例 4：比较局部加密方案</h2>
<pre><code class="language-bash">foamyHexMesh -case ../foamyFine
</code></pre>
<p>fine副本已改变shapeControlFunctions的目标尺寸；单独生成后比较小间隙单元数和表面分辨率。</p>
<h2>示例 5：并行生成网格</h2>
<pre><code class="language-bash">mpirun -np 4 foamyHexMesh -parallel
</code></pre>
<p>按算例的并行准备流程设置4个分区及decomposeParDict，再并行运行，检查各进程分配与最终网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-checkGeometry</code></td><td>Check all surface geometry for quality Conform to the initial points without any point motion Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/flange">mesh/foamyHexMesh/flange</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamyHexMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -checkGeometry    Check all surface geometry for quality
  -conformationOnly
                    Conform to the initial points without any point motion
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

Conformal Voronoi automatic mesh generator

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/foamyMesh/foamyHexMesh/foamyHexMesh.C">源码与说明</a> · <a href="/assets/command-help/foamyhexmesh.txt">帮助文本</a></p>
