---
title: "foamListRegions · 可按 fluid、solid 等 regionType 筛选，-finite-area 选择有限"
layout: reference
description: "可按 fluid、solid 等 regionType 筛选，-finite-area 选择有限面积区域。"
cms_slug: "command-foamlistregions"
---

<p>可按 fluid、solid 等 regionType 筛选，-finite-area 选择有限面积区域。</p><h2>开始前</h2>
<p>体区域名称与分类来自 constant/regionProperties；有限面积区域来自 constant/finite-area/regionProperties。</p>
<h2>示例 1：列出全部体区域</h2>
<pre><code class="language-bash">foamListRegions
</code></pre>
<p>读取区域清单并输出各区域名，便于核对多区域目录。</p>
<h2>示例 2：只列流体区域</h2>
<pre><code class="language-bash">foamListRegions fluid
</code></pre>
<p>选择名为 fluid 的分类，输出其中的区域，例如 air、water；分类名称以字典实际内容为准。</p>
<h2>示例 3：只列固体区域</h2>
<pre><code class="language-bash">foamListRegions solid
</code></pre>
<p>输出 solid 分类下的 heater 等区域，可据此逐个检查固体材料设置。</p>
<h2>示例 4：读取有限面积区域</h2>
<pre><code class="language-bash">foamListRegions -finite-area
</code></pre>
<p>切换到有限面积区域清单，用于薄膜、壳体等面积网格的区域管理。</p>
<h2>示例 5：兼容单区域与多区域目录</h2>
<pre><code class="language-bash">foamListRegions -case ../candidateCase -optional -verbose
</code></pre>
<p>显式选择算例并显示读取细节；缺少 regionProperties 时允许继续，适合批量检查不同算例。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dry-run</code></td><td>Make reading optional and add verbosity Override the file handler type</td></tr><tr><td><code>-finite-area</code></td><td>List constant/finite-area/regionProperties (if available) Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-optional</code></td><td>A missing regionProperties is not treated as an error</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamListRegions [OPTIONS] [&lt;regionType ... regionType&gt;]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dry-run          Make reading optional and add verbosity
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -finite-area      List constant/finite-area/regionProperties (if available)
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -optional         A missing regionProperties is not treated as an error
  -verbose          Additional verbosity
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

List volume regions from constant/regionProperties,
or area regions from constant/finite-area/regionProperties

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamListRegions/foamListRegions.C">源码与说明</a> · <a href="/assets/command-help/foamlistregions.txt">帮助文本</a></p>
