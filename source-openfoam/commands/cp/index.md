---
title: "cp · 复制文件或目录"
layout: reference
description: "复制文件或目录。"
cms_slug: "command-cp"
---

<p>复制文件或目录。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：备份控制字典</h2>
<pre><code class="language-bash">cp caseA/system/controlDict controlDict.before
</code></pre>
<p>得到独立副本，用于恢复或比较。</p>
<h2>示例 2：复制完整算例</h2>
<pre><code class="language-bash">cp -a caseA caseB
</code></pre>
<p>caseB 尚不存在时生成完整副本；-a 保留属性和符号链接。</p>
<h2>示例 3：覆盖前确认</h2>
<pre><code class="language-bash">cp -i controlDict.before caseA/system/controlDict
</code></pre>
<p>目标存在时逐项确认，输入 y 后才覆盖。</p>
<h2>示例 4：提取初始场</h2>
<pre><code class="language-bash">mkdir -p initial-fields
cp -a caseA/0/. initial-fields/
</code></pre>
<p>0/. 复制目录内容，包括隐藏项，目标保留初始场文件。</p>
<h2>示例 5：集中诊断日志</h2>
<pre><code class="language-bash">mkdir -p report-logs
cp caseA/log.blockMesh caseA/log.checkMesh report-logs/
</code></pre>
<p>最后一个参数是目标目录，复制两份日志用于分享。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
