---
title: "constant/phaseChangeProperties · phaseChangeProperties"
layout: reference
description: "interCondensatingEvaporatingFoam 的凝结与蒸发模型配置。phaseChangeTwoPhaseModel 选择模型，constantCoeffs 中 coeffC 与 coeffE 分别控制凝结与蒸发模型系数。它与等温空化求解器在 transportProperties 中选择的相变模型不是同一套接口。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>interCondensatingEvaporatingFoam 的凝结与蒸发模型配置。phaseChangeTwoPhaseModel 选择模型，constantCoeffs 中 coeffC 与 coeffE 分别控制凝结与蒸发模型系数。它与等温空化求解器在 transportProperties 中选择的相变模型不是同一套接口。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>phaseChangeTwoPhaseModel</td><td>相变模型名称，本页凝结教程选择 constant。</td></tr><tr><td>constantCoeffs</td><td>与 constant 模型对应的系数字典。</td></tr><tr><td>coeffC</td><td>凝结方向的模型系数，含义由该相变模型实现确定。</td></tr><tr><td>coeffE</td><td>蒸发方向的模型系数，不能假定与 coeffC 总应相等。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>phaseChangeTwoPhaseModel</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 2 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · multiphase/interCondensatingEvaporatingFoam/condensatingVessel</h3><p>原始路径：<code>tutorials/multiphase/interCondensatingEvaporatingFoam/condensatingVessel/constant/phaseChangeProperties</code>；求解器：<code>interCondensatingEvaporatingFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interCondensatingEvaporatingFoam/condensatingVessel/constant/phaseChangeProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/phasechangeproperties/1-phaseChangeProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interCondensatingEvaporatingFoam/condensatingVessel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      phaseChangeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

phaseChangeTwoPhaseModel constant;

constantCoeffs
{
    coeffC          150;
    coeffE          150;
}


// ************************************************************************* //</code></pre><h3>示例 2 · verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam</h3><p>原始路径：<code>tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam/constant/phaseChangeProperties</code>；求解器：<code>interCondensatingEvaporatingFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam/constant/phaseChangeProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/phasechangeproperties/2-phaseChangeProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      phaseChangeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

phaseChangeTwoPhaseModel interfaceHeatResistance;//constant;


R               1e6;
maxAlphaRate    1;
spread          3;


coeffC          0;
coeffE          500;

// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/intercondensatingevaporatingfoam/">interCondensatingEvaporatingFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/phaseChangeProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/phaseChangeProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
