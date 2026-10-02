---
title: "createCode · 该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码"
layout: reference
description: "该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码。"
cms_slug: "command-createcode"
---

<p>该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/src/createCode&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: createCode
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/src/createCode

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

#!/bin/sh
cd &quot;${0%/*}&quot; || exit                                # Run from this directory
#------------------------------------------------------------------------------
# Manually create ragel scanner

&quot;${WM_PROJECT_DIR:?}/wmake/scripts/makeParser&quot; \
    -scanner=wmkdepend.rl \
    &quot;$@&quot;

#------------------------------------------------------------------------------</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/src/createCode">源码与说明</a> · <a href="/assets/command-help/createcode.txt">帮助文本</a></p>
