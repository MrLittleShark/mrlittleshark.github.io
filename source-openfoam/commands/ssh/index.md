---
title: "ssh · 通过加密连接登录远程计算机并执行命令"
layout: reference
description: "通过加密连接登录远程计算机并执行命令。"
cms_slug: "command-ssh"
---

<p>通过加密连接登录远程计算机并执行命令。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：登录远端</h2>
<pre><code class="language-bash">ssh student@compute.example.org
</code></pre>
<p>替换为自己的用户名和主机；首次连接需核对主机指纹。</p>
<h2>示例 2：指定端口</h2>
<pre><code class="language-bash">ssh -p 2222 student@compute.example.org
</code></pre>
<p>-p 是远端 SSH 服务端口。</p>
<h2>示例 3：指定密钥</h2>
<pre><code class="language-bash">ssh -i "$HOME/.ssh/id_ed25519" student@compute.example.org
</code></pre>
<p>-i 选择本机私钥，私钥文件留在本机。</p>
<h2>示例 4：远程检查空间</h2>
<pre><code class="language-bash">ssh student@compute.example.org 'df -h "$HOME"'
</code></pre>
<p>单引号让 $HOME 在远端展开，结果返回本地终端。</p>
<h2>示例 5：远程加载计算环境</h2>
<pre><code class="language-bash">ssh student@compute.example.org 'bash -lc "source /usr/lib/openfoam/openfoam2512/etc/bashrc &amp;&amp; foamInstallationTest"'
</code></pre>
<p>显式加载远端环境后运行安装检查，路径按服务器实际安装位置调整。</p>
<h2>参考</h2><p><a href="https://www.openssh.com/manual.html">源码与说明</a></p>
