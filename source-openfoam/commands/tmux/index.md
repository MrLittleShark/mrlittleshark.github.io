---
title: "tmux · 创建可分离终端会话；需安装 tmux"
layout: reference
description: "创建可分离终端会话；需安装 tmux。"
cms_slug: "command-tmux"
---

<p>创建可分离终端会话；需安装 tmux。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：新建会话</h2>
<pre><code class="language-bash">tmux new-session -s foam
</code></pre>
<p>进入 foam 会话，在其中加载环境并运行计算。</p>
<h2>示例 2：离开会话</h2>
<pre><code class="language-bash">tmux detach-client
</code></pre>
<p>在 tmux 内执行，返回外层终端，会话中的程序继续。</p>
<h2>示例 3：恢复会话</h2>
<pre><code class="language-bash">tmux attach-session -t foam
</code></pre>
<p>-t 指定会话名，恢复之前的终端。</p>
<h2>示例 4：新增日志窗口</h2>
<pre><code class="language-bash">tmux new-window -t foam -n logs 'tail -f "$HOME/foam-command-lab/caseA/log.icoFoam"'
</code></pre>
<p>已有 foam 会话中新增 logs 窗口，持续显示日志。</p>
<h2>示例 5：选择已有任务</h2>
<pre><code class="language-bash">tmux list-sessions
tmux attach-session -t foam
</code></pre>
<p>列出会话名称和窗口数量，再连接目标会话。</p>
<h2>参考</h2><p><a href="https://github.com/tmux/tmux/wiki">源码与说明</a></p>
