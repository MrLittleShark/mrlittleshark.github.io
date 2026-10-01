---
title: "第 12 章　system/controlDict"
layout: reference
description: "OpenCFD v2512 system/controlDict；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>它管什么：算多久、多久输出一次、用什么求解器、跑哪些后处理。每个算例必需。</p>
<h2>12.1 完整参数表</h2>
<div class="table-scroll"><table>
<tr><th>关键字</th><th>可选值</th><th>含义</th><th>备注</th></tr>
<tr><td>application</td><td>求解器名</td><td>记录用哪个求解器</td><td>只是记录；Allrun 里 getApplication 读它</td></tr>
<tr><td>startFrom</td><td>firstTime / startTime / latestTime</td><td>从哪开始</td><td>续算用 latestTime</td></tr>
<tr><td>startTime</td><td>数值</td><td>startFrom startTime 时的起始时刻</td><td></td></tr>
<tr><td>stopAt</td><td>endTime / writeNow / noWriteNow / nextWrite</td><td>何时停</td><td>见 7.5</td></tr>
<tr><td>endTime</td><td>数值</td><td>结束时刻</td><td>稳态求解器里是”最大迭代步数”</td></tr>
<tr><td>deltaT</td><td>数值</td><td>时间步长</td><td>稳态时通常写 1</td></tr>
<tr><td>writeControl</td><td>timeStep / runTime / adjustableRunTime / cpuTime / clockTime</td><td>按什么控制输出</td><td>变步长时用 adjustableRunTime</td></tr>
<tr><td>writeInterval</td><td>数值</td><td>输出间隔</td><td>配合上一条</td></tr>
<tr><td>purgeWrite</td><td>整数</td><td>只保留最近 N 个时间目录，0 = 全保留</td><td>长算例防止撑爆硬盘</td></tr>
<tr><td>writeFormat</td><td>ascii / binary</td><td>结果文件格式</td><td>大算例用 binary，省一半空间且快</td></tr>
<tr><td>writePrecision</td><td>整数（默认 6）</td><td>输出有效数字</td><td></td></tr>
<tr><td>writeCompression</td><td>on / off</td><td>是否 gzip 压缩</td><td>硬盘紧张时开</td></tr>
<tr><td>timeFormat</td><td>general / fixed / scientific</td><td>时间目录名格式</td><td></td></tr>
<tr><td>timePrecision</td><td>整数（默认 6）</td><td>时间目录名的有效数字</td><td>步长很小时要调大，否则目录重名</td></tr>
<tr><td>runTimeModifiable</td><td>true / false</td><td>允许运行中改字典</td><td>建议一直开着</td></tr>
<tr><td>adjustTimeStep</td><td>yes / no</td><td>自适应时间步</td><td>瞬态常用</td></tr>
<tr><td>maxCo</td><td>数值</td><td>最大 Courant 数</td><td>配合上一条</td></tr>
<tr><td>maxAlphaCo</td><td>数值</td><td>界面处最大 Co（VOF）</td><td>interFoam 类</td></tr>
<tr><td>maxDeltaT</td><td>数值</td><td>时间步上限</td><td>防止步长失控变大</td></tr>
<tr><td>graphFormat</td><td>raw / gnuplot / csv</td><td>曲线输出格式</td><td></td></tr>
<tr><td>libs</td><td>库名列表</td><td>运行时加载额外库</td><td>用自定义边界条件时</td></tr>
<tr><td>functions</td><td>子字典</td><td>functionObject 列表</td><td>见第 8 章</td></tr>
<tr><td>DebugSwitches</td><td>子字典</td><td>打开某个类的调试输出</td><td>排查疑难问题时</td></tr>
<tr><td>OptimisationSwitches</td><td>子字典</td><td>fileHandler、I/O 缓冲等</td><td>大规模并行时</td></tr>
</table></div>
<h2>12.2 两个典型例子</h2>
<p>瞬态（interFoam 溃坝）</p>
<pre><code class="language-openfoam">application     interFoam;
startFrom       startTime;
startTime       0;
stopAt          endTime;
endTime         1;
deltaT          0.001;
writeControl    adjustableRunTime;    // 按物理时间等间隔输出，且不打乱变步长
writeInterval   0.05;
purgeWrite      0;
writeFormat     binary;
writePrecision  6;
writeCompression off;
timeFormat      general;
timePrecision   6;
runTimeModifiable yes;
adjustTimeStep  yes;
maxCo           1;
maxAlphaCo      1;
maxDeltaT       1;</code></pre>
<p>稳态（simpleFoam）</p>
<pre><code class="language-openfoam">application     simpleFoam;
startFrom       latestTime;
stopAt          endTime;
endTime         2000;         // ← 稳态时这是"最多迭代 2000 步"
deltaT          1;            // ← 稳态时步长无物理意义，写 1
writeControl    timeStep;
writeInterval   200;          // 每 200 步存一次
runTimeModifiable yes;

functions
{
    #includeFunc solverInfo
    #includeFunc yPlus
}</code></pre>
<p>writeControl 到底选哪个：变步长（adjustTimeStep yes）时选 runTime 会导致输出时刻对不齐（步长恰好跨过输出时刻就跳过了）；adjustableRunTime 会微调步长让它正好落在输出时刻上，这才是变步长算例的正确选择。做动画时尤其重要——帧间隔必须均匀。</p><h2>v2512 的残差记录接口</h2><p>使用 <code>type solverInfo</code>，并加载 <code>utilityFunctionObjects</code>。<code>#includeFunc solverInfo</code> 的官方模板默认选择 p 和 U；如需其他字段，应复制模板并修改 fields。此功能读取求解过程中的 solverPerformance 数据，事后只读取已写出的 U、p 不能重建历史残差。</p><p><a href="/dictionaries/functions-solverinfo/">完整配置、字段解释与三个 v2512 示例</a></p>
{% endraw %}
