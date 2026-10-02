---
title: "foamCloneCase · 默认复制初始时刻、constant 和 system"
layout: reference
description: "默认复制初始时刻、constant 和 system。-latestTime 选择最后时刻，-force 覆盖目标目录。"
cms_slug: "command-foamclonecase"
---

<p>默认复制初始时刻、constant 和 system。-latestTime 选择最后时刻，-force 覆盖目标目录。</p><h2>用法</h2><pre><code class="language-bash">foamCloneCase ../cavity ./cavityCopy</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-force</td><td>Force overwrite of existing target</td></tr><tr><td>-l | -latestTime</td><td>Select the latest time directory</td></tr><tr><td>-h | -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCloneCase [OPTION] &lt;sourceCase&gt; &lt;targetCase&gt;
options:
  -force              Force overwrite of existing target
  -l | -latestTime    Select the latest time directory
  -h | -help          Print the usage

Create a new &lt;targetCase&gt; case directory with a copy of time, system, constant
directories from &lt;sourceCase&gt; directory.
The time directory is the first time directory by default.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCloneCase">源码与说明</a> · <a href="/assets/command-help/foamclonecase.txt">帮助文本</a></p>
