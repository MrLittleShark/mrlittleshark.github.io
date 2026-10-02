---
title: "wmRefresh · 按当前设置重新加载 OpenFOAM 环境"
layout: reference
description: "按当前设置重新加载 OpenFOAM 环境。"
cms_slug: "command-wmrefresh"
---

<p>按当前设置重新加载 OpenFOAM 环境。</p><h2>开始前</h2>
<p>先加载 v2512 环境。wmRefresh 保存项目路径与 FOAM_SETTINGS，再清理并重新加载该环境。</p>
<h2>示例 1：重载当前设置</h2>
<pre><code class="language-bash">wmRefresh
echo "$WM_OPTIONS"
</code></pre>
<p>重新按保存的设置生成环境变量。</p>
<h2>示例 2：修改偏好后应用</h2>
<pre><code class="language-bash">${EDITOR:-vi} "$HOME/.OpenFOAM/prefs.sh"
wmRefresh
</code></pre>
<p>先编辑已存在的个人偏好文件，重载后其配置参与环境选择。</p>
<h2>示例 3：安装程序后刷新路径</h2>
<pre><code class="language-bash">wmRefresh
command -v blockMesh
</code></pre>
<p>确认重新生成的 PATH 解析到当前安装程序。</p>
<h2>示例 4：刷新个人程序目录</h2>
<pre><code class="language-bash">mkdir -p "$FOAM_USER_APPBIN"
wmRefresh
printf '%s\n' "$FOAM_USER_APPBIN"
</code></pre>
<p>目录建立后重新加载环境，输出当前用户程序位置。</p>
<h2>示例 5：比较刷新前后的选项</h2>
<pre><code class="language-bash">before=$WM_OPTIONS
wmRefresh
printf 'before=%s\nafter=%s\n' "$before" "$WM_OPTIONS"
</code></pre>
<p>设置未改变时两项应相同；偏好改变时可直接看到构建组合变化。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
