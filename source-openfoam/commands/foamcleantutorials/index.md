---
title: "foamCleanTutorials · 按规则删除结果并执行相关 Allclean；存在 0.orig 时，默认清理过程可移除 0 目录"
layout: reference
description: "按规则删除结果并执行相关 Allclean；存在 0.orig 时，默认清理过程可移除 0 目录。"
cms_slug: "command-foamcleantutorials"
---

<p>按规则删除结果并执行相关 Allclean；存在 0.orig 时，默认清理过程可移除 0 目录。</p><h2>开始前</h2>
<p>加载 v2512 环境，使用个人算例副本 caseA。并行示例先配置 decomposeParDict 并完成 decomposePar，程序和字典须匹配。 将测试集完整复制到 tutorial-clean-demo，清理只对该副本进行。该工具递归运行已有 Allclean/Allwclean，否则调用 CleanFunctions。</p>
<h2>示例 1：按默认规则清理</h2>
<pre><code class="language-bash">foamCleanTutorials -case tutorial-clean-demo
</code></pre>
<p>默认 auto 模式在存在 0.orig 时移除 0，同时清理计算产物。</p>
<h2>示例 2：保留初始目录</h2>
<pre><code class="language-bash">foamCleanTutorials -no-auto -case tutorial-clean-demo
</code></pre>
<p>直接回退清理流程时保留 0；若子案例自带 Allclean，其具体动作由该脚本决定。</p>
<h2>示例 3：明确移除初始目录</h2>
<pre><code class="language-bash">foamCleanTutorials -0 -case tutorial-clean-demo
</code></pre>
<p>回退清理流程无条件移除 0，适合从 0.orig 重新建立初始场。</p>
<h2>示例 4：只处理测试集子目录</h2>
<pre><code class="language-bash">foamCleanTutorials -case tutorial-clean-demo/incompressible
</code></pre>
<p>限定递归范围，不处理测试集其他类别。</p>
<h2>示例 5：用于外层 Allclean</h2>
<pre><code class="language-bash">foamCleanTutorials -self -case tutorial-clean-demo
</code></pre>
<p>避免再次调用起点自己的 Allclean，防止脚本递归调用自身。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-0</code></td><td>Perform cleanCase, remove 0/ unconditionally</td></tr><tr><td><code>-auto</code></td><td>Perform cleanCase, remove 0/ if 0.orig/ exists [default]</td></tr><tr><td><code>-no-auto</code></td><td>Perform cleanCase only</td></tr><tr><td><code>-case=DIR</code></td><td>Specify starting directory, default is cwd</td></tr><tr><td><code>-self</code></td><td>Avoid Allclean script (prevent infinite recursion)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCleanTutorials [OPTION]
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
