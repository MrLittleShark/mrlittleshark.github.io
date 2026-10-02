---
title: "surfaceOrient · 默认按物体外部观察点定向，-inside 将指定点按内部点处理"
layout: reference
description: "默认按物体外部观察点定向，-inside 将指定点按内部点处理。"
cms_slug: "command-surfaceorient"
---

<p>默认按物体外部观察点定向，-inside 将指定点按内部点处理。</p><h2>开始前</h2>
<p>准备三角表面和一个坐标明确的观察点；闭合表面可选择已知内部点或外部点确定朝向。</p>
<h2>示例 1：按外部点统一法向</h2>
<pre><code class="language-bash">surfaceOrient body.stl '(10 10 10)' body-oriented.stl
</code></pre>
<p>假设给定点位于模型外部，按该外部参考确定表面方向。输出另存，使用 ParaView 的法向显示检查外表面朝向。</p>
<h2>示例 2：按内部点确定方向</h2>
<pre><code class="language-bash">surfaceOrient sphere.stl '(0 0 0)' sphere-oriented.stl -inside
</code></pre>
<p>适用于以原点为中心的闭合球面。-inside 明确该点在实体内部，程序据此判断表面内外。</p>
<h2>示例 3：复杂闭合表面使用穿透测试</h2>
<pre><code class="language-bash">surfaceOrient cavity.stl '(5 5 5)' cavity-oriented.stl -usePierceTest
</code></pre>
<p>通过射线与三角面的交点关系判断方向，适合常规判定效果不理想的几何。输入闭合性应先用 surfaceCheck 检查。</p>
<h2>示例 4：同时进行尺度转换</h2>
<pre><code class="language-bash">surfaceOrient body-mm.stl '(1 1 1)' body-m.stl -scale 0.001
</code></pre>
<p>表面坐标缩放到米后进行方向处理，参考点也按缩放后的坐标选择。输出边界框应缩小为原来的千分之一。</p>
<h2>示例 5：为表面惯性计算准备朝向</h2>
<pre><code class="language-bash">surfaceOrient closed.stl '(10 10 10)' oriented.stl
surfaceInertia oriented.stl
</code></pre>
<p>先统一闭合外表面的方向，再计算体积、质心和惯性参数。查看结果体积与尺寸是否一致，可帮助发现几何朝向问题。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-inside</code></td><td>将给定点视为内部点。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置输入几何的缩放系数。</td></tr><tr><td><code>-usePierceTest</code></td><td>通过射线与表面的交点数量判断方向。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceOrient/surfaceOrient.C">源码与说明</a> · <a href="/assets/command-help/surfaceorient.txt">帮助文本</a></p>
