---
title: "postProcess · 对已有结果执行函数对象，生成派生场或统计数据"
layout: reference
description: "对已有结果执行函数对象，生成派生场或统计数据。"
cms_slug: "command-postprocess"
---

<p>对已有结果执行函数对象，生成派生场或统计数据。</p><h2>列出预配置函数</h2>
<pre><code class="language-bash">postProcess -list
</code></pre>
<p>输出可直接通过 <code>-func</code> 调用的预配置名称。函数对象类型还可写入 <code>controlDict/functions</code>。</p>
<h2>计算速度大小</h2>
<pre><code class="language-bash">postProcess -func "mag(U)" -latestTime
</code></pre>
<p>在最新时刻读取 <code>U</code> 并生成速度大小场。引号让带括号的函数表达式作为一个参数传入。</p>
<h2>调用求解器后处理</h2>
<pre><code class="language-bash">simpleFoam -postProcess -func yPlus -latestTime
</code></pre>
<p>需要湍流模型等求解器对象时，使用对应求解器的 <code>-postProcess</code> 入口。本例应在 <code>simpleFoam</code> 湍流算例中运行。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-constant</td><td>将 constant 目录加入选择。</td></tr><tr><td>-dict &lt;file&gt;</td><td>改用指定字典文件。</td></tr><tr><td>-field &lt;name&gt;</td><td>Specify the name of the field to be processed, e.g. U</td></tr><tr><td>-fields &lt;list&gt;</td><td>按工具要求指定要处理的字段或仅处理字段。具体参数见完整帮助。</td></tr><tr><td>-func &lt;name&gt;</td><td>执行指定的预配置函数对象。</td></tr><tr><td>-funcs &lt;list&gt;</td><td>Specify the names of the functionObjects to execute, e.g. &#x27;(Q div(U))&#x27; Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-list</td><td>列出可用的预配置函数。</td></tr><tr><td>-noZero</td><td>跳过 0 时刻。</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-profiling</td><td>Activate application-level profiling</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-time &lt;ranges&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/functions-probes/">probes</a> · <a href="/dictionaries/functions-sets/">sets</a> · <a href="/dictionaries/functions-surfaces/">surfaces</a> · <a href="/dictionaries/functions-forces/">forces</a> · <a href="/dictionaries/functions-forcecoeffs/">forceCoeffs</a> · <a href="/dictionaries/functions-fieldaverage/">fieldAverage</a> · <a href="/dictionaries/functions-volfieldvalue/">volFieldValue</a> · <a href="/dictionaries/functions-surfacefieldvalue/">surfaceFieldValue</a> · <a href="/dictionaries/functions-yplus/">yPlus</a> · <a href="/dictionaries/functions-q/">Q</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: postProcess [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Read control dictionary from specified location
  -field &lt;name&gt;     Specify the name of the field to be processed, e.g. U
  -fields &lt;list&gt;    Specify a list of fields to be processed, e.g. &#x27;(U T p)&#x27;
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -func &lt;name&gt;      Specify the name of the functionObject to execute, e.g. Q
  -funcs &lt;list&gt;     Specify the names of the functionObjects to execute, e.g.
                    &#x27;(Q div(U))&#x27;
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -list             List the available configured functionObjects
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -profiling        Activate application-level profiling
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Execute the set of functionObjects specified in the selected dictionary or on
the command-line for the selected set of times on the selected set of fields

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/postProcess/postProcess.C">源码与说明</a> · <a href="/assets/command-help/postprocess.txt">帮助文本</a></p>
