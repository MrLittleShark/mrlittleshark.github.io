---
title: "randomise"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-randomise"
description: "给场添加随机扰动"
---
{% raw %}
<p>给场添加随机扰动</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    randomise1
    {
        type            randomise;
        libs            (fieldFunctionObjects);
        magPerturbation 0.1;
        field           U;
        region          region0;
        enabled         true;
        log             true;
        timeStart       0.25;
        timeEnd         1000;
        executeControl  timeStep;
        executeInterval 5;
        writeControl    timeStep;
        writeInterval   25;
    }
}</code></pre><p>为输入场加入给定幅值的随机扰动。本例以 U 为输入、magPerturbation 0.1 为扰动尺度，可用于准备带扰动的初始流动。</p><p>配套教程配置：<code>incompressible/pisoFoam/RAS/cavity/system/FOs/FOrandomise</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>randomise</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>magPerturbation</code></td><td>随机扰动幅值。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>field</code></td><td>输入场的名称。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>result</code></td><td>生成的结果场名称，用于区分输入场和输出场。</td><td>可选</td><td><code>工具默认名称</code></td></tr><tr><td><code>cellZones</code></td><td>参与统计的单元区域名称列表。</td><td>可选</td><td><code>全域</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>为输入场加入给定幅值的随机扰动。本例以 U 为输入、magPerturbation 0.1 为扰动尺度，可用于准备带扰动的初始流动。</p><pre><code class="language-foam">randomise1
{
    type            randomise;
    libs            (fieldFunctionObjects);
    magPerturbation 0.1;
    field           U;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0.25;
    timeEnd         1000;
    executeControl  timeStep;
    executeInterval 5;
    writeControl    timeStep;
    writeInterval   25;
}</code></pre><h3 id="example-2">示例 2 · 减小扰动</h3><p>把扰动幅值缩小十倍，观察初始扰动强度对后续流动的影响。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">magPerturbation 0.01;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">randomise1
{
    type            randomise;
    libs            (fieldFunctionObjects);
    magPerturbation 0.01;
    field           U;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0.25;
    timeEnd         1000;
    executeControl  timeStep;
    executeInterval 5;
    writeControl    timeStep;
    writeInterval   25;
}</code></pre></details><h3 id="example-3">示例 3 · 增大扰动</h3><p>增加初始扰动幅值，比较流动响应时保持其他计算条件相同。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">magPerturbation 0.2;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">randomise1
{
    type            randomise;
    libs            (fieldFunctionObjects);
    magPerturbation 0.2;
    field           U;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0.25;
    timeEnd         1000;
    executeControl  timeStep;
    executeInterval 5;
    writeControl    timeStep;
    writeInterval   25;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">randomise1
{
    type            randomise;
    libs            (fieldFunctionObjects);
    magPerturbation 0.1;
    field           U;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0.25;
    timeEnd         1000;
    executeControl  timeStep;
    executeInterval 5;
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">randomise1
{
    type            randomise;
    libs            (fieldFunctionObjects);
    magPerturbation 0.1;
    field           U;
    region          region0;
    enabled         true;
    log             true;
    timeStart 0.1;
    timeEnd 0.5;
    executeControl  timeStep;
    executeInterval 5;
    writeControl    timeStep;
    writeInterval   25;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%9C%BA%E8%BF%90%E7%AE%97">场运算速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/randomise/randomise.H">OpenFOAM v2512 · randomise 接口</a>。</p>
{% endraw %}
