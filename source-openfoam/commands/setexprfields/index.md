---
title: "setExprFields · 示例修改已有 T 场；采用 -create 新建场时需设置 dimensions"
layout: reference
description: "示例修改已有 T 场；采用 -create 新建场时需设置 dimensions。"
cms_slug: "command-setexprfields"
---

<p>示例修改已有 T 场；采用 -create 新建场时需设置 dimensions。</p><h2>用法</h2><pre><code class="language-bash">setExprFields -field T -expression &#x27;300 + 10*pos().x()&#x27;</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">setExprFields -field T -expression &#x27;300 + 10*pos().x()&#x27; -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-ascii</td><td>Write in ASCII format instead of the controlDict setting</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-create</td><td>Create a new field (command-line operation)</td></tr><tr><td>-debug-parser</td><td>Additional debugging information Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file</td></tr><tr><td>-dict &lt;file&gt;</td><td>改用指定字典文件。</td></tr><tr><td>-dry-run</td><td>Evaluate but do not write</td></tr><tr><td>-dummy-phi</td><td>Provide a zero phi field (command-line operation) The expression to evaluate (command-line operation)</td></tr><tr><td>-field &lt;name&gt;</td><td>The field to create/overwrite (command-line operation) The field mask (logical condition) when to apply the expression (command-line operation) Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-keepPatches</td><td>Leave patches unaltered (command-line operation)</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-noZero</td><td>跳过 0 时刻。</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-time &lt;ranges&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-setexprfieldsdict/">setExprFieldsDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: setExprFields [OPTIONS]
Options:
  -ascii            Write in ASCII format instead of the controlDict setting
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -create           Create a new field (command-line operation)
  -debug-parser     Additional debugging information
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative dictionary for setExprFieldsDict
  -dimensions &lt;dims&gt;
                    The dimensions for created fields (command-line operation)
  -dry-run          Evaluate but do not write
  -dummy-phi        Provide a zero phi field (command-line operation)
  -expression &lt;expr&gt;
                    The expression to evaluate (command-line operation)
  -field &lt;name&gt;     The field to create/overwrite (command-line operation)
  -field-mask &lt;logic&gt;
                    The field mask (logical condition) when to apply the
                    expression (command-line operation)
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -keepPatches      Leave patches unaltered (command-line operation)
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -load-fields &lt;wordList&gt;
                    Specify field or fields to preload. Eg, &#x27;T&#x27; or &#x27;(p T U)&#x27;
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-variable-cache
                    Disable caching of expression variables
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -value-patches &lt;(patches)&gt;
                    A list of patches that receive a fixed value (command-line
                    operation)
  -verbose          Additional verbosity
  -withFunctionObjects
                    Execute functionObjects
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprFields/setExprFields.C">源码与说明</a> · <a href="/assets/command-help/setexprfields.txt">帮助文本</a></p>
