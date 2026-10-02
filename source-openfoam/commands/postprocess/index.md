---
title: "postProcess · 在已有结果上执行功能对象"
layout: reference
description: "在已有结果上执行功能对象。"
cms_slug: "command-postprocess"
---

<p>在已有结果上执行功能对象。</p><h2>开始前</h2>
<p>已有所需字段和网格；-func使用预配置功能对象，-dict使用包含functions的控制字典。</p>
<h2>示例 1：计算速度大小</h2>
<pre><code class="language-bash">postProcess -func 'mag(U)' -latestTime
</code></pre>
<p>读取最新U，生成速度模场，适合查看流速分布或提取极值。</p>
<h2>示例 2：计算速度梯度</h2>
<pre><code class="language-bash">postProcess -func 'grad(U)' -time '0.1:0.5'
</code></pre>
<p>对区间内已有U逐时刻计算梯度张量，输出与各时刻对应的grad(U)。</p>
<h2>示例 3：同时计算涡量和Q</h2>
<pre><code class="language-bash">postProcess -funcs '(vorticity Q)' -latestTime
</code></pre>
<p>使用现有速度场生成涡量与Q判据，便于区分旋转强度与涡结构。</p>
<h2>示例 4：执行自定义采样方案</h2>
<pre><code class="language-bash">postProcess -dict system/postProcess-linesDict -time '1:2'
</code></pre>
<p>替代字典的functions已配置采样线或积分对象；对1至2秒已有结果执行，输出通常位于postProcessing。</p>
<h2>示例 5：后处理特定区域</h2>
<pre><code class="language-bash">postProcess -region fluid -func 'mag(U)' -latestTime
</code></pre>
<p>只读取fluid的U与网格，生成该区域速度大小，适合多区域案例。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-field &lt;name&gt;</code></td><td>Specify the name of the field to be processed, e.g. U</td></tr><tr><td><code>-fields &lt;list&gt;</code></td><td>按工具要求指定要处理的字段或仅处理字段。具体参数见完整帮助。</td></tr><tr><td><code>-func &lt;name&gt;</code></td><td>执行指定的预配置函数对象。</td></tr><tr><td><code>-funcs &lt;list&gt;</code></td><td>Specify the names of the functionObjects to execute, e.g. &#x27;(Q div(U))&#x27; Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-list</code></td><td>列出可用的预配置函数。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-profiling</code></td><td>Activate application-level profiling</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/functions-probes/">probes</a> · <a href="/dictionaries/functions-sets/">sets</a> · <a href="/dictionaries/functions-surfaces/">surfaces</a> · <a href="/dictionaries/functions-forces/">forces</a> · <a href="/dictionaries/functions-forcecoeffs/">forceCoeffs</a> · <a href="/dictionaries/functions-fieldaverage/">fieldAverage</a> · <a href="/dictionaries/functions-volfieldvalue/">volFieldValue</a> · <a href="/dictionaries/functions-surfacefieldvalue/">surfaceFieldValue</a> · <a href="/dictionaries/functions-yplus/">yPlus</a> · <a href="/dictionaries/functions-q/">Q</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: postProcess [OPTIONS]
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
