---
title: "foamJob · 默认日志名为 log"
layout: reference
description: "默认日志名为 log。-parallel 启用 MPI，-screen 同时输出至终端，-wait 等待计算结束。"
cms_slug: "command-foamjob"
---

<p>默认日志名为 log。-parallel 启用 MPI，-screen 同时输出至终端，-wait 等待计算结束。</p><h2>开始前</h2>
<p>加载 v2512 环境，使用个人算例副本 caseA。并行示例先配置 decomposeParDict 并完成 decomposePar，程序和字典须匹配。</p>
<h2>示例 1：后台运行</h2>
<pre><code class="language-bash">foamJob -case caseA icoFoam
</code></pre>
<p>默认后台启动，输出写入 caseA/log。</p>
<h2>示例 2：等待任务完成</h2>
<pre><code class="language-bash">foamJob -wait -case caseA icoFoam
</code></pre>
<p>保持等待到进程结束，适合串联多个顺序任务。</p>
<h2>示例 3：同时查看屏幕输出</h2>
<pre><code class="language-bash">foamJob -screen -case caseA icoFoam
</code></pre>
<p>屏幕同步显示运行信息，并保留日志。</p>
<h2>示例 4：按程序名保存日志</h2>
<pre><code class="language-bash">foamJob -log-app -case caseA checkMesh
</code></pre>
<p>日志为 log.checkMesh，便于与求解日志区分。</p>
<h2>示例 5：指定日志并追加</h2>
<pre><code class="language-bash">foamJob -append -log=log.restart -case caseA icoFoam
</code></pre>
<p>追加至指定日志；续算时仍需正确设置 controlDict 的 startFrom。</p>
<h2>示例 6：并行运行</h2>
<pre><code class="language-bash">foamJob -parallel -case caseA icoFoam
</code></pre>
<p>通过 MPI 启动，读取算例分区设置，结果写入相应子域。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-screen</code></td><td>also send output to screen</td></tr><tr><td><code>-append</code></td><td>append to existing log file instead of overwriting it</td></tr><tr><td><code>-log=FILE</code></td><td>specify the log file</td></tr><tr><td><code>-log-app</code></td><td>Use log.{appName} for the log file</td></tr><tr><td><code>-no-check</code></td><td>run without fewer checks (eg, processor dirs etc)</td></tr><tr><td><code>-no-log</code></td><td>run without log file</td></tr><tr><td><code>-wait</code></td><td>wait for execution to complete (when not using -screen)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamJob [OPTION] &lt;application&gt; ...
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
