---
title: "surfaceMeshExport · 将 OpenFOAM 的 surfMesh 导出为其他软件支持的表面格式"
layout: reference
description: "将 OpenFOAM 的 surfMesh 导出为其他软件支持的表面格式。"
cms_slug: "command-surfacemeshexport"
---

<p>将 OpenFOAM 的 surfMesh 导出为其他软件支持的表面格式。</p><h2>开始前</h2>
<p>案例内已有 surfMesh；可先使用 surfaceMeshImport 导入。它导出存储的表面网格，体网格边界另用 surfaceMeshExtract。</p>
<h2>示例 1：导出默认表面</h2>
<pre><code class="language-bash">surfaceMeshExport body.obj
</code></pre>
<p>读取当前案例中默认名称的 surfMesh 并导出为 OBJ。终端会显示读取的表面路径，可据此确认导出的对象。</p>
<h2>示例 2：导出命名表面</h2>
<pre><code class="language-bash">surfaceMeshExport blade.stl -name blade
</code></pre>
<p>选择名为 blade 的 surfMesh，输出 STL。适合一个案例同时保存叶片、轮毂等多个独立表面。</p>
<h2>示例 3：导出毫米坐标</h2>
<pre><code class="language-bash">surfaceMeshExport body-mm.obj -write-scale 1000
</code></pre>
<p>写文件前将坐标乘 1000；原来 0.2 m 的尺寸输出为 200。导出的文件单位需要在接收软件中设为毫米。</p>
<h2>示例 4：导出到指定坐标系</h2>
<pre><code class="language-bash">surfaceMeshExport body-local.obj -to local
</code></pre>
<p>前提是 constant/coordinateSystems 中存在 local。将案例坐标下的表面表示到该坐标系，便于相对零件原点检查几何。</p>
<h2>示例 5：导出其他案例的指定格式</h2>
<pre><code class="language-bash">surfaceMeshExport -case ../surfaceCase body.data -name blade -write-format obj
</code></pre>
<p>从 ../surfaceCase 读取 blade 表面，并将结果写为 OBJ 内容。输出路径 body.data 相对当前工作目录，使用绝对路径可明确存放位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-clean</code></td><td>对输入表面执行检查与清理。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 coordinateSystems 文件。</td></tr><tr><td><code>-from &lt;system&gt;</code></td><td>指定源坐标系；在 -read-scale 缩放后应用。</td></tr><tr><td><code>-name &lt;name&gt;</code></td><td>指定读取的表面名称，默认为 default。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-read-scale &lt;factor&gt;</code></td><td>设置输入几何的缩放系数。</td></tr><tr><td><code>-to &lt;system&gt;</code></td><td>指定目标坐标系；在 -write-scale 缩放前应用。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-write-format &lt;type&gt;</code></td><td>指定输出格式；默认由文件扩展名判断。</td></tr><tr><td><code>-write-scale &lt;factor&gt;</code></td><td>设置输出几何的缩放系数。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshExport/surfaceMeshExport.C">源码与说明</a> · <a href="/assets/command-help/surfacemeshexport.txt">帮助文本</a></p>
