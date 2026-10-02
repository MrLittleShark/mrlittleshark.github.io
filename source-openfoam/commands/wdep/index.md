---
title: "wdep · 定位源文件对应的 .dep 依赖文件"
layout: reference
description: "定位源文件对应的 .dep 依赖文件。"
cms_slug: "command-wdep"
---

<p>定位源文件对应的 .dep 依赖文件。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/wdep&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wdep &lt;file&gt;

Find the dep-file corresponding to &lt;file&gt; in the current directory
and print the path.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wdep">源码与说明</a> · <a href="/assets/command-help/wdep.txt">帮助文本</a></p>
