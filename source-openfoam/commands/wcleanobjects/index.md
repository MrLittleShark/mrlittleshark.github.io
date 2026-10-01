---
title: "wcleanObjects · 构建或开发辅助脚本"
layout: reference
description: "Deletes the specified 'build/' object files directories from the project top-level 'build/' directory $WM_PROJECT_DIR. special platforms - 'all' removes all platforms. - 'compiler' corresponds to $WM_ARCH$WM_COMPILER. - 'current' correspond"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>Deletes the specified &#x27;build/&#x27; object files directories from the project top-level &#x27;build/&#x27; directory &#36;WM_PROJECT_DIR. special platforms - &#x27;all&#x27; removes all platforms. - &#x27;compiler&#x27; corresponds to &#36;WM_ARCH&#36;WM_COMPILER. - &#x27;current&#x27; corresponds to &#36;WM_OPTIONS. You must be in the project or the third-party top-level directory to run this script. When called as wcleanPlatform, the target directory changes to &#x27;platforms/ and the &#x27;all&#x27; target also cleans up lnInclude dirs and tutorials</p><h2>v2512 源码中的用途</h2><p>Deletes the specified &#x27;build/&#x27; object files directories from the project top-level &#x27;build/&#x27; directory &#36;WM_PROJECT_DIR. special platforms - &#x27;all&#x27; removes all platforms. - &#x27;compiler&#x27; corresponds to &#36;WM_ARCH&#36;WM_COMPILER. - &#x27;current&#x27; corresponds to &#36;WM_OPTIONS. You must be in the project or the third-party top-level directory to run this script. When called as wcleanPlatform, the target directory changes to &#x27;platforms/ and the &#x27;all&#x27; target also cleans up lnInclude dirs and tutorials</p><h2>使用入口</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;&#36;WM_PROJECT_DIR/wmake/scripts/wcleanObjects&quot;</code></pre><p>该条属于内部构建或开发辅助入口，可能依赖调用方预先设置变量、工作目录和参数。正常使用应优先从 wmake、Allwmake 或相应公开脚本进入。</p><h2>使用条件与核对</h2><p>
Deletes the specified &#x27;build/&#x27; object files directories from the project top-level &#x27;build/&#x27; directory &#36;WM_PROJECT_DIR. special platforms - &#x27;all&#x27; removes all platforms. - &#x27;compiler&#x27; corresponds to &#36;WM_ARCH&#36;WM_COMPILER. - &#x27;current&#x27; corresponds to &#36;WM_OPTIONS. You must be in the project or the third-party top-level directory to run this script. When called as wcleanPlatform, the target directory changes to &#x27;platforms/ and the &#x27;all&#x27; target also cleans up lnInclude dirs and tutorials
辅助脚本不一定加入 PATH；不要把内部调用接口当作稳定的用户命令。
源码帮助选项：-a -comp -compiler -curr -help</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/wcleanobjects.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: wcleanObjects
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wcleanObjects

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: wcleanObjects &lt;option | platform&gt; [.. &lt;option | platform&gt;]

options:
  -a | -all             Same as &#x27;all&#x27;
  -curr | -current      Use \&#36;WM_OPTIONS (&#36;WM_OPTIONS)
  -comp | -compiler     Use \&#36;WM_ARCH\&#36;WM_COMPILER*  (&#36;WM_ARCH&#36;WM_COMPILER)
  -compiler=NAME        Use \&#36;WM_ARCH&lt;NAME&gt;*  (&#36;WM_ARCH&lt;NAME&gt;*)
  -help                 Print the usage

Deletes specified &#36;targetDir object file directories from project top-level:
Project:   &#36;WM_PROJECT_DIR
Directory: &#36;targetDir/

special platforms:
  all           Remove all platforms&#36;extraText
  compiler      &#36;WM_ARCH&#36;WM_COMPILER  (ie, \&#36;WM_ARCH\&#36;WM_COMPILER)
  current       &#36;WM_OPTIONS  (ie, \&#36;WM_OPTIONS)

You must be in the project or the third-party top-level directory
to run this script.</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wcleanObjects">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
