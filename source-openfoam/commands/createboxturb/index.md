---
title: "createBoxTurb · 按给定能谱和模态叠加生成各向同性湍流盒"
layout: reference
description: "按给定能谱和模态叠加生成各向同性湍流盒。"
cms_slug: "command-createboxturb"
---

<p>按给定能谱和模态叠加生成各向同性湍流盒。</p><h2>开始前</h2>
<p>constant/createBoxTurbDict 包含 L、N、nModes 和 Ek；L 是盒长，N 是网格数，Ek 为波数能谱函数。</p>
<h2>示例 1：仅创建周期盒网格</h2>
<pre><code class="language-bash">createBoxTurb -createBlockMesh
</code></pre>
<p>按L、N生成带周期边界的盒网格后退出，先检查尺寸和分辨率。</p>
<h2>示例 2：生成湍流速度</h2>
<pre><code class="language-bash">createBoxTurb
</code></pre>
<p>在已有对应盒网格上叠加nModes个模态，写出U、k与div(U)，日志报告波数范围和场统计。</p>
<h2>示例 3：连贯创建并检查</h2>
<pre><code class="language-bash">createBoxTurb -createBlockMesh
checkMesh
createBoxTurb
</code></pre>
<p>先生成网格、检查周期连接，再生成速度；把几何错误与谱参数问题分开定位。</p>
<h2>示例 4：增加模态数量</h2>
<pre><code class="language-bash">foamDictionary constant/createBoxTurbDict -entry nModes -set 500
createBoxTurb
</code></pre>
<p>已有有效L、N、Ek时把模态数设为500，比较能谱近似与生成成本；模态数至少应大于1。</p>
<h2>示例 5：加密周期盒</h2>
<pre><code class="language-bash">foamDictionary constant/createBoxTurbDict -entry N -set '(64 64 64)'
createBoxTurb -createBlockMesh
createBoxTurb
</code></pre>
<p>在独立副本上改为64立方网格，重新生成网格和场；更小单元允许更高的离散最大波数。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-createBlockMesh</code></td><td>create the block mesh and exit Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: createBoxTurb [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -createBlockMesh  create the block mesh and exit
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

Create a box of isotropic turbulence based on a user-specified energy spectrum.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/createBoxTurb/createBoxTurb.C">源码与说明</a> · <a href="/assets/command-help/createboxturb.txt">帮助文本</a></p>
