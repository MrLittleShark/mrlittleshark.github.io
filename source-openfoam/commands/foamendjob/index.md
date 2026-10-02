---
title: "foamEndJob · 需启用 runTimeModifiable"
layout: reference
description: "需启用 runTimeModifiable。默认在下一写出时刻结束，-now 请求立即写出并结束；PID 使用实际进程号。"
cms_slug: "command-foamendjob"
---

<p>需启用 runTimeModifiable。默认在下一写出时刻结束，-now 请求立即写出并结束；PID 使用实际进程号。</p><h2>开始前</h2>
<p>加载 v2512 环境，使用个人算例副本 caseA。并行示例先配置 decomposeParDict 并完成 decomposePar，程序和字典须匹配。 只对自己的正在运行的进程使用。solverPid 为求解器 PID；controlDict 须有 runTimeModifiable true，以及 startTime/stopAt/writeControl/writeInterval/endTime 的普通条目。</p>
<h2>示例 1：在下一次正常写出后结束</h2>
<pre><code class="language-bash">foamEndJob -case caseA "$solverPid"
</code></pre>
<p>将 stopAt 改为 nextWrite，等待目标进程结束后恢复控制字典。</p>
<h2>示例 2：在下一时间步写出并结束</h2>
<pre><code class="language-bash">foamEndJob -now -case caseA "$solverPid"
</code></pre>
<p>将 writeControl 改为 timeStep、writeInterval 改为 1，并设置 nextWrite，以便下一步写出后结束。</p>
<h2>示例 3：从算例内部操作</h2>
<pre><code class="language-bash">cd caseA
foamEndJob "$solverPid"
</code></pre>
<p>省略 -case 使用当前目录；PID 必须属于此算例。</p>
<h2>示例 4：读取自己保存的 PID</h2>
<pre><code class="language-bash">solverPid=$(cat caseA/solver.pid)
ps -p "$solverPid" -o pid,args
foamEndJob -case caseA "$solverPid"
</code></pre>
<p>先显示 PID 对应命令确认算例，再请求写出后结束。</p>
<h2>示例 5：撤销等待结束请求</h2>
<pre><code class="language-bash">foamEndJob -clear -case caseA
</code></pre>
<p>清理该算例已有的 foamEndJob 等待状态；用于取消此前请求，字典恢复行为由脚本备份状态决定。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-clear</code></td><td>清除该算例尚未执行的 foamEndJob 停止请求。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；默认使用当前目录。</td></tr><tr><td><code>-now</code></td><td>在下一个时间步停止计算。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamEndJob">源码与说明</a> · <a href="/assets/command-help/foamendjob.txt">帮助文本</a></p>
