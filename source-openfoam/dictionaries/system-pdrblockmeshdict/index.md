---
title: "PDRblockMeshDict"
layout: reference
description: "PDRblockMesh 的结构化网格输入，适用于 PDR 工作流。"
dictionary: true
cms_slug: "dictionary-pdrblockmeshdict"
---

<p>PDRblockMesh 的结构化网格输入，适用于 PDR 工作流。</p><p>位置：<code>system/PDRblockMeshDict</code></p><h2>配置实例</h2><p>incompressible/icoFoam/cavity/cavity 中的 PDRblockMeshDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      PDRblockMeshDict;
}

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
);</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/icoFoam/cavity/cavity</summary><p>PDRblockMesh 可以沿三个坐标方向给出分段坐标和单元数。本例生成顶盖驱动方腔的二维网格。</p>
<ul>
<li><code>scale 0.1</code> 将坐标缩放成米：x、y 的 0～1 对应 0.1 m，z 的 0～0.1 对应 0.01 m。</li>
<li>x、y 均分成 20 个单元，z 只有 1 层，总计 20×20×1=400 个六面体。</li>
<li><code>ratios 1</code> 表示各段内部均匀分布，面内单元宽度为 0.005 m。</li>
<li>面编号 3 命名为 movingWall，0、1、2 合并为 fixedWalls；4、5 合并为 empty 类型的 frontAndBack，使求解采用二维设置。</li>
</ul>
<p>细化时可把 x、y 的单元数同时改成 40，保持 z 一层和前后 empty 边界，便于比较相同几何上的速度分布。</p>
<p><a href="/assets/examples/v2512/pdrblockmeshdict/1-PDRblockMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/PDRblockMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/lumpedPointMotion/bridge/steady</summary><p>桥梁算例用分段网格覆盖桥梁附近与较远的外流区域，随后配合桥体几何及运动处理。</p>
<ul>
<li>x 从 −50 到 50，分 50 格，对应均匀间距 2 m。</li>
<li>y 分成 −300～−25、−25～25、25～300 三段，每段 10 格；中间段间距 5 m，两侧间距 27.5 m，桥梁附近分辨率更高。</li>
<li>z 的 0～50、50～80、80～250 分别用 2、10、10 格，形成地面到高空的不同网格尺度。</li>
<li>面 2 是 outlet，3 是 inlet，4 是 ground 壁面，5 是 sky，其余为 sides；这些名称会被后续场文件引用。</li>
</ul>
<p>本文件 <code>ratios 1</code> 使每一段内部均匀。需要平滑过渡时，同时调整分段位置、单元数和扩张比，并检查相邻单元尺寸跳变。</p>
<p><a href="/assets/examples/v2512/pdrblockmeshdict/2-PDRblockMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/lumpedPointMotion/bridge/steady/system/PDRblockMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/lumpedPointMotion/bridge/steady">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · combustion/PDRFoam/pipeLattice</summary><p>pipeLattice 在管阵列附近布置较细网格，向外部开阔区域扩展。PDRblockMeshDict 决定这层背景网格。</p>
<ul>
<li>x 的三段为 −19.4～0、0～4.26、4.26～23.66，分别用 14、13、14 格；y 采用对应的三段划分。</li>
<li>中间区域扩张比为 1，外侧比值约 0.0887 和 10.699，使网格向障碍物附近收缩、向远处增大。</li>
<li>z 从地面起分为 0～2.13 的 6 格、2.13～23.17 的 14 格，远离地面后逐渐放粗。</li>
<li><code>outer</code> 包含四个侧面与顶面，<code>wallFaces</code> 对应底面 4；blockedFaces、mergingFaces 预留给后续障碍物处理。</li>
</ul>
<p>调整阵列尺寸后同步修改分段位置和障碍物几何，检查细网格是否覆盖全部管阵列。</p>
<p><a href="/assets/examples/v2512/pdrblockmeshdict/3-PDRblockMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/PDRFoam/pipeLattice/system/PDRblockMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/PDRFoam/pipeLattice">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


//***************************************************************************//</code></pre></details><h2>相关命令</h2><p><a href="/commands/pdrblockmesh/">PDRblockMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
