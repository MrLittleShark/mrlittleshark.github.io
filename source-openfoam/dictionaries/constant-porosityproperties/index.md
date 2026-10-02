---
title: "porosityProperties"
layout: reference
description: "部分专用求解器或教程中的多孔介质属性。"
dictionary: true
cms_slug: "dictionary-porosityproperties"
---

<p>部分专用求解器或教程中的多孔介质属性。</p><p>位置：<code>constant/porosityProperties</code></p><h2>配置实例</h2><p>multiphase/interIsoFoam/discInConstantPorousFlow 中的 porosityProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      porosityProperties;
}

porosityEnabled true;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>cellZone</td><td>源项、运动或材料区域所引用的单元区名称。</td></tr><tr><td>origin</td><td>局部坐标系、旋转或几何操作的参考原点。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/interIsoFoam/discInConstantPorousFlow</summary><p>discInConstantPorousFlow 用固定孔隙率分布测试界面随流动的输运。这个文件只有一个总开关。</p>
<ul>
<li><code>porosityEnabled true</code> 开启该算例使用的孔隙率处理。</li>
<li>空间分布由算例的孔隙率场及配套初始化提供；这里没有给出完整的 Darcy–Forchheimer 阻力系数。</li>
</ul>
<p>复用时连同场文件、初始化步骤和实际调用的求解流程一起复制，并查看固体占比变化是否与几何设置一致。</p>
<p><a href="/assets/examples/v2512/porosityproperties/1-porosityProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/discInConstantPorousFlow/constant/porosityProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/discInConstantPorousFlow">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      porosityProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

porosityEnabled true;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · verificationAndValidation/multiphase/interIsoFoam/porousDamBreak</summary><p>porousDamBreak 研究水体冲入多孔材料后的阻滞与惯性效应，interIsoFoam 将相应项加入动量方程。</p>
<ul>
<li><code>porosityEnabled true</code> 启用多孔处理，JensenEtAl2014Coeffs 提供本实现使用的参数。</li>
<li><code>alpha 500</code> 控制与黏度和速度相关的 Darcy 阻力部分；<code>beta 2</code> 控制随速度幅值增加的 Forchheimer 阻力部分。</li>
<li><code>d50 0.0159</code> 表示 15.9 mm 的代表性粒径。阻力公式包含粒径的一次、二次倒数，因此粒径变化会明显改变阻力。</li>
<li><code>KC 128</code> 进入惯性阻力修正因子 <code>1 + 7.5/KC</code>，<code>gamma_p 0.34</code> 通过 <code>Cm = gamma_p*(1 - porosity)</code> 设置附加质量项。</li>
</ul>
<p>孔隙率由空间场提供，材料系数与孔隙率应配套设定；比较迎水面水位、透水量与压力可以观察参数影响。</p>
<p><a href="/assets/examples/v2512/porosityproperties/2-porosityProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/interIsoFoam/porousDamBreak/constant/porosityProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/interIsoFoam/porousDamBreak">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      porosityProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

porosityModel JensenEtAl2014;

porosityEnabled true;

JensenEtAl2014Coeffs
{
    alpha 500;
    beta 2;
    gamma_p 0.34;
    d50 0.0159;
    KC 128;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/porousSimpleFoam/straightDuctImplicit</summary><p>straightDuctImplicit 用 Darcy–Forchheimer 模型表示管道中的各向异性多孔阻力。</p>
<ul>
<li><code>cellZone porosity</code> 将阻力限定在名为 porosity 的单元区。</li>
<li><code>d (5e7 -1000 -1000)</code> 的 x 分量是 5×10⁷ m⁻²；负分量采用“最大正分量的倍数”写法，因此 y、z 对应 5×10¹⁰ m⁻²，强烈抑制横向运动。</li>
<li><code>f (0 0 0)</code> 关闭二次速度阻力项，保留线性 Darcy 项。</li>
<li>局部坐标的 e1、e2 分别沿 x、y，决定这些阻力主方向在网格中的方向。</li>
</ul>
<p>旋转多孔介质时修改局部坐标方向；拟合实验压降时同时检查长度、黏度、流速和阻力单位。</p>
<p><a href="/assets/examples/v2512/porosityproperties/3-porosityProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/porousSimpleFoam/straightDuctImplicit/constant/porosityProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/porousSimpleFoam/straightDuctImplicit">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      porosityProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

porosity1
{
    type            DarcyForchheimer;

    cellZone        porosity;

    d   (5e7 -1000 -1000);
    f   (0 0 0);

    coordinateSystem
    {
        origin  (0 0 0);
        e1      (1 0 0);
        e2      (0 1 0);
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/poroussimplefoam/">porousSimpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
