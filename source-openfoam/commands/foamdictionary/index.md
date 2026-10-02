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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-add &lt;value&gt;</code></td><td>添加一个新条目。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-diff &lt;dict&gt;</code></td><td>输出当前字典相对于指定字典的差异。</td></tr><tr><td><code>-diff-etc &lt;dict&gt;</code></td><td>比较字典差异；对照文件按 foamEtcFile 的规则查找。</td></tr><tr><td><code>-disableFunctionEntries</code></td><td>按原文读取 #include、#codeStream 等指令，跳过展开。</td></tr><tr><td><code>-entry &lt;name&gt;</code></td><td>选择并显示指定的键或子字典。</td></tr><tr><td><code>-expand</code></td><td>读取字典，展开宏等内容，将展开后的字典输出到终端。</td></tr><tr><td><code>-includes</code></td><td>将 #include、#sinclude 引用的文件列表输出到终端。</td></tr><tr><td><code>-keywords</code></td><td>列出键名。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-precision &lt;int&gt;</code></td><td>设置 IOstreams 的默认输出精度。</td></tr><tr><td><code>-remove</code></td><td>删除指定条目。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（21 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-set &lt;value&gt;</code></td><td>设置条目值；条目不存在时添加。</td></tr><tr><td><code>-value</code></td><td>仅输出条目的值。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamDictionary/foamDictionary.C">源码与说明</a> · <a href="/assets/command-help/foamdictionary.txt">帮助文本</a></p>
