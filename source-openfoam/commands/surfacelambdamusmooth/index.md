---
title: "surfaceLambdaMuSmooth · 通过 lambda/mu 平滑减少表面起伏，并可固定特征点"
layout: reference
description: "通过 lambda/mu 平滑减少表面起伏，并可固定特征点。"
cms_slug: "command-surfacelambdamusmooth"
---

<p>通过 lambda/mu 平滑减少表面起伏，并可固定特征点。</p><h2>开始前</h2>
<p>输入为三角表面，lambda与mu按工具接口取0到1；输出另存，比较轮廓和体积变化。</p>
<h2>示例 1：轻度拉普拉斯平滑</h2>
<pre><code class="language-bash">surfaceLambdaMuSmooth raw.stl 0.2 0 5 smooth5.stl
</code></pre>
<p>mu=0采用拉普拉斯平滑，lambda=0.2控制每次松弛量，先做5次观察。</p>
<h2>示例 2：增加平滑轮数</h2>
<pre><code class="language-bash">surfaceLambdaMuSmooth raw.stl 0.2 0 20 smooth20.stl
</code></pre>
<p>从同一原表面开始做20次，与5次结果比较噪声减少和轮廓收缩。</p>
<h2>示例 3：采用双参数平滑</h2>
<pre><code class="language-bash">surfaceLambdaMuSmooth raw.stl 0.3 0.31 10 smoothLM.stl
</code></pre>
<p>使用lambda/mu两步平滑，以不同参数对抗单步平滑造成的收缩；检查实际体积变化。</p>
<h2>示例 4：保护特征点和边</h2>
<pre><code class="language-bash">surfaceLambdaMuSmooth -featureFile body.eMesh raw.stl 0.3 0.31 10 preserved.stl
</code></pre>
<p>已有与表面对应的特征边文件时，固定其中指定的特征，保留关键棱角。</p>
<h2>示例 5：比较平滑后的质量</h2>
<pre><code class="language-bash">surfaceLambdaMuSmooth raw.stl 0.3 0.31 10 smooth.stl
surfaceCheck -checkSelfIntersection smooth.stl
</code></pre>
<p>查看自相交、开边和包围盒，判断平滑是否改善局部三角形而保留所需几何。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（4 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceLambdaMuSmooth/surfaceLambdaMuSmooth.C">源码与说明</a> · <a href="/assets/command-help/surfacelambdamusmooth.txt">帮助文本</a></p>
