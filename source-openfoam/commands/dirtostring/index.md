---
title: "dirToString · 将目录路径转换为驼峰式名称"
layout: reference
description: "将目录路径转换为驼峰式名称。"
cms_slug: "command-dirtostring"
---

<p>将目录路径转换为驼峰式名称。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 只转换字符串，不要求对应目录存在。输出供 Make/files 的目录变量命名。</p>
<h2>示例 1：转换两级目录</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/dirToString" models/transport
</code></pre>
<p>输出 modelsTransport，将后一段首字母大写。</p>
<h2>示例 2：去掉当前目录前缀</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/dirToString" ./models/transport
</code></pre>
<p>默认剥离开头的点号和斜线，仍得到 modelsTransport。</p>
<h2>示例 3：转换三级路径</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/dirToString" fields/volume/scalar
</code></pre>
<p>输出 fieldsVolumeScalar，可用作源码分组变量名。</p>
<h2>示例 4：保留前导字符</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/dirToString" -no-strip ./models/transport
</code></pre>
<p>保留 ./ 对分段转换的影响，用于比较生成器的命名规则。</p>
<h2>示例 5：批量生成目录变量</h2>
<pre><code class="language-bash">for path in models/transport models/turbulence fields/volume; do name=$("$WM_PROJECT_DIR/wmake/scripts/dirToString" "$path"); printf '%s = %s\n' "$name" "$path"; done
</code></pre>
<p>输出变量名与原路径映射，便于理解 makeFiles 自动生成的清单。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-no-strip</code></td><td>Do not ignore leading [./] characters</td></tr><tr><td><code>-strip</code></td><td>Ignore leading [./] characters (default)</td></tr><tr><td><code>-h, -help</code></td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: dirToString [OPTION] dir

options:
  -no-strip         Do not ignore leading [./] characters
  -strip            Ignore leading [./] characters (default)
  -h, -help         Print the usage

Converts a directory path into a camelCase string</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/dirToString">源码与说明</a> · <a href="/assets/command-help/dirtostring.txt">帮助文本</a></p>
