---
title: "mirrorMesh · 按字典定义的平面镜像并扩展网格"
layout: reference
description: "按字典定义的平面镜像并扩展网格。"
cms_slug: "command-mirrormesh"
---

<p>按字典定义的平面镜像并扩展网格。</p><h2>开始前</h2>
<p>已有半域网格和 system/mirrorMeshDict，字典定义镜像平面及 planeTolerance。</p>
<h2>示例 1：生成完整对称域</h2>
<pre><code class="language-bash">mirrorMesh
</code></pre>
<p>读取默认镜像平面，复制镜像侧单元；平面上的匹配边界转为内部连接，结果写入新网格时间。</p>
<h2>示例 2：采用另一镜像平面</h2>
<pre><code class="language-bash">mirrorMesh -dict system/mirrorMesh-yDict
</code></pre>
<p>替代字典描述另一个平面，可用于沿不同对称面扩展同一基础网格的副本。</p>
<h2>示例 3：镜像后直接继续预处理</h2>
<pre><code class="language-bash">mirrorMesh -overwrite
checkMesh
</code></pre>
<p>把完整域写回当前网格，检查镜像连接处的单元质量和边界分组。</p>
<h2>示例 4：调整平面识别容差</h2>
<pre><code class="language-bash">foamDictionary system/mirrorMeshDict -entry planeTolerance -set 1e-7
mirrorMesh
</code></pre>
<p>planeTolerance 用于判定点是否位于镜像平面上；1e-7 应结合本案例长度单位选择，结果中检查平面处是否出现细小缝隙。</p>
<h2>示例 5：镜像后修正周期配对</h2>
<pre><code class="language-bash">mirrorMesh -overwrite
createPatch -dict system/createPatch-cyclicDict -overwrite
</code></pre>
<p>输入网格带 cyclic 边界时，镜像可能改变面的对应顺序；替代 createPatchDict 重新建立周期配对，再用于后续计算。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: mirrorMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative mirrorMeshDict
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
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Mirrors a mesh around a given plane.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/mirrorMesh/mirrorFvMesh.C">源码与说明</a> · <a href="/assets/command-help/mirrormesh.txt">帮助文本</a></p>
