---
title: "constant/thermophysicalProperties"
layout: "reference"
description: "下例采用单相理想气体、常热容和常输运系数，能量变量为显焓。热物性类型和能量形式应与求解器接口对应。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>constant/thermophysicalProperties</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>thermoType</code> · <code>type</code> · <code>mixture</code> · <code>transport</code> · <code>thermo</code> · <code>equationOfState</code> · <code>specie</code> · <code>energy</code></p><h2>关联命令</h2><p><a href="/commands/?q=rhoPimpleFoam">rhoPimpleFoam</a> · <a href="/commands/?q=chtMultiRegionFoam">chtMultiRegionFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary constant/thermophysicalProperties -keywords
rhoPimpleFoam -help</code></pre><h2>9.7 constant/thermophysicalProperties</h2><p>下例采用单相理想气体、常热容和常输运系数，能量变量为显焓。热物性类型和能量形式应与求解器接口对应。</p>
<pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object thermophysicalProperties;
}
thermoType
{
    type hePsiThermo;
    mixture pureMixture;
    transport const;
    thermo hConst;
    equationOfState perfectGas;
    specie specie;
    energy sensibleEnthalpy;
}
mixture
{
    specie { molWeight 28.96; }
    thermodynamics { Cp 1005; Hf 0; }
    transport { mu 1.8e-5; Pr 0.7; }
}</code></pre>
<div class="table-scroll"><table>
<tr><th>参数</th><th>作用</th><th>设置方法</th></tr>
<tr><td>type</td><td>热物性基类</td><td>hePsiThermo、heRhoThermo 等；须与求解器匹配</td></tr>
<tr><td>mixture</td><td>混合物模型</td><td>pureMixture 单组分；反应流使用相应多组分模型</td></tr>
<tr><td>transport</td><td>输运模型</td><td>const、sutherland 等</td></tr>
<tr><td>thermo</td><td>热容模型</td><td>hConst 常热容；janaf 温度相关多项式</td></tr>
<tr><td>equationOfState</td><td>状态方程</td><td>perfectGas、rhoConst 等，按介质状态关系选择</td></tr>
<tr><td>energy</td><td>能量变量</td><td>sensibleEnthalpy 或 sensibleInternalEnergy 等</td></tr>
<tr><td>molWeight</td><td>摩尔质量</td><td>单位为 kg/kmol，空气示例为 28.96</td></tr>
<tr><td>Cp、Hf</td><td>定压比热、生成焓</td><td>按模型定义及参考态赋值</td></tr>
<tr><td>mu、Pr</td><td>动力黏度和 Prandtl 数</td><td>采用一致的单位与适用温度范围</td></tr>
<tr><td>As、Ts</td><td>Sutherland 输运系数</td><td>选择 sutherland 后按该模型填写</td></tr>
<tr><td>Tlow、Thigh、Tcommon、lowCpCoeffs、highCpCoeffs</td><td>JANAF 温度区间及系数</td><td>从可靠物性数据或机理文件提取</td></tr>
</table></div>
<p>rhoCentralFoam 等采用相应的热物性基类和能量变量。使用显内能的求解器应配置 sensibleInternalEnergy，并保留配套教程中的热物性组合。</p>
<h2>18.3 thermophysicalProperties（可压/传热必需）</h2><pre><code>thermoType
{
    type            hePsiThermo;          // hePsiThermo(可压理想气体) / heRhoThermo(液体)
    mixture         pureMixture;          // 单组分
    transport       sutherland;           // const / sutherland / polynomial
    thermo          janaf;                // hConst / eConst / janaf
    equationOfState perfectGas;           // perfectGas / rhoConst / Boussinesq / PengRobinson
    specie          specie;
    energy          sensibleInternalEnergy;   // sensibleEnthalpy / sensibleInternalEnergy
}

mixture
{
    specie          { molWeight  28.96; }
    thermodynamics  { Cp 1004.5; Hf 0; }
    transport       { mu 1.8e-05; Pr 0.7; }
}</code></pre>
<p>七个字段各自的意思：type 决定用 \(\psi (=1/RT)\) 还是 \(\rho\) 作为基本量；mixture 是单组分还是多组分；transport 是粘性/导热系数的模型；thermo 是比热模型（hConst 常数比热，janaf 用 JANAF 多项式）；equationOfState 是状态方程；energy 是用焓还是内能作为求解变量。修改时七个字段必须相互兼容，不兼容时报错信息会把所有合法组合列出来——照着报错里的列表挑就行，这是 OpenFOAM 少数几个报错比文档还好用的地方。</p>
<p>sensibleEnthalpy 还是 sensibleInternalEnergy：基于压力的求解器（rhoPimpleFoam）一般用焓；基于密度的（rhoCentralFoam）用内能。照抄对应教程即可。</p>
{% endraw %}