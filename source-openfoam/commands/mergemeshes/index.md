---
title: "mergeMeshes · 把两个独立网格合并到主案例中"
layout: reference
description: "把两个独立网格合并到主案例中。"
cms_slug: "command-mergemeshes"
---

<p>把两个独立网格合并到主案例中。</p><h2>开始前</h2>
<p>masterCase 与 addCase 都有有效网格；两套坐标已对齐。合并后若要把接触边界变成内部面，还需拼接步骤。</p>
<h2>示例 1：合并两个网格</h2>
<pre><code class="language-bash">mergeMeshes baseCase extensionCase
</code></pre>
<p>baseCase 是接收结果的主案例，extensionCase 提供追加网格；输出位于主案例的新网格时间。</p>
<h2>示例 2：指定结果时间</h2>
<pre><code class="language-bash">mergeMeshes baseCase extensionCase -resultTime 2
</code></pre>
<p>把合并网格写到 baseCase 的时间 2，便于保留并选择不同预处理阶段。</p>
<h2>示例 3：合并指定区域</h2>
<pre><code class="language-bash">mergeMeshes baseCase extensionCase -masterRegion fluid -addRegion fluid
</code></pre>
<p>两个案例均含 fluid 区域时，只读取并合并这两个区域网格，结果仍归主案例的 fluid 区域。</p>
<h2>示例 4：直接更新主网格并检查</h2>
<pre><code class="language-bash">mergeMeshes baseCase extensionCase -overwrite
checkMesh -case baseCase
</code></pre>
<p>-overwrite 更新主案例当前网格；随后检查合并后的单元数、连通区域和边界。</p>
<h2>示例 5：合并后缝合吻合界面</h2>
<pre><code class="language-bash">mergeMeshes baseCase extensionCase -overwrite
stitchMesh -case baseCase -perfect interfaceA interfaceB -overwrite
checkMesh -case baseCase
</code></pre>
<p>两个网格有完全吻合的 interfaceA/interfaceB 时，合并后将这对边界缝合成内部面，形成连通计算域。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: mergeMeshes [OPTIONS] &lt;masterCase&gt; &lt;addCase&gt;
Options:
  -addRegion &lt;name&gt;
                    Specify alternative mesh region for the additional mesh
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
  -masterRegion &lt;name&gt;
                    Specify alternative mesh region for the master mesh
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
  -resultTime &lt;time&gt;
                    Specify a time for the resulting mesh
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Merge two meshes

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/mergeMeshes/mergePolyMesh.C">源码与说明</a> · <a href="/assets/command-help/mergemeshes.txt">帮助文本</a></p>
