---
title: "bladeForces"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-bladeforces"
description: "推进器和叶片载荷"
---
{% raw %}
<p>推进器和叶片载荷</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    _bladeForces
    {
        type    bladeForces;
        libs    (forces);
        writeControl    timeStep;
        writeInterval   1;
        writeFields     true;
        fieldsInterval   1;
        patches     (&quot;propeller.*&quot;);
        outputName  blades;
        lefthand    true;
        rho         rhoInf;
        log         true;
        rhoInf      1;
        origin      (0 0 0);
        axis        (1 0 0);
        radius      0.5;
        nRadial     10;
        n           25;
        Uref        5;
        pRef        0;
        nearCellValue   true;
    }
}</code></pre><p>分析旋转叶片上的载荷分布。本例以 x 轴为转轴、25 转/秒为转速，并沿半径分段；nearCellValue 选择从邻近流体单元读取速度的方式。</p><p>配套教程配置：<code>incompressible/pimpleFoam/RAS/propeller1/system/bladeForces</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>bladeForces</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(forces)</code></td></tr><tr><td><code>patches</code></td><td>需要处理的边界名称列表；支持名称匹配表达式。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>writeFields</code></td><td>是否将计算得到的场或所选原始场写出。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>fieldsInterval</code></td><td>保存表面场的间隔，相对于 writeInterval 指定的输出频率。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>useNamePrefix</code></td><td>在输出名称前加对象名前缀，便于区分多个同类对象。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>outputName</code></td><td>注册到对象数据库及写出 VTP 文件时使用的表面名称。</td><td>可选</td><td><code>&lt;name&gt;</code></td></tr><tr><td><code>origin</code></td><td>局部坐标系或旋转轴的原点。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>axis</code></td><td>旋转轴或圆柱坐标系的轴向向量。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>n</code></td><td>旋转速度，单位转/秒；rpm 使用转/分钟。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>rpm</code></td><td>每分钟转数。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>p</code></td><td>压力场名称。</td><td>可选</td><td><code>p</code></td></tr><tr><td><code>U</code></td><td>速度场名称。</td><td>可选</td><td><code>U</code></td></tr><tr><td><code>rho</code></td><td>密度场名称；使用常密度时按示例选择 rhoInf。</td><td>可选</td><td><code>rho</code></td></tr><tr><td><code>rhoInf</code></td><td>不可压缩计算使用的参考密度。</td><td>条件必填</td><td><code>1</code></td></tr><tr><td><code>pRef</code></td><td>参考压力。</td><td>条件必填</td><td><code>0</code></td></tr><tr><td><code>Uref</code></td><td>参考速度。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>radius</code></td><td>叶片外半径。</td><td>可选</td><td><code>1</code></td></tr><tr><td><code>nRadial</code></td><td>径向采样分段数量。</td><td>可选</td><td><code>10</code></td></tr><tr><td><code>lefthand</code></td><td>是否采用左旋叶片约定。</td><td>条件必填</td><td><code>false</code></td></tr><tr><td><code>nearCellValue</code></td><td>使用邻近流体单元值外推边界速度。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>geometricVelocity</code></td><td>按边界位置变化计算几何速度。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>mag.thrust</code></td><td>是否对推力取绝对值。</td><td>条件必填</td><td><code>false</code></td></tr><tr><td><code>mag.drag</code></td><td>是否对阻力取绝对值。</td><td>条件必填</td><td><code>false</code></td></tr><tr><td><code>writeToFile</code></td><td>是否保存统计文本文件</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>writePrecision</code></td><td>文本数值的有效位数</td><td>可选</td><td><code>全局写出精度</code></td></tr><tr><td><code>useUserTime</code></td><td>是否采用用户时间单位</td><td>可选</td><td><code>true</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>分析旋转叶片上的载荷分布。本例以 x 轴为转轴、25 转/秒为转速，并沿半径分段；nearCellValue 选择从邻近流体单元读取速度的方式。</p><pre><code class="language-foam">_bladeForces
{
    type    bladeForces;
    libs    (forces);
    writeControl    timeStep;
    writeInterval   1;
    writeFields     true;
    fieldsInterval   1;
    patches     (&quot;propeller.*&quot;);
    outputName  blades;
    lefthand    true;
    rho         rhoInf;
    log         true;
    rhoInf      1;
    origin      (0 0 0);
    axis        (1 0 0);
    radius      0.5;
    nRadial     10;
    n           25;
    Uref        5;
    pRef        0;
    nearCellValue   true;
}</code></pre><h3 id="example-2">示例 2 · 减少径向分段</h3><p>较少分段便于先观察沿半径的总体变化。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">nRadial 5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">_bladeForces
{
    type    bladeForces;
    libs    (forces);
    writeControl    timeStep;
    writeInterval   1;
    writeFields     true;
    fieldsInterval   1;
    patches     (&quot;propeller.*&quot;);
    outputName  blades;
    lefthand    true;
    rho         rhoInf;
    log         true;
    rhoInf      1;
    origin      (0 0 0);
    axis        (1 0 0);
    radius      0.5;
    nRadial 5;
    n           25;
    Uref        5;
    pRef        0;
    nearCellValue   true;
}</code></pre></details><h3 id="example-3">示例 3 · 加密径向分段</h3><p>在几何与网格分辨率允许的条件下观察更细的叶片载荷分布。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">nRadial 20;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">_bladeForces
{
    type    bladeForces;
    libs    (forces);
    writeControl    timeStep;
    writeInterval   1;
    writeFields     true;
    fieldsInterval   1;
    patches     (&quot;propeller.*&quot;);
    outputName  blades;
    lefthand    true;
    rho         rhoInf;
    log         true;
    rhoInf      1;
    origin      (0 0 0);
    axis        (1 0 0);
    radius      0.5;
    nRadial 20;
    n           25;
    Uref        5;
    pRef        0;
    nearCellValue   true;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">_bladeForces
{
    type    bladeForces;
    libs    (forces);
    writeControl timeStep;
    writeInterval 10;
    writeFields     true;
    fieldsInterval   1;
    patches     (&quot;propeller.*&quot;);
    outputName  blades;
    lefthand    true;
    rho         rhoInf;
    log         true;
    rhoInf      1;
    origin      (0 0 0);
    axis        (1 0 0);
    radius      0.5;
    nRadial     10;
    n           25;
    Uref        5;
    pRef        0;
    nearCellValue   true;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">_bladeForces
{
    type    bladeForces;
    libs    (forces);
    writeControl    timeStep;
    writeInterval   1;
    writeFields     true;
    fieldsInterval   1;
    patches     (&quot;propeller.*&quot;);
    outputName  blades;
    lefthand    true;
    rho         rhoInf;
    log         true;
    rhoInf      1;
    origin      (0 0 0);
    axis        (1 0 0);
    radius      0.5;
    nRadial     10;
    n           25;
    Uref        5;
    pRef        0;
    nearCellValue   true;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/forces/bladeForces/bladeForces.H">OpenFOAM v2512 · bladeForces 接口</a>。</p>
{% endraw %}
