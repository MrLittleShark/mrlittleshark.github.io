---
title: "renumberMesh · 重排单元与面编号以减小矩阵带宽，并同步重排场"
layout: reference
description: "重排单元与面编号以减小矩阵带宽，并同步重排场。"
cms_slug: "command-renumbermesh"
---

<p>重排单元与面编号以减小矩阵带宽，并同步重排场。</p><h2>开始前</h2>
<p>已有网格；选定时间的场与网格相匹配。默认重编号方法为 CuthillMcKee。</p>
<h2>示例 1：测试编号效果</h2>
<pre><code class="language-bash">renumberMesh -dry-run -frontWidth
</code></pre>
<p>只计算重排方案与带宽、前沿宽度指标，保留原网格；可判断该网格是否值得重排。</p>
<h2>示例 2：应用默认重编号</h2>
<pre><code class="language-bash">renumberMesh -overwrite
</code></pre>
<p>把重排后的网格和相应场写回当前案例，几何形状和物理场分布保持对应。</p>
<h2>示例 3：保存编号映射</h2>
<pre><code class="language-bash">renumberMesh -overwrite -write-maps
</code></pre>
<p>额外保存旧编号与新编号的映射，用于对照外部单元数据、源项选区或调试信息。</p>
<h2>示例 4：显式选择反向编号</h2>
<pre><code class="language-bash">renumberMesh -renumber-method CuthillMcKee -renumber-coeffs 'reverse true;' -overwrite
</code></pre>
<p>命令行选择方法并传入 reverse 系数，使用反向 Cuthill–McKee 排序，比较带宽和线性求解性能。</p>
<h2>示例 5：对最后时刻的动网格重排</h2>
<pre><code class="language-bash">renumberMesh -latestTime -overwrite -write-maps
</code></pre>
<p>读取最后保存状态的网格和场，重排并输出映射；后续重启使用这一时间的匹配数据。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中的全部区域。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decompose</code></td><td>先按分区方法聚合单元，仅适用于串行运行。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 renumberMeshDict 文件。</td></tr><tr><td><code>-dry-run</code></td><td>仅测试编号，暂不写回；此时 -write-maps 改为输出 VTK。</td></tr><tr><td><code>-frontWidth</code></td><td>计算矩阵前沿宽度的均方根。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-list-renumber</code></td><td>列出可用的重编号方法。</td></tr><tr><td><code>-no-fields</code></td><td>保留场的原有编号，例如场仅含 uniform 值时。</td></tr><tr><td><code>-noZero</code></td><td>排除 0/ 目录；当前实现会忽略此选项。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-renumbermeshdict/">renumberMeshDict</a></p><details class="command-more-options"><summary>更多参数（26 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，例如 -region gas。</td></tr><tr><td><code>-regions &lt;wordRes&gt;</code></td><td>指定一个区域或按 regionProperties 匹配多个区域，例如 -regions gas 或 -regions &#x27;(gas &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-renumber-coeffs &lt;string-content&gt;</code></td><td>用字符串传入重编号参数，例如 &#x27;reverse true;&#x27;。</td></tr><tr><td><code>-renumber-method &lt;name&gt;</code></td><td>直接指定重编号方法，默认采用 CuthillMcKee。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-time &lt;value&gt;</code></td><td>选择最接近给定数值的时刻。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-write-maps</code></td><td>写出重编号映射。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/renumberMesh/renumberMesh.C">源码与说明</a> · <a href="/assets/command-help/renumbermesh.txt">帮助文本</a></p>
