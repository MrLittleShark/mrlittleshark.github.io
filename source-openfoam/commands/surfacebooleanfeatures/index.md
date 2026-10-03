---
title: "surfaceBooleanFeatures · 提取两个表面进行并集、交集或差集运算时产生的交线特征"
layout: reference
description: "提取两个表面进行并集、交集或差集运算时产生的交线特征。"
cms_slug: "command-surfacebooleanfeatures"
---

<p>提取两个表面进行并集、交集或差集运算时产生的交线特征。</p><h2>开始前</h2>
<p>准备相交的两个表面，并在含controlDict的工作算例中运行。输出是布尔界面的extendedFeatureEdgeMesh特征线。</p>
<h2>示例 1：提取并集的交界特征</h2>
<pre><code class="language-bash">surfaceBooleanFeatures union body.stl boss.stl
</code></pre>
<p>按并集关系识别两表面相交处的特征边，供后续特征控制使用。</p>
<h2>示例 2：提取交集特征</h2>
<pre><code class="language-bash">surfaceBooleanFeatures intersection body.stl box.stl
</code></pre>
<p>选择两个实体重叠部分的布尔界面，观察被box限定区域的交界线。</p>
<h2>示例 3：提取差集特征</h2>
<pre><code class="language-bash">surfaceBooleanFeatures difference body.stl cutter.stl
</code></pre>
<p>按第一个实体减去第二个实体的关系生成特征线，输入顺序决定差集含义。</p>
<h2>示例 4：处理退化交点</h2>
<pre><code class="language-bash">surfaceBooleanFeatures -perturb union body.stl boss.stl
</code></pre>
<p>两表面局部共面或交点退化导致求交困难时，小幅扰动点位以尝试获得稳定交线。</p>
<h2>示例 5：限制交线保留范围</h2>
<pre><code class="language-bash">surfaceBooleanFeatures -trim '((clip.stl inside))' union body.stl boss.stl
</code></pre>
<p>clip.stl为额外闭合选择表面，仅保留位于其内部的交线段，适合局部特征提取。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-invertedSpace</code></td><td>采用反向空间定义，即将无穷远点视为内部点；适用于并集与交集运算。</td></tr><tr><td><code>-no-cgal</code></td><td>使用 CGAL 以外的算法。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-perturb</code></td><td>微调表面点的位置，消除退化的交线情况。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>对两个表面应用相同的几何缩放系数。</td></tr><tr><td><code>-surf1Baffle</code></td><td>将表面 1 视为挡板。</td></tr><tr><td><code>-surf2Baffle</code></td><td>将表面 2 视为挡板。</td></tr><tr><td><code>-trim &lt;((surface1 volumeType) .. (surfaceN volumeType))&gt;</code></td><td>用额外表面裁剪交线：inside 保留内部边段，outside 保留外部边段，mixed 保留全部。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceBooleanFeatures/surfaceBooleanFeatures.C">源码与说明</a> · <a href="/assets/command-help/surfacebooleanfeatures.txt">帮助文本</a></p>
