---
title: "regionSizeDistribution"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-regionsizedistribution"
description: "统计连通相区域的等效直径分布。"
---
{% raw %}
<p>统计连通相区域的等效直径分布。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    regionSizeDistribution1
    {
        type            regionSizeDistribution;
        libs            (fieldFunctionObjects);
        field           alpha.air;
        patches         (inlet);
        fields          (p U);
        threshold       0.5;
        maxDiameter     0.5;
        nBins           100;
        setFormat       gnuplot;
        minDiameter     0.0;
        isoPlanes       false;
        writePrecision  12;
        writeToFile     true;
        useUserTime     true;
        region          region0;
        enabled         true;
        log             true;
        timeStart       0;
        timeEnd         1000;
        executeControl  onEnd;
        writeControl    onEnd;
    }
}</code></pre><p>按相分数阈值识别连通区域，计算等效直径和分布。本例用 alpha.air&gt;0.5 识别区域，并通过 inlet 区分与入口相连的核心区域；统计范围由直径上下限和箱数决定。</p><p>配套教程配置：<code>multiphase/twoPhaseEulerFoam/RAS/bubbleColumn/system/controlDict</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>regionSizeDistribution</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>field</code></td><td>输入场的名称。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>patches</code></td><td>需要处理的边界名称列表；支持名称匹配表达式。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>threshold</code></td><td>用于区分有效区域的场值阈值。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>maxDiameter</code></td><td>统计或识别的最大直径。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>minDiameter</code></td><td>统计或识别的最小直径。</td><td>可选</td><td><code>0.0</code></td></tr><tr><td><code>nBins</code></td><td>分箱数量；数量增加可以观察更细的分布。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>setFormat</code></td><td>点集或线采样的输出格式，例如 raw、csv、vtk。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>isoPlanes</code></td><td>是否启用沿下游位置的分布统计。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>origin</code></td><td>局部坐标系或旋转轴的原点。</td><td>isoPlanes 为 true 时</td><td><code>—</code></td></tr><tr><td><code>direction</code></td><td>追踪方向或几何方向，具体含义见本页配置。</td><td>isoPlanes 为 true 时</td><td><code>—</code></td></tr><tr><td><code>maxD</code></td><td>isoPlanes 模式下采样圆柱的最大直径。</td><td>isoPlanes 为 true 时</td><td><code>—</code></td></tr><tr><td><code>nDownstreamBins</code></td><td>下游方向的分箱数量。</td><td>isoPlanes 为 true 时</td><td><code>—</code></td></tr><tr><td><code>maxDownstream</code></td><td>从原点起的最大下游距离。</td><td>isoPlanes 为 true 时</td><td><code>—</code></td></tr><tr><td><code>writeToFile</code></td><td>是否保存统计文本文件</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>writePrecision</code></td><td>文本数值的有效位数</td><td>可选</td><td><code>全局写出精度</code></td></tr><tr><td><code>useUserTime</code></td><td>是否采用用户时间单位</td><td>可选</td><td><code>true</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>按相分数阈值识别连通区域，计算等效直径和分布。本例用 alpha.air&gt;0.5 识别区域，并通过 inlet 区分与入口相连的核心区域；统计范围由直径上下限和箱数决定。</p><pre><code class="language-foam">regionSizeDistribution1
{
    type            regionSizeDistribution;
    libs            (fieldFunctionObjects);
    field           alpha.air;
    patches         (inlet);
    fields          (p U);
    threshold       0.5;
    maxDiameter     0.5;
    nBins           100;
    setFormat       gnuplot;
    minDiameter     0.0;
    isoPlanes       false;
    writePrecision  12;
    writeToFile     true;
    useUserTime     true;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         1000;
    executeControl  onEnd;
    writeControl    onEnd;
}</code></pre><h3 id="example-2">示例 2 · 减少粒径箱数</h3><p>在相同直径范围内使用更宽的箱，观察总体分布。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">nBins 50;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">regionSizeDistribution1
{
    type            regionSizeDistribution;
    libs            (fieldFunctionObjects);
    field           alpha.air;
    patches         (inlet);
    fields          (p U);
    threshold       0.5;
    maxDiameter     0.5;
    nBins 50;
    setFormat       gnuplot;
    minDiameter     0.0;
    isoPlanes       false;
    writePrecision  12;
    writeToFile     true;
    useUserTime     true;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         1000;
    executeControl  onEnd;
    writeControl    onEnd;
}</code></pre></details><h3 id="example-3">示例 3 · 聚焦小尺度区域</h3><p>收窄直径统计范围，并保留较细的分箱。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">maxDiameter 0.1;
nBins 50;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">regionSizeDistribution1
{
    type            regionSizeDistribution;
    libs            (fieldFunctionObjects);
    field           alpha.air;
    patches         (inlet);
    fields          (p U);
    threshold       0.5;
    maxDiameter 0.1;
    nBins 50;
    setFormat       gnuplot;
    minDiameter     0.0;
    isoPlanes       false;
    writePrecision  12;
    writeToFile     true;
    useUserTime     true;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         1000;
    executeControl  onEnd;
    writeControl    onEnd;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">regionSizeDistribution1
{
    type            regionSizeDistribution;
    libs            (fieldFunctionObjects);
    field           alpha.air;
    patches         (inlet);
    fields          (p U);
    threshold       0.5;
    maxDiameter     0.5;
    nBins           100;
    setFormat       gnuplot;
    minDiameter     0.0;
    isoPlanes       false;
    writePrecision  12;
    writeToFile     true;
    useUserTime     true;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         1000;
    executeControl  onEnd;
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">regionSizeDistribution1
{
    type            regionSizeDistribution;
    libs            (fieldFunctionObjects);
    field           alpha.air;
    patches         (inlet);
    fields          (p U);
    threshold       0.5;
    maxDiameter     0.5;
    nBins           100;
    setFormat       gnuplot;
    minDiameter     0.0;
    isoPlanes       false;
    writePrecision  12;
    writeToFile     true;
    useUserTime     true;
    region          region0;
    enabled         true;
    log             true;
    timeStart 0.1;
    timeEnd 0.5;
    executeControl  onEnd;
    writeControl    onEnd;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%A2%97%E7%B2%92%E4%B8%8E%E4%B8%A4%E7%9B%B8">颗粒与两相速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-12">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/regionSizeDistribution/regionSizeDistribution.H">OpenFOAM v2512 · regionSizeDistribution 接口</a>。</p>
{% endraw %}
