---
title: "wmakeWindowsDlOpenLibs · 为 Windows 程序生成运行时加载的动态库列表"
layout: reference
description: "为 Windows 程序生成运行时加载的动态库列表。"
cms_slug: "command-wmakewindowsdlopenlibs"
---

<p>为 Windows 程序生成运行时加载的动态库列表。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/wmakeWindowsDlOpenLibs&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: wmakeWindowsDlOpenLibs
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wmakeWindowsDlOpenLibs

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Extract library dependencies from the EXE_LIBS entry for Windows applications and emit as FOAM_DLOPEN_LIBS for use with setRootCase.H Forcibly dlOpen&#x27;ing these libraries ensures that they are truly loaded for the windows application binary. An alternative means is to define external entry points into particular libraries and linking with &#x27;-u symbol&#x27;, which would possibly have a lower overhead but is more code-intrusive and somewhat ad hoc.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wmakeWindowsDlOpenLibs">源码与说明</a> · <a href="/assets/command-help/wmakewindowsdlopenlibs.txt">帮助文本</a></p>
