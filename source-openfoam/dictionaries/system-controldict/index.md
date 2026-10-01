---
title: "system/controlDict"
layout: "reference"
description: "Courant 数由局部速度、通量、单元尺寸和时间步共同决定。可压缩激波计算还需考虑声速约束，时间步上限应结合所用求解器和离散格式确定。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/controlDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>application</code> · <code>startFrom</code> · <code>startTime</code> · <code>stopAt</code> · <code>endTime</code> · <code>deltaT</code> · <code>writeControl</code> · <code>writeInterval</code> · <code>purgeWrite</code> · <code>adjustTimeStep</code> · <code>maxCo</code> · <code>maxAlphaCo</code> · <code>functions</code> · <code>libs</code></p><h2>关联命令</h2><p><a href="/commands/?q=icoFoam">icoFoam</a> · <a href="/commands/?q=interFoam">interFoam</a> · <a href="/commands/?q=simpleFoam">simpleFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/controlDict -keywords
icoFoam -help</code></pre><h2>8.1 system/controlDict</h2><pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object controlDict;
}
application pimpleFoam;
startFrom startTime;
startTime 0;
stopAt endTime;
endTime 1;
deltaT 0.001;
writeControl adjustableRunTime;
writeInterval 0.05;
purgeWrite 0;
writeFormat ascii;
writePrecision 8;
writeCompression off;
timeFormat general;
timePrecision 8;
runTimeModifiable true;
adjustTimeStep true;
maxCo 0.5;
maxDeltaT 0.01;
functions {};</code></pre>
<div class="table-scroll"><table>
<tr><th>参数</th><th>含义与可选值</th><th>设置方法</th></tr>
<tr><td>application</td><td>供运行脚本选择的应用名称</td><td>脚本按此项调用程序；终端直接调用时执行指定程序</td></tr>
<tr><td>startFrom</td><td>startTime、firstTime、latestTime</td><td>续算通常用 latestTime</td></tr>
<tr><td>startTime</td><td>开始时刻</td><td>在采用相应 startFrom 模式时读取</td></tr>
<tr><td>stopAt</td><td>endTime、writeNow、noWriteNow、nextWrite</td><td>指定停止时刻及结果写出方式</td></tr>
<tr><td>endTime</td><td>结束时刻或稳态迭代终点</td><td>稳态求解中的时间可表示迭代计数</td></tr>
<tr><td>deltaT</td><td>时间步或迭代步</td><td>瞬态计算按时间精度及稳定性确定</td></tr>
<tr><td>writeControl</td><td>timeStep、runTime、adjustableRunTime、cpuTime、clockTime 等</td><td>timeStep 下 writeInterval 是步数；runTime 下是模拟时间</td></tr>
<tr><td>writeInterval</td><td>输出间隔</td><td>由 writeControl 确定单位，并按瞬态特征设置间隔</td></tr>
<tr><td>purgeWrite</td><td>仅保留最近若干常规输出时刻</td><td>0 保留全部输出；正整数指定保留的最近时刻数</td></tr>
<tr><td>writeFormat、writePrecision</td><td>格式与有效数字</td><td>ASCII 便于检查；binary 减少 IO</td></tr>
<tr><td>writeCompression</td><td>输出压缩</td><td>on 或 off，后处理软件需支持相应格式</td></tr>
<tr><td>timeFormat、timePrecision</td><td>时间目录命名格式和精度</td><td>精度应能区分相邻输出时刻</td></tr>
<tr><td>runTimeModifiable</td><td>运行中重新读取可修改字典</td><td>可修改范围由模型和求解器的读取机制确定</td></tr>
<tr><td>adjustTimeStep、maxCo、maxDeltaT</td><td>自动时间步控制</td><td>仅在实现相应时间步控制的求解器中生效</td></tr>
<tr><td>maxAlphaCo</td><td>VOF 相分数相关 Courant 限制</td><td>仅相关求解器使用</td></tr>
<tr><td>maxDi</td><td>热扩散数控制</td><td>仅相关传热求解器使用</td></tr>
<tr><td>libs</td><td>加载自定义或功能库</td><td>例如 (&quot;libMyBC.so&quot;)</td></tr>
<tr><td>functions</td><td>运行时函数对象</td><td>见第 10 章</td></tr>
</table></div>
<p>Courant 数由局部速度、通量、单元尺寸和时间步共同决定。可压缩激波计算还需考虑声速约束，时间步上限应结合所用求解器和离散格式确定。</p>
<h2>第 12 章　system/controlDict</h2><p>它管什么：算多久、多久输出一次、用什么求解器、跑哪些后处理。每个算例必需。</p>
{% endraw %}