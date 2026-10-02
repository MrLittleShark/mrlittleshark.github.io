---
title: "setFieldsDict"
layout: reference
description: "用几何区域为已有场赋初值，例如设置溃坝算例的初始水柱。"
dictionary: true
cms_slug: "dictionary-setfieldsdict"
---

<p>用几何区域为已有场赋初值，例如设置溃坝算例的初始水柱。</p><p>位置：<code>system/setFieldsDict</code></p><h2>配置实例</h2><p>setFields 首先按 defaultFieldValues 设置全域初值，再依次执行 regions 中的区域赋值。区域重叠时，后续赋值覆盖先前结果。目标场文件须预先建立，并设置相应的 class 和 dimensions。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object setFieldsDict;
}
defaultFieldValues
(
    volScalarFieldValue alpha.water 0
    volVectorFieldValue U (0 0 0)
);
regions
(
    boxToCell
    {
        box (0 0 -1) (0.2 0.3 1);
        fieldValues (volScalarFieldValue alpha.water 1);
    }
);</code></pre>
<p>boxToCell 按单元位置选取长方体区域；sphereToCell 通过 centre 和 radius 定义球形区域；cylinderToCell 通过 p1、p2 和 radius 定义圆柱区域。边界面可采用 boxToFace 等选择器。</p>
<p>赋值后检查 alpha.water 的极值与空间分布，边界条件在场文件中另行设置。需采用数学表达式赋值时，使用 setExprFields。</p>
<h2>17.2 setFieldsDict（区域初始化）</h2><pre><code class="language-openfoam">defaultFieldValues              // 先把全场设成默认值
(
    volScalarFieldValue alpha.water 0
    volVectorFieldValue U (0 0 0)
);

regions                          // 再覆盖指定区域
(
    boxToCell
    {
        box (0 0 -1) (0.1461 0.292 1);
        fieldValues ( volScalarFieldValue alpha.water 1 );
    }

    cylinderToCell
    {
        p1 (0 0 0);  p2 (0 0 0.1);  radius 0.05;
        fieldValues ( volScalarFieldValue T 500 );
    }

    sphereToCell
    {
        origin (0 0 0);  radius 0.1;
        fieldValues ( volScalarFieldValue p 1e6 );
    }
);</code></pre>
<p>常用区域类型：boxToCell、sphereToCell、cylinderToCell、rotatedBoxToCell、surfaceToCell（用 STL 划区）、cellToCell（用已有 cellSet）、zoneToCell。</p>
<p>注意：setFields 直接修改 0/ 里的文件。跑之前先 cp -r 0.orig 0，否则第二次运行是在被改过的场上再改一次。</p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>defaultFieldValues</td><td>在局部区域赋值之前设置的默认场值。</td></tr><tr><td>regions</td><td>几何选择区域或多区域列表；在不同字典中结构不同，不能只复制键名。</td></tr><tr><td>fieldValues</td><td>指定选择区域内要设置的场及其数值。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/interIsoFoam/notchedDiscInSolidBodyRotation</summary><p>带缺口圆盘的刚体旋转测试先生成液相圆盘，再用一个长方体切出缺口。</p>
<ul>
<li><code>regions</code> 中选择 <code>boxToCell</code>，按单元中心是否落入盒子来赋值。</li>
<li>盒子范围为 x: 0.47～0.53、y: −1～1、z: 0～0.85，定义狭长切除区域。</li>
<li><code>volScalarFieldValue alpha.water 0</code> 将选中区域变为另一相，从已存在的水相形状中去掉缺口。</li>
</ul>
<p>改变缺口宽度时修改 x 两端，并比较缺口内的网格分辨率；本文件没有重新定义盒外初场。</p>
<p><a href="/assets/examples/v2512/setfieldsdict/1-setFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/notchedDiscInSolidBodyRotation/system/setFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/notchedDiscInSolidBodyRotation">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;system&quot;;
    object      setFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

regions
(
    boxToCell
    {
        box (.47 -1 0) (.53 1 .85);
        fieldValues
        (
            volScalarFieldValue alpha.water 0
        );
    }
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/interFoam/laminar/waves/waveMakerFlap</summary><p>翻板造波算例在启动前用水平高度初始化水层。</p>
<ul>
<li><code>defaultFieldValues</code> 先把 <code>alpha.water</code> 全域设为 0，表示背景为非水相。</li>
<li><code>boxToCell</code> 的盒子从 (−100,−100,−1) 到 (100,100,0.25)，选取 z≤0.25 的初始水域。</li>
<li>盒内 <code>alpha.water 1</code> 表示纯水，几何水面由盒子上缘给出。</li>
</ul>
<p>改变静水深时修改高度并对应调整造波参数；贴近初始界面的部分单元由网格中心判据划分。</p>
<p><a href="/assets/examples/v2512/setfieldsdict/2-setFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerFlap/system/setFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerFlap">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      setFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

defaultFieldValues
(
    volScalarFieldValue alpha.water 0
);

regions
(
    boxToCell
    {
        box ( -100 -100 -1 ) ( 100.0 100.0 0.25 );
        fieldValues ( volScalarFieldValue alpha.water 1 );
    }
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · heatTransfer/buoyantBoussinesqPimpleFoam/hotRoom</summary><p>浮力热房间先给空气统一温度，再在底部局部面上设置加热区。</p>
<ul>
<li>默认 <code>T 300</code> 给体场 300 K 的初值。</li>
<li><code>boxToFace</code> 按面位置选择区域，盒子 x、z 范围为 4.5～5.5，y 上限为 1e-5，定位底部中央热源。</li>
<li>选中面的 <code>T 600</code> 形成 600 K 加热区，使用的是面选择而非整块体积升温。</li>
</ul>
<p>热源移动时修改盒子范围，并检查温度边界类型是否按预期维持或演化该值。</p>
<p><a href="/assets/examples/v2512/setfieldsdict/3-setFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantBoussinesqPimpleFoam/hotRoom/system/setFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantBoussinesqPimpleFoam/hotRoom">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      setFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

defaultFieldValues
(
    volScalarFieldValue T 300
);

regions
(
    boxToFace
    {
        box (4.5 -1000 4.5) (5.5 1e-5 5.5);

        fieldValues
        (
            volScalarFieldValue T 600
        );
    }
);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/setfields/">setFields</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
