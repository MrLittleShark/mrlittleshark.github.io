---
title: "less · 分页阅读配置与日志"
layout: reference
description: "分页阅读配置与日志。"
cms_slug: "command-less"
---

<p>分页阅读配置与日志。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：翻阅日志</h2>
<pre><code class="language-bash">less caseA/log.icoFoam
</code></pre>
<p>空格下一屏、b 上一屏、q 退出。</p>
<h2>示例 2：显示字典行号</h2>
<pre><code class="language-bash">less -N caseA/system/blockMeshDict
</code></pre>
<p>-N 显示行号；输入 120g 跳至第 120 行。</p>
<h2>示例 3：从匹配位置打开</h2>
<pre><code class="language-bash">less +/FOAM caseA/log.icoFoam
</code></pre>
<p>+/FOAM 指定初始搜索；随后 /FATAL 搜索错误，n 查下一处。</p>
<h2>示例 4：持续跟踪日志</h2>
<pre><code class="language-bash">less +F caseA/log.icoFoam
</code></pre>
<p>等待新增内容，Ctrl+C 暂停跟踪后可向上翻阅。</p>
<h2>示例 5：阅读彩色差异</h2>
<pre><code class="language-bash">git diff --color=always -- caseA/system/fvSchemes | less -R
</code></pre>
<p>在 Git 项目中执行；-R 保留颜色，突出设置变化。</p>
<h2>参考</h2><p><a href="https://www.greenwoodsoftware.com/less/">源码与说明</a></p>
