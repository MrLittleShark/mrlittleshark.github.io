---
title: "fieldExtents"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-fieldextents"
description: "场值超过阈值的空间范围"
---
{% raw %}
<p>场值超过阈值的空间范围</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    fieldExtents
    {
        type            fieldExtents;
        libs            (fieldFunctionObjects);
        region          wallFilmRegion;
        threshold       0.5;
        fields          (alpha);
        internalField   yes;
        patches         ();
    }
}</code></pre><p>求字段超过 threshold 的区域在空间中的包围范围。本例在 wallFilmRegion 中以 alpha&gt;0.5 识别液膜覆盖区域，fields、region 和 threshold 共同决定统计对象。</p><p>配套教程配置：<code>lagrangian/reactingParcelFoam/rivuletPanel/system/controlDict</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>fieldExtents</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>threshold</code></td><td>用于区分有效区域的场值阈值。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>internalField</code></td><td>是否把内部单元纳入范围统计。</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>referencePosition</code></td><td>计算范围所采用的参考位置。</td><td>可选</td><td><code>(0 0 0)</code></td></tr><tr><td><code>patches</code></td><td>需要处理的边界名称列表；支持名称匹配表达式。</td><td>可选</td><td><code>\&lt;all patches\&gt;</code></td></tr><tr><td><code>writeToFile</code></td><td>是否保存统计文本文件</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>writePrecision</code></td><td>文本数值的有效位数</td><td>可选</td><td><code>全局写出精度</code></td></tr><tr><td><code>useUserTime</code></td><td>是否采用用户时间单位</td><td>可选</td><td><code>true</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>求字段超过 threshold 的区域在空间中的包围范围。本例在 wallFilmRegion 中以 alpha&gt;0.5 识别液膜覆盖区域，fields、region 和 threshold 共同决定统计对象。</p><pre><code class="language-foam">fieldExtents
{
    type            fieldExtents;
    libs            (fieldFunctionObjects);
    region          wallFilmRegion;
    threshold       0.5;
    fields          (alpha);
    internalField   yes;
    patches         ();
}</code></pre><h3 id="example-2">示例 2 · 放宽识别阈值</h3><p>把较薄的液膜也纳入范围统计。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">threshold 0.1;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">fieldExtents
{
    type            fieldExtents;
    libs            (fieldFunctionObjects);
    region          wallFilmRegion;
    threshold 0.1;
    fields          (alpha);
    internalField   yes;
    patches         ();
}</code></pre></details><h3 id="example-3">示例 3 · 收紧识别阈值</h3><p>聚焦相分数更高的连续液体区域。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">threshold 0.9;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">fieldExtents
{
    type            fieldExtents;
    libs            (fieldFunctionObjects);
    region          wallFilmRegion;
    threshold 0.9;
    fields          (alpha);
    internalField   yes;
    patches         ();
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">fieldExtents
{
    type            fieldExtents;
    libs            (fieldFunctionObjects);
    region          wallFilmRegion;
    threshold       0.5;
    fields          (alpha);
    internalField   yes;
    patches         ();
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">fieldExtents
{
    type            fieldExtents;
    libs            (fieldFunctionObjects);
    region          wallFilmRegion;
    threshold       0.5;
    fields          (alpha);
    internalField   yes;
    patches         ();
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/fieldExtents/fieldExtents.H">OpenFOAM v2512 · fieldExtents 接口</a>。</p>
{% endraw %}
