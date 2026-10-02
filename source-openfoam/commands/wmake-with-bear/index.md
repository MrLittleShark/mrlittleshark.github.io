---
title: "wmake-with-bear · 通过 Bear 调用 wmake，生成编译命令数据库"
layout: reference
description: "通过 Bear 调用 wmake，生成编译命令数据库。"
cms_slug: "command-wmake-with-bear"
---

<p>通过 Bear 调用 wmake，生成编译命令数据库。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/wmake-with-bear&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-bear-output-dir=DIR</td><td>Specify output directory</td></tr><tr><td>-version</td><td>Print bear version</td></tr><tr><td>-h | -help</td><td>Display short help and exit</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmake-with-bear [wmake options and args]

options:
  -bear-output-dir=DIR  Specify output directory
  -version              Print bear version
  -h | -help            Display short help and exit

Call wmake via &#x27;bear&#x27; to create json output.
Output: ${outputDir:-&quot;${WM_PROJECT_DIR:-&lt;project&gt;}/$cacheDirName&quot;}</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wmake-with-bear">源码与说明</a> · <a href="/assets/command-help/wmake-with-bear.txt">帮助文本</a></p>
