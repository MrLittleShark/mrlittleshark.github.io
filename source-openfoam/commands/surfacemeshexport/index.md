---
title: "surfaceMeshExport · 输入为算例中已有的 surfaceMesh"
layout: reference
description: "输入为算例中已有的 surfaceMesh。"
cms_slug: "command-surfacemeshexport"
---

<p>输入为算例中已有的 surfaceMesh。</p><h2>开始前</h2>
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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-clean</code></td><td>Perform some surface checking/cleanup on the input surface Set named DebugSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-from &lt;system&gt;</code></td><td>The source coordinate system, applied after &#x27;-read-scale&#x27; Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-name &lt;name&gt;</code></td><td>Specify an alternative surface name when reading - default is &#x27;default&#x27;</td></tr><tr><td><code>-to &lt;system&gt;</code></td><td>The target coordinate system, applied before &#x27;-write-scale&#x27;</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times) Output format (default: use file extension) Output geometry scaling factor</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceMeshExport [OPTIONS] &lt;output&gt;
Arguments:
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
  -name &lt;name&gt;      Specify an alternative surface name when reading - default
                    is &#x27;default&#x27;
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -read-scale &lt;factor&gt;
                    Input geometry scaling factor
  -to &lt;system&gt;      The target coordinate system, applied before &#x27;-write-scale&#x27;
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

Export from surfMesh to various third-party surface formats

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshExport/surfaceMeshExport.C">源码与说明</a> · <a href="/assets/command-help/surfacemeshexport.txt">帮助文本</a></p>
