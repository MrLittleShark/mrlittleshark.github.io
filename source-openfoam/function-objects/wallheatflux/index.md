---
title: "wallHeatFlux"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-wallheatflux"
description: "计算壁面热流密度与热流积分。"
---
{% raw %}
<p>计算壁面热流密度与热流积分。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    wallHeatFlux
    {
        type wallHeatFlux;
        libs (fieldFunctionObjects);

        writeControl writeTime;
        writeInterval 1;
        model wall;
    }
}</code></pre><p>从传热模型计算壁面热流密度。本例 model wall 用于热房间壁面，输出各壁面的最小值、最大值和面积积分；热流积分可用于比较壁面的净传热。</p><p>示例算例：浮力传热房间。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>wallHeatFlux</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>model</code></td><td>wall 计算壁面热流；gauge 模拟指定温度的热流计。</td><td>可选</td><td><code>wall</code></td></tr><tr><td><code>patches</code></td><td>wall 模型：需要处理的边界名称列表；支持名称匹配表达式。</td><td>可选</td><td><code>所有 wall 类型边界</code></td></tr><tr><td><code>qr</code></td><td>wall 模型：辐射热流密度场名称。</td><td>可选</td><td><code>qr</code></td></tr><tr><td><code>patch</code></td><td>gauge 模型：需要处理的单个边界名称。</td><td>gauge 中必填</td><td><code>—</code></td></tr><tr><td><code>Tgauge</code></td><td>gauge 模型：热流计温度，单位 K。</td><td>gauge 中必填</td><td><code>—</code></td></tr><tr><td><code>absorptivity</code></td><td>gauge 模型：热流计的吸收率。</td><td>gauge 中可选</td><td><code>1</code></td></tr><tr><td><code>emissivity</code></td><td>gauge 模型：热流计的发射率。</td><td>gauge 中可选</td><td><code>1</code></td></tr><tr><td><code>T</code></td><td>gauge 模型：温度场名称。</td><td>gauge 中可选</td><td><code>T</code></td></tr><tr><td><code>qin</code></td><td>gauge 模型：入射辐射热流密度场名称。</td><td>gauge 中可选</td><td><code>qin</code></td></tr><tr><td><code>alphat</code></td><td>gauge 模型：湍流热扩散场名称。</td><td>gauge 中可选</td><td><code>alphat</code></td></tr><tr><td><code>convective</code></td><td>gauge 模型：是否输出对流热流。</td><td>gauge 中可选</td><td><code>true</code></td></tr><tr><td><code>radiative</code></td><td>gauge 模型：是否输出辐射热流。</td><td>gauge 中可选</td><td><code>true</code></td></tr><tr><td><code>writeFields</code></td><td>gauge 模型：gauge 模式下是否保存 qConv 和 qRad。</td><td>gauge 中可选</td><td><code>true</code></td></tr><tr><td><code>writeToFile</code></td><td>是否保存统计文本文件</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>writePrecision</code></td><td>文本数值的有效位数</td><td>可选</td><td><code>全局写出精度</code></td></tr><tr><td><code>useUserTime</code></td><td>是否采用用户时间单位</td><td>可选</td><td><code>true</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>从传热模型计算壁面热流密度。本例 model wall 用于热房间壁面，输出各壁面的最小值、最大值和面积积分；热流积分可用于比较壁面的净传热。</p><pre><code class="language-foam">wallHeatFlux
{
    type wallHeatFlux;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    model wall;
}</code></pre><h3 id="example-2">示例 2 · 只统计地板</h3><p>把热流统计限制在供热地板上，积分值对应该边界的总传热率。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">patches (floor);</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallHeatFlux
{
    type wallHeatFlux;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    model wall;
    patches (floor);
}</code></pre></details><h3 id="example-3">示例 3 · 同时比较地板和顶板</h3><p>在同一输出频率下对照两个边界的热流，观察热量进入与离开房间的过程。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">patches (floor ceiling);</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallHeatFlux
{
    type wallHeatFlux;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    model wall;
    patches (floor ceiling);
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallHeatFlux
{
    type wallHeatFlux;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    model wall;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallHeatFlux
{
    type wallHeatFlux;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    model wall;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-11">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/wallHeatFlux/wallHeatFlux.H">OpenFOAM v2512 · wallHeatFlux 接口</a>。</p>
{% endraw %}
