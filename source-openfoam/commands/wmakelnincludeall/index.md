---
title: "wmakeLnIncludeAll · 为目录树中的库生成 lnInclude 链接目录"
layout: reference
description: "为目录树中的库生成 lnInclude 链接目录。"
cms_slug: "command-wmakelnincludeall"
---

<p>为目录树中的库生成 lnInclude 链接目录。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/wmakeLnIncludeAll&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-f | -force</td><td>Force remove of existing lnInclude before recreating</td></tr><tr><td>-u | -update</td><td>Update existing lnInclude directories</td></tr><tr><td>-j</td><td>Use all local cores/hyperthreads</td></tr><tr><td>-jN | -j N</td><td>Use N cores/hyperthreads</td></tr><tr><td>-extra</td><td>Also include all source files in lnInclude/</td></tr><tr><td>-no-extra</td><td>Do not include all source files in lnInclude/ [default]</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmakeLnIncludeAll [OPTION] [dir1 .. dirN]

options:
  -f | -force       Force remove of existing lnInclude before recreating
  -u | -update      Update existing lnInclude directories
  -j                Use all local cores/hyperthreads
  -jN | -j N        Use N cores/hyperthreads
  -extra            Also include all source files in lnInclude/
  -no-extra         Do not include all source files in lnInclude/ [default]
  -help             Display short help and exit

Find directories with a &#x27;Make/files&#x27; containing a &#x27;LIB =&#x27; directive
and execute &#x27;wmakeLnInclude&#x27; for each.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmakeLnIncludeAll">源码与说明</a> · <a href="/assets/command-help/wmakelnincludeall.txt">帮助文本</a></p>
