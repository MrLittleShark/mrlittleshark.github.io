---
title: "constant/thermophysicalProperties · thermophysicalProperties"
layout: reference
description: "下例采用单相理想气体、常热容和常输运系数，能量变量为显焓。热物性类型和能量形式应与求解器接口对应。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>下例采用单相理想气体、常热容和常输运系数，能量变量为显焓。热物性类型和能量形式应与求解器接口对应。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>constant/thermophysicalProperties</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>thermoType</code> · <code>type</code> · <code>mixture</code> · <code>transport</code> · <code>thermo</code> · <code>equationOfState</code> · <code>specie</code> · <code>energy</code></p><h2>关联命令</h2><p><a href="/commands/?q=rhoPimpleFoam">rhoPimpleFoam</a> · <a href="/commands/?q=chtMultiRegionFoam">chtMultiRegionFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary constant/thermophysicalProperties -keywords
rhoPimpleFoam -help</code></pre><h2>9.7 constant/thermophysicalProperties</h2><p>下例采用单相理想气体、常热容和常输运系数，能量变量为显焓。热物性类型和能量形式应与求解器接口对应。</p>
<pre><code class="language-openfoam">FoamFile
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
<h2>18.3 thermophysicalProperties（可压/传热必需）</h2><pre><code class="language-openfoam">thermoType
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
<p>sensibleEnthalpy 还是 sensibleInternalEnergy：基于压力的求解器（rhoPimpleFoam）一般用焓；基于密度的（rhoCentralFoam）用内能。照抄对应教程即可。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>phases</td><td>相名称列表；这些名称会影响相分数、速度、热物性等字段或字典的命名。</td></tr><tr><td>sigma</td><td>常见为表面张力系数，但在电磁模型中可表示电导率；以模型与量纲为准。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>TSat</td><td>saturation temperature</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · multiphase/interCondensatingEvaporatingFoam/condensatingVessel</h3><p>原始路径：<code>tutorials/multiphase/interCondensatingEvaporatingFoam/condensatingVessel/constant/thermophysicalProperties</code>；求解器：<code>interCondensatingEvaporatingFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interCondensatingEvaporatingFoam/condensatingVessel/constant/thermophysicalProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/thermophysicalproperties/1-thermophysicalProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interCondensatingEvaporatingFoam/condensatingVessel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      thermophysicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

TSat             367;   // saturation temperature


// ************************************************************************* //</code></pre><h3>示例 2 · multiphase/compressibleInterDyMFoam/laminar/sloshingTank2D</h3><p>原始路径：<code>tutorials/multiphase/compressibleInterDyMFoam/laminar/sloshingTank2D/constant/thermophysicalProperties</code>；求解器：<code>compressibleInterDyMFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/compressibleInterDyMFoam/laminar/sloshingTank2D/constant/thermophysicalProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/thermophysicalproperties/2-thermophysicalProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/compressibleInterDyMFoam/laminar/sloshingTank2D">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      thermophysicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

phases          (water air);

pMin            1000;

sigma           0;


// ************************************************************************* //</code></pre><h3>示例 3 · multiphase/compressibleInterFoam/laminar/depthCharge3D</h3><p>原始路径：<code>tutorials/multiphase/compressibleInterFoam/laminar/depthCharge3D/constant/thermophysicalProperties</code>；求解器：<code>compressibleInterFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/depthCharge3D/constant/thermophysicalProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/thermophysicalproperties/3-thermophysicalProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/depthCharge3D">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      thermophysicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

phases          (water air);

pMin            10000;

sigma           0.07;


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/rhopimplefoam/">rhoPimpleFoam</a> · <a href="/commands/chtmultiregionfoam/">chtMultiRegionFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/thermophysicalProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/thermophysicalProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
