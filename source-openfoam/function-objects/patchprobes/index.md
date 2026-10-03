---
title: "patchProbes"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-patchprobes"
description: "记录边界面上指定位置的场值。"
---
{% raw %}
<p>记录边界面上指定位置的场值。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    lidProbes
    {
        type patchProbes;
        libs (sampling);

        writeControl timeStep;
        writeInterval 10;
        patches (movingWall);
        fields (p U);
        probeLocations ((0.025 0.1 0.005) (0.075 0.1 0.005));
    }
}</code></pre><p>把探针位置投影到所选边界上并记录边界场值。本例 patches 选方腔的 movingWall，探针位于顶壁；这适合记录壁面压力，而域内测点使用 probes。</p><p>示例算例：顶盖驱动方腔。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>patchProbes</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(sampling)</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>probeLocations</code></td><td>探针坐标列表，每个坐标写成 (x y z)。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>patches</code></td><td>需要处理的边界名称列表；支持名称匹配表达式。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>verbose</code></td><td>是否打印更详细的运行信息。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>sampleOnExecute</code></td><td>在执行阶段采样并保存到内存，而不只在写出阶段采样。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>fixedLocations</code></td><td>固定空间采样位置；false 时允许采样位置随网格运动处理。</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>includeOutOfBounds</code></td><td>是否保留网格范围之外的探针位置。</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>interpolationScheme</code></td><td>插值方法；cell 取单元值，cellPoint 结合单元和顶点值插值。</td><td>可选</td><td><code>cell</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>把探针位置投影到所选边界上并记录边界场值。本例 patches 选方腔的 movingWall，探针位于顶壁；这适合记录壁面压力，而域内测点使用 probes。</p><pre><code class="language-foam">lidProbes
{
    type patchProbes;
    libs (sampling);

    writeControl timeStep;
    writeInterval 10;
    patches (movingWall);
    fields (p U);
    probeLocations ((0.025 0.1 0.005) (0.075 0.1 0.005));
}</code></pre><h3 id="example-2">示例 2 · 只记录顶壁压力</h3><p>测点和 movingWall 保持一致，只输出边界压力。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">fields (p);</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">lidProbes
{
    type patchProbes;
    libs (sampling);

    writeControl timeStep;
    writeInterval 10;
    patches (movingWall);
    fields (p);
    probeLocations ((0.025 0.1 0.005) (0.075 0.1 0.005));
}</code></pre></details><h3 id="example-3">示例 3 · 保存每步采样值供后续对象读取</h3><p>除了写出阶段，也在执行阶段更新内存中的采样值。依赖探针结果的后续功能对象应排在它后面。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">sampleOnExecute true;
executeControl timeStep;
executeInterval 1;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">lidProbes
{
    type patchProbes;
    libs (sampling);

    writeControl timeStep;
    writeInterval 10;
    patches (movingWall);
    fields (p U);
    probeLocations ((0.025 0.1 0.005) (0.075 0.1 0.005));
    sampleOnExecute true;
    executeControl timeStep;
    executeInterval 1;
}</code></pre></details><h3 id="example-4">示例 4 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">lidProbes
{
    type patchProbes;
    libs (sampling);

    writeControl timeStep;
    writeInterval 10;
    patches (movingWall);
    fields (p U);
    probeLocations ((0.025 0.1 0.005) (0.075 0.1 0.005));
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h3 id="example-5">示例 5 · 每五步保存一次</h3><p>采用五步间隔，在时间分辨率与数据量之间选择适合当前计算的输出频率。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">lidProbes
{
    type patchProbes;
    libs (sampling);

    writeControl timeStep;
    writeInterval 5;
    patches (movingWall);
    fields (p U);
    probeLocations ((0.025 0.1 0.005) (0.075 0.1 0.005));
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-02">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/sampling/probes/patchProbes.H">OpenFOAM v2512 · patchProbes 接口</a>。</p>
{% endraw %}
