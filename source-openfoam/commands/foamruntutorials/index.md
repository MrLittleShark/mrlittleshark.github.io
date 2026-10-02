---
title: "foamRunTutorials · 执行目标目录中的 Allrun 或 Alltest"
layout: reference
description: "执行目标目录中的 Allrun 或 Alltest。-dry-run 列出待执行脚本。"
cms_slug: "command-foamruntutorials"
---

<p>执行目标目录中的 Allrun 或 Alltest。-dry-run 列出待执行脚本。</p><h2>用法</h2><pre><code class="language-bash">foamRunTutorials -dry-run -case ./cases</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case=DIR</td><td>Specify starting directory, default is cwd</td></tr><tr><td>-serial</td><td>Prefer Allrun-serial if available</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-test</td><td>Prefer Alltest script, pass -test argument to scripts</td></tr><tr><td>-dry-run</td><td>Only report which script to run</td></tr><tr><td>-self</td><td>Avoid initial Allrun / Alltest scripts (prevent infinite recursion)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamRunTutorials [OPTION]
options:
  -case=DIR     Specify starting directory, default is cwd
  -serial       Prefer Allrun-serial if available
  -parallel     Prefer Allrun-parallel if available
  -test         Prefer Alltest script, pass -test argument to scripts
  -dry-run      Only report which script to run
  -self         Avoid initial Allrun / Alltest scripts
                (prevent infinite recursion)
  -help         Print the usage

Recursively run Alltest / Allrun / Allrun-parallel / Allrun-serial
(or simply blockMesh + application)
starting from the current directory or the specified -case directory.

Equivalent options:
  | -case=DIR  | -case DIR |</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamRunTutorials">源码与说明</a> · <a href="/assets/command-help/foamruntutorials.txt">帮助文本</a></p>
