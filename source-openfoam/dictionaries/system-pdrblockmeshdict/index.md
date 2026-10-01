---
title: "system/PDRblockMeshDict · PDRblockMeshDict"
layout: reference
description: "PDRblockMesh 的结构化网格输入，适用于 PDR 工作流。它不是 blockMeshDict 的别名，网格坐标和分块格式应按专用工具及配套教程解释。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>PDRblockMesh 的结构化网格输入，适用于 PDR 工作流。它不是 blockMeshDict 的别名，网格坐标和分块格式应按专用工具及配套教程解释。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>scale</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>boundary</td><td>Low resolution Faces: 0=x-min, 1=x-max, 2=y-min, 3=y-max, 4=z-min, 5=z-max</td></tr><tr><td>defaultPatch</td><td>Or could use defaultFaces = outer instead</td></tr><tr><td>outer</td><td>Or with defaultFaces = outer</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/icoFoam/cavity/cavity</h3><p>原始路径：<code>tutorials/incompressible/icoFoam/cavity/cavity/system/PDRblockMeshDict</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/PDRblockMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/pdrblockmeshdict/1-PDRblockMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      PDRblockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

scale   0.1;

x
{
    points  (0 1);
    nCells  (20);
    ratios  (1);
}

y
{
    points  (0 1);
    nCells  (20);
    ratios  (1);
}

z
{
    points  (0 0.1);
    nCells  (1);
    ratios  (1);
}


boundary
(
    movingWall
    {
        type  wall;
        faces (3);
    }
    fixedWalls
    {
        type  wall;
        faces (0 1 2);
    }
    frontAndBack
    {
        type  empty;
        faces (4 5);
    }
);


// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/lumpedPointMotion/bridge/steady</h3><p>原始路径：<code>tutorials/incompressible/lumpedPointMotion/bridge/steady/system/PDRblockMeshDict</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/lumpedPointMotion/bridge/steady/system/PDRblockMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/pdrblockmeshdict/2-PDRblockMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/lumpedPointMotion/bridge/steady">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      PDRblockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Bounding Box : (-23.275 -250 5) (23.275 250 200)

scale   1;

x
{
    points  ( -50 50 );
    nCells  ( 50 );
    ratios  ( 1 );
}

y
{
    points  ( -300 -25 25 300 );
    nCells  ( 10 10 10 );
    ratios  ( 1 1 1 );
}

z
{
    points  ( 0 50 80 250 );
    nCells  ( 2 10 10 );
    ratios  ( 1 1 1 );
}

// Low resolution


// Faces: 0=x-min, 1=x-max, 2=y-min, 3=y-max, 4=z-min, 5=z-max

boundary
(
    sides
    {
        type    patch;
        faces   ( 0 1 );
    }

    outlet
    {
        type    patch;
        faces   ( 2 );
    }

    inlet
    {
        type    patch;
        faces   ( 3 );
    }

    ground
    {
        type    wall;
        faces   ( 4 );
    }

    sky
    {
        type    patch;
        faces   ( 5 );
    }
);

// ************************************************************************* //</code></pre><h3>示例 3 · combustion/PDRFoam/pipeLattice</h3><p>原始路径：<code>tutorials/combustion/PDRFoam/pipeLattice/system/PDRblockMeshDict</code>；求解器：<code>PDRFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/PDRFoam/pipeLattice/system/PDRblockMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/pdrblockmeshdict/3-PDRblockMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/PDRFoam/pipeLattice">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      PDRblockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

scale   1.0;

x
{
    points  ( -19.4 0 4.26 23.66 );
    nCells  ( 14 13 14 );
    ratios  ( 0.0887187064230887 1 10.6993205379072 );
}

y
{
    points  ( -19.42 0 4.26 23.68 );
    nCells  ( 14 13 14 );
    ratios  ( 0.0887187064230887 1 10.6993205379072 );
}

z
{
    points  (0 2.13 23.17  );
    nCells  ( 6 14 );
    ratios  ( 1 10.6993205379072 );
}


// Or could use defaultFaces = outer instead
defaultPatch
{
    name    defaultFaces;
    type    wall;
}


// Faces: 0 = xmin, 1 = xmax, 2 = ymin, 3 = ymax, 4 = zmin, 5 = zmax

boundary
(
    // Or with defaultFaces = outer
    outer
    {
        type    patch;
        faces   ( 0 1 2 3 5 );
    }

    mergingFaces
    {
        type    wall;
        faces   ();
    }

    blockedFaces
    {
        type    wall;
        faces   ();
    }

    wallFaces
    {
        type    wall;
        faces   ( 4 );
    }
);


//***************************************************************************//</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/pdrblockmesh/">PDRblockMesh</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/PDRblockMeshDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/PDRblockMeshDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
