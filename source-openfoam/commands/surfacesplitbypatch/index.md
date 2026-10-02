---
title: "surfaceSplitByPatch · -patches 指定待拆分区域"
layout: reference
description: "-patches 指定待拆分区域。"
cms_slug: "command-surfacesplitbypatch"
---

<p>-patches 指定待拆分区域。</p><h2>开始前</h2>
<p>准备带多个表面区域的 STL、OBJ 等文件；先检查区域名称，再设置选取列表。</p>
<h2>示例 1：按全部区域拆分</h2>
<pre><code class="language-bash">surfaceSplitByPatch assembly.stl
</code></pre>
<p>为各表面区域写出独立文件，终端显示实际输出文件名。适合将装配体的入口、出口和壁面分开处理。</p>
<h2>示例 2：仅导出指定区域</h2>
<pre><code class="language-bash">surfaceSplitByPatch assembly.stl -patches '(inlet outlet)'
</code></pre>
<p>只为 inlet 和 outlet 写出文件，保留原区域内的三角面。可单独检查端面位置和封口情况。</p>
<h2>示例 3：使用名称模式选取</h2>
<pre><code class="language-bash">surfaceSplitByPatch assembly.obj -patches '("blade.*")'
</code></pre>
<p>匹配 blade 开头的区域，分别导出各叶片。正则表达式应放在列表中并加引号。</p>
<h2>示例 4：排除辅助区域</h2>
<pre><code class="language-bash">surfaceSplitByPatch assembly.stl -exclude-patches '(construction capTemporary)'
</code></pre>
<p>拆分其余区域，同时跳过施工辅助面和临时封口。适合整理准备交给其他软件的几何文件。</p>
<h2>示例 5：组合选取和排除</h2>
<pre><code class="language-bash">surfaceSplitByPatch assembly.stl -patches '("wall.*")' -exclude-patches '(wallTemporary)'
</code></pre>
<p>导出 wall 开头的目标表面并排除临时壁面。对生成文件逐个运行 surfaceCheck，可单独定位某一区域的开放边。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceSplitByPatch [OPTIONS] &lt;input&gt;
Arguments:
  &lt;input&gt;           The input surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -exclude-patches &lt;wordRes&gt;
                    Exclude single or multiple patches (name or regex) from
                    extracting.
                    Eg, &#x27;outlet&#x27; or &#x27;( inlet &quot;.*Wall&quot; )&#x27;
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
  -patches &lt;wordRes&gt;
                    Specify single patch or multiple patches to extract
                    Eg, &#x27;top&#x27; or &#x27;( front &quot;.*back&quot; )&#x27;
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Write surface mesh regions to separate files

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitByPatch/surfaceSplitByPatch.C">源码与说明</a> · <a href="/assets/command-help/surfacesplitbypatch.txt">帮助文本</a></p>
