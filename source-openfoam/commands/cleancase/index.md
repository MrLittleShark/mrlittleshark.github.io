---
title: "cleanCase · 清理时间结果、网格、分区和后处理输出，保留主要输入配置"
layout: reference
description: "清理时间结果、网格、分区和后处理输出，保留主要输入配置。"
cms_slug: "command-cleancase"
---

<p>清理时间结果、网格、分区和后处理输出，保留主要输入配置。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanCase
</code></pre>
<p>会删除生成的 polyMesh 和 processor 数据。适合从网格生成步骤重新开始的练习副本。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanCase
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanCase()
{
    cleanTimeDirectories
    cleanAdiosOutput
    cleanAuxiliary
    cleanDynamicCode
    cleanOptimisation
    cleanPostProcessing

    cleanFaMesh
    cleanPolyMesh
    cleanSnappyFiles

    rm -rf processor*
    rm -rf TDAC
    rm -rf probes*
    rm -rf forces*
    rm -rf graphs*
    rm -rf sets
    rm -rf system/machines

    # Debug output (blockMesh, decomposePar)
    rm -f \
        blockTopology.vtu blockFaces.vtp blockTopology.obj blockCentres.obj \
        cellDist.vtu decomposePar.vtu renumberMesh.vtu \
        0/cellDist

    # From mpirunDebug
    rm -f gdbCommands mpirun.schema

    (
        cd constant 2&gt;/dev/null || exit 0

        rm -rf \
          cellDecomposition cellToRegion cellLevel* pointLevel* \
          tetDualMesh \
          ;
    )
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
