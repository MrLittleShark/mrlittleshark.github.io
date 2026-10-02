---
title: "surfaceMeshImport · 导入对象为表面网格，-name 指定名称"
layout: reference
description: "导入对象为表面网格，-name 指定名称。"
cms_slug: "command-surfacemeshimport"
---

<p>导入对象为表面网格，-name 指定名称。</p><h2>开始前</h2>
<p>准备表面文件和包含 system/controlDict 的案例目录；命名导入可在同一案例保存多个 surfMesh。</p>
<h2>示例 1：导入默认表面</h2>
<pre><code class="language-bash">surfaceMeshImport body.stl
</code></pre>
<p>将 STL 转为案例内的 surfMesh 存储。随后 surfaceMeshExport body.obj 可将这一表面重新导出检查。</p>
<h2>示例 2：给表面指定名称</h2>
<pre><code class="language-bash">surfaceMeshImport blade.obj -name blade
</code></pre>
<p>以 blade 为名称保存表面，之后通过 surfaceMeshExport -name blade 选择它。适合分开管理多个零件。</p>
<h2>示例 3：导入毫米模型</h2>
<pre><code class="language-bash">surfaceMeshImport body-mm.stl -read-scale 0.001 -name body
</code></pre>
<p>读取时将坐标换算为米，再保存为 body 表面。查看终端边界框，应与目标计算域尺寸一致。</p>
<h2>示例 4：清理后导入</h2>
<pre><code class="language-bash">surfaceMeshImport body.obj -clean -name bodyClean
</code></pre>
<p>对输入表面执行清理再存储。对照原始与导出文件的点、面数量，确认清理处理了哪些实体。</p>
<h2>示例 5：从局部坐标导入另一案例</h2>
<pre><code class="language-bash">surfaceMeshImport blade.obj -case ../surfaceCase -name blade -from local
</code></pre>
<p>从指定案例的坐标系字典读取 local，将局部几何变换到案例坐标。导出检查叶片原点及轴向是否符合装配位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-clean</code></td><td>Perform some surface checking/cleanup on the input surface Set named DebugSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-from &lt;system&gt;</code></td><td>The source coordinate system, applied after &#x27;-read-scale&#x27; Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-name &lt;name&gt;</code></td><td>The surface name when writing (default is &#x27;default&#x27;)</td></tr><tr><td><code>-to &lt;system&gt;</code></td><td>The target coordinate system, applied before &#x27;-write-scale&#x27;</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times) Output geometry scaling factor</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceMeshImport [OPTIONS] &lt;surface&gt;
Arguments:
  &lt;surface&gt;         The input surface file
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
  -name &lt;name&gt;      The surface name when writing (default is &#x27;default&#x27;)
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
  -verbose          Additional verbosity (can be used multiple times)
  -write-scale &lt;factor&gt;
                    Output geometry scaling factor
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Import from various third-party surface formats into surfMesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshImport/surfaceMeshImport.C">源码与说明</a> · <a href="/assets/command-help/surfacemeshimport.txt">帮助文本</a></p>
