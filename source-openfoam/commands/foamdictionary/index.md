---
title: "foamDictionary · 读取、修改和展开 OpenFOAM 字典"
layout: reference
description: "读取、修改和展开 OpenFOAM 字典。"
cms_slug: "command-foamdictionary"
---

<p>读取、修改和展开 OpenFOAM 字典。</p><h2>开始前</h2>
<p>输入为 OpenFOAM 字典；修改示例在算例副本中执行。点号可定位嵌套条目。</p>
<h2>示例 1：读取停止时刻</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry endTime -value
</code></pre>
<p>只输出 endTime 的值，便于确认当前计算何时停止。</p>
<h2>示例 2：列出求解器设置</h2>
<pre><code class="language-bash">foamDictionary system/fvSolution -entry solvers -keywords
</code></pre>
<p>列出 solvers 子字典内的键，如 p、pFinal、U；由此确认哪些字段有线性求解设置。</p>
<h2>示例 3：修改时间步</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry deltaT -set 0.001
</code></pre>
<p>把 deltaT 改为0.001并保存原文件。瞬态计算中该值通常表示秒；实际步长还受自适应设置影响。</p>
<h2>示例 4：修改嵌套入口值</h2>
<pre><code class="language-bash">foamDictionary 0/U -entry boundaryField.inlet.value -set 'uniform (0.2 0 0)'
</code></pre>
<p>已有 inlet/value 时将其改为沿x方向0.2m/s；入口类型须使用 value 条目。</p>
<h2>示例 5：展开包含文件并比较修改</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -expand &gt; controlDict.expanded
foamDictionary system/controlDict -diff system/controlDict.original
</code></pre>
<p>先生成展开宏和包含后的文本，再与事先保存的原字典比较。展开文件另存，不覆盖工作字典。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-add &lt;value&gt;</code></td><td>Add a new entry</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-diff &lt;dict&gt;</code></td><td>Write differences with respect to the specified dictionary</td></tr><tr><td><code>-diff-etc &lt;dict&gt;</code></td><td>As per -diff, but locate the file as per foamEtcFile Disable expansion of dictionary directives - #include, #codeStream etc</td></tr><tr><td><code>-entry &lt;name&gt;</code></td><td>定位字典中的键或子字典路径。</td></tr><tr><td><code>-expand</code></td><td>展开字典引用和函数条目；#codeStream 等条目可能执行代码。</td></tr><tr><td><code>-includes</code></td><td>List the #include/#sinclude files to standard output Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-keywords</code></td><td>列出当前字典层级的键名。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-precision &lt;int&gt;</code></td><td>Set default write precision for IOstreams</td></tr><tr><td><code>-remove</code></td><td>Remove the entry Subprocess root directories for distributed running</td></tr><tr><td><code>-set &lt;value&gt;</code></td><td>设置条目值，会修改文件。</td></tr><tr><td><code>-value</code></td><td>仅输出所选条目的值。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamDictionary [OPTIONS] &lt;dict&gt;
Arguments:
  &lt;dict&gt;            The dictionary file to process
Options:
  -add &lt;value&gt;      Add a new entry
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -diff &lt;dict&gt;      Write differences with respect to the specified dictionary
  -diff-etc &lt;dict&gt;  As per -diff, but locate the file as per foamEtcFile
  -disableFunctionEntries
                    Disable expansion of dictionary directives - #include,
                    #codeStream etc
  -entry &lt;name&gt;     Report/select the named entry
  -expand           Read the specified dictionary file, expand the macros etc.
                    and write the resulting dictionary to standard output
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -includes         List the #include/#sinclude files to standard output
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -keywords         List keywords
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
  -precision &lt;int&gt;  Set default write precision for IOstreams
  -remove           Remove the entry
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -set &lt;value&gt;      Set entry value or add new entry
  -value            Print entry value
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Interrogate and manipulate dictionaries

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamDictionary/foamDictionary.C">源码与说明</a> · <a href="/assets/command-help/foamdictionary.txt">帮助文本</a></p>
