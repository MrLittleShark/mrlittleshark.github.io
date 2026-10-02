---
title: "objToVTK · 把 OBJ 折线数据转换为 legacy VTK"
layout: reference
description: "把 OBJ 折线数据转换为 legacy VTK。"
cms_slug: "command-objtovtk"
---

<p>把 OBJ 折线数据转换为 legacy VTK。</p><h2>开始前</h2>
<p>OBJ 包含 v 顶点和 l 折线记录；两个位置参数依次是输入OBJ与输出VTK。</p>
<h2>示例 1：转换一条已有折线</h2>
<pre><code class="language-bash">objToVTK centreline.obj centreline.vtk
</code></pre>
<p>读取 centreline.obj 的顶点与线连接，生成可由 ParaView 打开的 legacy VTK 折线。</p>
<h2>示例 2：创建最小三点折线</h2>
<pre><code class="language-bash">printf 'v 0 0 0\nv 1 0 0\nv 1 1 0\nl 1 2 3\n' &gt; elbow-line.obj
objToVTK elbow-line.obj elbow-line.vtk
</code></pre>
<p>v 定义3个点，l 按1开始的编号连接折线；输出显示一个直角转弯，便于理解格式。</p>
<h2>示例 3：转换两条独立线段</h2>
<pre><code class="language-bash">printf 'v 0 0 0\nv 1 0 0\nv 0 1 0\nv 1 1 0\nl 1 2\nl 3 4\n' &gt; two-lines.obj
objToVTK two-lines.obj two-lines.vtk
</code></pre>
<p>两条 l 记录生成两条独立线段，适合保存不同采样线或几何辅助线。</p>
<h2>示例 4：整理多份几何输出</h2>
<pre><code class="language-bash">mkdir -p vtk-lines
for f in lines/*.obj; do
    objToVTK "$f" "vtk-lines/$(basename "${f%.obj}").vtk"
done
</code></pre>
<p>lines 目录中已有若干OBJ折线；逐个转换并保留基本文件名，输出集中到 vtk-lines。</p>
<h2>示例 5：查看周期匹配辅助线</h2>
<pre><code class="language-bash">createPatch -writeObj
for f in final_*_match.obj; do
    objToVTK "$f" "${f%.obj}.vtk"
done
</code></pre>
<p>createPatchDict 已配置 cyclic 配对，-writeObj 会生成 final_&lt;两侧patch名&gt;_match.obj。这些折线连接配对面中心；转换成 VTK 后可检查配对方向与距离。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: objToVTK [OPTIONS] &lt;obj-file&gt; &lt;vtk-file&gt;
Arguments:
  &lt;obj-file&gt;        The input obj line file
  &lt;vtk-file&gt;        The output vtk file
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
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Read obj line (not surface) file and convert into legacy VTK file

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/objToVTK/objToVTK.C">源码与说明</a> · <a href="/assets/command-help/objtovtk.txt">帮助文本</a></p>
