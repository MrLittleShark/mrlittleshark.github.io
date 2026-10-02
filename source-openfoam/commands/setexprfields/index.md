---
title: "setExprFields · 用数学表达式创建或修改单元场"
layout: reference
description: "用数学表达式创建或修改单元场。"
cms_slug: "command-setexprfields"
---

<p>用数学表达式创建或修改单元场。</p><h2>开始前</h2>
<p>已有网格；修改模式要求目标场存在，创建模式需指定字段名、表达式和合适量纲。</p>
<h2>示例 1：把已有标量场设为常数</h2>
<pre><code class="language-bash">setExprFields -field T -expression '300' -time 0
</code></pre>
<p>T已存在时，将选中场值设为300；应按T的物理单位解释，温度场通常以K填写。</p>
<h2>示例 2：创建无量纲标记场</h2>
<pre><code class="language-bash">setExprFields -create -field marker -dimensions '[0 0 0 0 0 0 0]' -expression '1' -time 0
</code></pre>
<p>生成新的无量纲场marker，内部赋值1，可用作区域标记或后续表达式输入。</p>
<h2>示例 3：由速度计算单位质量动能</h2>
<pre><code class="language-bash">setExprFields -create -field kineticEnergy -dimensions '[0 2 -2 0 0 0 0]' -load-fields '(U)' -expression '0.5*magSqr(U)' -time 0
</code></pre>
<p>读取U，创建单位质量动能场，量纲为平方米每二次方秒；便于观察速度非均匀性。</p>
<h2>示例 4：保留边界只改内部温度</h2>
<pre><code class="language-bash">setExprFields -field T -expression '350' -keepPatches -time 0
</code></pre>
<p>内部T改为350，-keepPatches保留已有边界设置，适合调整初始温度而继续使用原边界条件。</p>
<h2>示例 5：先检查字典中的多场表达式</h2>
<pre><code class="language-bash">setExprFields -dict system/setExprFields-initialDict -dry-run -time 0
setExprFields -dict system/setExprFields-initialDict -time 0
</code></pre>
<p>字典已配置多项场表达式时，先求值检查，再正式写入，适合同时构造速度、标量或几何指示场。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-ascii</code></td><td>以 ASCII 文本格式写出，覆盖 controlDict 的输出格式设置。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-create</code></td><td>在命令行模式下创建新场。</td></tr><tr><td><code>-debug-parser</code></td><td>输出更多解析器调试信息。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 setExprFieldsDict 文件。</td></tr><tr><td><code>-dimensions &lt;dims&gt;</code></td><td>在命令行模式下指定新场的量纲。</td></tr><tr><td><code>-dry-run</code></td><td>计算表达式但暂不写入文件。</td></tr><tr><td><code>-dummy-phi</code></td><td>在命令行模式下提供一个值为零的 phi 场。</td></tr><tr><td><code>-expression &lt;expr&gt;</code></td><td>指定要计算的表达式，适用于命令行模式。</td></tr><tr><td><code>-field &lt;name&gt;</code></td><td>指定要创建或覆盖的场，适用于命令行模式。</td></tr><tr><td><code>-field-mask &lt;logic&gt;</code></td><td>用逻辑条件限定表达式生效的区域，适用于命令行模式。</td></tr><tr><td><code>-keepPatches</code></td><td>保留各边界原有的设置，适用于命令行模式。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-setexprfieldsdict/">setExprFieldsDict</a></p><details class="command-more-options"><summary>更多参数（28 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-load-fields &lt;wordList&gt;</code></td><td>指定预先加载的场，例如 T 或 &#x27;(p T U)&#x27;。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-no-variable-cache</code></td><td>每次重新计算表达式变量，跳过变量缓存。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-value-patches &lt;(patches)&gt;</code></td><td>指定采用固定值的边界列表，适用于命令行模式。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出。</td></tr><tr><td><code>-withFunctionObjects</code></td><td>执行函数对象。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprFields/setExprFields.C">源码与说明</a> · <a href="/assets/command-help/setexprfields.txt">帮助文本</a></p>
