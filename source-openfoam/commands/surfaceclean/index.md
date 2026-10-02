---
title: "surfaceClean · 长度和质量阈值按几何尺度设置；清理会改变局部表面细节"
layout: reference
description: "长度和质量阈值按几何尺度设置；清理会改变局部表面细节。"
cms_slug: "command-surfaceclean"
---

<p>长度和质量阈值按几何尺度设置；清理会改变局部表面细节。</p><h2>开始前</h2>
<p>长度阈值使用缩放后的几何单位，quality为三角形质量阈值。先用surfaceCheck了解最小特征尺度，输出另存。</p>
<h2>示例 1：清理极短边</h2>
<pre><code class="language-bash">surfaceClean raw.stl 1e-6 1e-6 clean.stl
</code></pre>
<p>将短于1μm的边和质量极差的三角形纳入清理，输出clean.stl以供对照。</p>
<h2>示例 2：提高质量阈值</h2>
<pre><code class="language-bash">surfaceClean raw.stl 1e-6 0.01 cleanQuality.stl
</code></pre>
<p>保持长度阈值，提高最小质量要求到0.01，适合进一步处理狭长薄片三角形。</p>
<h2>示例 3：按毫米输入清理</h2>
<pre><code class="language-bash">surfaceClean -scale 0.001 raw_mm.stl 1e-5 0.01 clean_m.stl
</code></pre>
<p>先把毫米坐标换成米，再使用10μm的长度阈值清理。</p>
<h2>示例 4：跳过预清理比较主算法</h2>
<pre><code class="language-bash">surfaceClean -no-clean raw.stl 1e-6 0.01 cleanNoPrepass.stl
</code></pre>
<p>-no-clean跳过输入阶段的一轮检查清理，后续按长度与质量要求处理，适合诊断不同阶段的影响。</p>
<h2>示例 5：清理后核对闭合性</h2>
<pre><code class="language-bash">surfaceClean raw.stl 1e-6 0.01 clean.stl
surfaceCheck -checkSelfIntersection clean.stl
</code></pre>
<p>检查输出的开边、自相交与包围盒，确认清理后的表面仍符合预期几何。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-no-clean</code></td><td>直接使用输入表面，跳过检查与清理。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置输入几何的缩放系数。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceClean/collapseBase.C">源码与说明</a> · <a href="/assets/command-help/surfaceclean.txt">帮助文本</a></p>
