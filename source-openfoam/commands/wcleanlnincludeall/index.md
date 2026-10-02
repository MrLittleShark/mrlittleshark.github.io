---
title: "wcleanLnIncludeAll · 删除目录树中的 lnInclude 头文件链接目录"
layout: reference
description: "删除目录树中的 lnInclude 头文件链接目录。"
cms_slug: "command-wcleanlnincludeall"
---

<p>删除目录树中的 lnInclude 头文件链接目录。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/wcleanLnIncludeAll&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-h, -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wcleanLnIncludeAll [dir1 [..dirN]]

options:
  -h, -help         Print the usage

Remove all lnInclude directories found in the tree</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wcleanLnIncludeAll">源码与说明</a> · <a href="/assets/command-help/wcleanlnincludeall.txt">帮助文本</a></p>
