---
title: "applyBoundaryLayer · 按七分之一次幂规律修正近壁速度及相应湍流场"
layout: reference
description: "按七分之一次幂规律修正近壁速度及相应湍流场。"
cms_slug: "command-applyboundarylayer"
---

<p>按七分之一次幂规律修正近壁速度及相应湍流场。</p><h2>开始前</h2>
<p>已有速度场、壁面和所需湍流模型输入；边界层厚度可用绝对长度 ybl 或相对系数 Cbl 指定。</p>
<h2>示例 1：设置明确的边界层厚度</h2>
<pre><code class="language-bash">applyBoundaryLayer -ybl 0.01
</code></pre>
<p>以0.01米厚度修正近壁速度，适合给外流案例构造初始速度剖面。</p>
<h2>示例 2：按网格平均壁距设置厚度</h2>
<pre><code class="language-bash">applyBoundaryLayer -Cbl 2
</code></pre>
<p>厚度取平均壁距的2倍，适合根据当前网格近壁尺度生成初始分布。</p>
<h2>示例 3：同时写湍流场</h2>
<pre><code class="language-bash">applyBoundaryLayer -ybl 0.01 -writeTurbulenceFields
</code></pre>
<p>更新速度并写相应湍流量，使初始湍流场与所构造近壁剖面配套。</p>
<h2>示例 4：比较更厚的入口发展层</h2>
<pre><code class="language-bash">applyBoundaryLayer -case ./thickLayer -ybl 0.02 -writeTurbulenceFields
</code></pre>
<p>thickLayer 是独立初始案例；厚度改为0.02米，可比较速度亏损范围与湍流场变化。</p>
<h2>示例 5：只处理流体区域</h2>
<pre><code class="language-bash">applyBoundaryLayer -region fluid -ybl 0.005 -writeTurbulenceFields
</code></pre>
<p>多区域中只修改fluid的近壁场，适合流固传热案例的流体初始状态准备。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-Cbl &lt;scalar&gt;</code></td><td>Boundary-layer thickness as Cbl * mean distance to wall</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-ybl &lt;scalar&gt;</code></td><td>Specify the boundary-layer thickness</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: applyBoundaryLayer [OPTIONS]
Options:
  -Cbl &lt;scalar&gt;     Boundary-layer thickness as Cbl * mean distance to wall
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
  -writeTurbulenceFields
                    Write the turbulence fields
  -ybl &lt;scalar&gt;     Specify the boundary-layer thickness
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Apply a simplified boundary-layer model to the velocity and turbulence fields
based on the 1/7th power-law.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/applyBoundaryLayer/applyBoundaryLayer.C">源码与说明</a> · <a href="/assets/command-help/applyboundarylayer.txt">帮助文本</a></p>
