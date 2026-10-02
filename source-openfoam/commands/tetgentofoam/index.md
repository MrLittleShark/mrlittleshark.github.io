---
title: "tetgenToFoam · 按前缀读取配套的 node、ele 和 face 等文件"
layout: reference
description: "按前缀读取配套的 node、ele 和 face 等文件。"
cms_slug: "command-tetgentofoam"
---

<p>按前缀读取配套的 node、ele 和 face 等文件。</p><h2>开始前</h2>
<p>准备 TetGen 同名前缀的 .node、.ele 和 .face 文件；边界标记用于建立表面分区。</p>
<h2>示例 1：按前缀导入</h2>
<pre><code class="language-bash">tetgenToFoam mesh.1
</code></pre>
<p>读取 mesh.1.node、mesh.1.ele 和 mesh.1.face，建立四面体网格。检查边界标记对应的 patch 数量。</p>
<h2>示例 2：仅使用节点与单元文件</h2>
<pre><code class="language-bash">tetgenToFoam mesh.1 -noFaceFile
</code></pre>
<p>适用于没有 .face 文件的输入。网格仍可由节点和单元建立，所需边界分区需要后续按几何重新配置。</p>
<h2>示例 3：检查四面体质量</h2>
<pre><code class="language-bash">tetgenToFoam mesh.1
checkMesh -constant -allGeometry -allTopology
</code></pre>
<p>检查转换后的单元体积、非正交性和边界连接，确认输入中的四面体能够用于预期离散格式。</p>
<h2>示例 4：将毫米坐标换算为米</h2>
<pre><code class="language-bash">tetgenToFoam mesh-mm.1
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>TetGen 文件中的坐标数值被直接读取，转换后统一缩放。通过边界框检查实际长度。</p>
<h2>示例 5：为缺失标记的网格划分边界</h2>
<pre><code class="language-bash">tetgenToFoam mesh.1 -noFaceFile
autoPatch 45 -overwrite
</code></pre>
<p>根据外表面的折角建立边界分区。之后在可视化中确认各区位置，再使用 createPatchDict 整理为入口、出口和壁面。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFaceFile</code></td><td>Skip reading .face file for boundary information Do not execute function objects Set named OptimisationSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: tetgenToFoam [OPTIONS] &lt;prefix&gt;
Arguments:
  &lt;prefix&gt;          The prefix for the input tetgen files
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
  -noFaceFile       Skip reading .face file for boundary information
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

Convert tetgen .ele and .node and .face files to an OpenFOAM mesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/tetgenToFoam/tetgenToFoam.C">源码与说明</a> · <a href="/assets/command-help/tetgentofoam.txt">帮助文本</a></p>
