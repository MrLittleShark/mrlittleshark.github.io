---
title: "sets"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-sets"
description: "沿线或点集采样，输出场值剖面。"
---
{% raw %}
<p>沿线或点集采样，输出场值剖面。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    centreLines
    {
        type sets;
        libs (sampling);

        writeControl writeTime;
        writeInterval 1;
        fields (U p);
        interpolationScheme cellPoint;
        setFormat raw;
        sets
        {
            vertical
            {
                type uniform;
                axis y;
                start (0.05 0.0001 0.005);
                end (0.05 0.0999 0.005);
                nPoints 51;
            }
            horizontal
            {
                type uniform;
                axis x;
                start (0.0001 0.05 0.005);
                end (0.0999 0.05 0.005);
                nPoints 51;
            }
        }
    }
}</code></pre><p>沿给定点集采样。配置中的 start、end 决定采样线位置，nPoints 决定点数；输出文件第一列是 axis 指定的坐标或距离，后续列是场值。</p><p>示例算例：顶盖驱动方腔。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>sets</code></td></tr><tr><td><code>sets</code></td><td>采样点集的定义，每个点集有自己的类型和几何参数。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>interpolationScheme</code></td><td>插值方法；cell 取单元值，cellPoint 结合单元和顶点值插值。</td><td>可选</td><td><code>cellPoint</code></td></tr><tr><td><code>setFormat</code></td><td>点集或线采样的输出格式，例如 raw、csv、vtk。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>sampleOnExecute</code></td><td>在执行阶段采样并保存到内存，而不只在写出阶段采样。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>formatOptions</code></td><td>输出格式的专用设置子字典。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>store</code></td><td>是否将计算结果保存在内存中的对象数据库，供后续工具使用。</td><td>可选</td><td><code>—</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>沿给定点集采样。配置中的 start、end 决定采样线位置，nPoints 决定点数；输出文件第一列是 axis 指定的坐标或距离，后续列是场值。</p><pre><code class="language-foam">centreLines
{
    type sets;
    libs (sampling);

    writeControl writeTime;
    writeInterval 1;
    fields (U p);
    interpolationScheme cellPoint;
    setFormat raw;
    sets
    {
        vertical
        {
            type uniform;
            axis y;
            start (0.05 0.0001 0.005);
            end (0.05 0.0999 0.005);
            nPoints 51;
        }
        horizontal
        {
            type uniform;
            axis x;
            start (0.0001 0.05 0.005);
            end (0.0999 0.05 0.005);
            nPoints 51;
        }
    }
}</code></pre><h3 id="example-2">示例 2 · 以 CSV 保存剖面</h3><p>保持原采样点不变，改为逗号分隔的数据文件，便于导入表格或绘图程序。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">setFormat csv;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">centreLines
{
    type sets;
    libs (sampling);

    writeControl writeTime;
    writeInterval 1;
    fields (U p);
    interpolationScheme cellPoint;
    setFormat csv;
    sets
    {
        vertical
        {
            type uniform;
            axis y;
            start (0.05 0.0001 0.005);
            end (0.05 0.0999 0.005);
            nPoints 51;
        }
        horizontal
        {
            type uniform;
            axis x;
            start (0.0001 0.05 0.005);
            end (0.0999 0.05 0.005);
            nPoints 51;
        }
    }
}</code></pre></details><h3 id="example-3">示例 3 · 同时采样压力和速度</h3><p>在同一组采样位置上保存 p 与 U，方便将压力变化和速度剖面对照。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">fields (p U);
interpolationScheme cellPoint;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">centreLines
{
    type sets;
    libs (sampling);

    writeControl writeTime;
    writeInterval 1;
    fields (p U);
    interpolationScheme cellPoint;
    setFormat raw;
    sets
    {
        vertical
        {
            type uniform;
            axis y;
            start (0.05 0.0001 0.005);
            end (0.05 0.0999 0.005);
            nPoints 51;
        }
        horizontal
        {
            type uniform;
            axis x;
            start (0.0001 0.05 0.005);
            end (0.0999 0.05 0.005);
            nPoints 51;
        }
    }
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">centreLines
{
    type sets;
    libs (sampling);

    writeControl timeStep;
    writeInterval 10;
    fields (U p);
    interpolationScheme cellPoint;
    setFormat raw;
    sets
    {
        vertical
        {
            type uniform;
            axis y;
            start (0.05 0.0001 0.005);
            end (0.05 0.0999 0.005);
            nPoints 51;
        }
        horizontal
        {
            type uniform;
            axis x;
            start (0.0001 0.05 0.005);
            end (0.0999 0.05 0.005);
            nPoints 51;
        }
    }
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">centreLines
{
    type sets;
    libs (sampling);

    writeControl writeTime;
    writeInterval 1;
    fields (U p);
    interpolationScheme cellPoint;
    setFormat raw;
    sets
    {
        vertical
        {
            type uniform;
            axis y;
            start (0.05 0.0001 0.005);
            end (0.05 0.0999 0.005);
            nPoints 51;
        }
        horizontal
        {
            type uniform;
            axis x;
            start (0.0001 0.05 0.005);
            end (0.0999 0.05 0.005);
            nPoints 51;
        }
    }
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-03">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/sampling/sampledSet/sampledSets/sampledSets.H">OpenFOAM v2512 · sets 接口</a>。</p>
{% endraw %}
