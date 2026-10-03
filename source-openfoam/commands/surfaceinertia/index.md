---
title: "surfaceInertia · 根据表面几何计算实体或薄壳的惯性张量、主轴和主惯性矩"
layout: reference
description: "根据表面几何计算实体或薄壳的惯性张量、主轴和主惯性矩。"
cms_slug: "command-surfaceinertia"
---

<p>根据表面几何计算实体或薄壳的惯性张量、主轴和主惯性矩。</p><h2>开始前</h2>
<p>实体惯量使用闭合且法向一致的表面；薄壳模式使用面密度。几何坐标按米准备。</p>
<h2>示例 1：计算单位密度实体惯量</h2>
<pre><code class="language-bash">surfaceInertia body.stl
</code></pre>
<p>根据闭合几何计算体积、质心、惯量张量和主惯量，默认单位密度便于检查几何贡献。</p>
<h2>示例 2：指定钢材密度</h2>
<pre><code class="language-bash">surfaceInertia -density 7850 body.stl
</code></pre>
<p>将实体密度设为7850kg/m³，质量与惯量随密度按比例改变。</p>
<h2>示例 3：计算铝材对照</h2>
<pre><code class="language-bash">surfaceInertia -density 2700 body.stl
</code></pre>
<p>保持几何不变改用2700kg/m³，质心位置不变，质量和惯量降低。</p>
<h2>示例 4：计算薄壳惯量</h2>
<pre><code class="language-bash">surfaceInertia -shellProperties -density 2 shell.stl
</code></pre>
<p>用2kg/m²的面密度计算壳体性质，适合已知厚度乘材料密度得到的面质量。</p>
<h2>示例 5：改用安装点作为参考</h2>
<pre><code class="language-bash">surfaceInertia -density 7850 -referencePoint '(0 0 0)' body.stl
</code></pre>
<p>输出相对于原点的惯量，用于与刚体运动中指定参考点的惯量配置对应。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-density &lt;scalar&gt;</code></td><td>指定密度：实体使用 kg/m³，薄壳使用 kg/m²。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-referencePoint &lt;vector&gt;</code></td><td>计算相对于指定点的转动惯量，替代相对于质心的计算。</td></tr><tr><td><code>-shellProperties</code></td><td>计算薄壳的转动惯量。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceInertia/surfaceInertia.C">源码与说明</a> · <a href="/assets/command-help/surfaceinertia.txt">帮助文本</a></p>
