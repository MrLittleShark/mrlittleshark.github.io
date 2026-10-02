---
title: "wrmo · 清理指定源文件或当前目标的对象文件"
layout: reference
description: "清理指定源文件或当前目标的对象文件。"
cms_slug: "command-wrmo"
---

<p>清理指定源文件或当前目标的对象文件。</p><h2>开始前</h2>
<p>在个人源码副本中使用，删除目标文件会触发后续重编译，源码文件保留。</p>
<h2>示例 1：清除当前配置目标文件</h2>
<pre><code class="language-bash">cd myUtility
wrmo
</code></pre>
<p>删除当前构建配置的 .o 文件。</p>
<h2>示例 2：只重编译一个源文件</h2>
<pre><code class="language-bash">cd myUtility
wrmo myUtility.C
wmake
</code></pre>
<p>移除对应目标文件后重新构建。</p>
<h2>示例 3：处理两个实现文件</h2>
<pre><code class="language-bash">cd myLibrary
wrmo modelA.C modelB.C
</code></pre>
<p>两个编译单元将在下次 wmake 时重新编译。</p>
<h2>示例 4：分别清理双精度与单精度构建</h2>
<pre><code class="language-bash">cd myLibrary
(
    source "$WM_PROJECT_DIR/etc/bashrc" WM_PRECISION_OPTION=DP
    wrmo myModel.C
)
(
    source "$WM_PROJECT_DIR/etc/bashrc" WM_PRECISION_OPTION=SP
    wrmo myModel.C
)
</code></pre>
<p>适用于已经构建过 DP 和 SP 两种配置的个人库。每个子 shell 加载对应配置，删除该配置中 myModel.C 对应的目标文件；退出子 shell 后，当前终端的配置保持原样。</p>
<h2>示例 5：库改动后重新链接</h2>
<pre><code class="language-bash">cd myLibrary
wrmo myModel.C
wmake libso
</code></pre>
<p>重编译该源文件并链接共享库，适用于重新核查编译选项的影响。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-a | -all | all</code></td><td>All platforms (current: $WM_OPTIONS)</td></tr><tr><td><code>-h | -help</code></td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wrmo [OPTION] [file1 [... fileN]]

options:
  -a | -all | all   All platforms (current: $WM_OPTIONS)
  -h | -help        Print the usage

Remove all .o files or remove .o file corresponding to &lt;file&gt;</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wrmo">源码与说明</a> · <a href="/assets/command-help/wrmo.txt">帮助文本</a></p>
