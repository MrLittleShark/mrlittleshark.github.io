---
title: "orientFaceZone · 根据外部参考点统一 faceZone 的定向标记"
layout: reference
description: "根据外部参考点统一 faceZone 的定向标记。"
cms_slug: "command-orientfacezone"
---

<p>根据外部参考点统一 faceZone 的定向标记。</p><h2>开始前</h2>
<p>已存在目标 faceZone；第二位置参数必须是网格外部参考点，用来确定面的外侧。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：统一闭合区域朝向</h2>
<pre><code class="language-bash">orientFaceZone shellFaces '(10 0 0)'
</code></pre>
<p>shellFaces 已包围目标区域，参考点(10,0,0)确在网格外；程序更新该zone的 flipMap 并报告翻转数量。</p>
<h2>示例 2：对另一侧外部点定向</h2>
<pre><code class="language-bash">orientFaceZone inletSection '(-10 0 0)'
</code></pre>
<p>入口截面附近的外部参考点位于负x方向，使定向与所选外侧对应；用于统一截面积分的符号约定。</p>
<h2>示例 3：处理多区域中的界面</h2>
<pre><code class="language-bash">orientFaceZone -region fluid interfaceFaces '(10 10 10)'
</code></pre>
<p>仅修改 fluid 的 interfaceFaces；参考点应位于该区域外，结果写入 fluid 的 faceZones。</p>
<h2>示例 4：生成 zone 后定向</h2>
<pre><code class="language-bash">topoSet -dict system/topoSet-interfaceDict
orientFaceZone interfaceFaces '(0 0 10)'
</code></pre>
<p>topoSet 字典先创建 interfaceFaces faceZone，再用外部参考点统一朝向，适合作为界面通量统计的前处理。</p>
<h2>示例 5：分区网格中同步定向</h2>
<pre><code class="language-bash">mpirun -np 4 orientFaceZone -parallel shellFaces '(10 0 0)'
</code></pre>
<p>已有4分区且耦合面两侧都进入zone；并行交换定向信息，使跨处理器的 flipMap 一致。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: orientFaceZone [OPTIONS] &lt;faceZone&gt; &lt;point&gt;
Arguments:
  &lt;faceZone&gt;
  &lt;point&gt;           A point outside of the mesh
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

Corrects the orientation of faceZone

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/orientFaceZone/orientFaceZone.C">源码与说明</a> · <a href="/assets/command-help/orientfacezone.txt">帮助文本</a></p>
