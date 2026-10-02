---
title: "doxyFilter · 为 Doxygen 过滤源码注释，控制求解器和工具程序文档的生成范围"
layout: reference
description: "为 Doxygen 过滤源码注释，控制求解器和工具程序文档的生成范围。"
cms_slug: "command-doxyfilter"
---

<p>为 Doxygen 过滤源码注释，控制求解器和工具程序文档的生成范围。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 输入为实际源码文件；输出是供 Doxygen 解析的过滤文本，保留原始源码。</p>
<h2>示例 1：过滤类声明</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/doxyFilter" "$WM_PROJECT_DIR/src/OpenFOAM/meshes/polyMesh/polyMesh.H" &gt; polyMesh.doxy
</code></pre>
<p>处理类文档标记并生成可供 Doxygen 读取的文本。</p>
<h2>示例 2：过滤求解器主文件</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/doxyFilter" "$WM_PROJECT_DIR/applications/solvers/incompressible/icoFoam/icoFoam.C" &gt; icoFoam.doxy
</code></pre>
<p>应用主文件主要保留首个文档块，内部代码通过文档条件标记抑制。</p>
<h2>示例 3：过滤应用包含文件</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/doxyFilter" "$WM_PROJECT_DIR/applications/solvers/incompressible/icoFoam/createFields.H" &gt; createFields.doxy
</code></pre>
<p>应用包含文件按文档工具规则处理，输出与主程序描述分开。</p>
<h2>示例 4：指向官方源码仓库</h2>
<pre><code class="language-bash">FOAM_ONLINE_REPO=https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512 "$WM_PROJECT_DIR/bin/tools/doxyFilter" "$WM_PROJECT_DIR/applications/solvers/incompressible/icoFoam/icoFoam.C" &gt; icoFoam-online.doxy
</code></pre>
<p>环境变量用于生成指向该仓库前缀的源码链接。</p>
<h2>示例 5：连接到 Doxygen 配置</h2>
<pre><code class="language-bash">printf 'INPUT_FILTER = "%s/bin/tools/doxyFilter"\n' "$WM_PROJECT_DIR" &gt; Doxyfile.filter
</code></pre>
<p>生成供 Doxyfile 合并使用的设置行；完整 Doxyfile 仍需指定 INPUT、输出目录等。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: doxyFilter
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/doxyFilter

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

pass-through filter for doxygen Special treatment for applications/{solvers,utilities}/*.C - only keep the first comment block of the C source file use @cond / @endcond to suppress documenting all classes/variables Special treatment for applications/{solvers,utilities}/*.H - use @cond / @endcond to suppress documenting all classes/variables</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/doxyFilter">源码与说明</a> · <a href="/assets/command-help/doxyfilter.txt">帮助文本</a></p>
