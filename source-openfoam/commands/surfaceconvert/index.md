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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-clean</code></td><td>Perform some surface checking/cleanup on the input surface Set named DebugSwitch (default value: 1). [Can be used multiple times] Override the file handler type</td></tr><tr><td><code>-group</code></td><td>Reorder faces into groups; one per region Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-precision &lt;int&gt;</code></td><td>The output precision The input format (default: use file extension)</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Input geometry scaling factor</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times) The output format (default: use file extension)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceConvert [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;output&gt;          The output surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -clean            Perform some surface checking/cleanup on the input surface
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -group            Reorder faces into groups; one per region
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
  -precision &lt;int&gt;  The output precision
  -read-format &lt;type&gt;
                    The input format (default: use file extension)
  -scale &lt;factor&gt;   Input geometry scaling factor
  -verbose          Additional verbosity (can be used multiple times)
  -write-format &lt;type&gt;
                    The output format (default: use file extension)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert between surface formats, using triSurface library components

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceConvert/surfaceConvert.C">源码与说明</a> · <a href="/assets/command-help/surfaceconvert.txt">帮助文本</a></p>
