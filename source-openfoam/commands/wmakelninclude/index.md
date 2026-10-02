---
title: "wmakeLnInclude · 将头文件和模板实现链接到 lnInclude 目录"
layout: reference
description: "将头文件和模板实现链接到 lnInclude 目录。"
cms_slug: "command-wmakelninclude"
---

<p>将头文件和模板实现链接到 lnInclude 目录。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/wmakeLnInclude&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-f | -force</td><td>Force remove of existing lnInclude/ before recreating</td></tr><tr><td>-u | -update</td><td>Update existing lnInclude directories</td></tr><tr><td>-s | -silent</td><td>Silent mode (do not echo command)</td></tr><tr><td>-extra</td><td>Also include all source files in lnInclude/</td></tr><tr><td>-no-extra</td><td>Do not include all source files in lnInclude/ [default]</td></tr><tr><td>-pwd</td><td>Locate root directory containing Make/ directory</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmakeLnInclude [OPTION] [-pwd | dir [.. dirN]]

options:
  -f | -force       Force remove of existing lnInclude/ before recreating
  -u | -update      Update existing lnInclude directories
  -s | -silent      Silent mode (do not echo command)
  -extra            Also include all source files in lnInclude/
  -no-extra         Do not include all source files in lnInclude/ [default]
  -pwd              Locate root directory containing Make/ directory
  -help             Print the usage

Link header/template files from specified dir(s) into their respective
lnInclude/ directories. With &#x27;-update&#x27;, items are relinked with &#x27;ln -sf&#x27;</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmakeLnInclude">源码与说明</a> · <a href="/assets/command-help/wmakelninclude.txt">帮助文本</a></p>
