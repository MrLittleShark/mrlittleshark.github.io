---
title: "surfaceConvert · -scale 指定几何缩放系数，按输入与输出长度单位换算"
layout: reference
description: "-scale 指定几何缩放系数，按输入与输出长度单位换算。"
cms_slug: "command-surfaceconvert"
---

<p>-scale 指定几何缩放系数，按输入与输出长度单位换算。</p><h2>开始前</h2>
<p>输入与输出格式由扩展名识别，也可显式指定；该工具使用三角表面表示。</p>
<h2>示例 1：将STL转为OBJ</h2>
<pre><code class="language-bash">surfaceConvert body.stl body.obj
</code></pre>
<p>生成可显示分组信息的OBJ，便于查看三角表面。</p>
<h2>示例 2：按毫米转为米</h2>
<pre><code class="language-bash">surfaceConvert -scale 0.001 body_mm.stl body_m.stl
</code></pre>
<p>统一缩放全部坐标，输出网格几何大小缩小1000倍。</p>
<h2>示例 3：明确无扩展名输入格式</h2>
<pre><code class="language-bash">surfaceConvert -read-format stl geometry body.obj
</code></pre>
<p>geometry实际包含STL数据时显式指定读取格式，避免依赖文件名猜测。</p>
<h2>示例 4：分区排序并清理</h2>
<pre><code class="language-bash">surfaceConvert -clean -group body.stl grouped.obj
</code></pre>
<p>对输入进行基本清理，并按区域重新排列三角形，方便检查各区域连续分组。</p>
<h2>示例 5：控制文本输出精度</h2>
<pre><code class="language-bash">surfaceConvert -precision 12 body.obj precise.stl
</code></pre>
<p>用12位写出精度保存转换结果，适合小尺寸细节或后续格式往返对照。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-clean</code></td><td>对输入表面执行检查与清理。</td></tr><tr><td><code>-group</code></td><td>按区域对面重新分组。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-precision &lt;int&gt;</code></td><td>设置输出精度。</td></tr><tr><td><code>-read-format &lt;type&gt;</code></td><td>指定输入格式；默认由文件扩展名判断。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置输入几何的缩放系数。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-write-format &lt;type&gt;</code></td><td>指定输出格式；默认由文件扩展名判断。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceConvert/surfaceConvert.C">源码与说明</a> · <a href="/assets/command-help/surfaceconvert.txt">帮助文本</a></p>
