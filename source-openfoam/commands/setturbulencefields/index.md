---
title: "setTurbulenceFields · 按经验关系和壁距初始化选定的湍流字段"
layout: reference
description: "按经验关系和壁距初始化选定的湍流字段。"
cms_slug: "command-setturbulencefields"
---

<p>按经验关系和壁距初始化选定的湍流字段。</p><h2>开始前</h2>
<p>已有速度、湍流模型及system/setTurbulenceFieldsDict；initialiseK、initialiseOmega等开关决定写哪些字段。</p>
<h2>示例 1：应用默认初始化方案</h2>
<pre><code class="language-bash">setTurbulenceFields
</code></pre>
<p>读取字典并初始化其中启用的U、k、epsilon、omega或R，输出相应字段统计。</p>
<h2>示例 2：为k–omega方案初始化</h2>
<pre><code class="language-bash">foamDictionary system/setTurbulenceFieldsDict -entry initialiseK -set true
foamDictionary system/setTurbulenceFieldsDict -entry initialiseOmega -set true
setTurbulenceFields
</code></pre>
<p>其余必要经验参数和模型已配置；启用k和omega初场写入，适合给k–omega模型准备一致的起始量。</p>
<h2>示例 3：为k–epsilon方案初始化</h2>
<pre><code class="language-bash">setTurbulenceFields -dict system/setTurbulenceFields-kepsilonDict
</code></pre>
<p>替代字典启用initialiseK与initialiseEpsilon，并提供相应经验参数；生成配套的k与epsilon。</p>
<h2>示例 4：写出辅助分布f</h2>
<pre><code class="language-bash">foamDictionary system/setTurbulenceFieldsDict -entry writeF -set true
setTurbulenceFields
</code></pre>
<p>启用writeF后额外保存辅助场f，便于检查经验初始化随空间位置的变化。</p>
<h2>示例 5：处理指定流体区域</h2>
<pre><code class="language-bash">setTurbulenceFields -region fluid -dict system/setTurbulenceFields-fluidDict
</code></pre>
<p>在多区域fluid内使用专用参数初始化；检查输出字段与该区域选择的湍流模型匹配。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: setTurbulenceFields [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative setTurbulenceFieldsDict
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
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
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

Sets initial turbulence fields based on various empirical equations

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setTurbulenceFields/setTurbulenceFields.C">源码与说明</a> · <a href="/assets/command-help/setturbulencefields.txt">帮助文本</a></p>
