---
title: "dirToString · 将目录路径转换为驼峰式名称"
layout: reference
description: "将目录路径转换为驼峰式名称。"
cms_slug: "command-dirtostring"
---

<p>将目录路径转换为驼峰式名称。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/dirToString&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-no-strip</td><td>Do not ignore leading [./] characters</td></tr><tr><td>-strip</td><td>Ignore leading [./] characters (default)</td></tr><tr><td>-h, -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: dirToString [OPTION] dir

options:
  -no-strip         Do not ignore leading [./] characters
  -strip            Ignore leading [./] characters (default)
  -h, -help         Print the usage

Converts a directory path into a camelCase string</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/dirToString">源码与说明</a> · <a href="/assets/command-help/dirtostring.txt">帮助文本</a></p>
