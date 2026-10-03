---
title: "surfaceSplitByPatch · 将表面网格的各个区域分别保存为独立文件"
layout: reference
description: "将表面网格的各个区域分别保存为独立文件。"
cms_slug: "command-surfacesplitbypatch"
---

<p>将表面网格的各个区域分别保存为独立文件。</p><h2>开始前</h2>
<p>准备带多个表面区域的 STL、OBJ 等文件；先检查区域名称，再设置选取列表。</p>
<h2>示例 1：按全部区域拆分</h2>
<pre><code class="language-bash">surfaceSplitByPatch assembly.stl
</code></pre>
<p>为各表面区域写出独立文件，终端显示实际输出文件名。适合将装配体的入口、出口和壁面分开处理。</p>
<h2>示例 2：仅导出指定区域</h2>
<pre><code class="language-bash">surfaceSplitByPatch assembly.stl -patches '(inlet outlet)'
</code></pre>
<p>只为 inlet 和 outlet 写出文件，保留原区域内的三角面。可单独检查端面位置和封口情况。</p>
<h2>示例 3：使用名称模式选取</h2>
<pre><code class="language-bash">surfaceSplitByPatch assembly.obj -patches '("blade.*")'
</code></pre>
<p>匹配 blade 开头的区域，分别导出各叶片。正则表达式应放在列表中并加引号。</p>
<h2>示例 4：排除辅助区域</h2>
<pre><code class="language-bash">surfaceSplitByPatch assembly.stl -exclude-patches '(construction capTemporary)'
</code></pre>
<p>拆分其余区域，同时跳过施工辅助面和临时封口。适合整理准备交给其他软件的几何文件。</p>
<h2>示例 5：组合选取和排除</h2>
<pre><code class="language-bash">surfaceSplitByPatch assembly.stl -patches '("wall.*")' -exclude-patches '(wallTemporary)'
</code></pre>
<p>导出 wall 开头的目标表面并排除临时壁面。对生成文件逐个运行 surfaceCheck，可单独定位某一区域的开放边。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-exclude-patches &lt;wordRes&gt;</code></td><td>按名称或正则表达式排除边界，例如 outlet 或 &#x27;(inlet &quot;.*Wall&quot;)&#x27;。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-patches &lt;wordRes&gt;</code></td><td>选择要提取的边界，例如 top 或 &#x27;(front &quot;.*back&quot;)&#x27;。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitByPatch/surfaceSplitByPatch.C">源码与说明</a> · <a href="/assets/command-help/surfacesplitbypatch.txt">帮助文本</a></p>
