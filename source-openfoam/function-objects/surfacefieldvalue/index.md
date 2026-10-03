---
title: "surfaceFieldValue"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-surfacefieldvalue"
description: "计算选定表面的流量、平均值或积分。"
---
{% raw %}
<p>计算选定表面的流量、平均值或积分。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    inletFlux
    {
        type surfaceFieldValue;
        libs (fieldFunctionObjects);

        writeControl timeStep;
        writeInterval 10;
        regionType patch;
        name inlet;
        operation sum;
        fields (phi);
        writeFields false;
    }
}</code></pre><p>本例对 pitzDaily 的 inlet 面通量 phi 求和。phi 已包含面面积，因此 sum 给出总流量；入口法向朝外，流入通常表现为负值。</p><p>示例算例：后台阶湍流。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>surfaceFieldValue</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>regionType</code></td><td>patch、faceZone、sampledSurface 等表面选择方式。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>name</code></td><td>所选 patch 或 faceZone 的名称。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>names</code></td><td>额外选择的名称或正则表达式列表。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>operation</code></td><td>对输入数据执行的运算。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>postOperation</code></td><td>主运算之后的附加运算，例如 none、mag 或 sqrt。</td><td>可选</td><td><code>none</code></td></tr><tr><td><code>weightField</code></td><td>进行加权统计时采用的权重场。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>weightFields</code></td><td>多个权重场的名称列表。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>writeArea</code></td><td>是否同时记录所选表面的面积。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>surfaceFormat</code></td><td>表面结果的输出格式，例如 vtk、ensight、raw。</td><td>条件必填</td><td><code>none</code></td></tr><tr><td><code>empty-surface</code></td><td>所选表面为空时采用的处理方式。</td><td>可选</td><td><code>default</code></td></tr><tr><td><code>sampledSurfaceDict</code></td><td>regionType 为 sampledSurface 时的采样表面定义。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>writeFields</code></td><td>是否保存表面采样原始值</td><td>必填</td><td><code>true / false</code></td></tr><tr><td><code>direction</code></td><td>sumDirection 等操作的参考方向</td><td>条件必填</td><td><code>—</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h3 id="operations">常用统计操作</h3><div class="table-scroll"><table><thead><tr><th>operation</th><th>计算内容</th></tr></thead><tbody><tr><td><code>sum</code></td><td>求和；用于 phi 时得到面通量总和</td></tr><tr><td><code>average</code></td><td>各面值的算术平均</td></tr><tr><td><code>areaAverage</code></td><td>按面面积加权平均</td></tr><tr><td><code>areaIntegrate</code></td><td>将场值乘面积后求和</td></tr><tr><td><code>areaNormalAverage</code></td><td>向法向投影后进行面积平均</td></tr><tr><td><code>areaNormalIntegrate</code></td><td>向法向投影后进行面积积分</td></tr><tr><td><code>weightedAreaAverage</code></td><td>同时采用面积和 weightField 加权</td></tr><tr><td><code>min / max</code></td><td>所选面上的最小值 / 最大值</td></tr><tr><td><code>CoV</code></td><td>变异系数</td></tr><tr><td><code>uniformity</code></td><td>均匀性指标</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>本例对 pitzDaily 的 inlet 面通量 phi 求和。phi 已包含面面积，因此 sum 给出总流量；入口法向朝外，流入通常表现为负值。</p><pre><code class="language-foam">inletFlux
{
    type surfaceFieldValue;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    regionType patch;
    name inlet;
    operation sum;
    fields (phi);
    writeFields false;
}</code></pre><h3 id="example-2">示例 2 · 监测出口流量</h3><p>将统计边界改为 outlet。对照入口和出口的总流量可以检查质量或体积收支。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">name outlet;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">inletFlux
{
    type surfaceFieldValue;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    regionType patch;
    name outlet;
    operation sum;
    fields (phi);
    writeFields false;
}</code></pre></details><h3 id="example-3">示例 3 · 计算入口平均压力</h3><p>压力是面上的强度量，使用面积加权平均。areaAverage 与对已积分面通量求和是两种不同的操作。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">fields (p);
operation areaAverage;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">inletFlux
{
    type surfaceFieldValue;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    regionType patch;
    name inlet;
    operation areaAverage;
    fields (p);
    writeFields false;
}</code></pre></details><h3 id="example-4">示例 4 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">inletFlux
{
    type surfaceFieldValue;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    regionType patch;
    name inlet;
    operation sum;
    fields (phi);
    writeFields false;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h3 id="example-5">示例 5 · 每五步保存一次</h3><p>采用五步间隔，在时间分辨率与数据量之间选择适合当前计算的输出频率。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">inletFlux
{
    type surfaceFieldValue;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 5;
    regionType patch;
    name inlet;
    operation sum;
    fields (phi);
    writeFields false;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-06">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/fieldValues/surfaceFieldValue/surfaceFieldValue.H">OpenFOAM v2512 · surfaceFieldValue 接口</a>。</p>
{% endraw %}
