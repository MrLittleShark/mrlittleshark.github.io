---
title: "wrmdep · 清理指定源文件或当前目标的依赖文件"
layout: reference
description: "清理指定源文件或当前目标的依赖文件。"
cms_slug: "command-wrmdep"
---

<p>清理指定源文件或当前目标的依赖文件。</p><h2>开始前</h2>
<p>在个人源码副本中使用，清除依赖缓存后 wmake 会重新生成。跨精度配置的示例要求个人库已经分别构建过 DP 和 SP 版本。</p>
<h2>示例 1：清除当前配置依赖</h2>
<pre><code class="language-bash">cd myUtility
wrmdep
</code></pre>
<p>移除当前配置的 .dep 文件。</p>
<h2>示例 2：只针对一个头文件</h2>
<pre><code class="language-bash">cd myLibrary
wrmdep myModel.H
</code></pre>
<p>移除引用该文件的依赖记录，让相关编译单元重新分析。</p>
<h2>示例 3：针对多个变动文件</h2>
<pre><code class="language-bash">cd myLibrary
wrmdep modelA.H modelB.H
</code></pre>
<p>处理依赖两项输入的缓存。</p>
<h2>示例 4：分别更新两种精度的依赖记录</h2>
<pre><code class="language-bash">cd myLibrary
(
    source "$WM_PROJECT_DIR/etc/bashrc" WM_PRECISION_OPTION=DP
    wrmdep myModel.H
)
(
    source "$WM_PROJECT_DIR/etc/bashrc" WM_PRECISION_OPTION=SP
    wrmdep myModel.H
)
</code></pre>
<p>两次命令分别在 DP、SP 的构建目录中查找引用 myModel.H 的 .dep 文件并删除。终端列出删除的依赖文件路径；随后在各自配置下执行 wmake，即可重新分析头文件依赖。</p>
<h2>示例 5：清理移动源码留下的依赖</h2>
<pre><code class="language-bash">wrmdep -old myUtility
</code></pre>
<p>查找没有对应源文件的依赖项；用于源码搬迁后的整理。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wrmdep">源码与说明</a> · <a href="/assets/command-help/wrmdep.txt">帮助文本</a></p>
