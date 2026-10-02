---
title: "query-detect · 调用依赖检测脚本，列出发现的软件位置"
layout: reference
description: "调用依赖检测脚本，列出发现的软件位置。"
cms_slug: "command-query-detect"
---

<p>调用依赖检测脚本，列出发现的软件位置。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/query-detect&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-all</td><td>Test all</td></tr><tr><td>-mode=MODE</td><td>Pass-through option for foamEtcFile</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: query-detect [OPTIONS] [name1 .. [nameN]]
options:
  -all              Test all
  -mode=MODE        Pass-through option for foamEtcFile
  -help             Display short help and exit

Calls various wmake &#x27;have_*&#x27; scripts with -test to report the
detected software locations</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/query-detect">源码与说明</a> · <a href="/assets/command-help/query-detect.txt">帮助文本</a></p>
