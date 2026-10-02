---
title: "wmSP · 重新加载环境并设置 WM_PRECISION_OPTION=SP"
layout: reference
description: "重新加载环境并设置 WM_PRECISION_OPTION=SP。"
cms_slug: "command-wmsp"
---

<p>重新加载环境并设置 WM_PRECISION_OPTION=SP。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/etc/config.sh/aliases"
wmSP
echo "$WM_OPTIONS"
</code></pre>
<p>这会选择对应的精度或标签长度环境。该配置需要匹配的程序与库，可从源码构建。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type wmSP
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">alias wmSP='wmSet WM_PRECISION_OPTION=SP'
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
