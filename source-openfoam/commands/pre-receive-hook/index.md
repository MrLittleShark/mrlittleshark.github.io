---
title: "pre-receive-hook · 在 Git 接收提交时检查源码格式"
layout: reference
description: "在 Git 接收提交时检查源码格式。"
cms_slug: "command-pre-receive-hook"
---

<p>在 Git 接收提交时检查源码格式。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 此脚本用于服务端提交范围检查，标准输入每行是 oldCommit newCommit refName。下面只手动检查本地已有提交，不推送或修改远端。练习仓库须有至少三个提交；使用普通已有分支更新，避开该旧脚本对全零 SHA 新建/删除引用的兼容问题。</p>
<h2>示例 1：检查最近一次更新</h2>
<pre><code class="language-bash">printf '%s %s %s\n' "$(git rev-parse HEAD~1)" "$(git rev-parse HEAD)" refs/heads/main | "$WM_PROJECT_DIR/bin/tools/pre-receive-hook"
</code></pre>
<p>检查两个提交之间变更文件的制表符与行长。</p>
<h2>示例 2：检查累计两次提交</h2>
<pre><code class="language-bash">printf '%s %s %s\n' "$(git rev-parse HEAD~2)" "$(git rev-parse HEAD)" refs/heads/main | "$WM_PROJECT_DIR/bin/tools/pre-receive-hook"
</code></pre>
<p>扩大到两次提交的合并变化，适用于一次推送多个提交。</p>
<h2>示例 3：从已记录基线检查</h2>
<pre><code class="language-bash">baseCommit=$(git rev-parse HEAD~2)
targetCommit=$(git rev-parse HEAD)
printf '%s %s %s\n' "$baseCommit" "$targetCommit" refs/heads/review | "$WM_PROJECT_DIR/bin/tools/pre-receive-hook"
</code></pre>
<p>将提交 ID 保存为变量，可在审查记录中保留明确的起止点。</p>
<h2>示例 4：批量检查两次更新</h2>
<pre><code class="language-bash">printf '%s %s %s\n' "$(git rev-parse HEAD~2)" "$(git rev-parse HEAD~1)" refs/heads/reviewA "$(git rev-parse HEAD~1)" "$(git rev-parse HEAD)" refs/heads/reviewB | "$WM_PROJECT_DIR/bin/tools/pre-receive-hook"
</code></pre>
<p>标准输入给出两行，模拟一次接收多个引用更新，脚本逐行检查。</p>
<h2>示例 5：从保存的更新清单复查</h2>
<pre><code class="language-bash">printf '%s %s %s\n' "$(git rev-parse HEAD~1)" "$(git rev-parse HEAD)" refs/heads/main &gt; receive-check.txt
"$WM_PROJECT_DIR/bin/tools/pre-receive-hook" &lt; receive-check.txt
</code></pre>
<p>保存的清单使之后的检查指向同一提交范围，输出问题文件及行号。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/pre-receive-hook">源码与说明</a> · <a href="/assets/command-help/pre-receive-hook.txt">帮助文本</a></p>
