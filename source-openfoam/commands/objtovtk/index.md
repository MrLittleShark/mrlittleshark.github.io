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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/objToVTK/objToVTK.C">源码与说明</a> · <a href="/assets/command-help/objtovtk.txt">帮助文本</a></p>
