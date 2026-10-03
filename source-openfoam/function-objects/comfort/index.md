---
title: "comfort"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-comfort"
description: "热舒适度指标"
---
{% raw %}
<p>热舒适度指标</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    comfort
    {
        type            comfort;
        libs            (fieldFunctionObjects);
        clothing        0.5;
        metabolicRate   1.2;
        extWork         0.0;
        relHumidity     60.0;
        pSat            0.0;
        tolerance       1e-4;
        maxClothIter    100;
        meanVelocity    false;
        region          region0;
        enabled         true;
        log             true;
        timeStart       0;
        timeEnd         10000;
        executeControl  writeTime;
        executeInterval 1;
        writeControl    writeTime;
        writeInterval 1;
    }
}</code></pre><p>根据速度、温度、湿度及人体参数计算热舒适度。本例 clothing 0.5、metabolicRate 1.2 描述衣着与活动水平，relHumidity 60 表示相对湿度为 60%。</p><p>配套教程配置：<code>heatTransfer/buoyantSimpleFoam/comfortHotRoom/system/FOcomfort</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>comfort</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>clothing</code></td><td>服装热阻，通常以 clo 为单位。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>metabolicRate</code></td><td>人体代谢率，通常以 met 为单位。</td><td>可选</td><td><code>0.8</code></td></tr><tr><td><code>extWork</code></td><td>人体对外做功。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>Trad</code></td><td>平均辐射温度。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>relHumidity</code></td><td>空气相对湿度。</td><td>可选</td><td><code>0.5</code></td></tr><tr><td><code>pSat</code></td><td>水的饱和蒸气压。</td><td>可选</td><td><code>-1</code></td></tr><tr><td><code>tolerance</code></td><td>衣服表面温度迭代的收敛容差。</td><td>可选</td><td><code>1e-4</code></td></tr><tr><td><code>maxClothIter</code></td><td>衣服表面温度求解的最大迭代次数。</td><td>可选</td><td><code>100</code></td></tr><tr><td><code>meanVelocity</code></td><td>是否用全域统一的平均速度计算舒适度。</td><td>可选</td><td><code>false</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>根据速度、温度、湿度及人体参数计算热舒适度。本例 clothing 0.5、metabolicRate 1.2 描述衣着与活动水平，relHumidity 60 表示相对湿度为 60%。</p><pre><code class="language-foam">comfort
{
    type            comfort;
    libs            (fieldFunctionObjects);
    clothing        0.5;
    metabolicRate   1.2;
    extWork         0.0;
    relHumidity     60.0;
    pSat            0.0;
    tolerance       1e-4;
    maxClothIter    100;
    meanVelocity    false;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         10000;
    executeControl  writeTime;
    executeInterval 1;
    writeControl    writeTime;
    writeInterval 1;
}</code></pre><h3 id="example-2">示例 2 · 比较较厚衣着</h3><p>衣着热阻提高后，比较相同环境下的舒适度变化。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">clothing 1;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">comfort
{
    type            comfort;
    libs            (fieldFunctionObjects);
    clothing 1;
    metabolicRate   1.2;
    extWork         0.0;
    relHumidity     60.0;
    pSat            0.0;
    tolerance       1e-4;
    maxClothIter    100;
    meanVelocity    false;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         10000;
    executeControl  writeTime;
    executeInterval 1;
    writeControl    writeTime;
    writeInterval 1;
}</code></pre></details><h3 id="example-3">示例 3 · 比较较高活动水平</h3><p>代谢率增大，人体产热相应变化；其余环境条件保持一致。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">metabolicRate 2;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">comfort
{
    type            comfort;
    libs            (fieldFunctionObjects);
    clothing        0.5;
    metabolicRate 2;
    extWork         0.0;
    relHumidity     60.0;
    pSat            0.0;
    tolerance       1e-4;
    maxClothIter    100;
    meanVelocity    false;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         10000;
    executeControl  writeTime;
    executeInterval 1;
    writeControl    writeTime;
    writeInterval 1;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">comfort
{
    type            comfort;
    libs            (fieldFunctionObjects);
    clothing        0.5;
    metabolicRate   1.2;
    extWork         0.0;
    relHumidity     60.0;
    pSat            0.0;
    tolerance       1e-4;
    maxClothIter    100;
    meanVelocity    false;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         10000;
    executeControl  writeTime;
    executeInterval 1;
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">comfort
{
    type            comfort;
    libs            (fieldFunctionObjects);
    clothing        0.5;
    metabolicRate   1.2;
    extWork         0.0;
    relHumidity     60.0;
    pSat            0.0;
    tolerance       1e-4;
    maxClothIter    100;
    meanVelocity    false;
    region          region0;
    enabled         true;
    log             true;
    timeStart 0.1;
    timeEnd 0.5;
    executeControl  writeTime;
    executeInterval 1;
    writeControl    writeTime;
    writeInterval 1;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/comfort/comfort.H">OpenFOAM v2512 · comfort 接口</a>。</p>
{% endraw %}
