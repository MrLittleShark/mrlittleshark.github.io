---
title: "foamVersion · v2512 源码提供的环境函数，可查询或切换版本；部分打包环境或非交互 shell 未加载该函数"
layout: reference
description: "v2512 源码提供的环境函数，可查询或切换版本；部分打包环境或非交互 shell 未加载该函数时，直接检查 WM_PROJECT_VERSION。"
cms_slug: "command-foamversion"
---

<p>v2512 源码提供的环境函数，可查询或切换版本；部分打包环境或非交互 shell 未加载该函数时，直接检查 WM_PROJECT_VERSION。</p><h2>开始前</h2>
<p>先加载 v2512 的 etc/bashrc。foamVersion 是 shell 函数；查询文字写到标准错误。切换只搜索当前安装目录的同级 OpenFOAM-&lt;版本&gt;。</p>
<h2>示例 1：查询当前版本</h2>
<pre><code class="language-bash">foamVersion
</code></pre>
<p>输出 OpenFOAM-v2512。</p>
<h2>示例 2：将版本存入记录</h2>
<pre><code class="language-bash">foamVersion 2&gt; version.txt
cat version.txt
</code></pre>
<p>2&gt; 捕获标准错误，避免得到空文件。</p>
<h2>示例 3：选择同级 v2512 安装</h2>
<pre><code class="language-bash">foamVersion v2512
</code></pre>
<p>同级存在 OpenFOAM-v2512/etc/bashrc 时切换并报告使用版本；包管理器安装路径可能不满足此命名规则。</p>
<h2>示例 4：切换后确认实际程序</h2>
<pre><code class="language-bash">if foamVersion v2512; then command -v blockMesh; fi
</code></pre>
<p>只在切换成功时显示程序路径，确认 PATH 已更新。</p>
<h2>示例 5：在子 shell 中运行指定安装</h2>
<pre><code class="language-bash">(foamVersion v2512 &amp;&amp; checkMesh -case "$HOME/foam-command-lab/caseA")
</code></pre>
<p>子 shell 切换环境并检查网格，退出后外层环境保持原样。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
