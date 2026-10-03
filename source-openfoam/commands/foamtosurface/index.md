---
title: "foamToSurface · 提取 OpenFOAM 网格的外边界，并导出为表面网格文件"
layout: reference
description: "提取 OpenFOAM 网格的外边界，并导出为表面网格文件。"
cms_slug: "command-foamtosurface"
---

<p>提取 OpenFOAM 网格的外边界，并导出为表面网格文件。</p><h2>开始前</h2>
<p>案例已有体网格；工具导出体网格边界表面，输出格式由文件扩展名决定。</p>
<h2>示例 1：导出初始边界</h2>
<pre><code class="language-bash">foamToSurface boundary.stl -constant
</code></pre>
<p>提取 constant 网格的边界并写成 STL。可在 CAD 或可视化软件中检查计算域外形。</p>
<h2>示例 2：保留多边形表面表示</h2>
<pre><code class="language-bash">foamToSurface boundary.obj -constant
</code></pre>
<p>输出 OBJ 表面，便于读取网格边界上的多边形。需要三角形表示时，可配合 -tri 选项。</p>
<h2>示例 3：显式三角化边界</h2>
<pre><code class="language-bash">foamToSurface boundary-tri.obj -constant -tri
</code></pre>
<p>将边界多边形分解为三角形后导出。适合需要三角表面的下游几何工具。</p>
<h2>示例 4：导出毫米坐标</h2>
<pre><code class="language-bash">foamToSurface boundary-mm.stl -constant -scale 1000
</code></pre>
<p>将米制网格的坐标乘 1000。接收端应使用毫米单位，并检查几何边界框。</p>
<h2>示例 5：导出最新变形边界</h2>
<pre><code class="language-bash">foamToSurface moved.stl -latestTime
</code></pre>
<p>提取最新时间对应的网格边界。与初始输出叠加，可检查动网格位移和变形范围。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 1。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-tri</code></td><td>将表面三角化。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamToSurface/foamToSurface.C">源码与说明</a> · <a href="/assets/command-help/foamtosurface.txt">帮助文本</a></p>
