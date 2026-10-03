---
title: "nearWallFields"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-nearwallfields"
description: "距壁面指定距离处采样"
---
{% raw %}
<p>距壁面指定距离处采样</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    near
    {
        type    nearWallFields;
        libs    (fieldFunctionObjects);
        writeControl    writeTime;
        executeControl  writeTime;
        fields
        (
            (U UNear)
        );
        patches         (motorBikeGroup);
        distance        0.001;
    }
}</code></pre><p>沿壁面法向在给定距离处采样，把结果保存在新的字段中。本例距离为 0.001 m，输入 U、输出 UNear，供沿壁面流线追踪使用。</p><p>配套教程配置：<code>incompressible/simpleFoam/motorBike/system/wallBoundedStreamLines</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>nearWallFields</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>fields</code></td><td>输入、输出字段名称对，例如 ((U UNear))。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>patches</code></td><td>需要处理的边界名称列表；支持名称匹配表达式。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>distance</code></td><td>沿壁面法向离开壁面的采样距离。</td><td>必填</td><td><code>—</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>沿壁面法向在给定距离处采样，把结果保存在新的字段中。本例距离为 0.001 m，输入 U、输出 UNear，供沿壁面流线追踪使用。</p><pre><code class="language-foam">near
{
    type    nearWallFields;
    libs    (fieldFunctionObjects);
    writeControl    writeTime;
    executeControl  writeTime;
    fields
    (
        (U UNear)
    );
    patches         (motorBikeGroup);
    distance        0.001;
}</code></pre><h3 id="example-2">示例 2 · 靠近壁面采样</h3><p>把采样高度从 1 mm 改为 0.5 mm，分析更近壁面的速度。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">distance 0.0005;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">near
{
    type    nearWallFields;
    libs    (fieldFunctionObjects);
    writeControl    writeTime;
    executeControl  writeTime;
    fields
    (
        (U UNear)
    );
    patches         (motorBikeGroup);
    distance 0.0005;
}</code></pre></details><h3 id="example-3">示例 3 · 远离壁面采样</h3><p>把采样高度增至 2 mm，与较低采样高度的结果对照。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">distance 0.002;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">near
{
    type    nearWallFields;
    libs    (fieldFunctionObjects);
    writeControl    writeTime;
    executeControl  writeTime;
    fields
    (
        (U UNear)
    );
    patches         (motorBikeGroup);
    distance 0.002;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">near
{
    type    nearWallFields;
    libs    (fieldFunctionObjects);
    writeControl timeStep;
    executeControl  writeTime;
    fields
    (
        (U UNear)
    );
    patches         (motorBikeGroup);
    distance        0.001;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">near
{
    type    nearWallFields;
    libs    (fieldFunctionObjects);
    writeControl    writeTime;
    executeControl  writeTime;
    fields
    (
        (U UNear)
    );
    patches         (motorBikeGroup);
    distance        0.001;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/nearWallFields/nearWallFields.H">OpenFOAM v2512 · nearWallFields 接口</a>。</p>
{% endraw %}
