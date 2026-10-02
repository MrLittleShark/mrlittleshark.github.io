---
title: "changeDictionaryDict"
layout: reference
description: "集中列出需要替换的字典条目，供 changeDictionary 批量修改算例文件。"
dictionary: true
cms_slug: "dictionary-changedictionarydict"
---

<p>集中列出需要替换的字典条目，供 changeDictionary 批量修改算例文件。</p><p>位置：<code>system/changeDictionaryDict</code></p><h2>配置实例</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object changeDictionaryDict;
}
dictionaryReplacement
{
    U
    {
        boundaryField
        {
            inlet { type fixedValue; value uniform (2 0 0); }
        }
    }
}</code></pre>
<p>dictionaryReplacement 按目标文件名组织替换条目，运行 changeDictionary 后写回相应文件。-instance 指定目标实例目录。单个键值可直接通过 foamDictionary 修改。</p>
<h2>17.10 changeDictionaryDict</h2><pre><code class="language-openfoam">dictionaryReplacement
{
    boundary
    {
        minZ { type wall; }
    }
    U
    {
        boundaryField
        {
            "(inlet|outlet)" { type zeroGradient; }
        }
    }
}</code></pre>
<p>多区域算例（chtMultiRegionFoam）里，每个 region 一份，放在 system/&lt;region&gt;/changeDictionaryDict。</p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>boundaryField</td><td>按网格 patch 名称设置边界条件；名称必须与 polyMesh/boundary 一致，类型还受网格边界类型约束。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · preProcessing/createZeroDirectory/snappyMultiRegionHeater</summary><p>这份配置位于 snappyMultiRegionHeater 的 topAir 区域目录，为批量修改该区域字典预留入口。</p>
<ul>
<li><code>dictionaryReplacement {}</code> 为空，目前没有列出替换内容。</li>
<li>所在区域路径决定它应与 topAir 的场和网格一起使用。</li>
<li>真正修改时需要给出目标对象及具体条目，替换会反映到对应区域文件。</li>
</ul>
<p>先在副本中写一项明确修改并检查差异，再扩展为多个字段或边界的批量变更。</p>
<p><a href="/assets/examples/v2512/changedictionarydict/1-changeDictionaryDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/snappyMultiRegionHeater/system/topAir/changeDictionaryDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/snappyMultiRegionHeater">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      changeDictionaryDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dictionaryReplacement
{
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · compressible/acousticFoam/obliqueAirJet/precursor</summary><p>射流 precursor 的配置将名为 box 的网格边界整理为一般 patch。</p>
<ul>
<li>外层 <code>boundary</code> 指向边界字典的修改内容。</li>
<li><code>box/type patch</code> 改变网格边界类型，<code>inGroups 1 (patch)</code> 同步设置所属分组。</li>
<li>场文件中该边界的速度、压力条件仍由各自条目给出。</li>
</ul>
<p>边界名称变化时先核对 constant/polyMesh/boundary，避免修改到不同的几何面组。</p>
<p><a href="/assets/examples/v2512/changedictionarydict/2-changeDictionaryDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/precursor/system/changeDictionaryDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/precursor">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      changeDictionaryDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

boundary
{
    box
    {
        type      patch;
        inGroups  1 ( patch );
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/pimpleFoam/RAS/ellipsekkLOmega</summary><p>椭圆绕流算例用 changeDictionary 调整镜像平面配置。</p>
<ul>
<li>目标对象为 <code>mirrorMeshDict</code>。</li>
<li><code>pointAndNormalDict/point (0 0 0)</code> 让镜面经过原点。</li>
<li><code>normal (0 -1 0)</code> 表示镜面法向沿 y，平面为 y=0。</li>
</ul>
<p>移动镜面时修改 point，改变方向时修改 normal；随后检查镜像后的网格是否与原网格按预期相接。</p>
<p><a href="/assets/examples/v2512/changedictionarydict/3-changeDictionaryDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/ellipsekkLOmega/system/changeDictionaryDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/ellipsekkLOmega">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      changeDictionaryDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

mirrorMeshDict
{
    pointAndNormalDict
    {
        point   (0 0 0);
        normal  (0 -1 0);
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/changedictionary/">changeDictionary</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
