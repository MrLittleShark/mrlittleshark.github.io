---
title: "wmUnset · 清除当前 shell 中的 OpenFOAM 环境设置"
layout: reference
description: "清除当前 shell 中的 OpenFOAM 环境设置。"
cms_slug: "command-wmunset"
---

<p>清除当前 shell 中的 OpenFOAM 环境设置。</p><h2>开始前</h2>
<p>在已加载环境的交互式 Bash 中使用。wmUnset 清理 OpenFOAM 环境；先用 foamRc="$WM_PROJECT_DIR/etc/bashrc" 保存恢复路径。</p>
<h2>示例 1：清除环境再恢复</h2>
<pre><code class="language-bash">foamRc="$WM_PROJECT_DIR/etc/bashrc"
wmUnset
source "$foamRc"
</code></pre>
<p>恢复路径保存在独立变量中，清理后重新加载同一安装。</p>
<h2>示例 2：查看项目变量变化</h2>
<pre><code class="language-bash">foamRc="$WM_PROJECT_DIR/etc/bashrc"
wmUnset
printf 'project=%s\n' "${WM_PROJECT_DIR-unset}"
source "$foamRc"
</code></pre>
<p>清理后显示 unset，重新 source 恢复变量。</p>
<h2>示例 3：对比外部程序路径</h2>
<pre><code class="language-bash">foamRc="$WM_PROJECT_DIR/etc/bashrc"
wmUnset
command -v g++
source "$foamRc"
</code></pre>
<p>观察没有 OpenFOAM 路径修饰时的系统编译器。</p>
<h2>示例 4：避免两个安装路径叠加</h2>
<pre><code class="language-bash">wmUnset
source /usr/lib/openfoam/openfoam2512/etc/bashrc
</code></pre>
<p>先清理，再显式加载目标安装；路径按实际位置修改。</p>
<h2>示例 5：在子 shell 中检查清理行为</h2>
<pre><code class="language-bash">(wmUnset; printf '%s\n' "${WM_OPTIONS-unset}")
echo "$WM_OPTIONS"
</code></pre>
<p>交互式终端已定义 alias 后执行；子 shell 显示 unset，外层仍保留原配置。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
