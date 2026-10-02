---
title: "tut · 切换到官方教程目录"
layout: reference
description: "切换到官方教程目录。"
cms_slug: "command-tut"
---

<p>切换到官方教程目录。</p><h2>开始前</h2>
<p>这是 Bash alias。先加载 v2512 的 etc/bashrc，再在交互式终端逐行执行。脚本中可直接写 cd "$FOAM_TUTORIALS"；使用 alias 时须先启用 shopt -s expand_aliases 并分行解析。</p>
<h2>示例 1：进入官方教程目录</h2>
<pre><code class="language-bash">tut
pwd
ls
</code></pre>
<p>快捷名称展开为 cd "$FOAM_TUTORIALS"，随后显示完整路径和一级内容。</p>
<h2>示例 2：浏览一个分类</h2>
<pre><code class="language-bash">tut
ls incompressible
</code></pre>
<p>列出 incompressible 下的文件，继续按应用或模型名称进入。</p>
<h2>示例 3：查找源码与配置</h2>
<pre><code class="language-bash">tut
find . -name controlDict -print
</code></pre>
<p>从该目录递归查找，输出相对路径，便于定位实际算例或编译单元。</p>
<h2>示例 4：比较两个分类</h2>
<pre><code class="language-bash">tut
ls -d compressible multiphase
</code></pre>
<p>列出两个类别的目录名，观察源码或教程的分类。</p>
<h2>示例 5：返回原算例继续工作</h2>
<pre><code class="language-bash">tut
find heatTransfer -maxdepth 2 -type d
cd -
</code></pre>
<p>查看目录树后用 cd - 返回前一个工作目录，适合从算例跳到源码再返回。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
