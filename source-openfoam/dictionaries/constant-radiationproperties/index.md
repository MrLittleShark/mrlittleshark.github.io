---
title: "constant/radiationProperties"
layout: "reference"
description: "air 和 solidBlock 分别配置 constant/区域名/polyMesh、热物性文件以及 system/区域名 下的 fvSchemes 和 fvSolution。初始场位于 0/区域名/。流固界面通常采用 mappedWall 网格边界，并设置相邻区域映射和温度耦合条件。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>constant/radiationProperties</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>radiation</code> · <code>radiationModel</code> · <code>absorptionEmissionModel</code> · <code>scatterModel</code> · <code>sootModel</code></p><h2>关联命令</h2><p><a href="/commands/?q=buoyantSimpleFoam">buoyantSimpleFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary constant/radiationProperties -keywords
buoyantSimpleFoam -help</code></pre><h2>9.12 多区域传热及专用模型配置</h2><pre><code>// constant/regionProperties 片段
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
<h2>18.6 radiationProperties</h2><pre><code>radiation       on;
radiationModel  P1;              // none / P1 / fvDOM / viewFactor / opaqueSolid
solverFreq      10;
absorptionEmissionModel constantAbsorptionEmission;
constantAbsorptionEmissionCoeffs { absorptivity 0.5; emissivity 0.5; E 0; }
scatterModel    none;</code></pre>
{% endraw %}