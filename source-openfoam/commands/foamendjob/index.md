---
title: "foamEndJob · 需启用 runTimeModifiable"
layout: reference
description: "需启用 runTimeModifiable。默认在下一写出时刻结束，-now 请求立即写出并结束；PID 使用实际进程号。"
cms_slug: "command-foamendjob"
---

<p>需启用 runTimeModifiable。默认在下一写出时刻结束，-now 请求立即写出并结束；PID 使用实际进程号。</p><h2>用法</h2><pre><code class="language-bash">foamEndJob -case . -now 12345</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-clear</td><td>clear any outstanding foamEndJob for the case</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-now</td><td>stop at next time step</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamEndJob [OPTION] &lt;pid&gt;
Usage: foamEndJob [OPTION] -c

options:
  -clear            clear any outstanding foamEndJob for the case
  -case &lt;dir&gt;       specify alternative case directory, default is the cwd
  -now              stop at next time step
  -help             print the usage

Tries to end running OpenFOAM application at next write (or optionally
at the next time step). It needs runTimeModifiable switched on in the
controlDict. It changes stopAt in the controlDict and waits for the
job to finish. Restores original controlDict if

    - job has finished
    - controlDict gets modified (by user)
    - foamEndJob gets killed.

The -clear option clears any outstanding foamEndJob for the case.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamEndJob">源码与说明</a> · <a href="/assets/command-help/foamendjob.txt">帮助文本</a></p>
