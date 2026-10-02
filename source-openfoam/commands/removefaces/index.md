---
title: "removeFaces · 输入为预先建立的 faceSet"
layout: reference
description: "输入为预先建立的 faceSet。"
cms_slug: "command-removefaces"
---

<p>输入为预先建立的 faceSet。</p><h2>开始前</h2>
<p>已有 faceSet，内含拟移除的内部面；移除这些面会合并相邻单元。使用案例副本并检查合并后单元形状。</p>
<h2>示例 1：合并指定内部面两侧的单元</h2>
<pre><code class="language-bash">removeFaces internalFaces
</code></pre>
<p>读取 internalFaces，执行内部面移除与单元合并，结果写入新的网格实例。检查单元数是否按预期减少。</p>
<h2>示例 2：从几何选区建立移除面集</h2>
<pre><code class="language-bash">topoSet -dict system/topoSet-removeFacesDict
removeFaces mergeFaces
</code></pre>
<p>前提是该 topoSet 字典生成只含目标内部面的 mergeFaces。先在可视化中检查选区，再合并这些面的相邻单元。</p>
<h2>示例 3：把修改限制在独立案例</h2>
<pre><code class="language-bash">removeFaces internalFaces -case ../mergeTest
checkMesh -case ../mergeTest -latestTime -allGeometry
</code></pre>
<p>使用 mergeTest 的面集和网格，检查生成的多面体体积、凹性及面质量。</p>
<h2>示例 4：将确认的修改写回原实例</h2>
<pre><code class="language-bash">removeFaces internalFaces -overwrite
checkMesh -constant -allTopology
</code></pre>
<p>适合已经在副本验证过的面集。更新原网格位置后，检查内部面与边界连接并核对已有场数据。</p>
<h2>示例 5：并行合并单元</h2>
<pre><code class="language-bash">mpirun -np 4 removeFaces internalFaces -parallel -overwrite
mpirun -np 4 checkMesh -parallel
</code></pre>
<p>网格和面集需已一致分解到四个子域。并行运行后检查处理器界面，确认跨分区连接保持一致。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: removeFaces [OPTIONS] &lt;faceSet&gt;
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

Remove faces specified in faceSet by combining cells on both sides

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/removeFaces/removeFaces.C">源码与说明</a> · <a href="/assets/command-help/removefaces.txt">帮助文本</a></p>
