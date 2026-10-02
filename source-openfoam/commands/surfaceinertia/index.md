---
title: "surfaceInertia · 按选项采用实体或薄壳模型，密度单位与几何长度单位保持一致"
layout: reference
description: "按选项采用实体或薄壳模型，密度单位与几何长度单位保持一致。"
cms_slug: "command-surfaceinertia"
---

<p>按选项采用实体或薄壳模型，密度单位与几何长度单位保持一致。</p><h2>用法</h2><pre><code class="language-bash">surfaceInertia body.stl -density 1000</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">surfaceInertia body.stl -density 1000 -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-shellProperties</td><td>Inertia of a thin shell</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceInertia [OPTIONS] &lt;input&gt;
Arguments:
  &lt;input&gt;           The input surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -density &lt;scalar&gt;
                    Specify density, kg/m3 for solid properties, kg/m2 for
                    shell properties
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
  -referencePoint &lt;vector&gt;
                    Inertia relative to this point, not the centre of mass
  -shellProperties  Inertia of a thin shell
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Calculates the inertia tensor and principal axes and moments of the specified
surface.
Inertia can either be of the solid body or of a thin shell.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceInertia/surfaceInertia.C">源码与说明</a> · <a href="/assets/command-help/surfaceinertia.txt">帮助文本</a></p>
