---
title: "surfaceInflate · 安全因子范围为 [1,10]，膨胀后检查表面自相交"
layout: reference
description: "安全因子范围为 [1,10]，膨胀后检查表面自相交。"
cms_slug: "command-surfaceinflate"
---

<p>安全因子范围为 [1,10]，膨胀后检查表面自相交。</p><h2>开始前</h2>
<p>在工作算例中准备表面及controlDict；distance按几何长度单位填写，factor为额外延伸安全系数，常用1～2。</p>
<h2>示例 1：生成小幅外偏移</h2>
<pre><code class="language-bash">surfaceInflate body.stl 0.001 1.2
</code></pre>
<p>沿点法向膨胀约1mm，并使用1.2安全系数；查看日志列出的表面与迭代输出。</p>
<h2>示例 2：增大包络距离</h2>
<pre><code class="language-bash">surfaceInflate body.stl 0.005 1.2
</code></pre>
<p>对同一原始几何生成5mm级外包络，适合比较间隙或外围包络。</p>
<h2>示例 3：减少法向平滑次数</h2>
<pre><code class="language-bash">surfaceInflate -nSmooth 5 body.stl 0.001 1.2
</code></pre>
<p>将平滑迭代数设为5，比较棱角附近法向传播与局部偏移形状。</p>
<h2>示例 4：设置特征角</h2>
<pre><code class="language-bash">surfaceInflate -featureAngle 45 -nSmooth 2 body.stl 0.002 1.5
</code></pre>
<p>用45°特征角和两次平滑处理有棱角表面，观察锐边附近的膨胀效果。</p>
<h2>示例 5：加入自相交检查</h2>
<pre><code class="language-bash">surfaceInflate -checkSelfIntersection body.stl 0.002 1.2
</code></pre>
<p>狭窄间隙或凹角处启用自相交检查，检查偏移是否导致表面互相穿过。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-checkSelfIntersection</code></td><td>同时检查表面自相交。</td></tr><tr><td><code>-debug</code></td><td>启用额外的调试输出。</td></tr><tr><td><code>-featureAngle &lt;scalar&gt;</code></td><td>设置特征角。</td></tr><tr><td><code>-nSmooth &lt;integer&gt;</code></td><td>设置平滑迭代次数，默认为 20。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceInflate/surfaceInflate.C">源码与说明</a> · <a href="/assets/command-help/surfaceinflate.txt">帮助文本</a></p>
