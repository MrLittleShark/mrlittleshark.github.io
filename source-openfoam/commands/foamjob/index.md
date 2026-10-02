---
title: "foamJob · 默认日志名为 log"
layout: reference
description: "默认日志名为 log。-parallel 启用 MPI，-screen 同时输出至终端，-wait 等待计算结束。"
cms_slug: "command-foamjob"
---

<p>默认日志名为 log。-parallel 启用 MPI，-screen 同时输出至终端，-wait 等待计算结束。</p><h2>用法</h2><pre><code class="language-bash">foamJob -log-app simpleFoam</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">foamJob -log-app simpleFoam -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-screen</td><td>also send output to screen</td></tr><tr><td>-append</td><td>append to existing log file instead of overwriting it</td></tr><tr><td>-log=FILE</td><td>specify the log file</td></tr><tr><td>-log-app</td><td>Use log.{appName} for the log file</td></tr><tr><td>-no-check</td><td>run without fewer checks (eg, processor dirs etc)</td></tr><tr><td>-no-log</td><td>run without log file</td></tr><tr><td>-wait</td><td>wait for execution to complete (when not using -screen)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamJob [OPTION] &lt;application&gt; ...
options:
  -case &lt;dir&gt;       specify alternative case directory, default is the cwd
  -parallel         run in parallel (with mpirun)
  -screen           also send output to screen
  -append           append to existing log file instead of overwriting it
  -log=FILE         specify the log file
  -log-app          Use log.{appName} for the log file
  -no-check         run without fewer checks (eg, processor dirs etc)
  -no-log           run without log file
  -wait             wait for execution to complete (when not using -screen)
  -help             print the usage

Run an OpenFOAM job in background, redirecting output to a &#x27;log&#x27; file
in the case directory</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamJob">源码与说明</a> · <a href="/assets/command-help/foamjob.txt">帮助文本</a></p>
