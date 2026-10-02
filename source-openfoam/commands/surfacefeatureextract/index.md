---
title: "surfaceFeatureExtract · 从表面提取特征线，供 snappyHexMesh 控制棱边细化"
layout: reference
description: "从表面提取特征线，供 snappyHexMesh 控制棱边细化。"
cms_slug: "command-surfacefeatureextract"
---

<p>从表面提取特征线，供 snappyHexMesh 控制棱边细化。</p><h2>开始前</h2>
<p>已有constant/triSurface表面及system/surfaceFeatureExtractDict；字典中逐个指定表面、提取方法与夹角。</p>
<h2>示例 1：按默认配置提取</h2>
<pre><code class="language-bash">surfaceFeatureExtract
</code></pre>
<p>读取默认字典，生成对应eMesh等特征数据，供snappyHexMesh的features条目引用。</p>
<h2>示例 2：使用独立特征配置</h2>
<pre><code class="language-bash">surfaceFeatureExtract -dict system/surfaceFeatureExtractDict.fine
</code></pre>
<p>fine字典中已设置另一夹角或表面列表时，单独选择该方案提取。</p>
<h2>示例 3：检查另一几何算例</h2>
<pre><code class="language-bash">surfaceFeatureExtract -case ../gearCase
</code></pre>
<p>gearCase包含自身几何和提取字典；结果写入其constant/triSurface。</p>
<h2>示例 4：把特征边转为可视线</h2>
<pre><code class="language-bash">surfaceFeatureExtract
surfaceFeatureConvert constant/triSurface/body.eMesh bodyEdges.obj
</code></pre>
<p>字典中输入为body.stl时，提取后将eMesh转换为OBJ，与齿尖或棱边位置对照。</p>
<h2>示例 5：用于贴体网格流程</h2>
<pre><code class="language-bash">surfaceFeatureExtract
snappyHexMesh
</code></pre>
<p>snappyHexMeshDict已引用本次生成的eMesh及细化等级；先生成特征，再进行体网格细化与贴合。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>从指定位置读取 surfaceFeatureExtractDict。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-surfacefeatureextractdict/">surfaceFeatureExtractDict</a></p><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceFeatureExtract/surfaceFeatureExtract.C">源码与说明</a> · <a href="/assets/command-help/surfacefeatureextract.txt">帮助文本</a></p>
