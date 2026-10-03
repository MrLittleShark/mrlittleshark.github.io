---
title: "fieldMinMax"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-fieldminmax"
description: "记录场的最小值、最大值及其位置。"
---
{% raw %}
<p>记录场的最小值、最大值及其位置。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    waterRange
    {
        type fieldMinMax;
        libs (fieldFunctionObjects);

        writeControl timeStep;
        writeInterval 10;
        fields (alpha.water);
    }
}</code></pre><p>逐次记录所选场的最小值和最大值。本例监测 alpha.water，可从输出中查看相分数的取值范围；对于向量场，mode 决定按模还是按分量比较。</p><p>示例算例：溃坝两相流。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>fieldMinMax</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>location</code></td><td>是否输出极值所在位置。</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>mode</code></td><td>magnitude 按模比较，component 按分量比较。</td><td>可选</td><td><code>magnitude</code></td></tr><tr><td><code>writeToFile</code></td><td>是否保存统计文本文件</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>writePrecision</code></td><td>文本数值的有效位数</td><td>可选</td><td><code>全局写出精度</code></td></tr><tr><td><code>useUserTime</code></td><td>是否采用用户时间单位</td><td>可选</td><td><code>true</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>逐次记录所选场的最小值和最大值。本例监测 alpha.water，可从输出中查看相分数的取值范围；对于向量场，mode 决定按模还是按分量比较。</p><pre><code class="language-foam">waterRange
{
    type fieldMinMax;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    fields (alpha.water);
}</code></pre><h3 id="example-2">示例 2 · 同时监测相分数和速度</h3><p>速度按模比较，输出最大速度所在位置；相分数仍按标量统计。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">fields (alpha.water U);
mode magnitude;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">waterRange
{
    type fieldMinMax;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    fields (alpha.water U);
    mode magnitude;
}</code></pre></details><h3 id="example-3">示例 3 · 仅保存极值而省略坐标</h3><p>当只需要绘制极值随时间变化的曲线时，可以缩短每行输出。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">location false;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">waterRange
{
    type fieldMinMax;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    fields (alpha.water);
    location false;
}</code></pre></details><h3 id="example-4">示例 4 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">waterRange
{
    type fieldMinMax;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    fields (alpha.water);
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h3 id="example-5">示例 5 · 每五步保存一次</h3><p>采用五步间隔，在时间分辨率与数据量之间选择适合当前计算的输出频率。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">waterRange
{
    type fieldMinMax;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 5;
    fields (alpha.water);
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-05">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/fieldMinMax/fieldMinMax.H">OpenFOAM v2512 · fieldMinMax 接口</a>。</p>
{% endraw %}
