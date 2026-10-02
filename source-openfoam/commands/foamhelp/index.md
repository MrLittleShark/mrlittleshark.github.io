---
title: "foamHelp · 查询边界条件、函数对象和求解器的帮助"
layout: reference
description: "查询边界条件、函数对象和求解器的帮助。"
cms_slug: "command-foamhelp"
---

<p>查询边界条件、函数对象和求解器的帮助。</p><h2>开始前</h2>
<p>已加载 v2512；在含网格及所查字段的算例中运行。boundary、solver 等类别放在选项之前；在线文档查询需要可访问文档索引。</p>
<h2>示例 1：查询速度可用边界</h2>
<pre><code class="language-bash">foamHelp boundary -field U
</code></pre>
<p>读取速度场 U 的类型，列出可用于该矢量场的边界条件，供填写 0/U 时选择。</p>
<h2>示例 2：查询压力可用边界</h2>
<pre><code class="language-bash">foamHelp boundary -field p
</code></pre>
<p>已有 0/p 时查询标量边界；所得类型列表与 U 的矢量边界列表可对照阅读。</p>
<h2>示例 3：筛选固定值速度边界</h2>
<pre><code class="language-bash">foamHelp boundary -field U -fixedValue
</code></pre>
<p>在速度边界中筛选定值类实现，适合寻找给定入口速度及其派生条件。</p>
<h2>示例 4：查询网格约束类型</h2>
<pre><code class="language-bash">foamHelp boundary -constraint
</code></pre>
<p>显示约束类边界信息，用于区分 empty、symmetry 等几何约束与普通场边界。</p>
<h2>示例 5：按当前算例查询求解器</h2>
<pre><code class="language-bash">foamHelp solver -read
</code></pre>
<p>从 system/controlDict 读取 application，再查询对应求解器文档；先确认该条目已设置为所用求解器。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamHelp [OPTIONS] &lt;tool&gt;
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

Valid &lt;tool&gt; options include:
    boundary
    functionObject
    solver

NOTE the &lt;tool&gt; must actually appear *before* any options

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamHelp/foamHelp.C">源码与说明</a> · <a href="/assets/command-help/foamhelp.txt">帮助文本</a></p>
