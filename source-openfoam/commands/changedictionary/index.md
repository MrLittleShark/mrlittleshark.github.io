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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 changeDictionaryDict 文件。</td></tr><tr><td><code>-disablePatchGroups</code></td><td>仅匹配边界名称，跳过边界组匹配。</td></tr><tr><td><code>-enableFunctionEntries</code></td><td>展开 #include、#codeStream 等字典指令。</td></tr><tr><td><code>-instance &lt;name&gt;</code></td><td>指定对象所在的目录，默认使用当前时间名称。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-literalRE</code></td><td>将正则表达式按普通键名原样匹配。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-subDict &lt;name&gt;</code></td><td>指定替换规则所在的子字典。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-changedictionarydict/">changeDictionaryDict</a></p><details class="command-more-options"><summary>更多参数（19 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/changeDictionary/changeDictionary.C">源码与说明</a> · <a href="/assets/command-help/changedictionary.txt">帮助文本</a></p>
