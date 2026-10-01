---
title: "constant/boundaryRadiationProperties · boundaryRadiationProperties"
layout: reference
description: "按边界配置辐射发射率、吸收率或透射率的模型。体介质的 radiationProperties 与壁面的辐射属性承担不同职责；不透明灰壁、半透明壁面和与相邻区域耦合的壁面需要不同处理。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>按边界配置辐射发射率、吸收率或透射率的模型。体介质的 radiationProperties 与壁面的辐射属性承担不同职责；不透明灰壁、半透明壁面和与相邻区域耦合的壁面需要不同处理。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>emissivity</td><td>发射率或发射率模型输入；应与辐射模型和壁面物理条件一致。</td></tr><tr><td>absorptivity</td><td>吸收率或其模型输入。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · combustion/fireFoam/LES/simplePMMApanel</h3><p>原始路径：<code>tutorials/combustion/fireFoam/LES/simplePMMApanel/constant/boundaryRadiationProperties</code>；求解器：<code>fireFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/simplePMMApanel/constant/boundaryRadiationProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/boundaryradiationproperties/1-boundaryRadiationProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/simplePMMApanel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      boundaryRadiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

&quot;.*&quot;
{
    type            lookup;
    emissivity      1.0;
}


// ************************************************************************* //</code></pre><h3>示例 2 · combustion/reactingFoam/RAS/SandiaD_LTS</h3><p>原始路径：<code>tutorials/combustion/reactingFoam/RAS/SandiaD_LTS/constant/boundaryRadiationProperties</code>；求解器：<code>reactingFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS/constant/boundaryRadiationProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/boundaryradiationproperties/2-boundaryRadiationProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      boundaryRadiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

&quot;.*&quot;
{
    type            lookup;
    emissivity      1;
    absorptivity    0;
}


// ************************************************************************* //</code></pre><h3>示例 3 · heatTransfer/buoyantSimpleFoam/hotRadiationRoom</h3><p>原始路径：<code>tutorials/heatTransfer/buoyantSimpleFoam/hotRadiationRoom/constant/boundaryRadiationProperties</code>；求解器：<code>buoyantSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/hotRadiationRoom/constant/boundaryRadiationProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/boundaryradiationproperties/3-boundaryRadiationProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/hotRadiationRoom">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      boundaryRadiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

&quot;.*&quot;
{
    type            lookup;
    emissivity      1.0;
    absorptivity    1.0;
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/buoyantsimplefoam/">buoyantSimpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/boundaryRadiationProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/boundaryRadiationProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
