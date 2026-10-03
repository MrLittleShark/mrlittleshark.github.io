---
title: "surfaceRefineRedGreen · 细分指定表面三角形，并调整相邻三角形以保持连接连续"
layout: reference
description: "细分指定表面三角形，并调整相邻三角形以保持连接连续。"
cms_slug: "command-surfacerefineredgreen"
---

<p>细分指定表面三角形，并调整相邻三角形以保持连接连续。</p><h2>开始前</h2>
<p>准备三角表面。红绿细化增加三角面数量，主要改变离散密度；新顶点位于原三角形上。</p>
<h2>示例 1：细化一次</h2>
<pre><code class="language-bash">surfaceRefineRedGreen body.stl body-refined.stl
</code></pre>
<p>使用默认一次细化，将表面的三角形继续细分。输出面数增加，原有表面外形保持为同一个分片线性几何。</p>
<h2>示例 2：连续细化两次</h2>
<pre><code class="language-bash">surfaceRefineRedGreen body.stl body-refined2.stl -steps 2
</code></pre>
<p>在第一轮结果上继续细分，获得更密的表面离散。运行前评估面数和内存，避免对已经很密的 CAD 曲面重复加密。</p>
<h2>示例 3：转换格式并细化</h2>
<pre><code class="language-bash">surfaceRefineRedGreen body.obj body-refined.stl -steps 1
</code></pre>
<p>从受支持的三角表面格式读取并输出 STL。适合已有 OBJ 三角面需要进一步细分的场景。</p>
<h2>示例 4：检查细化后的拓扑</h2>
<pre><code class="language-bash">surfaceRefineRedGreen coarse.stl fine.stl -steps 1
surfaceCheck coarse.stl
surfaceCheck fine.stl
</code></pre>
<p>对比面数、开放边和连通性。细分应保留原来的边界结构；开放几何经过细化后仍需按开放表面使用。</p>
<h2>示例 5：细化后再进行平滑</h2>
<pre><code class="language-bash">surfaceRefineRedGreen faceted.stl dense.stl -steps 1
surfaceLambdaMuSmooth dense.stl 0.5 0.53 5 smooth.stl
</code></pre>
<p>先增加离散点，再做五轮 λ–μ 平滑。结果会改变几何形状，应对照原始轮廓和关键尺寸选择平滑强度。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-steps &lt;N&gt;</code></td><td>设置细化次数，默认为 1。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceRefineRedGreen/surfaceRefineRedGreen.C">源码与说明</a> · <a href="/assets/command-help/surfacerefineredgreen.txt">帮助文本</a></p>
