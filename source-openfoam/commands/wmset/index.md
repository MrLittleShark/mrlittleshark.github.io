---
title: "wmSet · 按给定变量重新加载 OpenFOAM 环境"
layout: reference
description: "按给定变量重新加载 OpenFOAM 环境。"
cms_slug: "command-wmset"
---

<p>按给定变量重新加载 OpenFOAM 环境。</p><h2>开始前</h2>
<p>在交互式 Bash 中先加载环境。wmSet 将参数传给当前安装的 etc/bashrc，选择已有或待编译的配置。</p>
<h2>示例 1：采用双精度</h2>
<pre><code class="language-bash">wmSet WM_PRECISION_OPTION=DP
echo "$WM_OPTIONS"
</code></pre>
<p>设置浮点精度并打印组合编译标识。</p>
<h2>示例 2：使用 64 位索引</h2>
<pre><code class="language-bash">wmSet WM_LABEL_SIZE=64
echo "$FOAM_LIBBIN"
</code></pre>
<p>库目录随 Int64 配置变化；运行程序前需有相匹配的二进制库。</p>
<h2>示例 3：组合调试配置</h2>
<pre><code class="language-bash">wmSet WM_COMPILE_OPTION=Debug WM_PRECISION_OPTION=DP
echo "$WM_OPTIONS"
</code></pre>
<p>使用 Debug 规则，适合源码调试；需要对应配置已构建。</p>
<h2>示例 4：选择系统 GCC</h2>
<pre><code class="language-bash">wmSet WM_COMPILER=Gcc WM_COMPILER_TYPE=system
wmake -show-path-cxx
</code></pre>
<p>使用系统编译器并打印实际 C++ 编译器路径。</p>
<h2>示例 5：恢复常用构建组合</h2>
<pre><code class="language-bash">wmSet WM_COMPILER=Gcc WM_PRECISION_OPTION=DP WM_LABEL_SIZE=32 WM_COMPILE_OPTION=Opt
echo "$WM_OPTIONS"
</code></pre>
<p>一次显式选定四个参数，回到常见 GccDPInt32Opt 配置。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
