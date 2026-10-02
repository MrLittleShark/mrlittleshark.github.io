---
title: "surfaceSplitNonManifolds · 拆分后使用 surfaceCheck 检查表面"
layout: reference
description: "拆分后使用 surfaceCheck 检查表面。"
cms_slug: "command-surfacesplitnonmanifolds"
---

<p>拆分后使用 surfaceCheck 检查表面。</p><h2>开始前</h2>
<p>输入存在多个面共享同一条边的非流形连接。工具通过复制点分开这类连接，输出应结合预期零件拓扑检查。</p>
<h2>示例 1：断开非流形连接</h2>
<pre><code class="language-bash">surfaceSplitNonManifolds junction.stl junction-split.stl
</code></pre>
<p>复制需要分离的连接点，使非流形连接按表面结构拆开。原始文件保留，输出用于后续网格处理。</p>
<h2>示例 2：定位处理的连接</h2>
<pre><code class="language-bash">surfaceSplitNonManifolds junction.stl junction-debug.stl -debug
</code></pre>
<p>启用工具自身的调试输出，查看处理非流形边的细节。适合普通运行后仍不清楚哪些连接被分开的情况。</p>
<h2>示例 3：对照拓扑统计</h2>
<pre><code class="language-bash">surfaceCheck junction.stl
surfaceSplitNonManifolds junction.stl split.stl
surfaceCheck split.stl
</code></pre>
<p>比较处理前后的非流形边和开放边数量。分开连接后可能形成独立开放边，需确认这与实体或薄片模型的要求一致。</p>
<h2>示例 4：按区域检查拆分结果</h2>
<pre><code class="language-bash">surfaceSplitNonManifolds assembly.stl split.stl
surfaceSplitByPatch split.stl
</code></pre>
<p>先断开异常共享连接，再逐区域导出检查。区域划分来自输入，第二步便于分别查看各部件的边界。</p>
<h2>示例 5：为后续方向整理准备表面</h2>
<pre><code class="language-bash">surfaceSplitNonManifolds closed-parts.stl split-parts.stl
surfaceOrient split-parts.stl '(10 10 10)' oriented-parts.stl
</code></pre>
<p>适用于分离后由多个闭合零件组成的输入；选取明确位于所有零件外部的点统一方向。随后检查各零件的闭合性和法向。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-debug</code></td><td>Add debugging output Set named DebugSwitch (default value: 1). [Can be used multiple times] Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceSplitNonManifolds [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;output&gt;          The output surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug            Add debugging output
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
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Split multiply connected surface edges by duplicating points

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitNonManifolds/surfaceSplitNonManifolds.C">源码与说明</a> · <a href="/assets/command-help/surfacesplitnonmanifolds.txt">帮助文本</a></p>
