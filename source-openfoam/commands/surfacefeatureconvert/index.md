---
title: "surfaceFeatureConvert · 输入和输出采用该程序支持的边线格式"
layout: reference
description: "输入和输出采用该程序支持的边线格式。"
cms_slug: "command-surfacefeatureconvert"
---

<p>输入和输出采用该程序支持的边线格式。</p><h2>开始前</h2>
<p>输入为边网格，而非三角表面；常见用途是将提取的eMesh特征边转换为可查看的OBJ线。</p>
<h2>示例 1：显示提取的特征边</h2>
<pre><code class="language-bash">surfaceFeatureConvert constant/triSurface/body.eMesh bodyEdges.obj
</code></pre>
<p>把已有特征边网格导出为OBJ线段，可与原STL叠加检查。</p>
<h2>示例 2：将OBJ边转为eMesh</h2>
<pre><code class="language-bash">surfaceFeatureConvert featureLines.obj featureLines.eMesh
</code></pre>
<p>输入OBJ应包含有效线段连接；输出可供支持eMesh的网格工具读取。</p>
<h2>示例 3：缩放特征边单位</h2>
<pre><code class="language-bash">surfaceFeatureConvert -scale 0.001 edges_mm.eMesh edges_m.eMesh
</code></pre>
<p>毫米特征边转换为米，使其与已经缩放的表面一致。</p>
<h2>示例 4：读取无扩展名边文件</h2>
<pre><code class="language-bash">surfaceFeatureConvert -read-format eMesh featureData edges.obj
</code></pre>
<p>featureData实际为OpenFOAM边网格时显式指定格式。</p>
<h2>示例 5：指定输出格式并检查形状</h2>
<pre><code class="language-bash">surfaceFeatureConvert -write-format obj body.eMesh edgePreview
surfaceFeatureConvert -read-format obj edgePreview checked.eMesh
</code></pre>
<p>先输出无扩展名OBJ线，再读回eMesh；比较边数及坐标，检查格式转换是否保留连接。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-read-format &lt;type&gt;</code></td><td>指定输入格式；默认由文件扩展名判断。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置输入几何的缩放系数。</td></tr><tr><td><code>-write-format &lt;type&gt;</code></td><td>指定输出格式；默认由文件扩展名判断。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceFeatureConvert/surfaceFeatureConvert.C">源码与说明</a> · <a href="/assets/command-help/surfacefeatureconvert.txt">帮助文本</a></p>
