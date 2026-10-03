---
title: "surfaces"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-surfaces"
description: "在截面、等值面或指定表面上采样。"
---
{% raw %}
<p>在截面、等值面或指定表面上采样。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    freeSurface
    {
        type surfaces;
        libs (sampling);

        writeControl writeTime;
        writeInterval 1;
        fields (U p_rgh);
        surfaceFormat vtk;
        surfaces
        {
            waterAir
            {
                type isoSurfaceCell;
                isoField alpha.water;
                isoValue 0.5;
                interpolate true;
            }
        }
    }
}</code></pre><p>在指定几何表面上提取场。本例从溃坝的 alpha.water=0.5 等值面提取水气界面，并在该表面采样 U、p_rgh；surfaceFormat vtk 便于用 ParaView 打开。</p><p>示例算例：溃坝两相流。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>surfaces</code></td></tr><tr><td><code>surfaces</code></td><td>采样表面的定义，例如平面或等值面。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>sampleScheme</code></td><td>表面面中心处的采样方式。</td><td>可选</td><td><code>cell</code></td></tr><tr><td><code>interpolationScheme</code></td><td>插值方法；cell 取单元值，cellPoint 结合单元和顶点值插值。</td><td>可选</td><td><code>cellPoint</code></td></tr><tr><td><code>surfaceFormat</code></td><td>表面结果的输出格式，例如 vtk、ensight、raw。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>formatOptions</code></td><td>输出格式的专用设置子字典。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>sampleOnExecute</code></td><td>在执行阶段采样并保存到内存，而不只在写出阶段采样。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>store</code></td><td>是否将计算结果保存在内存中的对象数据库，供后续工具使用。</td><td>可选</td><td><code>false</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>在指定几何表面上提取场。本例从溃坝的 alpha.water=0.5 等值面提取水气界面，并在该表面采样 U、p_rgh；surfaceFormat vtk 便于用 ParaView 打开。</p><pre><code class="language-foam">freeSurface
{
    type surfaces;
    libs (sampling);

    writeControl writeTime;
    writeInterval 1;
    fields (U p_rgh);
    surfaceFormat vtk;
    surfaces
    {
        waterAir
        {
            type isoSurfaceCell;
            isoField alpha.water;
            isoValue 0.5;
            interpolate true;
        }
    }
}</code></pre><h3 id="example-2">示例 2 · 只导出界面速度</h3><p>保留同一水气界面，只输出速度，减小每个时间目录的数据量。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">fields (U);</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">freeSurface
{
    type surfaces;
    libs (sampling);

    writeControl writeTime;
    writeInterval 1;
    fields (U);
    surfaceFormat vtk;
    surfaces
    {
        waterAir
        {
            type isoSurfaceCell;
            isoField alpha.water;
            isoValue 0.5;
            interpolate true;
        }
    }
}</code></pre></details><h3 id="example-3">示例 3 · 改用 EnSight 表面输出</h3><p>几何选择保持不变，改变结果的文件格式，适合统一到 EnSight 数据处理流程。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">surfaceFormat ensight;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">freeSurface
{
    type surfaces;
    libs (sampling);

    writeControl writeTime;
    writeInterval 1;
    fields (U p_rgh);
    surfaceFormat ensight;
    surfaces
    {
        waterAir
        {
            type isoSurfaceCell;
            isoField alpha.water;
            isoValue 0.5;
            interpolate true;
        }
    }
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">freeSurface
{
    type surfaces;
    libs (sampling);

    writeControl timeStep;
    writeInterval 10;
    fields (U p_rgh);
    surfaceFormat vtk;
    surfaces
    {
        waterAir
        {
            type isoSurfaceCell;
            isoField alpha.water;
            isoValue 0.5;
            interpolate true;
        }
    }
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">freeSurface
{
    type surfaces;
    libs (sampling);

    writeControl writeTime;
    writeInterval 1;
    fields (U p_rgh);
    surfaceFormat vtk;
    surfaces
    {
        waterAir
        {
            type isoSurfaceCell;
            isoField alpha.water;
            isoValue 0.5;
            interpolate true;
        }
    }
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-04">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/sampling/sampledSurface/sampledSurfaces/sampledSurfaces.H">OpenFOAM v2512 · surfaces 接口</a>。</p>
{% endraw %}
