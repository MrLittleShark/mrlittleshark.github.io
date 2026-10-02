---
title: "foamNewCase · 模板来自用户或站点配置"
layout: reference
description: "模板来自用户或站点配置。-list 列出可用模板；创建命令为 foamNewCase -app simpleFoam -case newCase。"
cms_slug: "command-foamnewcase"
---

<p>模板来自用户或站点配置。-list 列出可用模板；创建命令为 foamNewCase -app simpleFoam -case newCase。</p><h2>用法</h2><pre><code class="language-bash">foamNewCase -list</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">foamNewCase -list -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-app NAME</td><td>specify the application to use</td></tr><tr><td>-case DIR</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-list</td><td>列出可用的预配置函数。</td></tr><tr><td>-with-api=NUM</td><td>specify alternative api to use (default: \$FOAM_API)</td></tr><tr><td>-version VER</td><td>[obsolete]</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamNewCase [OPTION]
options:
  -app NAME         specify the application to use
  -case DIR         specify alternative case directory, default is the cwd
  -list             list the applications available
  -with-api=NUM     specify alternative api to use (default: \$FOAM_API)
  -version VER      [obsolete]
  -help             Print the usage

clone initial application settings to the specified case from
    $userDir/$templateDir/{$projectApi,}/APP
    $groupDir/$templateDir/{$projectApi,}/APP</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewCase">源码与说明</a> · <a href="/assets/command-help/foamnewcase.txt">帮助文本</a></p>
