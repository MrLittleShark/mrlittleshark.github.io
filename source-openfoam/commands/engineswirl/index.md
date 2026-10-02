---
title: "engineSwirl · 根据发动机几何参数生成初始旋流速度场"
layout: reference
description: "根据发动机几何参数生成初始旋流速度场。"
cms_slug: "command-engineswirl"
---

<p>根据发动机几何参数生成初始旋流速度场。</p><h2>开始前</h2>
<p>已有U场和constant/engineGeometry，包含swirlAxis、swirlCenter、swirlRPMRatio、swirlProfile、bore及rpm。</p>
<h2>示例 1：生成基准旋流</h2>
<pre><code class="language-bash">engineSwirl
</code></pre>
<p>按缸径、转速和旋流剖面更新U，日志输出Umax，便于核对初始速度量级。</p>
<h2>示例 2：提高旋流比</h2>
<pre><code class="language-bash">foamDictionary constant/engineGeometry -entry swirlRPMRatio -set 1.5
engineSwirl
</code></pre>
<p>旋流比设为1.5，保持发动机转速和几何不变；生成的切向速度幅值随旋流比改变。</p>
<h2>示例 3：改变旋流中心</h2>
<pre><code class="language-bash">foamDictionary constant/engineGeometry -entry swirlCenter -set '(0.01 0 0)'
engineSwirl
</code></pre>
<p>将旋流轴中心平移到指定坐标，适合检查偏心初始旋流的空间分布。</p>
<h2>示例 4：改为绕y轴旋转</h2>
<pre><code class="language-bash">foamDictionary constant/engineGeometry -entry swirlAxis -set '(0 1 0)'
engineSwirl
</code></pre>
<p>swirlAxis给出旋转轴方向；程序构造垂直于该轴的横截面，并在其中生成切向速度。</p>
<h2>示例 5：导出初始旋流进行检查</h2>
<pre><code class="language-bash">engineSwirl
foamToVTK -time 0 -fields '(U)' -name VTK-swirl
</code></pre>
<p>初始时间为0时生成并导出U；用箭头或截面查看旋向、旋流中心和缸壁附近速度。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: engineSwirl [OPTIONS]
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

Generate a swirl flow for engine calculations

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/engineSwirl/engineSwirl.C">源码与说明</a> · <a href="/assets/command-help/engineswirl.txt">帮助文本</a></p>
