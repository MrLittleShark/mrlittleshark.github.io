---
title: "surfaceMeshImport · 导入对象为表面网格，-name 指定名称"
layout: reference
description: "导入对象为表面网格，-name 指定名称。"
cms_slug: "command-surfacemeshimport"
---

<p>导入对象为表面网格，-name 指定名称。</p><h2>用法</h2><pre><code class="language-bash">surfaceMeshImport body.stl</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">surfaceMeshImport body.stl -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-clean</td><td>Perform some surface checking/cleanup on the input surface Set named DebugSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-dict &lt;file&gt;</td><td>改用指定字典文件。</td></tr><tr><td>-from &lt;system&gt;</td><td>The source coordinate system, applied after &#x27;-read-scale&#x27; Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-name &lt;name&gt;</td><td>The surface name when writing (default is &#x27;default&#x27;)</td></tr><tr><td>-to &lt;system&gt;</td><td>The target coordinate system, applied before &#x27;-write-scale&#x27;</td></tr><tr><td>-verbose</td><td>Additional verbosity (can be used multiple times) Output geometry scaling factor</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceMeshImport [OPTIONS] &lt;surface&gt;
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
