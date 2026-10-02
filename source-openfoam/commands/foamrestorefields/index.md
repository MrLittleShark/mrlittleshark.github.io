---
title: "foamRestoreFields · 在原场与 Mean 平均场之间切换文件，并维护 .orig 备份"
layout: reference
description: "在原场与 Mean 平均场之间切换文件，并维护 .orig 备份。"
cms_slug: "command-foamrestorefields"
---

<p>在原场与 Mean 平均场之间切换文件，并维护 .orig 备份。</p><h2>开始前</h2>
<p>已有UMean、pMean等平均场，或此前生成的.orig备份；-method必须为mean或orig。</p>
<h2>示例 1：预览用均值替换速度的动作</h2>
<pre><code class="language-bash">foamRestoreFields -method mean -latestTime -dry-run U
</code></pre>
<p>只报告文件重命名计划，检查UMean与U的对应关系。</p>
<h2>示例 2：使用平均速度和压力</h2>
<pre><code class="language-bash">foamRestoreFields -method mean -latestTime U p
</code></pre>
<p>用UMean、pMean替代U、p，原有文件保存为.orig，便于把均值场交给后处理。</p>
<h2>示例 3：恢复原始字段</h2>
<pre><code class="language-bash">foamRestoreFields -method orig -latestTime U p
</code></pre>
<p>存在U.orig、p.orig时将其恢复为原字段名称，返回切换前的瞬时结果。</p>
<h2>示例 4：处理明确的时间范围</h2>
<pre><code class="language-bash">foamRestoreFields -method mean -time '1:2' U
</code></pre>
<p>仅对1至2秒已有平均速度的时刻切换U，保留其他时间。</p>
<h2>示例 5：切换并行案例的均值场</h2>
<pre><code class="language-bash">foamRestoreFields -method mean -processor -latestTime U p
</code></pre>
<p>串行调用但扫描processor目录，在各子域最新时间进行相同字段切换，适合并行结果的统一整理。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中的全部区域。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dry-run</code></td><td>仅显示移动或重命名计划。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-method &lt;name&gt;</code></td><td>必填恢复方式：mean 将以 Mean 结尾的文件恢复为原场名，并把已有场备份为 .orig；orig 恢复以 .orig 结尾的备份。</td></tr><tr><td><code>-noZero</code></td><td>排除 0/ 目录；此选项优先于 -withZero。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-processor</code></td><td>串行调用时从 processor0/ 获取时间列表，并对各 processor 数字目录执行操作。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，例如 -region gas。</td></tr><tr><td><code>-regions &lt;wordRes&gt;</code></td><td>指定一个区域或按 regionProperties 匹配多个区域，例如 -regions gas 或 -regions &#x27;(gas &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（20 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-withZero</code></td><td>将 0/ 目录加入时间选择。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamRestoreFields/foamRestoreFields.C">源码与说明</a> · <a href="/assets/command-help/foamrestorefields.txt">帮助文本</a></p>
