---
title: "foamHasLibrary · -detail 输出详细信息"
layout: reference
description: "-detail 输出详细信息。"
cms_slug: "command-foamhaslibrary"
---

<p>-detail 输出详细信息。</p><h2>开始前</h2>
<p>共享库位于当前 OpenFOAM 或用户库搜索路径。工具用退出状态表示装载是否成功，适合编译后的依赖检查。</p>
<h2>示例 1：检查有限体积库</h2>
<pre><code class="language-bash">foamHasLibrary libfiniteVolume.so
</code></pre>
<p>尝试装载有限体积库；成功退出表示当前环境能够找到并加载它。</p>
<h2>示例 2：同时检查两个依赖</h2>
<pre><code class="language-bash">foamHasLibrary libfiniteVolume.so libmeshTools.so
</code></pre>
<p>默认要求两个库都能加载，适合检查依赖有限体积与网格工具的自定义程序。</p>
<h2>示例 3：显示加载细节</h2>
<pre><code class="language-bash">foamHasLibrary -detail -verbose libsampling.so
</code></pre>
<p>查看采样库的详细装载信息，帮助定位库文件或其依赖缺失。</p>
<h2>示例 4：检查任一候选实现</h2>
<pre><code class="language-bash">foamHasLibrary -or libcustomModelA.so libcustomModelB.so
</code></pre>
<p>已编译两个候选插件时，任一个可加载即可成功；两个名称都仍会检查。</p>
<h2>示例 5：在运行前验证自定义边界库</h2>
<pre><code class="language-bash">if foamHasLibrary libfoamLabPulsedInlet.so; then icoFoam; fi
</code></pre>
<p>在已配置该边界的算例中，仅在库加载成功后启动求解器。该检查关注装载，边界参数由求解器继续读取。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-detail</code></td><td>Additional detail Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-or</code></td><td>Success if any of the libraries can be loaded (does not short-circuit)</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamHasLibrary [OPTIONS] [&lt;lib...&gt;]
Options:
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -detail           Additional detail
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -or               Success if any of the libraries can be loaded
                    (does not short-circuit)
  -verbose          Additional verbosity (can be used multiple times)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Test if given libraries can be loaded

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamHasLibrary/foamHasLibrary.C">源码与说明</a> · <a href="/assets/command-help/foamhaslibrary.txt">帮助文本</a></p>
