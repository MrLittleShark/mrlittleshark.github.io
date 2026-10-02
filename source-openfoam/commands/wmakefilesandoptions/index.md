---
title: "wmakeFilesAndOptions · 扫描当前源码目录并生成 Make/files 和 Make/options"
layout: reference
description: "扫描当前源码目录并生成 Make/files 和 Make/options。"
cms_slug: "command-wmakefilesandoptions"
---

<p>扫描当前源码目录并生成 Make/files 和 Make/options。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/wmakeFilesAndOptions&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmakeFilesAndOptions [-help]

Scans current directory for directories and source files and constructs
the &#x27;Make/files&#x27; and &#x27;Make/options&#x27; files.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wmakeFilesAndOptions">源码与说明</a> · <a href="/assets/command-help/wmakefilesandoptions.txt">帮助文本</a></p>
