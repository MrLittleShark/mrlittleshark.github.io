---
title: "Allrun · 算例提供的运行脚本，具体执行步骤由该文件定义"
layout: reference
description: "算例提供的运行脚本，具体执行步骤由该文件定义。"
cms_slug: "command-allrun"
---

<p>算例提供的运行脚本，具体执行步骤由该文件定义。</p><h2>用法</h2><pre><code class="language-bash">./Allrun</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-collect</td><td>Collect logs only. Can be useful for aborted runs.</td></tr><tr><td>-no-collect</td><td>Run without collecting logs</td></tr><tr><td>-test</td><td>Pass -test argument to scripts, end of option processing</td></tr><tr><td>--</td><td>End of option processing</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: Allrun [OPTION]
options:
  -collect          Collect logs only. Can be useful for aborted runs.
  -no-collect       Run without collecting logs
  -test             Pass -test argument to scripts, end of option processing
  --                End of option processing
  -help             print the usage

Run tutorial cases and summarize the outcome as &#x27;testLoopReport&#x27;</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/Allrun">源码与说明</a> · <a href="/assets/command-help/allrun.txt">帮助文本</a></p>
