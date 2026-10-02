---
title: "extrudeToRegionMesh · 用于薄层或膜区域，源面和目标区域名称由字典指定"
layout: reference
description: "用于薄层或膜区域，源面和目标区域名称由字典指定。"
cms_slug: "command-extrudetoregionmesh"
---

<p>用于薄层或膜区域，源面和目标区域名称由字典指定。</p><h2>开始前</h2>
<p>已有faceZone或faceSet以及system/extrudeToRegionMeshDict；字典给出新region名、源面、厚度、层数和映射方式。</p>
<h2>示例 1：生成壁膜区域</h2>
<pre><code class="language-bash">extrudeToRegionMesh
</code></pre>
<p>按默认定义从源面拉伸出新区域，例如wallFilmRegion，输出新的区域网格及界面设置。</p>
<h2>示例 2：选择固体板方案</h2>
<pre><code class="language-bash">extrudeToRegionMesh -dict system/extrudeToRegionMeshDict.panel
</code></pre>
<p>在完整panel定义中指定region panelRegion，生成固体板区域，适合共轭传热或热解模型。</p>
<h2>示例 3：加密厚度方向</h2>
<pre><code class="language-bash">foamDictionary system/extrudeToRegionMeshDict -entry nLayers -set 8
extrudeToRegionMesh
</code></pre>
<p>同一源面、同一厚度下生成8层；线性均匀拉伸且expansionRatio=1时每层厚度为总厚度的1/8。</p>
<h2>示例 4：从指定体区域拉伸</h2>
<pre><code class="language-bash">extrudeToRegionMesh -region air -dict system/extrudeToRegionMeshDict.panel
</code></pre>
<p>源面位于air区域时选择该体网格，避免在默认区域查找同名faceZone。</p>
<h2>示例 5：建立并检查新区域</h2>
<pre><code class="language-bash">extrudeToRegionMesh
checkMesh -region panelRegion
</code></pre>
<p>字典中的region必须为panelRegion；检查生成区域的单元体积、厚度及耦合面，确认它可供后续区域求解。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: extrudeToRegionMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative extrudeToRegionMeshDict
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

Create region mesh by extruding a faceZone or faceSet

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/extrude/extrudeToRegionMesh/extrudeToRegionMesh.C">源码与说明</a> · <a href="/assets/command-help/extrudetoregionmesh.txt">帮助文本</a></p>
