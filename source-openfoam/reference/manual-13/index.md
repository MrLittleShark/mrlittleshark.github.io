---
title: "13 典型算例运行流程"
layout: reference
description: "OpenCFD v2512 典型算例运行流程；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h3>13.1 方腔流动串行计算</h3>
<p>将官方方腔教程复制至新的 cavity2512 工作目录，依次生成网格、检查网格、求解并提取日志。</p>
<pre><code class="language-bash">mkdir -p "&#36;FOAM_RUN"
cp -a "&#36;FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" \
      "&#36;FOAM_RUN/cavity2512"
cd "&#36;FOAM_RUN/cavity2512"
blockMesh &gt; log.blockMesh 2&gt;&amp;1
checkMesh &gt; log.checkMesh 2&gt;&amp;1
icoFoam &gt; log.icoFoam 2&gt;&amp;1
foamLog log.icoFoam
paraFoam -builtin</code></pre>
<p>各步骤成功后再执行下一步。方腔教程的流动条件由几何尺度、速度和运动黏度共同确定。</p>
<h3>13.2 并行计算</h3>
<p>下例采用 simpleFoam 和 4 个 MPI 进程。执行前完成初始场设置，并在 decomposeParDict 中将 numberOfSubdomains 设为 4。</p>
<pre><code class="language-bash">decomposePar &gt; log.decomposePar 2&gt;&amp;1
mpirun -np 4 simpleFoam -parallel &gt; log.simpleFoam 2&gt;&amp;1
reconstructPar -latestTime &gt; log.reconstructPar 2&gt;&amp;1
foamToVTK -latestTime -fields '(U p)'</code></pre>
<p>并行网格生成后，按需先用 reconstructParMesh 重构网格，再重构场。部分格式转换器仅支持串行。采用 Slurm 等调度系统时，通过作业脚本申请资源并启动计算。</p>
<h3>13.3 续算与停止</h3>
<pre><code class="language-bash">foamDictionary system/controlDict -entry startFrom -set latestTime
foamDictionary system/controlDict -entry endTime -set 2
pimpleFoam &gt; log.restart 2&gt;&amp;1</code></pre>
<p>并行续算采用 -parallel，各 processor 目录应具有一致的时刻和网格数据。运行中将 stopAt 设为 writeNow 或 nextWrite，可在写出结果后停止；该操作要求 runTimeModifiable 为 true，且求解器在运行中读取控制字典。</p>
<pre><code class="language-bash">foamDictionary system/controlDict -entry stopAt -set writeNow</code></pre>
<p>再次启动前将 stopAt 恢复为 endTime；保留 writeNow 会使程序在启动后即停止。</p>
<h3>13.4 Allrun 模板</h3>
<pre><code class="language-bash">#!/bin/bash
set -e
cd "&#36;(dirname "$0")"
. "&#36;WM_PROJECT_DIR/bin/tools/RunFunctions"

# 使用 0.orig 恢复初始场时，取消下一行注释
# restore0Dir
runApplication blockMesh
runApplication checkMesh
# 使用 setFields 初始化时，取消下一行注释
# runApplication setFields
runApplication decomposePar
runParallel "&#36;(getApplication)"
runApplication reconstructPar -latestTime</code></pre>
<p>runApplication 和 runParallel 自动记录日志，并按已有日志决定是否跳过执行。重新运行前应处理对应日志。Allclean 的清理范围应限定于本算例可重新生成的文件。</p>
<h3>13.5 一维激波管计算</h3>
<p>v2512 的一维激波管教程位于 tutorials/compressible/rhoCentralFoam/shockTube。其 fvSchemes 采用 fluxScheme Kurganov，并分别设置 reconstruct(rho) vanLeer、reconstruct(U) vanLeerV 和 reconstruct(T) vanLeer，以完成可压缩流变量重构。</p>
<pre><code class="language-bash">cp -a "&#36;FOAM_TUTORIALS/compressible/rhoCentralFoam/shockTube" \
      "&#36;FOAM_RUN/shockTube2512"
cd "&#36;FOAM_RUN/shockTube2512"
less Allrun
./Allrun</code></pre>
<p>Allrun 定义该教程的网格、初值和求解步骤。验证结果时，可与解析解或基准解比较波前位置、压力和密度分布，并分析网格及时间步敏感性。</p>
{% endraw %}
