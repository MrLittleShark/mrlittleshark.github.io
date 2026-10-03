---
title: "propellerInfo"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-propellerinfo"
description: "推进器和叶片载荷"
---
{% raw %}
<p>推进器和叶片载荷</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    propellerInfo1
    {
        type            propellerInfo;
        libs            (forces);
        writeControl    writeTime;
        patches         (&quot;propeller.*&quot;);
        URef            functionObjectValue;
        functionObject  propellerInfo1;
        functionObjectResult UzMean;
        rho             rhoInf;
        rhoInf          1.2;
        writePropellerPerformance yes;
        radius          0.1;
        rotationMode    specified;
        origin          (0 -0.1 0);
        axis            (0 1 0);
        n               25.15;
        writeWakeFields yes;
        sampleDisk
        {
            r1              0.05;
            r2              0.2;
            nTheta          36;
            nRadial         10;
            interpolationScheme cellPoint;
            surfaceWriter   vtk;
        }
    }
}</code></pre><p>对推进器载荷和尾流进行统计。origin、axis、n 定义转轴与转速，radius 和参考速度用于性能系数，sampleDisk 规定尾流采样圆盘。</p><p>配套教程配置：<code>incompressible/pimpleFoam/RAS/propeller/system/propellerInfo</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>propellerInfo</code></td></tr><tr><td><code>log</code></td><td>是否将常规信息输出到日志。</td><td>可选</td><td><code>no</code></td></tr><tr><td><code>patches</code></td><td>需要处理的边界名称列表；支持名称匹配表达式。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>p</code></td><td>压力场名称。</td><td>可选</td><td><code>p</code></td></tr><tr><td><code>U</code></td><td>速度场名称。</td><td>可选</td><td><code>U</code></td></tr><tr><td><code>rho</code></td><td>密度场名称；使用常密度时按示例选择 rhoInf。</td><td>可选</td><td><code>rho</code></td></tr><tr><td><code>URef</code></td><td>入口参考轴向速度大小。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>rotationMode</code></td><td>旋转方式，可按转速或 MRF 区域设置。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>origin</code></td><td>局部坐标系或旋转轴的原点。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>axis</code></td><td>旋转轴或圆柱坐标系的轴向向量。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>alphaAxis</code></td><td>定义零角度方向的坐标轴。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>n</code></td><td>旋转速度，单位转/秒。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>rpm</code></td><td>每分钟转数。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>MRF</code></td><td>旋转参考系区域名称。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>originOffset</code></td><td>MRF 模式下的原点偏移。</td><td>可选</td><td><code>(0 0 0)</code></td></tr><tr><td><code>writePropellerPerformance</code></td><td>是否写出推进器性能文本文件。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>writeWakeFields</code></td><td>是否写出尾流场文本数据。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>surfaceWriter</code></td><td>采样圆盘的表面输出格式。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>r1</code></td><td>采样圆盘内半径。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>r2</code></td><td>采样圆盘外半径。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>nTheta</code></td><td>圆周方向采样分段数量。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>nRadial</code></td><td>径向采样分段数量。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>interpolationScheme</code></td><td>插值方法；cell 取单元值，cellPoint 结合单元和顶点值插值。</td><td>条件必填</td><td><code>cell</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>对推进器载荷和尾流进行统计。origin、axis、n 定义转轴与转速，radius 和参考速度用于性能系数，sampleDisk 规定尾流采样圆盘。</p><pre><code class="language-foam">propellerInfo1
{
    type            propellerInfo;
    libs            (forces);
    writeControl    writeTime;
    patches         (&quot;propeller.*&quot;);
    URef            functionObjectValue;
    functionObject  propellerInfo1;
    functionObjectResult UzMean;
    rho             rhoInf;
    rhoInf          1.2;
    writePropellerPerformance yes;
    radius          0.1;
    rotationMode    specified;
    origin          (0 -0.1 0);
    axis            (0 1 0);
    n               25.15;
    writeWakeFields yes;
    sampleDisk
    {
        r1              0.05;
        r2              0.2;
        nTheta          36;
        nRadial         10;
        interpolationScheme cellPoint;
        surfaceWriter   vtk;
    }
}</code></pre><h3 id="example-2">示例 2 · 只保存性能指标</h3><p>关闭尾流数据，重点监测推力、转矩及相关性能。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeWakeFields false;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">propellerInfo1
{
    type            propellerInfo;
    libs            (forces);
    writeControl    writeTime;
    patches         (&quot;propeller.*&quot;);
    URef            functionObjectValue;
    functionObject  propellerInfo1;
    functionObjectResult UzMean;
    rho             rhoInf;
    rhoInf          1.2;
    writePropellerPerformance yes;
    radius          0.1;
    rotationMode    specified;
    origin          (0 -0.1 0);
    axis            (0 1 0);
    n               25.15;
    writeWakeFields false;
    sampleDisk
    {
        r1              0.05;
        r2              0.2;
        nTheta          36;
        nRadial         10;
        interpolationScheme cellPoint;
        surfaceWriter   vtk;
    }
}</code></pre></details><h3 id="example-3">示例 3 · 同时保存尾流</h3><p>保留采样圆盘上的流场信息，与推进器性能曲线对照。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeWakeFields true;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">propellerInfo1
{
    type            propellerInfo;
    libs            (forces);
    writeControl    writeTime;
    patches         (&quot;propeller.*&quot;);
    URef            functionObjectValue;
    functionObject  propellerInfo1;
    functionObjectResult UzMean;
    rho             rhoInf;
    rhoInf          1.2;
    writePropellerPerformance yes;
    radius          0.1;
    rotationMode    specified;
    origin          (0 -0.1 0);
    axis            (0 1 0);
    n               25.15;
    writeWakeFields true;
    sampleDisk
    {
        r1              0.05;
        r2              0.2;
        nTheta          36;
        nRadial         10;
        interpolationScheme cellPoint;
        surfaceWriter   vtk;
    }
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">propellerInfo1
{
    type            propellerInfo;
    libs            (forces);
    writeControl timeStep;
    patches         (&quot;propeller.*&quot;);
    URef            functionObjectValue;
    functionObject  propellerInfo1;
    functionObjectResult UzMean;
    rho             rhoInf;
    rhoInf          1.2;
    writePropellerPerformance yes;
    radius          0.1;
    rotationMode    specified;
    origin          (0 -0.1 0);
    axis            (0 1 0);
    n               25.15;
    writeWakeFields yes;
    sampleDisk
    {
        r1              0.05;
        r2              0.2;
        nTheta          36;
        nRadial         10;
        interpolationScheme cellPoint;
        surfaceWriter   vtk;
    }
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">propellerInfo1
{
    type            propellerInfo;
    libs            (forces);
    writeControl    writeTime;
    patches         (&quot;propeller.*&quot;);
    URef            functionObjectValue;
    functionObject  propellerInfo1;
    functionObjectResult UzMean;
    rho             rhoInf;
    rhoInf          1.2;
    writePropellerPerformance yes;
    radius          0.1;
    rotationMode    specified;
    origin          (0 -0.1 0);
    axis            (0 1 0);
    n               25.15;
    writeWakeFields yes;
    sampleDisk
    {
        r1              0.05;
        r2              0.2;
        nTheta          36;
        nRadial         10;
        interpolationScheme cellPoint;
        surfaceWriter   vtk;
    }
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/forces/propellerInfo/propellerInfo.H">OpenFOAM v2512 · propellerInfo 接口</a>。</p>
{% endraw %}
