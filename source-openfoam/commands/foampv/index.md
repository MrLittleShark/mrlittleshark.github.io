---
title: "foamPV · 重新加载 ParaView 版本配置"
layout: reference
description: "重新加载 ParaView 版本配置。"
cms_slug: "command-foampv"
---

<p>重新加载 ParaView 版本配置。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/etc/config.sh/aliases"
foamPV
</code></pre>
<p>读取当前 OpenFOAM 的 ParaView 环境设置；指定版本时会按安装配置寻找相应程序。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type foamPV
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">foamPV()
{
    . "$WM_PROJECT_DIR/etc/config.sh/paraview" "${@+ParaView_VERSION=$@}"
    # If not already reported
    if [ -z "$FOAM_VERBOSE" ]
    then
        echo "paraview=${ParaView_DIR##*/}" 1&gt;&amp;2
    fi
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
