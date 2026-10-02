---
title: "surfaceSplitByTopology · 用于分离拓扑不连通的部件"
layout: reference
description: "用于分离拓扑不连通的部件。"
cms_slug: "command-surfacesplitbytopology"
---

<p>用于分离拓扑不连通的部件。</p><h2>开始前</h2>
<p>工具根据三角面拓扑识别并分离 baffle 等区域；输入中的开放边和多连接边决定分区，适合薄片附着在主体表面的几何。</p>
<h2>示例 1：分离附着薄片区域</h2>
<pre><code class="language-bash">surfaceSplitByTopology body-with-baffle.stl body-separated.stl
</code></pre>
<p>读取包含附着薄片的三角表面，沿其拓扑关系划分区域并写入输出。查看区域名称和颜色，确认薄片与主体的分离范围。</p>
<h2>示例 2：先诊断连接关系</h2>
<pre><code class="language-bash">surfaceCheck junction.stl
surfaceSplitByTopology junction.stl junction-zones.stl
</code></pre>
<p>先查看开放边、多连接边数量，再进行拓扑分区。处理后可把新区域与异常边位置对应，判断几何连接是否符合模型。</p>
<h2>示例 3：将分区导出为独立文件</h2>
<pre><code class="language-bash">surfaceSplitByTopology assembly.stl assembly-zones.stl
surfaceSplitByPatch assembly-zones.stl
</code></pre>
<p>第一步在输出中建立区域，第二步把区域分别写成文件。便于后续单独保留或修复薄片部分。</p>
<h2>示例 4：处理 OBJ 三角表面</h2>
<pre><code class="language-bash">surfaceSplitByTopology plate.obj plate-zones.obj
</code></pre>
<p>使用 OBJ 输入和输出保留可视化工作流程。检查分区边界是否沿附着边，而不是仅凭文件中的原分组推断结果。</p>
<h2>示例 5：比较处理前后的拓扑</h2>
<pre><code class="language-bash">surfaceSplitByTopology model.stl model-zones.stl
surfaceCheck model.stl
surfaceCheck model-zones.stl
</code></pre>
<p>核对面数与连接统计，并在可视化中按区域着色。分区结果用于选择区域；是否需要真正断开共享点，可继续评估 surfaceSplitNonManifolds。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（4 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitByTopology/surfaceSplitByTopology.C">源码与说明</a> · <a href="/assets/command-help/surfacesplitbytopology.txt">帮助文本</a></p>
