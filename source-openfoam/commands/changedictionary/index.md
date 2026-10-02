---
title: "changeDictionary · 读取 changeDictionaryDict，并将替换结果写回文件"
layout: reference
description: "读取 changeDictionaryDict，并将替换结果写回文件。"
cms_slug: "command-changedictionary"
---

<p>读取 changeDictionaryDict，并将替换结果写回文件。</p><h2>用法</h2><pre><code class="language-bash">changeDictionary</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">changeDictionary -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-constant</td><td>将 constant 目录加入选择。</td></tr><tr><td>-dict &lt;file&gt;</td><td>改用指定字典文件。</td></tr><tr><td>-instance &lt;name&gt;</td><td>Override instance setting (default is the time name)</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-literalRE</td><td>Treat regular expressions literally (i.e., as a keyword)</td></tr><tr><td>-noZero</td><td>跳过 0 时刻。</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-subDict &lt;name&gt;</td><td>Specify the subDict name of the replacements dictionary</td></tr><tr><td>-time &lt;ranges&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-changedictionarydict/">changeDictionaryDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: changeDictionary [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative changeDictionaryDict
  -disablePatchGroups
                    Disable matching keys to patch groups
  -enableFunctionEntries
                    Enable expansion of dictionary directives - #include,
                    #codeStream etc
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -instance &lt;name&gt;  Override instance setting (default is the time name)
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -literalRE        Treat regular expressions literally (i.e., as a keyword)
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
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -subDict &lt;name&gt;   Specify the subDict name of the replacements dictionary
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Utility to change dictionary entries (such as the patch type for fields and
polyMesh/boundary files).

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/changeDictionary/changeDictionary.C">源码与说明</a> · <a href="/assets/command-help/changedictionary.txt">帮助文本</a></p>
