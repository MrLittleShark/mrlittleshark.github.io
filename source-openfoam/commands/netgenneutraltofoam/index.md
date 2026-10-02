---
title: "netgenNeutralToFoam · 转换后检查边界划分"
layout: reference
description: "转换后检查边界划分。"
cms_slug: "command-netgenneutraltofoam"
---

<p>转换后检查边界划分。</p><h2>开始前</h2>
<p>准备 NETGEN Neutral 格式文件；边界标签随输入读取，转换后需根据几何位置核对各 patch。</p>
<h2>示例 1：导入四面体网格</h2>
<pre><code class="language-bash">netgenNeutralToFoam mesh.neu
</code></pre>
<p>读取顶点、四面体以及表面三角形，生成 OpenFOAM 网格。日志给出各边界分区的面数。</p>
<h2>示例 2：检查边界面连接</h2>
<pre><code class="language-bash">netgenNeutralToFoam mesh.neu
checkMesh -constant -allTopology
</code></pre>
<p>检查边界三角形是否与体单元正确相连。若转换器提示某些边界面没有相邻单元，应回到输入网格核对表面数据。</p>
<h2>示例 3：换算毫米坐标</h2>
<pre><code class="language-bash">netgenNeutralToFoam mesh-mm.neu
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>将转换后的全网格统一缩放为米，再通过 bounding box 核对模型尺寸。</p>
<h2>示例 4：整理编号式边界名称</h2>
<pre><code class="language-bash">netgenNeutralToFoam mesh.neu
createPatch -overwrite
</code></pre>
<p>前提是根据转换输出的 patch 编号配置 createPatchDict。把实际入口、出口和壁面改为有物理意义的名称，方便配置场文件。</p>
<h2>示例 5：在指定案例导出外表面</h2>
<pre><code class="language-bash">netgenNeutralToFoam /data/mesh.neu -case ../netgenCase
foamToSurface netgen-boundary.obj -case ../netgenCase -constant
</code></pre>
<p>将网格转换到 netgenCase，并导出边界用于与 NETGEN 原模型对比。检查孔洞、几何尺度及各边界的位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: netgenNeutralToFoam [OPTIONS] &lt;Neutral file&gt;
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

Convert a neutral file format (Netgen v4.4) to OpenFOAM

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/netgenNeutralToFoam/netgenNeutralToFoam.C">源码与说明</a> · <a href="/assets/command-help/netgenneutraltofoam.txt">帮助文本</a></p>
