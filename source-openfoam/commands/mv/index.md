---
title: "mv · 移动文件或目录，也可用于重命名"
layout: reference
description: "移动文件或目录，也可用于重命名。"
cms_slug: "command-mv"
---

<p>移动文件或目录，也可用于重命名。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：重命名日志</h2>
<pre><code class="language-bash">mv log.checkMesh mesh-quality.log
</code></pre>
<p>先在练习目录准备该日志。内容不变，文件名变化。</p>
<h2>示例 2：移动到归档目录</h2>
<pre><code class="language-bash">mkdir -p archive
mv mesh-quality.log archive/
</code></pre>
<p>日志移入 archive，原位置不再保留副本。</p>
<h2>示例 3：替换前确认</h2>
<pre><code class="language-bash">mv -i controlDict.new caseA/system/controlDict
</code></pre>
<p>controlDict.new 是修改后的文件；-i 在覆盖前请求确认。</p>
<h2>示例 4：给算例改名</h2>
<pre><code class="language-bash">mv caseB cavity-fine
</code></pre>
<p>目标不存在时对整个目录改名；内部写死的绝对路径需同步修改。</p>
<h2>示例 5：批量归档</h2>
<pre><code class="language-bash">mkdir -p old-logs
for f in log.*; do [ -f "$f" ] &amp;&amp; mv -i -- "$f" old-logs/; done
</code></pre>
<p>只处理匹配的普通文件；-- 结束选项解析，-i 保护同名目标。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
