---
title: "mkdir · 创建工作目录"
layout: reference
description: "创建工作目录。"
cms_slug: "command-mkdir"
---

<p>创建工作目录。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：创建目录</h2>
<pre><code class="language-bash">mkdir study
</code></pre>
<p>生成空目录；同名目录存在时会报错。</p>
<h2>示例 2：生成算例骨架</h2>
<pre><code class="language-bash">mkdir -p case-new/{0,constant,system}
</code></pre>
<p>Bash 花括号展开为三条路径，-p 自动建立父目录。</p>
<h2>示例 3：分组存放结果</h2>
<pre><code class="language-bash">mkdir -p results/{coarse,medium,fine}
</code></pre>
<p>建立三个网格尺度的结果目录。</p>
<h2>示例 4：建立私人目录</h2>
<pre><code class="language-bash">mkdir -m 700 private-notes
</code></pre>
<p>700 赋予所有者读写和进入权限，其他用户没有访问权限。</p>
<h2>示例 5：建立参数扫描目录</h2>
<pre><code class="language-bash">for re in 100 400 1000; do mkdir -p "runs/Re-$re"; done
</code></pre>
<p>为三个雷诺数生成独立目录，以目录名区分参数。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
