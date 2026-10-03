---
title: "hydrostaticPressure"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-hydrostaticpressure"
description: "静水压力初始化 / 计算"
---
{% raw %}
<p>静水压力初始化 / 计算</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    hydrostaticPressureExample
    {
        type hydrostaticPressure;
        libs (initialisationFunctionObjects);
    p_rgh p_rgh;
        ph_rgh ph_rgh;
        rho rho;
        U U;
        nCorrectors 5;
        reInitialise true;
    }
}</code></pre><p>根据重力、密度与热物性模型建立静水平衡压力。适用于已经准备 p_rgh、ph_rgh 及相应边界的浮力算例，nCorrectors 指定压力校正次数。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>hydrostaticPressure</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(initialisationFunctionObjects)</code></td></tr><tr><td><code>p_rgh</code></td><td>扣除静水压力项后的压力场名称。</td><td>可选</td><td><code>p_rgh</code></td></tr><tr><td><code>ph_rgh</code></td><td>静水平衡初始化所用的压力场名称。</td><td>可选</td><td><code>ph_rgh</code></td></tr><tr><td><code>pRef</code></td><td>参考压力。</td><td>可选</td><td><code>pRef</code></td></tr><tr><td><code>pRefValue</code></td><td>参考压力值。</td><td>条件必填</td><td><code>0</code></td></tr><tr><td><code>rho</code></td><td>密度场名称；使用常密度时按示例选择 rhoInf。</td><td>可选</td><td><code>rho</code></td></tr><tr><td><code>U</code></td><td>速度场名称。</td><td>可选</td><td><code>U</code></td></tr><tr><td><code>gh</code></td><td>单元中心处重力势场名称。</td><td>可选</td><td><code>gh</code></td></tr><tr><td><code>ghf</code></td><td>面中心处重力势场名称。</td><td>可选</td><td><code>ghf</code></td></tr><tr><td><code>nCorrectors</code></td><td>静水压力校正次数。</td><td>条件必填</td><td><code>no</code></td></tr><tr><td><code>reInitialise</code></td><td>计算开始时是否重新初始化静水压力。</td><td>可选</td><td><code>false</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>根据重力、密度与热物性模型建立静水平衡压力。适用于已经准备 p_rgh、ph_rgh 及相应边界的浮力算例，nCorrectors 指定压力校正次数。</p><pre><code class="language-foam">hydrostaticPressureExample
{
    type hydrostaticPressure;
    libs (initialisationFunctionObjects);
p_rgh p_rgh;
    ph_rgh ph_rgh;
    rho rho;
    U U;
    nCorrectors 5;
    reInitialise true;
}</code></pre><h3 id="example-2">示例 2 · 增加压力校正次数</h3><p>对密度与压力耦合较强的初始化，增加校正以进一步调整静水平衡。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">nCorrectors 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">hydrostaticPressureExample
{
    type hydrostaticPressure;
    libs (initialisationFunctionObjects);
p_rgh p_rgh;
    ph_rgh ph_rgh;
    rho rho;
    U U;
    nCorrectors 10;
    reInitialise true;
}</code></pre></details><h3 id="example-3">示例 3 · 延用已保存的初始化状态</h3><p>在具备已有初始化结果的重启算例中保留该状态。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">reInitialise false;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">hydrostaticPressureExample
{
    type hydrostaticPressure;
    libs (initialisationFunctionObjects);
p_rgh p_rgh;
    ph_rgh ph_rgh;
    rho rho;
    U U;
    nCorrectors 5;
    reInitialise false;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">hydrostaticPressureExample
{
    type hydrostaticPressure;
    libs (initialisationFunctionObjects);
p_rgh p_rgh;
    ph_rgh ph_rgh;
    rho rho;
    U U;
    nCorrectors 5;
    reInitialise true;
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">hydrostaticPressureExample
{
    type hydrostaticPressure;
    libs (initialisationFunctionObjects);
p_rgh p_rgh;
    ph_rgh ph_rgh;
    rho rho;
    U U;
    nCorrectors 5;
    reInitialise true;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/initialisation/hydrostaticPressure/hydrostaticPressure.H">OpenFOAM v2512 · hydrostaticPressure 接口</a>。</p>
{% endraw %}
