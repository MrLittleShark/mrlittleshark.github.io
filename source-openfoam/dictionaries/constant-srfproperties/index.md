---
title: "constant/SRFProperties"
layout: "reference"
description: "rotor 为预先建立的 cellZone，omega 的单位为 rad/s。nonRotatingPatches 指定区域内保持静止的边界。MRF 在固定网格上采用旋转参考系近似处理。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>constant/SRFProperties</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>SRFModel</code> · <code>origin</code> · <code>axis</code> · <code>rpm</code></p><h2>关联命令</h2><p><a href="/commands/?q=SRFSimpleFoam">SRFSimpleFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary constant/SRFProperties -keywords
SRFSimpleFoam -help</code></pre><h2>9.10 constant/MRFProperties 与 SRFProperties</h2><pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object MRFProperties;
}
rotorZone
{
    active yes;
    cellZone rotor;
    nonRotatingPatches (stator);
    origin (0 0 0);
    axis (0 0 1);
    omega constant 100;
}</code></pre>
<p>rotor 为预先建立的 cellZone，omega 的单位为 rad/s。nonRotatingPatches 指定区域内保持静止的边界。MRF 在固定网格上采用旋转参考系近似处理。</p>
<p>SRFProperties 配置单参考系模型，常用 SRFModel rpm 和 rpmCoeffs/rpm，以 rpm 表示转速。使用两种模型时应分别采用对应的角速度单位。</p>
{% endraw %}