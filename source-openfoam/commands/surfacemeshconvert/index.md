---
title: "surfaceMeshConvert · 转换表面网格格式，并可进行缩放、旋转和平移"
layout: reference
description: "转换表面网格格式，并可进行缩放、旋转和平移。"
cms_slug: "command-surfacemeshconvert"
---

<p>转换表面网格格式，并可进行缩放、旋转和平移。</p><h2>开始前</h2>
<p>准备工具支持的表面网格；坐标变换示例还需在 constant/coordinateSystems 定义 local 坐标系。-from 与 -to 分别用于两个方向的变换，每次选一个。</p>
<h2>示例 1：转换表面格式</h2>
<pre><code class="language-bash">surfaceMeshConvert body.obj body.stl
</code></pre>
<p>读取 OBJ 的顶点和面，写成 STL；输出格式由扩展名决定。转换后用 surfaceCheck body.stl 查看三角面数量和连通性。</p>
<h2>示例 2：读取时换算毫米</h2>
<pre><code class="language-bash">surfaceMeshConvert body-mm.stl body-m.obj -read-scale 0.001
</code></pre>
<p>输入坐标乘 0.001，再写出 OBJ。原长 100 mm 的边输出为 0.1，适合与以米建立的背景网格对齐。</p>
<h2>示例 3：清理并三角化</h2>
<pre><code class="language-bash">surfaceMeshConvert body.obj body-clean.stl -clean -tri
</code></pre>
<p>先清理表面中可处理的退化或重复实体，再将多边形转为三角形。检查输出面数及几何轮廓，确认细小结构仍然保留。</p>
<h2>示例 4：从局部坐标转到全局坐标</h2>
<pre><code class="language-bash">surfaceMeshConvert blade.obj blade-global.obj -from local
</code></pre>
<p>前提是 constant/coordinateSystems 中存在 local。按其原点和方向将局部几何变换到全局坐标，供装配使用；若要继续转到另一个局部系，可对输出另运行一次 -to。</p>
<h2>示例 5：指定格式并输出毫米</h2>
<pre><code class="language-bash">surfaceMeshConvert body.data body.export -read-format obj -write-format stl -write-scale 1000
</code></pre>
<p>为没有标准扩展名的文件明确指定格式。输出坐标乘 1000，可将米制模型交给使用毫米坐标的工具。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-clean</code></td><td>对输入表面执行检查与清理。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 coordinateSystems 文件。</td></tr><tr><td><code>-from &lt;system&gt;</code></td><td>指定源坐标系；在 -read-scale 缩放后应用。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-read-format &lt;type&gt;</code></td><td>指定输入格式；默认由文件扩展名判断。</td></tr><tr><td><code>-read-scale &lt;factor&gt;</code></td><td>设置输入几何的缩放系数。</td></tr><tr><td><code>-to &lt;system&gt;</code></td><td>指定目标坐标系；在 -write-scale 缩放前应用。</td></tr><tr><td><code>-tri</code></td><td>将表面三角化。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-write-format &lt;type&gt;</code></td><td>指定输出格式；默认由文件扩展名判断。</td></tr><tr><td><code>-write-scale &lt;factor&gt;</code></td><td>设置输出几何的缩放系数。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshConvert/surfaceMeshConvert.C">源码与说明</a> · <a href="/assets/command-help/surfacemeshconvert.txt">帮助文本</a></p>
