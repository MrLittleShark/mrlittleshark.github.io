---
title: "surfaceSubset · 按选择规则从三角表面中提取所需区域"
layout: reference
description: "按选择规则从三角表面中提取所需区域。"
cms_slug: "command-surfacesubset"
---

<p>按选择规则从三角表面中提取所需区域。</p><h2>开始前</h2>
<p>准备三角表面及选择字典。点、边、面编号均从 0 开始；每个示例都从完整基础字典开始或在其上修改。</p>
<h2>示例 1：按面编号提取</h2>
<pre><code class="language-bash">cat &gt; subsetDict &lt;&lt;'EOF'
localPoints ();
edges ();
faces (0 1 2);
zone ();
addFaceNeighbours no;
EOF
surfaceSubset subsetDict body.stl selected.stl
</code></pre>
<p>仅选择编号 0、1、2 的三角面。输出是表面子集，可先用小范围检查输入的编号与可视化选择是否对应。</p>
<h2>示例 2：提取盒内面</h2>
<pre><code class="language-bash">foamDictionary subsetDict -entry faces -set '()'
foamDictionary subsetDict -entry zone -set '((0 0 0) (0.1 0.1 0.1))'
surfaceSubset subsetDict body.stl box.stl
</code></pre>
<p>清空显式面列表，按两个角点定义选择盒。以面中心是否处于该盒内选择三角面，适合提取局部结构。</p>
<h2>示例 3：扩大到相邻面</h2>
<pre><code class="language-bash">foamDictionary subsetDict -entry addFaceNeighbours -set true
surfaceSubset subsetDict body.stl expanded.stl
</code></pre>
<p>在已有选择基础上加入面邻域，扩大局部提取范围。与未扩展结果比较边界，可为局部修复保留周围过渡区域。</p>
<h2>示例 4：导出选择的补集</h2>
<pre><code class="language-bash">foamDictionary subsetDict -entry invertSelection -set true
surfaceSubset subsetDict body.stl remaining.stl
</code></pre>
<p>输出当前选择以外的面。适合把模型分为待修复局部与其余主体；使用前确认之前的选择参数符合目标。</p>
<h2>示例 5：按局部点选择相连面</h2>
<pre><code class="language-bash">foamDictionary subsetDict -entry invertSelection -set false
foamDictionary subsetDict -entry addFaceNeighbours -set false
foamDictionary subsetDict -entry zone -set '()'
foamDictionary subsetDict -entry localPoints -set '(0 1)'
surfaceSubset subsetDict body.stl near-points.stl
</code></pre>
<p>保留 faces 为空，并按局部点 0、1 选取相关面。适合检查某一接缝端点周围的三角形连接。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSubset/surfaceSubset.C">源码与说明</a> · <a href="/assets/command-help/surfacesubset.txt">帮助文本</a></p>
