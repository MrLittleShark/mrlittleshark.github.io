---
title: "foamCreateCompletionCache · 生成 OpenFOAM 命令补全缓存"
layout: reference
description: "生成 OpenFOAM 命令补全缓存。"
cms_slug: "command-foamcreatecompletioncache"
---

<p>生成 OpenFOAM 命令补全缓存。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/foamCreateCompletionCache&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-dir DIR</td><td>Directory to process</td></tr><tr><td>-user</td><td>Add \$FOAM_USER_APPBIN to the search directories</td></tr><tr><td>-no-header</td><td>Suppress header generation Write to alternative output</td></tr><tr><td>-h | -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCreateCompletionCache [OPTION] [appName .. [appNameN]]
options:
  -dir DIR          Directory to process
  -user             Add \$FOAM_USER_APPBIN to the search directories
  -no-header        Suppress header generation
  -output FILE, -o FILE
                    Write to alternative output
  -h | -help        Print the usage

Create cache of bash completion values for OpenFOAM applications.
The cached values are typically used by the tcsh completion wrapper.
Default search: \$FOAM_APPBIN only.
Default output: $defaultOutputFile

Uses the search directory if applications are specified.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamCreateCompletionCache">源码与说明</a> · <a href="/assets/command-help/foamcreatecompletioncache.txt">帮助文本</a></p>
