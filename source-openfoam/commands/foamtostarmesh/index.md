---
title: "foamToStarMesh · 输出 bnd、cel 和 vrt 等文件"
layout: reference
description: "输出 bnd、cel 和 vrt 等文件。"
cms_slug: "command-foamtostarmesh"
---

<p>输出 bnd、cel 和 vrt 等文件。</p><h2>开始前</h2>
<p>案例已有网格；默认导出比例为 1000，即常见米制 OpenFOAM 网格转为毫米制 STAR-CD 坐标。</p>
<h2>示例 1：按默认比例导出</h2>
<pre><code class="language-bash">foamToStarMesh -constant
</code></pre>
<p>输出 STAR-CD 的顶点、单元和边界文件。默认坐标乘 1000，原 1 m 长度写为 1000。</p>
<h2>示例 2：保持原坐标数值</h2>
<pre><code class="language-bash">foamToStarMesh -constant -scale 1
</code></pre>
<p>显式指定比例 1，适合接收端也使用米制坐标的情况。导入外部软件后核对边界框。</p>
<h2>示例 3：仅导出几何连接</h2>
<pre><code class="language-bash">foamToStarMesh -constant -noBnd
</code></pre>
<p>输出顶点和单元，跳过 .bnd 边界文件。适合接收端计划重新建立边界分区的流程。</p>
<h2>示例 4：导出最新网格位置</h2>
<pre><code class="language-bash">foamToStarMesh -latestTime -scale 1
</code></pre>
<p>选择最新时间的网格，保持米制坐标。动网格输出可用于检查最后时刻的几何形状。</p>
<h2>示例 5：导出选定时间的网格</h2>
<pre><code class="language-bash">foamToStarMesh -time '0.2,0.5,1' -scale 1000
</code></pre>
<p>选择已有的 0.2、0.5 和 1 时间目录。比较输出几何可以分析位移过程；所有输出采用相同的毫米坐标尺度。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noBnd</code></td><td>跳过边界 .bnd 文件的输出。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 1000，即将米转换为毫米。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamToStarMesh/foamToStarMesh.C">源码与说明</a> · <a href="/assets/command-help/foamtostarmesh.txt">帮助文本</a></p>
