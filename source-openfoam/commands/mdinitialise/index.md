---
title: "mdInitialise · 按晶格、密度、温度和整体速度生成分子动力学初态"
layout: reference
description: "按晶格、密度、温度和整体速度生成分子动力学初态。"
cms_slug: "command-mdinitialise"
---

<p>按晶格、密度、温度和整体速度生成分子动力学初态。</p><h2>开始前</h2>
<p>已有MD网格、system/mdInitialiseDict、分子类型和势函数；初始化区域与字典中的分子分组一致。</p>
<h2>示例 1：生成基准分子云</h2>
<pre><code class="language-bash">mdInitialise
</code></pre>
<p>读取各分组的晶格与热运动参数，生成分子并写出初态，日志汇总分子数量。</p>
<h2>示例 2：提高初始温度</h2>
<pre><code class="language-bash">foamDictionary system/mdInitialiseDict -entry liquid/temperature -set 350
mdInitialise
</code></pre>
<p>字典已有liquid分组时，将热运动初始化温度设为350K，观察后续平衡过程。</p>
<h2>示例 3：给分子云加入整体平移</h2>
<pre><code class="language-bash">foamDictionary system/mdInitialiseDict -entry liquid/bulkVelocity -set '(100 0 0)'
mdInitialise
</code></pre>
<p>整体速度沿x方向为100米每秒，叠加在热运动上，可用于平移流或动量检查。</p>
<h2>示例 4：旋转初始晶格</h2>
<pre><code class="language-bash">foamDictionary system/mdInitialiseDict -entry liquid/orientationAngles -set '(0 0 45)'
mdInitialise
</code></pre>
<p>欧拉角按字典约定以度填写；改变晶格取向，适合研究结构相对边界的排列。</p>
<h2>示例 5：初始化后进行热平衡</h2>
<pre><code class="language-bash">mdInitialise
mdEquilibrationFoam
</code></pre>
<p>案例已配置mdEquilibrationFoam及温控参数；先建分子初态，再让系统按势函数松弛到目标状态。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: mdInitialise [OPTIONS]
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

Initialises fields for a molecular dynamics (MD) simulation

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/mdInitialise/mdInitialise.C">源码与说明</a> · <a href="/assets/command-help/mdinitialise.txt">帮助文本</a></p>
