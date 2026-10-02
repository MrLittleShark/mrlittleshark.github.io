---
title: "uapp · 切换到个人应用源码目录"
layout: reference
description: "切换到个人应用源码目录。"
cms_slug: "command-uapp"
---

<p>切换到个人应用源码目录。</p><h2>开始前</h2>
<p>这是 Bash alias。先加载 v2512 的 etc/bashrc，再在交互式终端逐行执行。脚本中可直接写 cd "$WM_PROJECT_USER_DIR/applications"；使用 alias 时须先启用 shopt -s expand_aliases 并分行解析。目录可用 mkdir -p "$WM_PROJECT_USER_DIR/applications" 预先建立。</p>
<h2>示例 1：进入个人应用目录</h2>
<pre><code class="language-bash">uapp
pwd
ls
</code></pre>
<p>快捷名称展开为 cd "$WM_PROJECT_USER_DIR/applications"，随后显示完整路径和一级内容。</p>
<h2>示例 2：建立分类目录</h2>
<pre><code class="language-bash">uapp
mkdir -p solvers
</code></pre>
<p>目录位于个人工作区，便于将相关源码或算例集中存放。</p>
<h2>示例 3：查找已有配置</h2>
<pre><code class="language-bash">uapp
find . -name Make -print
</code></pre>
<p>从该目录递归查找，输出相对路径，便于定位实际算例或编译单元。</p>
<h2>示例 4：建立第二组项目</h2>
<pre><code class="language-bash">uapp
mkdir -p utilities tests
</code></pre>
<p>建立独立子目录，可分别存放不同模型或测试程序；不会混在已有源码中。</p>
<h2>示例 5：返回原算例继续工作</h2>
<pre><code class="language-bash">uapp
find . -maxdepth 2 -type d
cd -
</code></pre>
<p>查看目录树后用 cd - 返回前一个工作目录，适合从算例跳到源码再返回。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
