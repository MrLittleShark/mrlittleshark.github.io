---
title: "volFieldValue"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-volfieldvalue"
description: "对体区域计算平均、积分或其他归约值。"
---
{% raw %}
<p>对体区域计算平均、积分或其他归约值。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    meanTemperature
    {
        type volFieldValue;
        libs (fieldFunctionObjects);

        writeControl timeStep;
        writeInterval 1;
        regionType all;
        operation volAverage;
        fields (T);
        writeFields false;
    }
}</code></pre><p>本例在整个热房间区域统计 T 的体积加权平均值。volAverage 使大小不同的单元按各自体积贡献权重，结果可直接作为域平均温度。</p><p>示例算例：浮力传热房间。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>volFieldValue</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>regionType</code></td><td>all 选择全域，cellZone 选择命名单元区。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>operation</code></td><td>对输入数据执行的运算。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>postOperation</code></td><td>主运算之后的附加运算，例如 none、mag 或 sqrt。</td><td>可选</td><td><code>none</code></td></tr><tr><td><code>weightField</code></td><td>进行加权统计时采用的权重场。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>weightFields</code></td><td>多个权重场的名称列表。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>name</code></td><td>cellZone 的区域名称</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>writeFields</code></td><td>是否写出所选原始场</td><td>必填</td><td><code>true / false</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h3 id="operations">常用统计操作</h3><div class="table-scroll"><table><thead><tr><th>operation</th><th>计算内容</th></tr></thead><tbody><tr><td><code>sum</code></td><td>单元值之和</td></tr><tr><td><code>average</code></td><td>单元值的算术平均</td></tr><tr><td><code>volAverage</code></td><td>按单元体积加权平均</td></tr><tr><td><code>volIntegrate</code></td><td>单元值与体积相乘后求和</td></tr><tr><td><code>weightedVolAverage</code></td><td>体积与 weightField 共同加权</td></tr><tr><td><code>min / max</code></td><td>最小值 / 最大值</td></tr><tr><td><code>CoV</code></td><td>变异系数</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>本例在整个热房间区域统计 T 的体积加权平均值。volAverage 使大小不同的单元按各自体积贡献权重，结果可直接作为域平均温度。</p><pre><code class="language-foam">meanTemperature
{
    type volFieldValue;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 1;
    regionType all;
    operation volAverage;
    fields (T);
    writeFields false;
}</code></pre><h3 id="example-2">示例 2 · 查看最高温度</h3><p>同样选择全部单元，但改为找 T 的最大值，用于监测局部热点。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">operation max;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">meanTemperature
{
    type volFieldValue;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 1;
    regionType all;
    operation max;
    fields (T);
    writeFields false;
}</code></pre></details><h3 id="example-3">示例 3 · 计算温度的体积积分</h3><p>得到各单元 T×体积的总和，单位为 K·m³。除以总体积后即为体积平均温度；计算热量还需要密度和比热。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">operation volIntegrate;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">meanTemperature
{
    type volFieldValue;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 1;
    regionType all;
    operation volIntegrate;
    fields (T);
    writeFields false;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">meanTemperature
{
    type volFieldValue;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    regionType all;
    operation volAverage;
    fields (T);
    writeFields false;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">meanTemperature
{
    type volFieldValue;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 1;
    regionType all;
    operation volAverage;
    fields (T);
    writeFields false;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-05">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/fieldValues/volFieldValue/volFieldValue.H">OpenFOAM v2512 · volFieldValue 接口</a>。</p>
{% endraw %}
