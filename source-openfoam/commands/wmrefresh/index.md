---
title: "wmRefresh · 按当前设置重新加载 OpenFOAM 环境"
layout: reference
description: "按当前设置重新加载 OpenFOAM 环境。"
cms_slug: "command-wmrefresh"
---

<p>按当前设置重新加载 OpenFOAM 环境。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/etc/config.sh/aliases"
wmRefresh
</code></pre>
<p>先清理旧环境变量，再读取同一项目的 etc/bashrc。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type wmRefresh
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">wmRefresh()
{
    local projectDir="$WM_PROJECT_DIR"
    local foamSettings="$FOAM_SETTINGS"
    . "$projectDir/etc/config.sh/unset"  2&gt;/dev/null
    . "$projectDir/etc/bashrc" "$foamSettings"
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
