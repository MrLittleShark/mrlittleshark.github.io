---
title: "constant/radiationProperties · radiationProperties"
layout: reference
description: "air 和 solidBlock 分别配置 constant/区域名/polyMesh、热物性文件以及 system/区域名 下的 fvSchemes 和 fvSolution。初始场位于 0/区域名/。流固界面通常采用 mappedWall 网格边界，并设置相邻区域映射和温度耦合条件。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>air 和 solidBlock 分别配置 constant/区域名/polyMesh、热物性文件以及 system/区域名 下的 fvSchemes 和 fvSolution。初始场位于 0/区域名/。流固界面通常采用 mappedWall 网格边界，并设置相邻区域映射和温度耦合条件。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>constant/radiationProperties</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>radiation</code> · <code>radiationModel</code> · <code>absorptionEmissionModel</code> · <code>scatterModel</code> · <code>sootModel</code></p><h2>关联命令</h2><p><a href="/commands/?q=buoyantSimpleFoam">buoyantSimpleFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary constant/radiationProperties -keywords
buoyantSimpleFoam -help</code></pre><h2>9.12 多区域传热及专用模型配置</h2><pre><code class="language-openfoam">// constant/regionProperties 片段
regions
(
    fluid (air)
    solid (solidBlock)
);</code></pre>
<p>air 和 solidBlock 分别配置 constant/区域名/polyMesh、热物性文件以及 system/区域名 下的 fvSchemes 和 fvSolution。初始场位于 0/区域名/。流固界面通常采用 mappedWall 网格边界，并设置相邻区域映射和温度耦合条件。</p>
<div class="table-scroll"><table>
<tr><th>文件</th><th>用途</th><th>主要参数</th></tr>
<tr><td>constant/radiationProperties</td><td>辐射模型</td><td>radiation on/off、radiationModel（P1、fvDOM、viewFactor 等）、solverFreq 及模型专用系数</td></tr>
<tr><td>constant/viewFactorsDict</td><td>视角因子设置</td><td>指定参与边界，按生成工具配置积分或射线参数</td></tr>
<tr><td>constant/chemistryProperties</td><td>化学积分</td><td>chemistry、chemistryType 中的 solver/method、initialChemicalTimeStep、ODE 系数</td></tr>
<tr><td>constant/combustionProperties</td><td>燃烧闭合模型</td><td>combustionModel 及 PaSR、EDC、laminar 等模型的专用系数</td></tr>
<tr><td>constant/reactions</td><td>反应机理</td><td>物种名称、反应式、速率系数；可由 chemkinToFoam 转换</td></tr>
<tr><td>constant/thermophysicalProperties.相名</td><td>多相分相热物性</td><td>各相 thermoType、状态方程、热容与输运</td></tr>
<tr><td>constant/phaseProperties</td><td>Euler 多相体系或特定多相模型</td><td>phases、直径模型、阻力、升力、传热等分相和相间模型</td></tr>
<tr><td>constant/kinematicCloudProperties 等</td><td>拉格朗日粒子云</td><td>solution、constantProperties、subModels、injectionModels、forces、patchInteractionModel</td></tr>
<tr><td>constant/sprayCloudProperties</td><td>喷雾云</td><td>在粒子设置基础上加入 atomization、breakup、phaseChange 等模型</td></tr>
<tr><td>constant/porosityProperties</td><td>部分求解器的多孔阻力入口</td><td>zone、Darcy–Forchheimer 系数及局部坐标；也可通过 fvOptions 配置</td></tr>
<tr><td>constant/solidProperties 或 mechanicalProperties</td><td>固体材料</td><td>按固体求解器设置 rho、E、nu 和 planeStress；此处 nu 表示泊松比</td></tr>
<tr><td>system/faSchemes、faSolution 的有限面积位置</td><td>面上离散与求解</td><td>v2512 常位于 system/finite-area/；使用 faMesh 对应的字段和算子</td></tr>
<tr><td>system/finite-area/faMeshDefinition</td><td>有限面积网格生成</td><td>polyMeshPatches、boundary、面选取和边界命名</td></tr>
<tr><td>system/optimisationDict</td><td>伴随优化</td><td>优化类型、设计变量、目标函数、约束和更新算法</td></tr>
</table></div>
<p>专用模型的配置项随物种机理、粒子模型、燃烧模型和优化算法变化。可通过 find &quot;$FOAM_TUTORIALS&quot; -name 文件名 查找对应求解器算例，并据模型源码确定条目层级及参数。</p>
<h2>18.6 radiationProperties</h2><pre><code class="language-openfoam">radiation       on;
radiationModel  P1;              // none / P1 / fvDOM / viewFactor / opaqueSolid
solverFreq      10;
absorptionEmissionModel constantAbsorptionEmission;
constantAbsorptionEmissionCoeffs { absorptivity 0.5; emissivity 0.5; E 0; }
scatterModel    none;</code></pre><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>radiation</td><td>辐射计算开关，需与模型、壁面辐射条件及能量方程配合。</td></tr><tr><td>radiationModel</td><td>辐射传输模型名称，例如 P1、fvDOM 或 viewFactor；不同模型需要不同附加文件。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · heatTransfer/chtMultiRegionFoam/externalCoupledHeater</h3><p>原始路径：<code>tutorials/heatTransfer/chtMultiRegionFoam/externalCoupledHeater/constant/heater/radiationProperties</code>；求解器：<code>chtMultiRegionFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/externalCoupledHeater/constant/heater/radiationProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/radiationproperties/1-radiationProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/externalCoupledHeater">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      radiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

radiation off;

radiationModel  none;


// ************************************************************************* //</code></pre><h3>示例 2 · lagrangian/reactingParcelFoam/verticalChannel</h3><p>原始路径：<code>tutorials/lagrangian/reactingParcelFoam/verticalChannel/constant/radiationProperties</code>；求解器：<code>reactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/verticalChannel/constant/radiationProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/radiationproperties/2-radiationProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/verticalChannel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      radiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

radiation       off;

radiationModel  none;

solverFreq      10;


// ************************************************************************* //</code></pre><h3>示例 3 · lagrangian/reactingParcelFoam/parcelInBox</h3><p>原始路径：<code>tutorials/lagrangian/reactingParcelFoam/parcelInBox/constant/radiationProperties</code>；求解器：<code>reactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/parcelInBox/constant/radiationProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/radiationproperties/3-radiationProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/parcelInBox">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;constant&quot;;
    object      radiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

radiation       off;

radiationModel  none;

// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/buoyantsimplefoam/">buoyantSimpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/heater/radiationProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/heater/radiationProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
