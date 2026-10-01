---
title: "system/setFieldsDict · setFieldsDict"
layout: reference
description: "setFields 首先按 defaultFieldValues 设置全域初值，再依次执行 regions 中的区域赋值。区域重叠时，后续赋值覆盖先前结果。目标场文件须预先建立，并设置相应的 class 和 dimensions。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>setFields 首先按 defaultFieldValues 设置全域初值，再依次执行 regions 中的区域赋值。区域重叠时，后续赋值覆盖先前结果。目标场文件须预先建立，并设置相应的 class 和 dimensions。</p><figure><img src="/assets/diagrams/reference-1.svg" alt="初始化配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/setFieldsDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>defaultFieldValues</code> · <code>regions</code> · <code>boxToCell</code> · <code>sphereToCell</code> · <code>cylinderToCell</code> · <code>fieldValues</code></p><h2>关联命令</h2><p><a href="/commands/?q=setFields">setFields</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/setFieldsDict -keywords
setFields -help</code></pre><h2>7.5 system/setFieldsDict</h2><p>setFields 首先按 defaultFieldValues 设置全域初值，再依次执行 regions 中的区域赋值。区域重叠时，后续赋值覆盖先前结果。目标场文件须预先建立，并设置相应的 class 和 dimensions。</p>
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
<p>注意：setFields 直接修改 0/ 里的文件。跑之前先 cp -r 0.orig 0，否则第二次运行是在被改过的场上再改一次。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>regions</td><td>几何选择区域或多区域列表；在不同字典中结构不同，不能只复制键名。</td></tr><tr><td>fieldValues</td><td>指定选择区域内要设置的场及其数值。</td></tr><tr><td>defaultFieldValues</td><td>在局部区域赋值之前设置的默认场值。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · multiphase/interIsoFoam/notchedDiscInSolidBodyRotation</h3><p>原始路径：<code>tutorials/multiphase/interIsoFoam/notchedDiscInSolidBodyRotation/system/setFieldsDict</code>；求解器：<code>interIsoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/notchedDiscInSolidBodyRotation/system/setFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setfieldsdict/1-setFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/notchedDiscInSolidBodyRotation">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · multiphase/interFoam/laminar/waves/waveMakerFlap</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/waves/waveMakerFlap/system/setFieldsDict</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerFlap/system/setFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setfieldsdict/2-setFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerFlap">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · heatTransfer/buoyantBoussinesqPimpleFoam/hotRoom</h3><p>原始路径：<code>tutorials/heatTransfer/buoyantBoussinesqPimpleFoam/hotRoom/system/setFieldsDict</code>；求解器：<code>buoyantBoussinesqPimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantBoussinesqPimpleFoam/hotRoom/system/setFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setfieldsdict/3-setFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantBoussinesqPimpleFoam/hotRoom">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/setfields/">setFields</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/setFieldsDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/setFieldsDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
