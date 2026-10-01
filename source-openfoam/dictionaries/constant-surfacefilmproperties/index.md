---
title: "constant/surfaceFilmProperties · surfaceFilmProperties"
layout: reference
description: "壁面液膜区域的模型与耦合参数，包括液膜热物性、相变、颗粒与壁面相互作用等。液膜网格、区域名称和主流场之间的映射必须配套，不能仅复制单个字典完成耦合。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>壁面液膜区域的模型与耦合参数，包括液膜热物性、相变、颗粒与壁面相互作用等。液膜网格、区域名称和主流场之间的映射必须配套，不能仅复制单个字典完成耦合。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>surfaceFilmModel</td><td>表面液膜模型选择，需与液膜区域和主流体耦合条件配套。</td></tr><tr><td>region</td><td>目标网格区域名称；多区域场与网格路径中应保持一致。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>injectionModels</td><td>注入时间、位置、流量与粒径分布等设置；需要同时满足总注入质量与统计分辨率要求。</td></tr><tr><td>radiationModel</td><td>辐射传输模型名称，例如 P1、fvDOM 或 viewFactor；不同模型需要不同附加文件。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · combustion/fireFoam/LES/smallPoolFire3D</h3><p>原始路径：<code>tutorials/combustion/fireFoam/LES/smallPoolFire3D/constant/surfaceFilmProperties</code>；求解器：<code>fireFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/smallPoolFire3D/constant/surfaceFilmProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/surfacefilmproperties/1-surfaceFilmProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/smallPoolFire3D">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFilmProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

surfaceFilmModel none;

region          none;

active          false;


// ************************************************************************* //</code></pre><h3>示例 2 · lagrangian/reactingParcelFoam/cylinder</h3><p>原始路径：<code>tutorials/lagrangian/reactingParcelFoam/cylinder/constant/surfaceFilmProperties</code>；求解器：<code>reactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/cylinder/constant/surfaceFilmProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/surfacefilmproperties/2-surfaceFilmProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/cylinder">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFilmProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

surfaceFilmModel thermoSingleLayer;

region          wallFilmRegion;

active          true;

thermoSingleLayerCoeffs
{
    filmThermoModel liquid;

    liquidCoeffs
    {
        useReferenceValues  no;
        liquid      H2O;
    }

    filmViscosityModel liquid;

    deltaWet    1e-4;

    hydrophilic no;

    turbulence  laminar;
    laminarCoeffs
    {
        Cf          0.005;
    }

    forces
    (
        thermocapillary
    );

    injectionModels ();

    phaseChangeModel none;

    radiationModel none;

    upperSurfaceModels
    {
        heatTransferModel constant;
        constantCoeffs
        {
            c0                1e-8;
        }
    }

    lowerSurfaceModels
    {
        heatTransferModel constant;
        constantCoeffs
        {
            c0                1e-8;
        }
    }
}


// ************************************************************************* //</code></pre><h3>示例 3 · lagrangian/reactingParcelFoam/splashPanel</h3><p>原始路径：<code>tutorials/lagrangian/reactingParcelFoam/splashPanel/constant/surfaceFilmProperties</code>；求解器：<code>reactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/splashPanel/constant/surfaceFilmProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/surfacefilmproperties/3-surfaceFilmProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/splashPanel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFilmProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

surfaceFilmModel thermoSingleLayer;

region          wallFilmRegion;

active          true;

thermoSingleLayerCoeffs
{
    filmThermoModel liquid;

    liquidCoeffs
    {
        useReferenceValues  no;
        liquid      H2O;
    }

    filmViscosityModel liquid;

    deltaWet    2e-4;
    hydrophilic no;

    turbulence  laminar;
    laminarCoeffs
    {
        Cf          0.005;
    }

    forces
    (
        thermocapillary
    );

    injectionModels
    ();

    phaseChangeModel none;

    radiationModel none;

    upperSurfaceModels
    {
        heatTransferModel constant;
        constantCoeffs
        {
            c0                1e-8;
        }
    }

    lowerSurfaceModels
    {
        heatTransferModel constant;
        constantCoeffs
        {
            c0                1e-8;
        }
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/reactingparcelfoam/">reactingParcelFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/surfaceFilmProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/surfaceFilmProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
