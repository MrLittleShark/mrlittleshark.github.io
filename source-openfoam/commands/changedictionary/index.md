---
title: "changeDictionary · 按替换字典批量修改场文件或网格字典条目"
layout: reference
description: "按替换字典批量修改场文件或网格字典条目。"
cms_slug: "command-changedictionary"
---

<p>按替换字典批量修改场文件或网格字典条目。</p><h2>开始前</h2>
<p>已有 system/changeDictionaryDict，替换内容与目标文件结构一致；操作将重写匹配文件。</p>
<h2>示例 1：更新初始场边界</h2>
<pre><code class="language-bash">changeDictionary -time 0
</code></pre>
<p>读取默认替换规则，修改0目录中的目标场；适合一组场的入口、出口条件同步调整。</p>
<h2>示例 2：选用温度方案</h2>
<pre><code class="language-bash">changeDictionary -dict system/changeDictionary-hotWallDict -time 0
</code></pre>
<p>使用热壁专用替换文件，把相关温度边界和配套条目一次更新到初始场。</p>
<h2>示例 3：修改constant实例</h2>
<pre><code class="language-bash">changeDictionary -instance constant
</code></pre>
<p>-instance把目标实例设为constant；替换字典已指定该位置的文件时，可用于边界或物性相关字典修改。</p>
<h2>示例 4：处理最新结果的重启边界</h2>
<pre><code class="language-bash">changeDictionary -latestTime -dict system/changeDictionary-restartDict
</code></pre>
<p>只修改最后保存时刻的字段，给重启计算准备新边界条件，同时保留更早时间。</p>
<h2>示例 5：选择一个替换子字典</h2>
<pre><code class="language-bash">changeDictionary -subDict restartReplacements -dict system/changeDictionary-allDict -time 2
</code></pre>
<p>替代字典中已有restartReplacements子字典时，仅应用该组规则到时间2，便于集中维护多个修改方案。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-instance &lt;name&gt;</code></td><td>Override instance setting (default is the time name)</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-literalRE</code></td><td>Treat regular expressions literally (i.e., as a keyword)</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-subDict &lt;name&gt;</code></td><td>Specify the subDict name of the replacements dictionary</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-changedictionarydict/">changeDictionaryDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: changeDictionary [OPTIONS]
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
