---
title: "wrmdep · OpenFOAM 官方脚本"
layout: reference
description: "This is a catch-all script for pruning .dep files, depending on the provided arguments. [-a | -all | all] [file1 [.. fileN]]: Remove all .dep files from the object directory tree corresponding to the current source directory or remove only "
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>This is a catch-all script for pruning .dep files, depending on the provided arguments. [-a | -all | all] [file1 [.. fileN]]: Remove all .dep files from the object directory tree corresponding to the current source directory or remove only the .dep files referring to the optionally specified file(s). With the -a/-all/all option the .dep files are removed for all platforms rather than just the current platform. [-o | -old] [dir1 [.. dirN]]: Remove *.dep files that are without a corresponding .C or .L source file. This occurs when a directory has been moved. - prints the questionable directory and *.dep file -update: Search all the &quot;src&quot; and &quot;application&quot; directories of the project for broken symbolic links for source code files and then remove all .dep files that relate to files that no longer exist. Must be executed in the project top-level directory: &#36;WM_PROJECT_DIR.</p><h2>v2512 源码中的用途</h2><p>This is a catch-all script for pruning .dep files, depending on the provided arguments. [-a | -all | all] [file1 [.. fileN]]: Remove all .dep files from the object directory tree corresponding to the current source directory or remove only the .dep files referring to the optionally specified file(s). With the -a/-all/all option the .dep files are removed for all platforms rather than just the current platform. [-o | -old] [dir1 [.. dirN]]: Remove *.dep files that are without a corresponding .C or .L source file. This occurs when a directory has been moved. - prints the questionable directory and *.dep file -update: Search all the &quot;src&quot; and &quot;application&quot; directories of the project for broken symbolic links for source code files and then remove all .dep files that relate to files that no longer exist. Must be executed in the project top-level directory: &#36;WM_PROJECT_DIR.</p><h2>使用入口</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;&#36;WM_PROJECT_DIR/wmake/wrmdep&quot;</code></pre><h2>使用条件与核对</h2><p>
This is a catch-all script for pruning .dep files, depending on the provided arguments. [-a | -all | all] [file1 [.. fileN]]: Remove all .dep files from the object directory tree corresponding to the current source directory or remove only the .dep files referring to the optionally specified file(s). With the -a/-all/all option the .dep files are removed for all platforms rather than just the current platform. [-o | -old] [dir1 [.. dirN]]: Remove *.dep files that are without a corresponding .C or .L source file. This occurs when a directory has been moved. - prints the questionable directory and *.dep file -update: Search all the &quot;src&quot; and &quot;application&quot; directories of the project for broken symbolic links for source code files and then remove all .dep files that relate to files that no longer exist. Must be executed in the project top-level directory: &#36;WM_PROJECT_DIR.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/wrmdep.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: wrmdep
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wrmdep

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage:

wrmdep [-a | -all | all] [file1 [..fileN]]

    Remove all .dep files or remove .dep files referring to &lt;file&gt;.
    With the &#x27;all&#x27; option the .dep files are removed for all platforms
    rather than just the current platform (&#36;WM_OPTIONS).

wrmdep [-o | -old] [dir1 [..dirN]]

    Remove *.dep files that are without a corresponding .C or .L file.
    This occurs when a directory has been moved.
      - prints the questionable directory and *.dep file

    Note: to remove empty directories, run: wclean empty

wrmdep -update

    Search &quot;src&quot; and &quot;application&quot; directories of the project for broken
    symbolic links for source code files and remove all .dep files related
    to files that no longer exist.
    Must be executed in the project top-level directory:
        &#36;WM_PROJECT_DIR</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wrmdep">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
