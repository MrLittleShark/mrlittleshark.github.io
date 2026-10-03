---
title: "thermoCoupleProbes"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-thermocoupleprobes"
description: "辐射计与热电偶模型采样"
---
{% raw %}
<p>辐射计与热电偶模型采样</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    probes
    {
        type            thermoCoupleProbes;
        libs            (utilityFunctionObjects);
        writeControl    timeStep;
        writeInterval   1;
        solver          rodas23;
        absTol          1e-12;
        relTol          1e-8;
        interpolationScheme cellPoint;
        rho             8908;
        Cp              440;
        d               1e-3;
        epsilon         0.85;
        radiationField  G;
        probeLocations  ((0.5 0.5 0.5));
        fields          (T);
    }
}</code></pre><p>在探针位置求解热电偶温度响应，同时考虑对流与辐射。rho、Cp、d、epsilon 是热电偶材料和几何参数，G 为辐射模型提供的辐射场。</p><p>配套教程配置：<code>heatTransfer/buoyantPimpleFoam/thermocoupleTestCase/system/controlDict</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>thermoCoupleProbes</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(utilityFunctionObjects)</code></td></tr><tr><td><code>radiationField</code></td><td>供传感器模型读取的辐射场名称。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>rho</code></td><td>热电偶材料密度，单位 kg/m³。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>Cp</code></td><td>定压比热容。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>d</code></td><td>热电偶直径。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>epsilon</code></td><td>热电偶表面的发射率。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>U</code></td><td>速度场名称。</td><td>可选</td><td><code>U</code></td></tr><tr><td><code>probeLocations</code></td><td>热电偶测点坐标列表</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>fields</code></td><td>采样字段，通常为 (T)</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>solver</code></td><td>温度响应所用的常微分方程求解器</td><td>必填</td><td><code>如 rodas23</code></td></tr><tr><td><code>absTol</code></td><td>常微分方程绝对容差</td><td>可选</td><td><code>由求解设置决定</code></td></tr><tr><td><code>relTol</code></td><td>常微分方程相对容差</td><td>可选</td><td><code>由求解设置决定</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>在探针位置求解热电偶温度响应，同时考虑对流与辐射。rho、Cp、d、epsilon 是热电偶材料和几何参数，G 为辐射模型提供的辐射场。</p><pre><code class="language-foam">probes
{
    type            thermoCoupleProbes;
    libs            (utilityFunctionObjects);
    writeControl    timeStep;
    writeInterval   1;
    solver          rodas23;
    absTol          1e-12;
    relTol          1e-8;
    interpolationScheme cellPoint;
    rho             8908;
    Cp              440;
    d               1e-3;
    epsilon         0.85;
    radiationField  G;
    probeLocations  ((0.5 0.5 0.5));
    fields          (T);
}</code></pre><h3 id="example-2">示例 2 · 采用更细热电偶</h3><p>减小直径会改变热惯性与对流换热响应，可对照流体温度检查响应延迟。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">d 0.0005;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">probes
{
    type            thermoCoupleProbes;
    libs            (utilityFunctionObjects);
    writeControl    timeStep;
    writeInterval   1;
    solver          rodas23;
    absTol          1e-12;
    relTol          1e-8;
    interpolationScheme cellPoint;
    rho             8908;
    Cp              440;
    d 0.0005;
    epsilon         0.85;
    radiationField  G;
    probeLocations  ((0.5 0.5 0.5));
    fields          (T);
}</code></pre></details><h3 id="example-3">示例 3 · 降低发射率</h3><p>观察热电偶表面辐射性质对测量温度的影响。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">epsilon 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">probes
{
    type            thermoCoupleProbes;
    libs            (utilityFunctionObjects);
    writeControl    timeStep;
    writeInterval   1;
    solver          rodas23;
    absTol          1e-12;
    relTol          1e-8;
    interpolationScheme cellPoint;
    rho             8908;
    Cp              440;
    d               1e-3;
    epsilon 0.5;
    radiationField  G;
    probeLocations  ((0.5 0.5 0.5));
    fields          (T);
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">probes
{
    type            thermoCoupleProbes;
    libs            (utilityFunctionObjects);
    writeControl timeStep;
    writeInterval 10;
    solver          rodas23;
    absTol          1e-12;
    relTol          1e-8;
    interpolationScheme cellPoint;
    rho             8908;
    Cp              440;
    d               1e-3;
    epsilon         0.85;
    radiationField  G;
    probeLocations  ((0.5 0.5 0.5));
    fields          (T);
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">probes
{
    type            thermoCoupleProbes;
    libs            (utilityFunctionObjects);
    writeControl    timeStep;
    writeInterval   1;
    solver          rodas23;
    absTol          1e-12;
    relTol          1e-8;
    interpolationScheme cellPoint;
    rho             8908;
    Cp              440;
    d               1e-3;
    epsilon         0.85;
    radiationField  G;
    probeLocations  ((0.5 0.5 0.5));
    fields          (T);
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/utilities/thermoCoupleProbes/thermoCoupleProbes.H">OpenFOAM v2512 · thermoCoupleProbes 接口</a>。</p>
{% endraw %}
