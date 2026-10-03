---
title: "probes"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-probes"
description: "记录指定空间位置上的场值。"
---
{% raw %}
<p>记录指定空间位置上的场值。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    pointHistory
    {
        type probes;
        libs (sampling);

        writeControl timeStep;
        writeInterval 1;
        fields (U p);
        probeLocations ((0.05 0.05 0.005) (0.05 0.075 0.005));
        interpolationScheme cellPoint;
        fixedLocations true;
        includeOutOfBounds false;
    }
}</code></pre><p>在固定坐标连续记录速度和压力。本例的两个点位于边长 0.1 m 的方腔内部，z=0.005 m 位于薄层中面；每个字段的文件按时间排列，每列对应一个探针。</p><p>示例算例：顶盖驱动方腔。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>probes</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(sampling)</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>probeLocations</code></td><td>探针坐标列表，每个坐标写成 (x y z)。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>verbose</code></td><td>是否打印更详细的运行信息。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>sampleOnExecute</code></td><td>在执行阶段采样并保存到内存，而不只在写出阶段采样。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>fixedLocations</code></td><td>固定空间采样位置；false 时允许采样位置随网格运动处理。</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>includeOutOfBounds</code></td><td>是否保留网格范围之外的探针位置。</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>interpolationScheme</code></td><td>插值方法；cell 取单元值，cellPoint 结合单元和顶点值插值。</td><td>可选</td><td><code>cell</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>在固定坐标连续记录速度和压力。本例的两个点位于边长 0.1 m 的方腔内部，z=0.005 m 位于薄层中面；每个字段的文件按时间排列，每列对应一个探针。</p><pre><code class="language-foam">pointHistory
{
    type probes;
    libs (sampling);

    writeControl timeStep;
    writeInterval 1;
    fields (U p);
    probeLocations ((0.05 0.05 0.005) (0.05 0.075 0.005));
    interpolationScheme cellPoint;
    fixedLocations true;
    includeOutOfBounds false;
}</code></pre><h3 id="example-2">示例 2 · 只记录压力</h3><p>保留原探针位置，只保存压力时序。fields 控制采样变量，减少字段也会减少输出文件。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">fields (p);</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">pointHistory
{
    type probes;
    libs (sampling);

    writeControl timeStep;
    writeInterval 1;
    fields (p);
    probeLocations ((0.05 0.05 0.005) (0.05 0.075 0.005));
    interpolationScheme cellPoint;
    fixedLocations true;
    includeOutOfBounds false;
}</code></pre></details><h3 id="example-3">示例 3 · 沿方腔中线布置三个探针</h3><p>三个点具有相同 x、z 坐标，沿 y 方向排列。cellPoint 用单元与顶点信息插值，便于比较同一条线上的流速变化。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">probeLocations ((0.05 0.025 0.005) (0.05 0.05 0.005) (0.05 0.075 0.005));
interpolationScheme cellPoint;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">pointHistory
{
    type probes;
    libs (sampling);

    writeControl timeStep;
    writeInterval 1;
    fields (U p);
    probeLocations ((0.05 0.025 0.005) (0.05 0.05 0.005) (0.05 0.075 0.005));
    interpolationScheme cellPoint;
    fixedLocations true;
    includeOutOfBounds false;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">pointHistory
{
    type probes;
    libs (sampling);

    writeControl timeStep;
    writeInterval 10;
    fields (U p);
    probeLocations ((0.05 0.05 0.005) (0.05 0.075 0.005));
    interpolationScheme cellPoint;
    fixedLocations true;
    includeOutOfBounds false;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">pointHistory
{
    type probes;
    libs (sampling);

    writeControl timeStep;
    writeInterval 1;
    fields (U p);
    probeLocations ((0.05 0.05 0.005) (0.05 0.075 0.005));
    interpolationScheme cellPoint;
    fixedLocations true;
    includeOutOfBounds false;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-02">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/sampling/probes/probes.H">OpenFOAM v2512 · probes 接口</a>。</p>
{% endraw %}
