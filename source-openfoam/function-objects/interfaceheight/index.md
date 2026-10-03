---
title: "interfaceHeight"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-interfaceheight"
description: "监测两相流的等效液位。"
---
{% raw %}
<p>监测两相流的等效液位。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    level
    {
        type interfaceHeight;
        libs (fieldFunctionObjects);

        writeControl timeStep;
        writeInterval 10;
        alpha alpha.water;
        liquid true;
        direction (0 -1 0);
        locations ((0.1 0 0.0073) (0.3 0 0.0073));
    }
}</code></pre><p>沿给定方向积分相分数，得到等效液位。本例 alpha.water 表示水相，direction 指向重力方向；locations 指定水平位置，适合比较不同位置的液位变化。</p><p>示例算例：溃坝两相流。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>interfaceHeight</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>locations</code></td><td>测量液位的位置列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>alpha</code></td><td>相分数场名称。</td><td>可选</td><td><code>alpha</code></td></tr><tr><td><code>liquid</code></td><td>true 表示 alpha 对应液相，false 表示对应气相。</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>direction</code></td><td>积分方向向量，结合重力方向和所定义的液相选择。</td><td>可选</td><td><code>g</code></td></tr><tr><td><code>interpolationScheme</code></td><td>插值方法；cell 取单元值，cellPoint 结合单元和顶点值插值。</td><td>可选</td><td><code>cellPoint</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>沿给定方向积分相分数，得到等效液位。本例 alpha.water 表示水相，direction 指向重力方向；locations 指定水平位置，适合比较不同位置的液位变化。</p><pre><code class="language-foam">level
{
    type interfaceHeight;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    alpha alpha.water;
    liquid true;
    direction (0 -1 0);
    locations ((0.1 0 0.0073) (0.3 0 0.0073));
}</code></pre><h3 id="example-2">示例 2 · 只保留一个液位测点</h3><p>在溃坝区域内选一个水平位置，得到一条液位时序。坐标的竖直分量应结合该算例的方向设置理解。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">locations ((0.2 0 0.073));</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">level
{
    type interfaceHeight;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    alpha alpha.water;
    liquid true;
    direction (0 -1 0);
    locations ((0.2 0 0.073));
}</code></pre></details><h3 id="example-3">示例 3 · 增加液位测点</h3><p>在相同竖直方向上比较两个水平位置，观察波前通过时的先后变化。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">locations ((0.2 0 0.073) (0.4 0 0.073));</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">level
{
    type interfaceHeight;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    alpha alpha.water;
    liquid true;
    direction (0 -1 0);
    locations ((0.2 0 0.073) (0.4 0 0.073));
}</code></pre></details><h3 id="example-4">示例 4 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">level
{
    type interfaceHeight;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    alpha alpha.water;
    liquid true;
    direction (0 -1 0);
    locations ((0.1 0 0.0073) (0.3 0 0.0073));
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h3 id="example-5">示例 5 · 每五步保存一次</h3><p>采用五步间隔，在时间分辨率与数据量之间选择适合当前计算的输出频率。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">level
{
    type interfaceHeight;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 5;
    alpha alpha.water;
    liquid true;
    direction (0 -1 0);
    locations ((0.1 0 0.0073) (0.3 0 0.0073));
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%A2%97%E7%B2%92%E4%B8%8E%E4%B8%A4%E7%9B%B8">颗粒与两相速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-12">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/interfaceHeight/interfaceHeight.H">OpenFOAM v2512 · interfaceHeight 接口</a>。</p>
{% endraw %}
