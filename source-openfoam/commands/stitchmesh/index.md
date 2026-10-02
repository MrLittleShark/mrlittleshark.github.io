---
title: "stitchMesh · 把几何上可配对的两侧边界缝合为内部面"
layout: reference
description: "把几何上可配对的两侧边界缝合为内部面。"
cms_slug: "command-stitchmesh"
---

<p>把几何上可配对的两侧边界缝合为内部面。</p><h2>开始前</h2>
<p>同一网格中已有待拼接的 master、slave patch；其重叠关系决定 perfect、integral 或 partial 方式。</p>
<h2>示例 1：缝合完全吻合的面</h2>
<pre><code class="language-bash">stitchMesh -perfect interfaceA interfaceB -overwrite
</code></pre>
<p>两侧顶点和面分割完全一致时使用-perfect，写回网格并把接口改成内部面。</p>
<h2>示例 2：缝合完整覆盖但分割不同的接口</h2>
<pre><code class="language-bash">stitchMesh -integral interfaceA interfaceB -overwrite
</code></pre>
<p>两侧整体覆盖一致但面划分不同，用-integral进行完整接口耦合。</p>
<h2>示例 3：处理局部重叠</h2>
<pre><code class="language-bash">stitchMesh -partial masterPatch slavePatch -overwrite
</code></pre>
<p>只缝合两侧几何重叠部分，适合覆盖范围不完全一致的网格接口。</p>
<h2>示例 4：根据字典处理多组接口</h2>
<pre><code class="language-bash">stitchMesh -dict system/stitchMeshDict -overwrite
</code></pre>
<p>字典已列出接口操作时省略位置参数，按文件中的操作顺序完成多组缝合。</p>
<h2>示例 5：查看拼接中间阶段</h2>
<pre><code class="language-bash">stitchMesh -integral interfaceA interfaceB -intermediate -toleranceDict system/stitchTolerances
</code></pre>
<p>已有容差字典时，采用指定几何容差并保存中间阶段网格，便于定位小缝隙或错配面。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-integral</code></td><td>Couple integral master/slave patches (2 argument mode: default)</td></tr><tr><td><code>-intermediate</code></td><td>Write intermediate stages, not just the final result</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-partial</code></td><td>Couple partially overlapping master/slave patches (2 argument mode)</td></tr><tr><td><code>-perfect</code></td><td>Couple perfectly aligned master/slave patches (2 argument mode)</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/stitchMesh/simple-cube1">mesh/stitchMesh/simple-cube1</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: stitchMesh [OPTIONS] [&lt;master&gt; &lt;slave&gt;]
Arguments:
  &lt;master&gt;          The master patch name (non-dictionary mode)
  &lt;slave&gt;           The slave patch name (non-dictionary mode)
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative stitchMeshDict
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -integral         Couple integral master/slave patches (2 argument mode:
                    default)
  -intermediate     Write intermediate stages, not just the final result
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -partial          Couple partially overlapping master/slave patches (2
                    argument mode)
  -perfect          Couple perfectly aligned master/slave patches (2 argument
                    mode)
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -toleranceDict &lt;file&gt;
                    Dictionary file with tolerances
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Merge the faces on specified patches (if geometrically possible) so that the
faces become internal.
This utility can be called without arguments (uses stitchMeshDict) or with
two arguments (master/slave patch names).

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/stitchMesh/stitchMesh.C">源码与说明</a> · <a href="/assets/command-help/stitchmesh.txt">帮助文本</a></p>
