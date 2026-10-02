---
title: "cleanAuxiliary · 清理求解日志、ParaView 入口和辅助输出"
layout: reference
description: "清理求解日志、ParaView 入口和辅助输出。"
cms_slug: "command-cleanauxiliary"
---

<p>清理求解日志、ParaView 入口和辅助输出。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanAuxiliary
</code></pre>
<p>本函数会删除 log.<em>、</em>.foam 等匹配文件，适合已保存所需日志的算例副本。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanAuxiliary
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanAuxiliary()
{
    rm -rf \
        ./mpirun.files \
        ./log ./log.* ./log-* ./logSummary.* \
        ./.fxLock ./*.xml ./ParaView* ./paraFoam* \
        ./*.blockMesh ./*.foam ./*.OpenFOAM \
        ./.setSet
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
