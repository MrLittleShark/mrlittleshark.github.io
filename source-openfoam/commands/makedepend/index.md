---
title: "makeDepend · 封装预处理器的依赖生成命令，供构建规则使用"
layout: reference
description: "封装预处理器的依赖生成命令，供构建规则使用。"
cms_slug: "command-makedepend"
---

<p>封装预处理器的依赖生成命令，供构建规则使用。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/makeDepend&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: makeDepend
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeDepend

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Wrapping for cpp -M with argument/options compatible with &lt;wmake/rules/General/transform&gt; calls of wmkdepend or wmkdep. This is for testing purposes only, but could used as a hook for other dependency generation systems (eg, ninja).</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeDepend">源码与说明</a> · <a href="/assets/command-help/makedepend.txt">帮助文本</a></p>
