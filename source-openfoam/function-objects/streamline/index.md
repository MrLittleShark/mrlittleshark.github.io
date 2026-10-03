---
title: "streamLine"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-streamline"
description: "从种子点出发追踪流线。"
---
{% raw %}
<p>从种子点出发追踪流线。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    streamlines
    {
        type streamLine;
        libs (fieldFunctionObjects);

        writeControl writeTime;
        writeInterval 1;
        U U;
        fields (U p);
        setFormat vtk;
        direction bidirectional;
        lifeTime 200;
        nSubCycle 5;
        seedSampleSet
        {
            type uniform;
            axis y;
            start (0.05 0.01 0.005);
            end (0.05 0.09 0.005);
            nPoints 5;
        }
    }
}</code></pre><p>从 seedSampleSet 指定的种子点沿 U 追踪流线。本例在方腔中线放置五个点，双向追踪并保存沿线的 U 与 p；nSubCycle 控制单元内的追踪细分。</p><p>示例算例：顶盖驱动方腔。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>streamLine</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>U</code></td><td>速度场名称。</td><td>可选</td><td><code>U</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>setFormat</code></td><td>点集或线采样的输出格式，例如 raw、csv、vtk。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>direction</code></td><td>forward 向下游，backward 向上游，bidirectional 双向追踪。</td><td>可选</td><td><code>forward</code></td></tr><tr><td><code>lifeTime</code></td><td>每条流线允许的最大追踪步数。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>cloud</code></td><td>要处理的颗粒云名称。</td><td>可选</td><td><code>typeName</code></td></tr><tr><td><code>seedSampleSet</code></td><td>流线种子点的定义，可指定均匀线、点云等采样类型。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>bounds</code></td><td>保留轨迹的包围盒，写成最小点和最大点。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>trackLength</code></td><td>流线每个追踪段的长度。</td><td>可选</td><td><code>VGREAT</code></td></tr><tr><td><code>nSubCycle</code></td><td>在每个网格单元内执行的追踪子步数。</td><td>可选</td><td><code>1</code></td></tr><tr><td><code>interpolationScheme</code></td><td>插值方法；cell 取单元值，cellPoint 结合单元和顶点值插值。</td><td>可选</td><td><code>cellPoint</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>从 seedSampleSet 指定的种子点沿 U 追踪流线。本例在方腔中线放置五个点，双向追踪并保存沿线的 U 与 p；nSubCycle 控制单元内的追踪细分。</p><pre><code class="language-foam">streamlines
{
    type streamLine;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    U U;
    fields (U p);
    setFormat vtk;
    direction bidirectional;
    lifeTime 200;
    nSubCycle 5;
    seedSampleSet
    {
        type uniform;
        axis y;
        start (0.05 0.01 0.005);
        end (0.05 0.09 0.005);
        nPoints 5;
    }
}</code></pre><h3 id="example-2">示例 2 · 只向下游追踪</h3><p>从种子点沿速度方向积分，适合观察流体之后经过的区域。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">direction forward;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">streamlines
{
    type streamLine;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    U U;
    fields (U p);
    setFormat vtk;
    direction forward;
    lifeTime 200;
    nSubCycle 5;
    seedSampleSet
    {
        type uniform;
        axis y;
        start (0.05 0.01 0.005);
        end (0.05 0.09 0.005);
        nPoints 5;
    }
}</code></pre></details><h3 id="example-3">示例 3 · 增加单元内追踪步数</h3><p>提高轨迹在单元内的分辨率，代价是更多追踪计算。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">nSubCycle 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">streamlines
{
    type streamLine;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    U U;
    fields (U p);
    setFormat vtk;
    direction bidirectional;
    lifeTime 200;
    nSubCycle 10;
    seedSampleSet
    {
        type uniform;
        axis y;
        start (0.05 0.01 0.005);
        end (0.05 0.09 0.005);
        nPoints 5;
    }
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">streamlines
{
    type streamLine;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    U U;
    fields (U p);
    setFormat vtk;
    direction bidirectional;
    lifeTime 200;
    nSubCycle 5;
    seedSampleSet
    {
        type uniform;
        axis y;
        start (0.05 0.01 0.005);
        end (0.05 0.09 0.005);
        nPoints 5;
    }
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">streamlines
{
    type streamLine;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    U U;
    fields (U p);
    setFormat vtk;
    direction bidirectional;
    lifeTime 200;
    nSubCycle 5;
    seedSampleSet
    {
        type uniform;
        axis y;
        start (0.05 0.01 0.005);
        end (0.05 0.09 0.005);
        nPoints 5;
    }
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-04">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/streamLine/streamLine.H">OpenFOAM v2512 · streamLine 接口</a>。</p>
{% endraw %}
