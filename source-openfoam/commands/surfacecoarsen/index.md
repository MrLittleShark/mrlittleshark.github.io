---
title: "surfaceCoarsen · 简化因子取值范围为 [0,1)，简化后检查几何完整性"
layout: reference
description: "简化因子取值范围为 [0,1)，简化后检查几何完整性。"
cms_slug: "command-surfacecoarsen"
---

<p>简化因子取值范围为 [0,1)，简化后检查几何完整性。</p><h2>开始前</h2>
<p>输入为三角表面。源码按factor×原顶点数确定目标顶点数；使用0到1之间的正因子，输出另存。</p>
<h2>示例 1：温和减少顶点</h2>
<pre><code class="language-bash">surfaceCoarsen fine.stl 0.8 coarse80.stl
</code></pre>
<p>目标约保留80%的原顶点，先观察主要轮廓和小圆角是否保持。</p>
<h2>示例 2：减半顶点数</h2>
<pre><code class="language-bash">surfaceCoarsen fine.stl 0.5 coarse50.stl
</code></pre>
<p>目标顶点数约减为一半，适合降低可视化或初步几何检查成本。</p>
<h2>示例 3：较强粗化对照</h2>
<pre><code class="language-bash">surfaceCoarsen fine.stl 0.25 coarse25.stl
</code></pre>
<p>约保留四分之一顶点，与0.8和0.5方案比较细节损失，避免直接用最粗表面替代精细几何。</p>
<h2>示例 4：缩放后粗化</h2>
<pre><code class="language-bash">surfaceCoarsen -scale 0.001 fine_mm.stl 0.5 coarse_m.stl
</code></pre>
<p>先将毫米坐标转换为米，再按相同顶点保留比例粗化。</p>
<h2>示例 5：检查粗化结果</h2>
<pre><code class="language-bash">surfaceCoarsen fine.stl 0.5 coarse.stl
surfaceCheck coarse.stl
</code></pre>
<p>比较输入输出面数、开边及包围盒；factor控制顶点目标，三角面数随重建结果变化。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置输入几何的缩放系数。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceCoarsen/surfaceCoarsen.C">源码与说明</a> · <a href="/assets/command-help/surfacecoarsen.txt">帮助文本</a></p>
