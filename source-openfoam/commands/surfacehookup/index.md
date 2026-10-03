---
title: "surfaceHookUp · 连接距离接近的开放边缘，缝合表面网格"
layout: reference
description: "连接距离接近的开放边缘，缝合表面网格。"
cms_slug: "command-surfacehookup"
---

<p>连接距离接近的开放边缘，缝合表面网格。</p><h2>开始前</h2>
<p>system/surfaceHookUpDict逐项列出待连接表面及type triSurfaceMesh，文件位于constant/triSurface；容差与几何长度单位一致。</p>
<h2>示例 1：连接微小间隙</h2>
<pre><code class="language-bash">surfaceHookUp 1e-5
</code></pre>
<p>用10μm连接容差移动并重三角化邻近边界，生成hookedSurface_前缀的新表面。</p>
<h2>示例 2：比较更严格容差</h2>
<pre><code class="language-bash">surfaceHookUp 1e-6
</code></pre>
<p>在相同原始几何副本中采用1μm容差，只处理更近的边界，比较仍未连接的缝隙。</p>
<h2>示例 3：限制处理轮数</h2>
<pre><code class="language-bash">surfaceHookUp -maxIters 20 1e-5
</code></pre>
<p>把最大迭代次数设为20，观察一小段连接过程的进展与剩余间隙。</p>
<h2>示例 4：选择另一组连接面</h2>
<pre><code class="language-bash">surfaceHookUp -dict system/surfaceHookUpDict.inlet 1e-5
</code></pre>
<p>完整inlet字典只列需要连接的入口相关表面，缩小本次处理范围。</p>
<h2>示例 5：检查连接后的表面</h2>
<pre><code class="language-bash">surfaceHookUp 1e-5
surfaceCheck constant/triSurface/hookedSurface_surface1.stl
</code></pre>
<p>字典包含surface1.stl时检查其新文件，核对开边、交叉及区域，确认连接是否达到预期。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 surfaceHookUpDict 文件。</td></tr><tr><td><code>-maxIters &lt;number&gt;</code></td><td>设置最大迭代次数，默认为 100。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceHookUp/surfaceHookUp.C">源码与说明</a> · <a href="/assets/command-help/surfacehookup.txt">帮助文本</a></p>
