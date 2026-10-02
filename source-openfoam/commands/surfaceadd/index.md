---
title: "surfaceAdd · 连接两个表面数据集，不执行几何布尔并集"
layout: reference
description: "连接两个表面数据集，不执行几何布尔并集。"
cms_slug: "command-surfaceadd"
---

<p>连接两个表面数据集，不执行几何布尔并集。</p><h2>开始前</h2>
<p>两个输入为可读取的表面文件，坐标系和长度单位一致；输出文件使用新名称。</p>
<h2>示例 1：合并两个部件</h2>
<pre><code class="language-bash">surfaceAdd housing.stl rotor.stl assembly.stl
</code></pre>
<p>把壳体和转子组合为一个表面文件，并对重合点做几何合并；保留各部件区域信息。</p>
<h2>示例 2：按同名区域合并</h2>
<pre><code class="language-bash">surfaceAdd -mergeRegions left.stl right.stl joined.stl
</code></pre>
<p>两块表面区域含相同名称时，将对应区域组合，适合被分成多个文件的同一边界。</p>
<h2>示例 3：合并毫米几何</h2>
<pre><code class="language-bash">surfaceAdd -scale 0.001 housing_mm.stl rotor_mm.stl assembly_m.stl
</code></pre>
<p>两个输入都以毫米表示时，先按0.001缩放再合并，输出坐标以米表示。</p>
<h2>示例 4：逐步组合三个部件</h2>
<pre><code class="language-bash">surfaceAdd body.stl inlet.stl bodyInlet.stl
surfaceAdd bodyInlet.stl outlet.stl complete.stl
</code></pre>
<p>通过中间文件组合三个表面，每一步均保留输入，便于判断区域在何时发生变化。</p>
<h2>示例 5：检查合并后的交叉</h2>
<pre><code class="language-bash">surfaceAdd a.stl b.stl combined.stl
surfaceCheck -checkSelfIntersection combined.stl
</code></pre>
<p>合并前两表面已在同一坐标系。第二步检查交叉三角形；surfaceAdd本身做组合与点合并，不执行实体布尔裁切。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-mergeRegions</code></td><td>合并两个表面的区域。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-points &lt;file&gt;</code></td><td>提供额外的点文件。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置输入表面的几何缩放系数。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceAdd/surfaceAdd.C">源码与说明</a> · <a href="/assets/command-help/surfaceadd.txt">帮助文本</a></p>
