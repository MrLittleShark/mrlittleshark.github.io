---
title: "wrmo · 清理指定源文件或当前目标的对象文件"
layout: reference
description: "清理指定源文件或当前目标的对象文件。"
cms_slug: "command-wrmo"
---

<p>清理指定源文件或当前目标的对象文件。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/wrmo&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-a | -all | all</td><td>All platforms (current: $WM_OPTIONS)</td></tr><tr><td>-h | -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wrmo [OPTION] [file1 [... fileN]]

options:
  -a | -all | all   All platforms (current: $WM_OPTIONS)
  -h | -help        Print the usage

Remove all .o files or remove .o file corresponding to &lt;file&gt;</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wrmo">源码与说明</a> · <a href="/assets/command-help/wrmo.txt">帮助文本</a></p>
