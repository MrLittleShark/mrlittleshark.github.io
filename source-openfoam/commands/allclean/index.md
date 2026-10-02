---
title: "Allclean · 算例提供的清理脚本，执行前检查其删除范围"
layout: reference
description: "算例提供的清理脚本，执行前检查其删除范围。"
cms_slug: "command-allclean"
---

<p>算例提供的清理脚本，执行前检查其删除范围。</p><h2>开始前</h2>
<p>这里指教程测试集的 Allclean。只在完整复制的 tutorial-clean-demo 中执行；各单独案例可能定义其他清理逻辑。顶层脚本还会处理对应 tutorials 构建缓存。</p>
<h2>示例 1：清理完整测试副本</h2>
<pre><code class="language-bash">cd tutorial-clean-demo
./Allclean
</code></pre>
<p>调用日志清理和递归教程清理，保留输入模板。</p>
<h2>示例 2：从父目录调用</h2>
<pre><code class="language-bash">bash tutorial-clean-demo/Allclean
</code></pre>
<p>脚本自己切换到所在目录，清理范围由脚本位置确定。</p>
<h2>示例 3：先保留测试报告</h2>
<pre><code class="language-bash">cp tutorial-clean-demo/testLoopReport report.before-clean
bash tutorial-clean-demo/Allclean
</code></pre>
<p>先把需要保留的汇总复制到测试集外，再清除产物。</p>
<h2>示例 4：清理两个独立测试集</h2>
<pre><code class="language-bash">for tree in tutorial-clean-demoA tutorial-clean-demoB; do bash "$tree/Allclean"; done
</code></pre>
<p>两个目录都应是专门副本，分别按自身脚本清理。</p>
<h2>示例 5：恢复并重跑测试</h2>
<pre><code class="language-bash">cd tutorial-clean-demo
./Allclean
./Allrun -test
</code></pre>
<p>清理后由测试运行脚本重新生成网格、初始场及结果。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: Allclean
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/Allclean

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

#!/bin/sh
cd &quot;${0%/*}&quot; || exit                            # Run from this directory
. &quot;${WM_PROJECT_DIR:?}&quot;/bin/tools/LogFunctions  # Tutorial log-file functions
#------------------------------------------------------------------------------

echo &quot;--------&quot;

# Remove old build/ directory
buildDir=&quot;${WM_PROJECT_DIR}/build/${WM_OPTIONS}/${PWD##*/}&quot;
if [ -d &quot;$buildDir&quot; ]
then
    echo &quot;Removing old build directory: $buildDir&quot; 1&gt;&amp;2
    rm -rf -- &quot;$buildDir&quot;
fi

removeLogs

echo &quot;Cleaning tutorials ...&quot;
foamCleanTutorials -self    # Run recursively but avoid self

echo &quot;--------&quot;

#------------------------------------------------------------------------------</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/Allclean">源码与说明</a> · <a href="/assets/command-help/allclean.txt">帮助文本</a></p>
