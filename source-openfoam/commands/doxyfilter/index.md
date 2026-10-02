---
title: "doxyFilter · 为 Doxygen 过滤源码注释，控制求解器和工具程序文档的生成范围"
layout: reference
description: "为 Doxygen 过滤源码注释，控制求解器和工具程序文档的生成范围。"
cms_slug: "command-doxyfilter"
---

<p>为 Doxygen 过滤源码注释，控制求解器和工具程序文档的生成范围。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/doxyFilter&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: doxyFilter
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/doxyFilter

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

pass-through filter for doxygen Special treatment for applications/{solvers,utilities}/*.C - only keep the first comment block of the C source file use @cond / @endcond to suppress documenting all classes/variables Special treatment for applications/{solvers,utilities}/*.H - use @cond / @endcond to suppress documenting all classes/variables</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/doxyFilter">源码与说明</a> · <a href="/assets/command-help/doxyfilter.txt">帮助文本</a></p>
