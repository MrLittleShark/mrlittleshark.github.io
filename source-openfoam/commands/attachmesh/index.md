---
title: "attachMesh · 用于相应的拓扑连接流程"
layout: reference
description: "用于相应的拓扑连接流程。"
cms_slug: "command-attachmesh"
---

<p>用于相应的拓扑连接流程。</p><h2>开始前</h2>
<p>已有拓扑分离的接口，以及 polyMesh/meshModifiers 中为其定义的网格修改器和对应 zone。工具按这些设置连接接口，在独立副本运行。</p>
<h2>示例 1：连接已定义的滑移接口</h2>
<pre><code class="language-bash">attachMesh
</code></pre>
<p>读取网格修改器并执行接口连接，默认把结果写到下一时间实例。检查日志中的接口处理信息和生成网格路径。</p>
<h2>示例 2：检查连接后的网格</h2>
<pre><code class="language-bash">attachMesh
checkMesh -latestTime -allTopology
</code></pre>
<p>使用新时间实例检查内部面、边界面和区域连通性。连接正确时，原先分离接口两侧应具有预期的拓扑关系。</p>
<h2>示例 3：在目标案例测试接口</h2>
<pre><code class="language-bash">attachMesh -case ../interfaceTest
checkMesh -case ../interfaceTest -latestTime
</code></pre>
<p>从独立 interfaceTest 案例读取网格及 meshModifiers。适合保留原始分离网格，同时对接口设置进行调整比较。</p>
<h2>示例 4：将已确认方案写回原位置</h2>
<pre><code class="language-bash">attachMesh -overwrite
checkMesh -constant -allTopology
</code></pre>
<p>在网格原实例为 constant 的副本中直接保存连接结果。之后继续计算时，网格读取路径与常规初始网格一致。</p>
<h2>示例 5：连接后优化单元编号</h2>
<pre><code class="language-bash">attachMesh -overwrite
renumberMesh -overwrite
checkMesh -constant
</code></pre>
<p>先形成连续的网格连接，再优化单元编号。检查连接和几何保持一致，供后续线性方程求解使用。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/attachMesh/attachMesh.C">源码与说明</a> · <a href="/assets/command-help/attachmesh.txt">帮助文本</a></p>
