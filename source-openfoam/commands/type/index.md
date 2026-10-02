---
title: "type · 识别命令是别名、函数还是程序文件"
layout: reference
description: "识别命令是别名、函数还是程序文件。"
cms_slug: "command-type"
---

<p>识别命令是别名、函数还是程序文件。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：识别快捷目录</h2>
<pre><code class="language-bash">type tut
</code></pre>
<p>显示 tut 是 alias 及其展开内容。</p>
<h2>示例 2：识别运行函数</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
type runApplication
</code></pre>
<p>输出函数定义，可观察日志生成规则。</p>
<h2>示例 3：寻找所有同名程序</h2>
<pre><code class="language-bash">type -a blockMesh
</code></pre>
<p>检查 PATH 中多个安装目录的优先级。</p>
<h2>示例 4：仅输出类别</h2>
<pre><code class="language-bash">type -t source
type -t blockMesh
</code></pre>
<p>通常分别得到 builtin 和 file。</p>
<h2>示例 5：强制搜索外部程序</h2>
<pre><code class="language-bash">type -P cp
</code></pre>
<p>按 PATH 返回可执行文件路径，即使存在同名函数。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/bash/manual/">源码与说明</a></p>
