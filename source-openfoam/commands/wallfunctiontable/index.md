---
title: "wallFunctionTable · 为查表壁面函数生成速度壁面律反查表"
layout: reference
description: "为查表壁面函数生成速度壁面律反查表。"
cms_slug: "command-wallfunctiontable"
---

<p>为查表壁面函数生成速度壁面律反查表。</p><h2>开始前</h2>
<p>已有网格和constant/wallFunctionDict；官方注释示例采用SpaldingsLaw，可配置表名、步长、区间和对数坐标。</p>
<h2>示例 1：从官方示例生成表</h2>
<pre><code class="language-bash">cp "$WM_PROJECT_DIR/etc/caseDicts/annotated/wallFunctionDict" constant/wallFunctionDict
wallFunctionTable
</code></pre>
<p>使用SpaldingsLaw默认系数生成uPlusWallFunctionData，日志给出输出路径。</p>
<h2>示例 2：提高表格分辨率</h2>
<pre><code class="language-bash">foamDictionary constant/wallFunctionDict -entry dx -set 0.1
wallFunctionTable
</code></pre>
<p>dx由默认0.2改为0.1；在相同坐标区间内增加采样密度，减小后续查表间距。</p>
<h2>示例 3：扩展表格上限</h2>
<pre><code class="language-bash">foamDictionary constant/wallFunctionDict -entry xMax -set 8
wallFunctionTable
</code></pre>
<p>保留log10设置时，xMax表示对数坐标上界；提高上限扩展可查询的Re范围。</p>
<h2>示例 4：使用另一输出表名</h2>
<pre><code class="language-bash">foamDictionary constant/wallFunctionDict -entry invertedTableName -set uPlusFine
wallFunctionTable
</code></pre>
<p>将结果保存为uPlusFine，便于同时保留不同分辨率的壁面律表。</p>
<h2>示例 5：比较壁面律常数</h2>
<pre><code class="language-bash">foamDictionary constant/wallFunctionDict -entry SpaldingsLawCoeffs/kappa -set 0.40
wallFunctionTable
</code></pre>
<p>在独立参数方案中把kappa改为0.40，比较相同Re位置的u+；其余系数与坐标设置保持一致。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/wallFunctionTable/wallFunctionTable.C">源码与说明</a> · <a href="/assets/command-help/wallfunctiontable.txt">帮助文本</a></p>
