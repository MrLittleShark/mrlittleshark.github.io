---
title: "foamDictionary · 读取、修改和展开 OpenFOAM 字典"
layout: reference
description: "读取、修改和展开 OpenFOAM 字典。"
cms_slug: "command-foamdictionary"
---

<p>读取、修改和展开 OpenFOAM 字典。</p><h2>读取一个数值</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry endTime -value
</code></pre>
<p>输出 <code>endTime</code> 的值，适合检查设置，也便于在脚本中取值。此命令读取文件。</p>
<h2>修改结束时间</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry endTime -set 2
</code></pre>
<p>将 <code>endTime</code> 改成 <code>2</code> 并写回文件。单位由求解器的时间定义决定；瞬态计算通常是秒，稳态计算常用迭代计数。</p>
<h2>读取嵌套条目</h2>
<pre><code class="language-bash">foamDictionary system/fvSolution -entry solvers/p/tolerance -value
</code></pre>
<p><code>/</code> 分隔子字典层级。本例要求存在 <code>solvers</code> 下的 <code>p</code>，可先用下一组命令查看实际名称。</p>
<h2>列出键和展开引用</h2>
<pre><code class="language-bash">foamDictionary system/fvSolution -entry solvers -keywords
foamDictionary system/fvSolution -expand &gt; fvSolution.expanded
</code></pre>
<p>第一行列出线性求解器的字段条目。第二行将展开内容保存到新文件，适合检查宏与 include；含 <code>#codeStream</code> 等条目时，展开过程会执行相应代码。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-add &lt;value&gt;</td><td>Add a new entry</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-diff &lt;dict&gt;</td><td>Write differences with respect to the specified dictionary</td></tr><tr><td>-diff-etc &lt;dict&gt;</td><td>As per -diff, but locate the file as per foamEtcFile Disable expansion of dictionary directives - #include, #codeStream etc</td></tr><tr><td>-entry &lt;name&gt;</td><td>定位字典中的键或子字典路径。</td></tr><tr><td>-expand</td><td>展开字典引用和函数条目；#codeStream 等条目可能执行代码。</td></tr><tr><td>-includes</td><td>List the #include/#sinclude files to standard output Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-keywords</td><td>列出当前字典层级的键名。</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-precision &lt;int&gt;</td><td>Set default write precision for IOstreams</td></tr><tr><td>-remove</td><td>Remove the entry Subprocess root directories for distributed running</td></tr><tr><td>-set &lt;value&gt;</td><td>设置条目值，会修改文件。</td></tr><tr><td>-value</td><td>仅输出所选条目的值。</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamDictionary [OPTIONS] &lt;dict&gt;
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
