---
title: "surfaceHookUp · 连接规则和输入表面由相应字典指定"
layout: reference
description: "连接规则和输入表面由相应字典指定。"
cms_slug: "command-surfacehookup"
---

<p>连接规则和输入表面由相应字典指定。</p><h2>开始前</h2>
<p>system/surfaceHookUpDict逐项列出待连接表面及type triSurfaceMesh，文件位于constant/triSurface；容差与几何长度单位一致。</p>
<h2>示例 1：连接微小间隙</h2>
<pre><code class="language-bash">surfaceHookUp 1e-5
</code></pre>
<p>用10μm连接容差移动并重三角化邻近边界，生成hookedSurface_前缀的新表面。</p>
<h2>示例 2：比较更严格容差</h2>
<pre><code class="language-bash">surfaceHookUp 1e-6
</code></pre>
<p>在相同原始几何副本中采用1μm容差，只处理更近的边界，比较仍未连接的缝隙。</p>
<h2>示例 3：限制处理轮数</h2>
<pre><code class="language-bash">surfaceHookUp -maxIters 20 1e-5
</code></pre>
<p>把最大迭代次数设为20，观察一小段连接过程的进展与剩余间隙。</p>
<h2>示例 4：选择另一组连接面</h2>
<pre><code class="language-bash">surfaceHookUp -dict system/surfaceHookUpDict.inlet 1e-5
</code></pre>
<p>完整inlet字典只列需要连接的入口相关表面，缩小本次处理范围。</p>
<h2>示例 5：检查连接后的表面</h2>
<pre><code class="language-bash">surfaceHookUp 1e-5
surfaceCheck constant/triSurface/hookedSurface_surface1.stl
</code></pre>
<p>字典包含surface1.stl时检查其新文件，核对开边、交叉及区域，确认连接是否达到预期。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceHookUp [OPTIONS] &lt;hookTolerance&gt;
Arguments:
  &lt;hookTolerance&gt;   The point merge tolerance
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative surfaceHookUpDict
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -maxIters &lt;number&gt;
                    Maximum number of iterations (default: 100)
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

Hook surfaces to other surfaces by moving and retriangulating their boundary
edges to match other surface boundary edges

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceHookUp/surfaceHookUp.C">源码与说明</a> · <a href="/assets/command-help/surfacehookup.txt">帮助文本</a></p>
