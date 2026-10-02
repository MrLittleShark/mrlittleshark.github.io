---
title: "foamPV · 重新加载 ParaView 版本配置"
layout: reference
description: "重新加载 ParaView 版本配置。"
cms_slug: "command-foampv"
---

<p>重新加载 ParaView 版本配置。</p><h2>开始前</h2>
<p>先加载环境。foamPV 为当前 shell 选择 OpenFOAM 配套 ParaView 设置；示例中的版本需在 ThirdParty 或指定安装中实际存在，版本变量 pvVersion 用本机目录名中的版本填写。</p>
<h2>示例 1：加载默认设置</h2>
<pre><code class="language-bash">foamPV
command -v paraview
</code></pre>
<p>载入 config.sh/paraview 默认值并查找程序。</p>
<h2>示例 2：选择已安装版本</h2>
<pre><code class="language-bash">pvVersion=5.11.2
foamPV "$pvVersion"
</code></pre>
<p>将第一个参数转换成 ParaView_VERSION，配置对应的已安装版本。</p>
<h2>示例 3：显示详细环境处理</h2>
<pre><code class="language-bash">FOAM_VERBOSE=1 foamPV "$pvVersion"
</code></pre>
<p>FOAM_VERBOSE 让配置脚本显示查找信息，便于定位安装目录。</p>
<h2>示例 4：检查选定程序的版本</h2>
<pre><code class="language-bash">foamPV "$pvVersion"
paraview --version
</code></pre>
<p>前者选择环境，后者由实际二进制报告版本。</p>
<h2>示例 5：用选定阅读器打开算例</h2>
<pre><code class="language-bash">foamPV "$pvVersion"
paraFoam -vtk -case "$FOAM_RUN/caseA"
</code></pre>
<p>环境设置后启动 ParaView 内置阅读器；-case 指向已有算例。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
