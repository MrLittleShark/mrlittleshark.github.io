---
title: "pressure"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-pressure"
description: "静压、总压和系数转换"
---
{% raw %}
<p>静压、总压和系数转换</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    staticPressure
    {
        type pressure;
        libs (fieldFunctionObjects);

        writeControl writeTime;
        writeInterval 1;
        mode static;
        rho rhoInf;
        rhoInf 1;
        result pPa;
    }
}</code></pre><p>进行压力形式的转换。本例 mode static 配 rho rhoInf，把不可压缩求解器的运动压力转为实际静压；result pPa 指定输出名。</p><p>示例算例：后台阶湍流。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>pressure</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>mode</code></td><td>该工具的计算模式，具体取值见下方说明。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>field</code></td><td>输入场的名称。</td><td>可选</td><td><code>p</code></td></tr><tr><td><code>U</code></td><td>速度场名称。</td><td>可选</td><td><code>U</code></td></tr><tr><td><code>rho</code></td><td>密度场名称；使用常密度时按示例选择 rhoInf。</td><td>可选</td><td><code>rho</code></td></tr><tr><td><code>rhoInf</code></td><td>不可压缩计算使用的参考密度。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>pRef</code></td><td>参考压力。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>hydrostaticMode</code></td><td>静水压力贡献的处理方式，例如 none、add、subtract。</td><td>可选</td><td><code>none</code></td></tr><tr><td><code>g</code></td><td>重力加速度向量。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>hRef</code></td><td>重力势的参考高度。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>pInf</code></td><td>计算压力系数的来流参考压力。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>UInf</code></td><td>来流参考速度向量，用于压力系数。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>result</code></td><td>生成的结果场名称，用于区分输入场和输出场。</td><td>可选</td><td><code>工具默认名称</code></td></tr><tr><td><code>cellZones</code></td><td>参与统计的单元区域名称列表。</td><td>可选</td><td><code>全域</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>进行压力形式的转换。本例 mode static 配 rho rhoInf，把不可压缩求解器的运动压力转为实际静压；result pPa 指定输出名。</p><pre><code class="language-foam">staticPressure
{
    type pressure;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    mode static;
    rho rhoInf;
    rhoInf 1;
    result pPa;
}</code></pre><h3 id="example-2">示例 2 · 计算总压</h3><p>在静压基础上加入速度对应的动压，适合比较管道或扩压段的总压损失。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">mode total;
result pTotal;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">staticPressure
{
    type pressure;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    mode total;
    rho rhoInf;
    rhoInf 1;
    result pTotal;
}</code></pre></details><h3 id="example-3">示例 3 · 采用水的参考密度</h3><p>相同运动压力乘以 1000 kg/m³，得到以水的密度换算的实际压力。参考密度应与物理问题一致。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">rhoInf 1000;
result pWater;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">staticPressure
{
    type pressure;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    mode static;
    rho rhoInf;
    rhoInf 1000;
    result pWater;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">staticPressure
{
    type pressure;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    mode static;
    rho rhoInf;
    rhoInf 1;
    result pPa;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">staticPressure
{
    type pressure;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    mode static;
    rho rhoInf;
    rhoInf 1;
    result pPa;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-09">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/pressure/pressure.H">OpenFOAM v2512 · pressure 接口</a>。</p>
{% endraw %}
