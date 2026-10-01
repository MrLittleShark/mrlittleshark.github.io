---
title: "constant/moleculeProperties · moleculeProperties"
layout: reference
description: "分子动力学系统的分子种类与分子属性。需要与势函数、约束、温度初始化和边界处理共同配置；分子尺度参数不能直接套用宏观流体黏度。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>分子动力学系统的分子种类与分子属性。需要与势函数、约束、温度初始化和边界处理共同配置；分子尺度参数不能直接套用宏观流体黏度。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>Ar</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>water</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon</h3><p>原始路径：<code>tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon/constant/moleculeProperties</code>；求解器：<code>mdEquilibrationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon/constant/moleculeProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/moleculeproperties/1-moleculeProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      moleculeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

Ar
{
    siteIds                     (Ar);
    pairPotentialSiteIds        (Ar);
    siteReferencePositions
    (
        (0 0 0)
    );
    siteMasses
    (
        6.63352033e-26
    );
    siteCharges
    (
        0
    );
}


// ************************************************************************* //</code></pre><h3>示例 2 · discreteMethods/molecularDynamics/mdFoam/nanoNozzle</h3><p>原始路径：<code>tutorials/discreteMethods/molecularDynamics/mdFoam/nanoNozzle/constant/moleculeProperties</code>；求解器：<code>mdFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdFoam/nanoNozzle/constant/moleculeProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/moleculeproperties/2-moleculeProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdFoam/nanoNozzle">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      moleculeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

water
{
    siteIds                     (H H O M);
    pairPotentialSiteIds        (O);
    siteReferencePositions
    (
        (7.56950327263661e-11 5.85882276618295e-11 0)
        (-7.56950327263661e-11 5.85882276618295e-11 0)
        (0 0 0)
        (0 1.5e-11 0)
    );
    siteMasses
    (
        1.67353255e-27
        1.67353255e-27
        2.6560176e-26
        0
    );
    siteCharges
    (
        8.3313177324e-20
        8.3313177324e-20
        0
        -1.66626354648e-19
    );
}


// ************************************************************************* //</code></pre><h3>示例 3 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater</h3><p>原始路径：<code>tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater/constant/moleculeProperties</code>；求解器：<code>mdEquilibrationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater/constant/moleculeProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/moleculeproperties/3-moleculeProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      moleculeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

water
{
    siteIds                     (H H O M);
    pairPotentialSiteIds        (O);
    siteReferencePositions
    (
        (7.56950327263661e-11 5.85882276618295e-11 0)
        (-7.56950327263661e-11 5.85882276618295e-11 0)
        (0 0 0)
        (0 1.5e-11 0)
    );
    siteMasses
    (
        1.67353255e-27
        1.67353255e-27
        2.6560176e-26
        0
    );
    siteCharges
    (
        8.3313177324e-20
        8.3313177324e-20
        0
        -1.66626354648e-19
    );
}

water2
{
    siteIds                     (H2 H2 O M2);
    pairPotentialSiteIds        (O);
    siteReferencePositions
    (
        (7.56950327263661e-11 5.85882276618295e-11 0)
        (-7.56950327263661e-11 5.85882276618295e-11 0)
        (0 0 0)
        (0 1.5e-11 0)
    );
    siteMasses
    (
        1.67353255e-27
        1.67353255e-27
        2.6560176e-26
        0
    );
    siteCharges
    (
        8.3313177324e-20
        8.3313177324e-20
        0
        -1.66626354648e-19
    );
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/mdfoam/">mdFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/moleculeProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/moleculeProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
