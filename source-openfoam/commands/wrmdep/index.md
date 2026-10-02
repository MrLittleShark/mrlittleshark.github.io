---
title: "wrmdep · 清理指定源文件或当前目标的依赖文件"
layout: reference
description: "清理指定源文件或当前目标的依赖文件。"
cms_slug: "command-wrmdep"
---

<p>清理指定源文件或当前目标的依赖文件。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/wrmdep&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage:

wrmdep [-a | -all | all] [file1 [..fileN]]

    Remove all .dep files or remove .dep files referring to &lt;file&gt;.
    With the &#x27;all&#x27; option the .dep files are removed for all platforms
    rather than just the current platform ($WM_OPTIONS).

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
        $WM_PROJECT_DIR</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wrmdep">源码与说明</a> · <a href="/assets/command-help/wrmdep.txt">帮助文本</a></p>
