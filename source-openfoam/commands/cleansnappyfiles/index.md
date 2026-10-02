---
title: "cleanSnappyFiles · 清理 snappyHexMesh 的细化历史和辅助字段"
layout: reference
description: "清理 snappyHexMesh 的细化历史和辅助字段。"
cms_slug: "command-cleansnappyfiles"
---

<p>清理 snappyHexMesh 的细化历史和辅助字段。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanSnappyFiles
</code></pre>
<p>包含 cellLevel、pointLevel 和 refinementHistory 等数据；需要继续自适应细化时应保留这些文件。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanSnappyFiles
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanSnappyFiles()
{
    rm -f \
        constant/polyMesh/cellLevel \
        constant/polyMesh/pointLevel \
        constant/polyMesh/refinementHistory \
        constant/polyMesh/level0Edge \
        constant/polyMesh/surfaceIndex
    rm -f \
        processor*/constant/polyMesh/cellLevel \
        processor*/constant/polyMesh/pointLevel \
        processor*/constant/polyMesh/refinementHistory \
        processor*/constant/polyMesh/level0Edge \
        processor*/constant/polyMesh/surfaceIndex
    rm -f \
        constant/cellLevel \
        constant/pointLevel \
        0/cellLevel \
        0/pointLevel
    rm -f \
        processor*/constant/cellLevel \
        processor*/constant/pointLevel \
        processor*/0/cellLevel \
        processor*/0/pointLevel
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
