---
title: "extrudeMesh · 读取 extrudeMeshDict"
layout: reference
description: "读取 extrudeMeshDict。"
cms_slug: "command-extrudemesh"
---

<p>读取 extrudeMeshDict。</p><h2>开始前</h2>
<p>已有待拉伸patch或字典指定的源表面，并准备system/extrudeMeshDict；其中确定源、方向、层数和厚度。</p>
<h2>示例 1：按默认字典拉伸</h2>
<pre><code class="language-bash">extrudeMesh
</code></pre>
<p>读取extrudeMeshDict，从所选源patch或表面生成拉伸网格，检查日志中的源面数与层数。</p>
<h2>示例 2：指定拉伸方案</h2>
<pre><code class="language-bash">extrudeMesh -dict system/extrudeMeshDict.thin
</code></pre>
<p>使用完整thin字典生成薄层网格，输出位置由拉伸方式与源/目标算例设置决定。</p>
<h2>示例 3：增加法向层数</h2>
<pre><code class="language-bash">foamDictionary system/extrudeMeshDict -entry nLayers -set 10
extrudeMesh
</code></pre>
<p>在已有法向拉伸配置中改为10层，比较层厚与厚度方向分辨率；总厚度仍由模型系数决定。</p>
<h2>示例 4：调整层厚增长</h2>
<pre><code class="language-bash">foamDictionary system/extrudeMeshDict -entry expansionRatio -set 1.2
extrudeMesh
</code></pre>
<p>在独立副本中让相邻层按1.2增长，适合从近壁细层向外过渡；检查最终层厚是否过大。</p>
<h2>示例 5：检查多区域源网格</h2>
<pre><code class="language-bash">extrudeMesh -region solid -dict system/extrudeMeshDict.solid
</code></pre>
<p>已准备solid区域及相应源patch的字典时，选择该源区域进行拉伸，核对输出区域连接与边界。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-extrudemeshdict/">extrudeMeshDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/extrudeMesh/polyline">mesh/extrudeMesh/polyline</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: extrudeMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative extrudeMeshDict
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

Extrude mesh from existing patch.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/extrude/extrudeMesh/extrudedMesh/extrudedMesh.C">源码与说明</a> · <a href="/assets/command-help/extrudemesh.txt">帮助文本</a></p>
