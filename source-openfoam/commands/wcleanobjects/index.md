---
title: "wcleanObjects · 清理项目 build 目录中的指定平台编译中间文件"
layout: reference
description: "清理项目 build 目录中的指定平台编译中间文件。"
cms_slug: "command-wcleanobjects"
---

<p>清理项目 build 目录中的指定平台编译中间文件。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/wcleanObjects&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-a | -all</td><td>Same as &#x27;all&#x27;</td></tr><tr><td>-curr | -current</td><td>Use \$WM_OPTIONS ($WM_OPTIONS)</td></tr><tr><td>-comp | -compiler</td><td>Use \$WM_ARCH\$WM_COMPILER*  ($WM_ARCH$WM_COMPILER)</td></tr><tr><td>-compiler=NAME</td><td>Use \$WM_ARCH&lt;NAME&gt;*  ($WM_ARCH&lt;NAME&gt;*)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wcleanObjects &lt;option | platform&gt; [.. &lt;option | platform&gt;]

options:
  -a | -all             Same as &#x27;all&#x27;
  -curr | -current      Use \$WM_OPTIONS ($WM_OPTIONS)
  -comp | -compiler     Use \$WM_ARCH\$WM_COMPILER*  ($WM_ARCH$WM_COMPILER)
  -compiler=NAME        Use \$WM_ARCH&lt;NAME&gt;*  ($WM_ARCH&lt;NAME&gt;*)
  -help                 Print the usage

Deletes specified $targetDir object file directories from project top-level:
Project:   $WM_PROJECT_DIR
Directory: $targetDir/

special platforms:
  all           Remove all platforms$extraText
  compiler      $WM_ARCH$WM_COMPILER  (ie, \$WM_ARCH\$WM_COMPILER)
  current       $WM_OPTIONS  (ie, \$WM_OPTIONS)

You must be in the project or the third-party top-level directory
to run this script.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wcleanObjects">源码与说明</a> · <a href="/assets/command-help/wcleanobjects.txt">帮助文本</a></p>
