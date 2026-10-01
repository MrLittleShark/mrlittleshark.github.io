---
title: "13 典型算例运行流程"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 1
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM_v2512命令与配置参考手册（GPT整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><h3>13.1 方腔流动串行计算</h3>
<p>将官方方腔教程复制至新的 cavity2512 工作目录，依次生成网格、检查网格、求解并提取日志。</p>
<pre><code>mkdir -p &quot;$FOAM_RUN&quot;
cp -a &quot;$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity&quot; \
      &quot;$FOAM_RUN/cavity2512&quot;
cd &quot;$FOAM_RUN/cavity2512&quot;
blockMesh &gt; log.blockMesh 2&gt;&amp;1
checkMesh &gt; log.checkMesh 2&gt;&amp;1
icoFoam &gt; log.icoFoam 2&gt;&amp;1
foamLog log.icoFoam
paraFoam -builtin</code></pre>
<p>各步骤成功后再执行下一步。方腔教程的流动条件由几何尺度、速度和运动黏度共同确定。</p>
<h3>13.2 并行计算</h3>
<p>下例采用 simpleFoam 和 4 个 MPI 进程。执行前完成初始场设置，并在 decomposeParDict 中将 numberOfSubdomains 设为 4。</p>
<pre><code>decomposePar &gt; log.decomposePar 2&gt;&amp;1
mpirun -np 4 simpleFoam -parallel &gt; log.simpleFoam 2&gt;&amp;1
reconstructPar -latestTime &gt; log.reconstructPar 2&gt;&amp;1
foamToVTK -latestTime -fields &#x27;(U p)&#x27;</code></pre>
<p>并行网格生成后，按需先用 reconstructParMesh 重构网格，再重构场。部分格式转换器仅支持串行。采用 Slurm 等调度系统时，通过作业脚本申请资源并启动计算。</p>
<h3>13.3 续算与停止</h3>
<pre><code>foamDictionary system/controlDict -entry startFrom -set latestTime
foamDictionary system/controlDict -entry endTime -set 2
pimpleFoam &gt; log.restart 2&gt;&amp;1</code></pre>
<p>并行续算采用 -parallel，各 processor 目录应具有一致的时刻和网格数据。运行中将 stopAt 设为 writeNow 或 nextWrite，可在写出结果后停止；该操作要求 runTimeModifiable 为 true，且求解器在运行中读取控制字典。</p>
<pre><code>foamDictionary system/controlDict -entry stopAt -set writeNow</code></pre>
<p>再次启动前将 stopAt 恢复为 endTime；保留 writeNow 会使程序在启动后即停止。</p>
<h3>13.4 Allrun 模板</h3>
<pre><code>#!/bin/bash
set -e
cd &quot;$(dirname &quot;$0&quot;)&quot;
. &quot;$WM_PROJECT_DIR/bin/tools/RunFunctions&quot;

# 使用 0.orig 恢复初始场时，取消下一行注释
# restore0Dir
runApplication blockMesh
runApplication checkMesh
# 使用 setFields 初始化时，取消下一行注释
# runApplication setFields
runApplication decomposePar
runParallel &quot;$(getApplication)&quot;
runApplication reconstructPar -latestTime</code></pre>
<p>runApplication 和 runParallel 自动记录日志，并按已有日志决定是否跳过执行。重新运行前应处理对应日志。Allclean 的清理范围应限定于本算例可重新生成的文件。</p>
<h3>13.5 一维激波管计算</h3>
<p>v2512 的一维激波管教程位于 tutorials/compressible/rhoCentralFoam/shockTube。其 fvSchemes 采用 fluxScheme Kurganov，并分别设置 reconstruct(rho) vanLeer、reconstruct(U) vanLeerV 和 reconstruct(T) vanLeer，以完成可压缩流变量重构。</p>
<pre><code>cp -a &quot;$FOAM_TUTORIALS/compressible/rhoCentralFoam/shockTube&quot; \
      &quot;$FOAM_RUN/shockTube2512&quot;
cd &quot;$FOAM_RUN/shockTube2512&quot;
less Allrun
./Allrun</code></pre>
<p>Allrun 定义该教程的网格、初值和求解步骤。验证结果时，可与解析解或基准解比较波前位置、压力和密度分布，并分析网格及时间步敏感性。</p>
{% endraw %}