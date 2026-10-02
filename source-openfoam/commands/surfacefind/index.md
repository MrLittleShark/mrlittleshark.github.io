---
title: "surfaceFind · 用于定位和检查表面坐标"
layout: reference
description: "用于定位和检查表面坐标。"
cms_slug: "command-surfacefind"
---

<p>用于定位和检查表面坐标。</p><h2>开始前</h2>
<p>给定表面文件和查询点；未指定的坐标分量为0。输出最近面、顶点等定位信息。</p>
<h2>示例 1：查询原点附近表面</h2>
<pre><code class="language-bash">surfaceFind body.stl
</code></pre>
<p>以(0,0,0)查询最近面与顶点，用于确认几何与坐标原点的位置关系。</p>
<h2>示例 2：定位入口中心附近</h2>
<pre><code class="language-bash">surfaceFind -x 0.1 body.stl
</code></pre>
<p>查询点为(0.1,0,0)，适合轴向沿x的管道入口或截面附近定位。</p>
<h2>示例 3：查询侧壁附近</h2>
<pre><code class="language-bash">surfaceFind -x 0.1 -y 0.025 body.stl
</code></pre>
<p>明确两个坐标分量，查询侧壁附近最近三角面，便于定位局部几何。</p>
<h2>示例 4：查询三维缺陷点</h2>
<pre><code class="language-bash">surfaceFind -x 0.1 -y 0.025 -z 0.01 body.stl
</code></pre>
<p>使用检查报告给出的三维坐标，找出对应面和顶点编号。</p>
<h2>示例 5：比较修补前后位置</h2>
<pre><code class="language-bash">surfaceFind -x 0.1 -y 0.025 -z 0.01 raw.stl
surfaceFind -x 0.1 -y 0.025 -z 0.01 repaired.stl
</code></pre>
<p>对同一个查询点比较两份表面，观察最近点距离及所在面是否随修补发生明显改变。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-x &lt;X&gt;</code></td><td>The point x-coordinate (if non-zero)</td></tr><tr><td><code>-y &lt;Y&gt;</code></td><td>The point y-coordinate (if non-zero)</td></tr><tr><td><code>-z &lt;Z&gt;</code></td><td>The point y-coordinate (if non-zero)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceFind [OPTIONS] &lt;input&gt;
Arguments:
  &lt;input&gt;           The input surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
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
  -x &lt;X&gt;            The point x-coordinate (if non-zero)
  -y &lt;Y&gt;            The point y-coordinate (if non-zero)
  -z &lt;Z&gt;            The point y-coordinate (if non-zero)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Find nearest face and vertex. Uses a zero origin unless otherwise specified

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceFind/surfaceFind.C">源码与说明</a> · <a href="/assets/command-help/surfacefind.txt">帮助文本</a></p>
