---
title: "constant/fvOptions"
layout: "reference"
description: "fvOptions 用于配置源项和约束，文件位置由求解器的读取路径确定，常见于 constant 或 system。下例在指定 cellZone 内施加速度方程源项，采用 sources 条目。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>constant/fvOptions</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>active</code> · <code>selectionMode</code> · <code>cellZone</code> · <code>semiImplicitSource</code> · <code>scalarSemiImplicitSource</code> · <code>vectorSemiImplicitSource</code></p><h2>关联命令</h2><p><a href="/commands/?q=simpleFoam">simpleFoam</a> · <a href="/commands/?q=pimpleFoam">pimpleFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary constant/fvOptions -keywords
simpleFoam -help</code></pre><h2>9.9 constant/fvOptions</h2><p>fvOptions 用于配置源项和约束，文件位置由求解器的读取路径确定，常见于 constant 或 system。下例在指定 cellZone 内施加速度方程源项，采用 sources 条目。</p>
<pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object fvOptions;
}
drive
{
    type vectorSemiImplicitSource;
    active true;
    selectionMode cellZone;
    cellZone heater;
    volumeMode specific;
    sources
    {
        U ((0.1 0 0) 0);
    }
}</code></pre>
<p>半隐式源项写为 Su + Sp*字段，括号内依次给出显式项和隐式系数。specific 按单位体积定义，absolute 按所选体积的总量定义。源项量纲取决于控制方程；速度、动量以及以 h、e 或 T 为变量的能量方程应分别确定量纲和密度因子。</p>
<p>selectionMode 指定作用范围，可选 all、cellZone、cellSet 等；timeStart 和 duration 指定作用时间。常用类型包括 scalarSemiImplicitSource、vectorSemiImplicitSource、meanVelocityForce、explicitPorositySource、scalarFixedValueConstraint、limitTemperature 和 codedSource，其参数按对应模型设置。</p>
<h2>17.4 fvOptions（源项与区域模型）</h2><p>放在 system/fvOptions（或 constant/fvOptions）。它让你不改求解器就能加源项。</p>
<pre><code>momentumSource
{
    type            meanVelocityForce;      // 恒定流量驱动（周期性槽道流必用）
    active          yes;
    selectionMode   all;
    fields          (U);
    Ubar            (0.1335 0 0);
}

heatSource
{
    type            scalarSemiImplicitSource;
    active          yes;
    selectionMode   cellZone;
    cellZone        heater;
    volumeMode      absolute;               // absolute / specific
    sources         { h (500 0); }          // (显式部分 隐式部分)
}

porous
{
    type            explicitPorositySource;
    active          yes;
    selectionMode   cellZone;
    cellZone        porousZone;
    type            DarcyForchheimer;
    d   (5e7 -1000 -1000);
    f   (0 0 0);
    coordinateSystem { ... }
}

MRF1
{
    type            MRFSource;             // 旋转参考系（风机、搅拌器）
    selectionMode   cellZone;
    cellZone        rotor;
    origin          (0 0 0);
    axis            (0 0 1);
    omega           constant 104.72;       // rad/s
}</code></pre>
<p>常用类型还有：limitTemperature（限温，防发散）、limitVelocity、fixedTemperatureConstraint、buoyancyEnergy、radiation、solidificationMeltingSource（相变）、atmAmbientTurbSource（大气边界层）。</p>
<p>为什么它重要：初学者遇到”我要在某个区域加个热源/阻力/旋转”，第一反应常是去改求解器源码。用 fvOptions 一个字典就能解决，且不影响可维护性。</p>
{% endraw %}