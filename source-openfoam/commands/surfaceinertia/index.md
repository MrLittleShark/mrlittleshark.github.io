---
title: "surfaceInertia · 按选项采用实体或薄壳模型，密度单位与几何长度单位保持一致"
layout: reference
description: "按选项采用实体或薄壳模型，密度单位与几何长度单位保持一致。"
cms_slug: "command-surfaceinertia"
---

<p>按选项采用实体或薄壳模型，密度单位与几何长度单位保持一致。</p><h2>开始前</h2>
<p>实体惯量使用闭合且法向一致的表面；薄壳模式使用面密度。几何坐标按米准备。</p>
<h2>示例 1：计算单位密度实体惯量</h2>
<pre><code class="language-bash">surfaceInertia body.stl
</code></pre>
<p>根据闭合几何计算体积、质心、惯量张量和主惯量，默认单位密度便于检查几何贡献。</p>
<h2>示例 2：指定钢材密度</h2>
<pre><code class="language-bash">surfaceInertia -density 7850 body.stl
</code></pre>
<p>将实体密度设为7850kg/m³，质量与惯量随密度按比例改变。</p>
<h2>示例 3：计算铝材对照</h2>
<pre><code class="language-bash">surfaceInertia -density 2700 body.stl
</code></pre>
<p>保持几何不变改用2700kg/m³，质心位置不变，质量和惯量降低。</p>
<h2>示例 4：计算薄壳惯量</h2>
<pre><code class="language-bash">surfaceInertia -shellProperties -density 2 shell.stl
</code></pre>
<p>用2kg/m²的面密度计算壳体性质，适合已知厚度乘材料密度得到的面质量。</p>
<h2>示例 5：改用安装点作为参考</h2>
<pre><code class="language-bash">surfaceInertia -density 7850 -referencePoint '(0 0 0)' body.stl
</code></pre>
<p>输出相对于原点的惯量，用于与刚体运动中指定参考点的惯量配置对应。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-shellProperties</code></td><td>Inertia of a thin shell</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceInertia [OPTIONS] &lt;input&gt;
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
