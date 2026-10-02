---
title: "foamCleanTutorials · 按规则删除结果并执行相关 Allclean；存在 0.orig 时，默认清理过程可移除 0 目录"
layout: reference
description: "按规则删除结果并执行相关 Allclean；存在 0.orig 时，默认清理过程可移除 0 目录。"
cms_slug: "command-foamcleantutorials"
---

<p>按规则删除结果并执行相关 Allclean；存在 0.orig 时，默认清理过程可移除 0 目录。</p><h2>用法</h2><pre><code class="language-bash">foamCleanTutorials -case ./caseCopy</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-0</td><td>Perform cleanCase, remove 0/ unconditionally</td></tr><tr><td>-auto</td><td>Perform cleanCase, remove 0/ if 0.orig/ exists [default]</td></tr><tr><td>-no-auto</td><td>Perform cleanCase only</td></tr><tr><td>-case=DIR</td><td>Specify starting directory, default is cwd</td></tr><tr><td>-self</td><td>Avoid Allclean script (prevent infinite recursion)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCleanTutorials [OPTION]
       foamCleanTutorials [OPTION] directory
options:
  -0            Perform cleanCase, remove 0/ unconditionally
  -auto         Perform cleanCase, remove 0/ if 0.orig/ exists [default]
  -no-auto      Perform cleanCase only
  -case=DIR     Specify starting directory, default is cwd
  -self         Avoid Allclean script (prevent infinite recursion)
  -help         Print the usage

Recursively clean an OpenFOAM case directory, using Allclean or Allwclean
when present.

In the default &#x27;auto&#x27; mode, it will use cleanCase and will automatically
remove the 0/ directory if a corresponding 0.orig directory exists.

Equivalent options:
  | -case=DIR  | -case DIR |</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanTutorials">源码与说明</a> · <a href="/assets/command-help/foamcleantutorials.txt">帮助文本</a></p>
