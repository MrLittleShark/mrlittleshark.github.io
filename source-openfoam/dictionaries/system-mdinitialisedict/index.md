---
title: "system/mdInitialiseDict · mdInitialiseDict"
layout: reference
description: "分子初始排布、种类及速度分布的设置。过近的初始分子距离会引入极大排斥力，初始温度也依赖速度分配方式；初始化后先进行受控预平衡。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>分子初始排布、种类及速度分布的设置。过近的初始分子距离会引入极大排斥力，初始温度也依赖速度分配方式；初始化后先进行受控预平衡。</p><figure><img src="/assets/diagrams/reference-1.svg" alt="初始化配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>liquid</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // Euler angles, expressed in degrees as phi, theta, psi, see http://mathworld.wolfram.com/EulerAngles.html</td></tr><tr><td>sectionA</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // Euler angles, expressed in degrees as phi, theta, psi, see http://mathworld.wolfram.com/EulerAngles.html</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon</h3><p>原始路径：<code>tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon/system/mdInitialiseDict</code>；求解器：<code>mdEquilibrationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon/system/mdInitialiseDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/mdinitialisedict/1-mdInitialiseDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mdInitialiseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Euler angles, expressed in degrees as phi, theta, psi, see
// http://mathworld.wolfram.com/EulerAngles.html

liquid
{
    massDensity             1220;
    temperature             300;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds              (Ar);
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}


// ************************************************************************* //</code></pre><h3>示例 2 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater</h3><p>原始路径：<code>tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater/system/mdInitialiseDict</code>；求解器：<code>mdEquilibrationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater/system/mdInitialiseDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/mdinitialisedict/2-mdInitialiseDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mdInitialiseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Euler angles, expressed in degrees as phi, theta, psi, see
// http://mathworld.wolfram.com/EulerAngles.html

liquid
{
    massDensity             980;
    temperature             298;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds
    (
        water
        water2
        water
        water2
    );
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
        (0 0.5 0.5)
        (0.5 0 0.5)
        (0.5 0.5 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}


// ************************************************************************* //</code></pre><h3>示例 3 · discreteMethods/molecularDynamics/mdFoam/nanoNozzle</h3><p>原始路径：<code>tutorials/discreteMethods/molecularDynamics/mdFoam/nanoNozzle/system/mdInitialiseDict</code>；求解器：<code>mdFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdFoam/nanoNozzle/system/mdInitialiseDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/mdinitialisedict/3-mdInitialiseDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdFoam/nanoNozzle">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mdInitialiseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Euler angles, expressed in degrees as phi, theta, psi, see
// http://mathworld.wolfram.com/EulerAngles.html

sectionA
{
    massDensity             1004;
    temperature             298;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds
    (
        water
    );
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}

sectionB
{
    massDensity             1004;
    temperature             298;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds
    (
        water
    );
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}

sectionC
{
    massDensity             1004;
    temperature             298;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds
    (
        water
    );
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/mdinitialise/">mdInitialise</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/mdInitialiseDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/mdInitialiseDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
