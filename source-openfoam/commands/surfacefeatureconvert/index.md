---
title: "surfaceFeatureConvert · 输入和输出采用该程序支持的边线格式"
layout: reference
description: "输入和输出采用该程序支持的边线格式。"
cms_slug: "command-surfacefeatureconvert"
---

<p>输入和输出采用该程序支持的边线格式。</p><h2>开始前</h2>
<p>输入为边网格，而非三角表面；常见用途是将提取的eMesh特征边转换为可查看的OBJ线。</p>
<h2>示例 1：显示提取的特征边</h2>
<pre><code class="language-bash">surfaceFeatureConvert constant/triSurface/body.eMesh bodyEdges.obj
</code></pre>
<p>把已有特征边网格导出为OBJ线段，可与原STL叠加检查。</p>
<h2>示例 2：将OBJ边转为eMesh</h2>
<pre><code class="language-bash">surfaceFeatureConvert featureLines.obj featureLines.eMesh
</code></pre>
<p>输入OBJ应包含有效线段连接；输出可供支持eMesh的网格工具读取。</p>
<h2>示例 3：缩放特征边单位</h2>
<pre><code class="language-bash">surfaceFeatureConvert -scale 0.001 edges_mm.eMesh edges_m.eMesh
</code></pre>
<p>毫米特征边转换为米，使其与已经缩放的表面一致。</p>
<h2>示例 4：读取无扩展名边文件</h2>
<pre><code class="language-bash">surfaceFeatureConvert -read-format eMesh featureData edges.obj
</code></pre>
<p>featureData实际为OpenFOAM边网格时显式指定格式。</p>
<h2>示例 5：指定输出格式并检查形状</h2>
<pre><code class="language-bash">surfaceFeatureConvert -write-format obj body.eMesh edgePreview
surfaceFeatureConvert -read-format obj edgePreview checked.eMesh
</code></pre>
<p>先输出无扩展名OBJ线，再读回eMesh；比较边数及坐标，检查格式转换是否保留连接。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Input geometry scaling factor The output format (default: use file extension)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceFeatureConvert [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input edge file
  &lt;output&gt;          The output edge file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
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
                    The input format (default: use file extension)
  -scale &lt;factor&gt;   Input geometry scaling factor
  -write-format &lt;type&gt;
                    The output format (default: use file extension)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert between edgeMesh formats

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceFeatureConvert/surfaceFeatureConvert.C">源码与说明</a> · <a href="/assets/command-help/surfacefeatureconvert.txt">帮助文本</a></p>
