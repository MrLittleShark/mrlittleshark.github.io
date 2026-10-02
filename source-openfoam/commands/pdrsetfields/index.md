---
title: "PDRsetFields · 把几何障碍物转换成 PDRFoam 所需的等效阻塞场"
layout: reference
description: "把几何障碍物转换成 PDRFoam 所需的等效阻塞场。"
cms_slug: "command-pdrsetfields"
---

<p>把几何障碍物转换成 PDRFoam 所需的等效阻塞场。</p><h2>开始前</h2>
<p>已有PDR网格、障碍物输入和 system/PDRsetFieldsDict；几何尺度与网格单位一致。</p>
<h2>示例 1：先预览障碍物</h2>
<pre><code class="language-bash">PDRsetFields -dry-run
</code></pre>
<p>读取障碍物并写VTK预览，适合核对位置、尺寸和物体组，再生成阻塞场。</p>
<h2>示例 2：生成等效阻塞字段</h2>
<pre><code class="language-bash">PDRsetFields
</code></pre>
<p>按默认字典处理几何障碍物，计算对应网格上的等效阻塞影响，供PDRFoam使用。</p>
<h2>示例 3：使用另一障碍物方案</h2>
<pre><code class="language-bash">PDRsetFields -dict system/PDRsetFields-denseDict
</code></pre>
<p>替代字典描述更密集的障碍物布置；在案例副本中比较生成场的空间分布。</p>
<h2>示例 4：在指定时间初始化</h2>
<pre><code class="language-bash">PDRsetFields -time 0
</code></pre>
<p>明确把设置作用于0时刻，适合统一初始场目录的自动化流程。</p>
<h2>示例 5：读取旧式障碍物表</h2>
<pre><code class="language-bash">PDRsetFields -legacy -dict system/PDRsetFields-legacyDict -dry-run
</code></pre>
<p>输入确为legacy表时用-legacy强制该读取方式；先用VTK确认解析出的障碍物。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-dry-run</code></td><td>Read obstacles and write VTK only Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-legacy</code></td><td>Force use of legacy obstacles table</td></tr><tr><td><code>-time &lt;time&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: PDRsetFields [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative PDRsetFieldsDict
  -dry-run          Read obstacles and write VTK only
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -legacy           Force use of legacy obstacles table
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -time &lt;time&gt;      Specify a time
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Processes a set of geometrical obstructions to determine the equivalent
blockage effects when setting cases for PDRFoam

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/PDR/PDRsetFields/PDRsetFields.C">源码与说明</a> · <a href="/assets/command-help/pdrsetfields.txt">帮助文本</a></p>
