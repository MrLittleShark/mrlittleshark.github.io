---
title: "wmSPDP · 重新加载 OpenFOAM 环境，并选择单精度场与双精度求解的混合模式"
layout: reference
description: "重新加载 OpenFOAM 环境，并选择单精度场与双精度求解的混合模式。"
cms_slug: "command-wmspdp"
---

<p>重新加载 OpenFOAM 环境，并选择单精度场与双精度求解的混合模式。</p><h2>开始前</h2>
<p>先加载 v2512 环境，在交互式 Bash 中逐行执行。此 alias 重新加载环境并选择 WM_PRECISION_OPTION=SPDP；对应编译配置的程序和库需已安装，或在可写源码树中自行构建。</p>
<h2>示例 1：选择编译配置</h2>
<pre><code class="language-bash">wmSPDP
echo "$WM_PRECISION_OPTION"
</code></pre>
<p>输出 SPDP。DP 为双精度，SP 为单精度，SPDP 使用单精度存储并扩展求解精度；label size 控制整数索引位宽。</p>
<h2>示例 2：定位对应程序与库</h2>
<pre><code class="language-bash">wmSPDP
printf '%s\n' "$WM_OPTIONS" "$FOAM_APPBIN" "$FOAM_LIBBIN"
</code></pre>
<p>三行分别给出完整编译标识、程序目录、库目录，包含精度和索引设置。</p>
<h2>示例 3：检查编译参数</h2>
<pre><code class="language-bash">wmSPDP
wmake -show-cxxflags
</code></pre>
<p>输出该配置采用的 C++ 编译选项，可看到精度和 WM_LABEL_SIZE 宏。</p>
<h2>示例 4：为个人程序使用该配置</h2>
<pre><code class="language-bash">wmSPDP
cd "$WM_PROJECT_USER_DIR/applications/utilities/fieldStats"
wmake
</code></pre>
<p>先准备有 Make/files 和 Make/options 的 fieldStats。重新编译得到与当前配置匹配的用户程序；相应 OpenFOAM 库须存在。</p>
<h2>示例 5：检查同一网格</h2>
<pre><code class="language-bash">wmSPDP
checkMesh -case "$FOAM_RUN/caseA" &gt; "$FOAM_RUN/caseA/log.checkMesh.SPDP" 2&gt;&amp;1
</code></pre>
<p>对已有算例执行网格检查，并以配置名保存日志。切换环境本身不转换已有场文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
