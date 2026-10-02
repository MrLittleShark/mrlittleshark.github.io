---
title: "foamVersion · v2512 源码提供的环境函数，可查询或切换版本；部分打包环境或非交互 shell 未加载该函数"
layout: reference
description: "v2512 源码提供的环境函数，可查询或切换版本；部分打包环境或非交互 shell 未加载该函数时，直接检查 WM_PROJECT_VERSION。"
cms_slug: "command-foamversion"
---

<p>v2512 源码提供的环境函数，可查询或切换版本；部分打包环境或非交互 shell 未加载该函数时，直接检查 WM_PROJECT_VERSION。</p><h2>用法</h2><pre><code class="language-bash">printf &#x27;%s\n&#x27; &quot;$WM_PROJECT_VERSION&quot;
# foamVersion 是环境函数，先确认当前 shell 是否加载
type foamVersion</code></pre><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
