---
title: "wmUnset · 清除当前 shell 中的 OpenFOAM 环境设置"
layout: reference
description: "清除当前 shell 中的 OpenFOAM 环境设置。"
cms_slug: "command-wmunset"
---

<p>清除当前 shell 中的 OpenFOAM 环境设置。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/etc/config.sh/aliases"
wmUnset
</code></pre>
<p>随后可重新 source 所需版本的 etc/bashrc。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type wmUnset
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">alias wmUnset='. ${WM_PROJECT_DIR:?}/etc/config.sh/unset'
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
