---
title: "findEmptyMake · 查找缺少 files 或 options 的 Make 目录"
layout: reference
description: "查找缺少 files 或 options 的 Make 目录。"
cms_slug: "command-findemptymake"
---

<p>查找缺少 files 或 options 的 Make 目录。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/findEmptyMake&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: findEmptyMake [OPTION] [dir1 .. dirN]

Find Make/ directories without a &#x27;files&#x27; or &#x27;options&#x27; file.
This can occur when a directory has been moved.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/findEmptyMake">源码与说明</a> · <a href="/assets/command-help/findemptymake.txt">帮助文本</a></p>
