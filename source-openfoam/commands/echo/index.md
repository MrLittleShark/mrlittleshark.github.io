---
title: "echo · 显示环境变量或简单文本"
layout: reference
description: "显示环境变量或简单文本。"
cms_slug: "command-echo"
---

<p>显示环境变量或简单文本。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：查看版本</h2>
<pre><code class="language-bash">echo "$WM_PROJECT_VERSION"
</code></pre>
<p>当前已加载环境的版本字符串应为 v2512。</p>
<h2>示例 2：标明算例位置</h2>
<pre><code class="language-bash">caseDir="$PWD/caseA"
echo "Case: $caseDir"
</code></pre>
<p>将文字和变量组成一条路径提示。</p>
<h2>示例 3：写入单行条目</h2>
<pre><code class="language-bash">echo 'numberOfSubdomains 4;' &gt; decomposition-entry.txt
</code></pre>
<p>引号保护分号，输出为可放入字典的条目。</p>
<h2>示例 4：追加阶段标记</h2>
<pre><code class="language-bash">echo "mesh stage completed" &gt;&gt; workflow.log
</code></pre>
<blockquote>
<blockquote>
<p>保留已有内容并追加新行。</p>
</blockquote>
</blockquote>
<h2>示例 5：记录退出状态</h2>
<pre><code class="language-bash">checkMesh -case caseA &gt; check.log 2&gt;&amp;1
status=$?
echo "checkMesh exit: $status"
</code></pre>
<p>紧接运行保存 $?；具体网格质量从 check.log 阅读。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/bash/manual/">源码与说明</a></p>
