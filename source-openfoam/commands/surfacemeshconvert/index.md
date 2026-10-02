---
title: "surfaceMeshConvert · 采用 surfaceMesh 读写接口"
layout: reference
description: "采用 surfaceMesh 读写接口。"
cms_slug: "command-surfacemeshconvert"
---

<p>采用 surfaceMesh 读写接口。</p><h2>开始前</h2>
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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-clean</code></td><td>Perform some surface checking/cleanup on the input surface Set named DebugSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-from &lt;system&gt;</code></td><td>The source coordinate system, applied after &#x27;-read-scale&#x27; Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-to &lt;system&gt;</code></td><td>The target coordinate system, applied before &#x27;-write-scale&#x27;</td></tr><tr><td><code>-tri</code></td><td>Triangulate surface</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times) Output format (default: use file extension) Output geometry scaling factor</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceMeshConvert [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;output&gt;          The output surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -clean            Perform some surface checking/cleanup on the input surface
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative coordinateSystems
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -from &lt;system&gt;    The source coordinate system, applied after &#x27;-read-scale&#x27;
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -read-format &lt;type&gt;
                    Input format (default: use file extension)
  -read-scale &lt;factor&gt;
                    Input geometry scaling factor
  -to &lt;system&gt;      The target coordinate system, applied before &#x27;-write-scale&#x27;
  -tri              Triangulate surface
  -verbose          Additional verbosity (can be used multiple times)
  -write-format &lt;type&gt;
                    Output format (default: use file extension)
  -write-scale &lt;factor&gt;
                    Output geometry scaling factor
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert between surface formats, using MeshSurface library components

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshConvert/surfaceMeshConvert.C">源码与说明</a> · <a href="/assets/command-help/surfacemeshconvert.txt">帮助文本</a></p>
