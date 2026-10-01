---
title: "0/p_rgh"
layout: "reference"
description: "温度场 T 采用温度量纲，初值示例为 internalField uniform 300;。等温壁面使用 fixedValue，绝热壁面通常使用 zeroGradient。externalWallHeatFluxTemperature 可指定热通量或功率，并通过 mode、kappaMethod 等"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>0/p_rgh</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dimensions</code> · <code>internalField</code> · <code>boundaryField</code> · <code>fixedFluxPressure</code> · <code>prghPressure</code></p><h2>关联命令</h2><p><a href="/commands/?q=interFoam">interFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary 0/p_rgh -keywords
interFoam -help</code></pre><h2>9.3 温度场与多相流场</h2><p>温度场 T 采用温度量纲，初值示例为 internalField uniform 300;。等温壁面使用 fixedValue，绝热壁面通常使用 zeroGradient。externalWallHeatFluxTemperature 可指定热通量或功率，并通过 mode、kappaMethod 等参数定义施加方式和导热率来源。</p>
<p>p_rgh 表示扣除静水压项后的压力，常见定义为 \(p_{\mathrm{rgh}}=p-\rho gh\)。参考高度和量纲由求解器确定，不可压缩 Boussinesq 模型可采用归一化形式。恢复实际压力时，应按该求解器的定义还原静水压项。</p>
<p>alpha.water 表示水相体积分数，为无量纲量，取值范围为 [0,1]；多相体系中各相体积分数之和为 1。入口可指定相分数，开放边界可采用 inletOutlet，壁面可采用 zeroGradient 或接触角条件。字段后缀 water 与 phases 中的相名对应。</p>
<h2>19.4 压力 p / p_rgh 的常用边界条件</h2><div class="table-scroll"><table>
<tr><th>type</th><th>作用</th></tr>
<tr><td>zeroGradient</td><td>壁面标准做法（不可压）</td></tr>
<tr><td>fixedValue</td><td>出口给定压力（不可压时值是 \(p/\rho\)）</td></tr>
<tr><td>totalPressure</td><td>给定总压，静压随速度自动调整</td></tr>
<tr><td>fixedFluxPressure</td><td>壁面与动网格的正确做法：保证边界通量与速度边界一致</td></tr>
<tr><td>prghPressure / prghTotalPressure</td><td>多相流的 p_rgh（已扣除静水压）</td></tr>
<tr><td>freestreamPressure</td><td>远场</td></tr>
<tr><td>waveTransmissive</td><td>无反射出口（可压缩，防激波反射回来）</td></tr>
</table></div>
<pre><code>// 不可压出口
outlet { type fixedValue; value uniform 0; }

// 壁面（含浮力/动网格时必须这样写）
walls  { type fixedFluxPressure; value uniform 0; }

// 可压超声速出口，防止反射
outlet
{
    type            waveTransmissive;
    field           p;
    gamma           1.4;
    value           uniform 1e5;
}</code></pre>
<p>为什么壁面上不能简单写 zeroGradient：有重力或者动网格时，壁面法向压力梯度并不为零（要平衡重力/加速度）。fixedFluxPressure 会自动按动量方程推出正确的梯度。写错的后果是质量不守恒、界面处出现虚假速度。</p>
<p>p 和 p_rgh 的区别：多相流和浮力问题里求解的是 \(p_{\mathrm{rgh}}=p-\rho\boldsymbol g\cdot\boldsymbol h\)（扣掉静水压），这样数值上更好解。你在 0/ 里给的是 p_rgh，p 由程序算出。边界条件要给在 p_rgh 上。</p>
{% endraw %}