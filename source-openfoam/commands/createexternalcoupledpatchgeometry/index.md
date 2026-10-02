---
title: "createExternalCoupledPatchGeometry · 导出外部耦合patch组的几何信息"
layout: reference
description: "导出外部耦合patch组的几何信息。"
cms_slug: "command-createexternalcoupledpatchgeometry"
---

<p>导出外部耦合patch组的几何信息。</p><h2>开始前</h2>
<p>网格已有用于外部耦合的patch组；位置参数是组名，输出供外部程序按面顺序交换数据。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：导出耦合壁面组</h2>
<pre><code class="language-bash">createExternalCoupledPatchGeometry coupledWalls
</code></pre>
<p>coupledWalls 是已存在的patch组；生成该组的几何数据，供外部传热或结构程序读取。</p>
<h2>示例 2：指定通信目录</h2>
<pre><code class="language-bash">createExternalCoupledPatchGeometry coupledWalls -commsDir exchange
</code></pre>
<p>把通信几何输出到exchange，而非默认comms，便于与外部程序统一路径。</p>
<h2>示例 3：导出流体区域接口</h2>
<pre><code class="language-bash">createExternalCoupledPatchGeometry coupledWalls -region fluid
</code></pre>
<p>从fluid区域读取同名patch组，输出该区域的接口几何。</p>
<h2>示例 4：同时导出多个区域</h2>
<pre><code class="language-bash">createExternalCoupledPatchGeometry coupledWalls -regions '(fluid solid)' -commsDir exchange
</code></pre>
<p>两个区域均配置目标组时，批量输出接口几何，区域信息用于区分对应面。</p>
<h2>示例 5：网格分区后导出接口</h2>
<pre><code class="language-bash">mpirun -np 4 createExternalCoupledPatchGeometry coupledWalls -parallel -commsDir exchange
</code></pre>
<p>已有4分区网格和一致组名；按并行案例的接口布局生成几何，供外部耦合按相同面组织交换数据。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-commsDir &lt;dir&gt;</code></td><td>Specify communications directory (default is &#x27;comms&#x27;) Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: createExternalCoupledPatchGeometry [OPTIONS] &lt;patchGroup&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -commsDir &lt;dir&gt;   Specify communications directory (default is &#x27;comms&#x27;)
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
  -region &lt;name&gt;    Specify alternative mesh region
  -regions &lt;(name1 .. nameN)&gt;
                    Specify alternative mesh regions
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Generate the patch geometry (points and faces) for use with the externalCoupled
functionObject.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/createExternalCoupledPatchGeometry/createExternalCoupledPatchGeometry.C">源码与说明</a> · <a href="/assets/command-help/createexternalcoupledpatchgeometry.txt">帮助文本</a></p>
