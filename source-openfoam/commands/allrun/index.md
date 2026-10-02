---
title: "Allrun · 算例提供的运行脚本，具体执行步骤由该文件定义"
layout: reference
description: "算例提供的运行脚本，具体执行步骤由该文件定义。"
cms_slug: "command-allrun"
---

<p>算例提供的运行脚本，具体执行步骤由该文件定义。</p><h2>开始前</h2>
<p>这里指 tutorials/Allrun 测试驱动。先将需要测试的教程树复制到个人目录 tutorial-suite，保留顶层 Allrun 和其脚本依赖；本工具可运行大量案例。单个案例的 Allrun 参数由其源码决定。</p>
<h2>示例 1：执行教程测试集</h2>
<pre><code class="language-bash">cd tutorial-suite
./Allrun
</code></pre>
<p>遍历教程并汇总结果为 testLoopReport。</p>
<h2>示例 2：执行测试模式</h2>
<pre><code class="language-bash">cd tutorial-suite
./Allrun -test
</code></pre>
<p>向教程脚本传入 -test，缩短或改变测试流程的方式由各脚本实现。</p>
<h2>示例 3：只收集已有日志</h2>
<pre><code class="language-bash">cd tutorial-suite
./Allrun -collect
</code></pre>
<p>适用于已完成或中断的测试，整理已有日志和报告。</p>
<h2>示例 4：运行但不收集日志</h2>
<pre><code class="language-bash">cd tutorial-suite
./Allrun -no-collect
</code></pre>
<p>执行测试流程，暂时跳过末尾汇总步骤。</p>
<h2>示例 5：先运行后统一汇总</h2>
<pre><code class="language-bash">cd tutorial-suite
./Allrun -no-collect -test
./Allrun -collect
</code></pre>
<p>将执行与日志汇总分开，便于在不同阶段检查结果。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-collect</code></td><td>Collect logs only. Can be useful for aborted runs.</td></tr><tr><td><code>-no-collect</code></td><td>Run without collecting logs</td></tr><tr><td><code>-test</code></td><td>Pass -test argument to scripts, end of option processing</td></tr><tr><td><code>--</code></td><td>End of option processing</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: Allrun [OPTION]
options:
  -collect          Collect logs only. Can be useful for aborted runs.
  -no-collect       Run without collecting logs
  -test             Pass -test argument to scripts, end of option processing
  --                End of option processing
  -help             print the usage

Run tutorial cases and summarize the outcome as &#x27;testLoopReport&#x27;</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/Allrun">源码与说明</a> · <a href="/assets/command-help/allrun.txt">帮助文本</a></p>
