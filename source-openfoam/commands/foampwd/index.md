---
title: "foamPwd · 用 OpenFOAM 环境变量缩写显示当前路径"
layout: reference
description: "用 OpenFOAM 环境变量缩写显示当前路径。"
cms_slug: "command-foampwd"
---

<p>用 OpenFOAM 环境变量缩写显示当前路径。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/etc/config.sh/aliases"
foamPwd
</code></pre>
<p>例如把用户算例路径的公共前缀显示为 $FOAM_RUN，便于写入说明和日志。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type foamPwd
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">foamPwd()
{
    if [ -n "$WM_PROJECT_DIR" ]
    then
        echo "$PWD/" | sed \
        -e "s#^${FOAM_RUN}/#\$FOAM_RUN/#" \
        -e "s#^${WM_PROJECT_DIR}/#\$WM_PROJECT_DIR/#" \
        -e "s#^${WM_PROJECT_USER_DIR}/#\$WM_PROJECT_USER_DIR/#" \
        -e "s#^${HOME}/#~/#" \
        ;
    else
        echo "$PWD/" | sed -e "s#^${HOME}/#~/#";
    fi
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
