---
title: "renumberMeshDict"
layout: reference
description: "选择网格重编号方法，调整稀疏矩阵的编号排列。"
dictionary: true
cms_slug: "dictionary-renumbermeshdict"
---

<p>选择网格重编号方法，调整稀疏矩阵的编号排列。</p><p>位置：<code>system/renumberMeshDict</code></p><h2>配置实例</h2><p>renumberMethod 指定网格编号算法，如 CuthillMcKee；算法参数置于对应系数字典。运行 renumberMesh -list-renumber 可查询可用方法。重新编号用于调整稀疏矩阵带宽，网格几何分辨率保持不变。</p>
<p>FOAM_FILEHANDLER 设置默认文件处理器，常用值为 uncollated 和 collated；命令行 -fileHandler 可覆盖该设置。collated 通过合并并行 I/O 减少文件数量，其性能取决于文件系统、MPI 和缓冲策略。结果读取及重分配应使用支持该格式的工具。</p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>method</td><td>所采用的分区、插值或模型方法；含义由该字典的读取程序决定。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · etc/caseDicts/annotated</summary><p>这是 renumberMesh 的附注模板，当前实际选中 Cuthill–McKee 重编号，以改善矩阵寻址布局。</p>
<ul>
<li><code>method CuthillMcKee</code> 选择重排算法；下面 manual、structured、spring 等子字典展示其他算法的参数入口。</li>
<li><code>writeMaps false</code> 不额外写出新旧编号映射，<code>sortCoupledFaceCells false</code> 不将耦合边界单元专门排到末尾。</li>
<li><code>springCoeffs/maxCo 0.01</code> 只在 spring 方法下控制编号跳动尺度，含义与流动 Courant 数不同。</li>
</ul>
<p>需要追踪原编号时开启 writeMaps；更换算法后用相同算例比较矩阵带宽和实际求解耗时。</p>
<p><a href="/assets/examples/v2512/renumbermeshdict/1-renumberMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/renumberMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    note        &quot;mesh renumbering dictionary&quot;;
    object      renumberMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Additional libraries
//libs        (SloanRenumber);
//libs        (zoltanRenumber);

// Optional entry: write maps from renumbered back to original mesh
writeMaps   false;

// Optional entry: sort cells on coupled boundaries to last for use with
// e.g. nonBlockingGaussSeidel.
sortCoupledFaceCells false;

// Optional entry: renumber on a block-by-block basis. It uses a
// blockCoeffs dictionary to construct a decompositionMethod to do
// a block subdivision) and then applies the renumberMethod to each
// block in turn. This can be used in large cases to keep the blocks
// fitting in cache with all the cache misses bunched at the end.
// This number is the approximate size of the blocks - this gets converted
// to a number of blocks that is the input to the decomposition method.
//blockSize 1000;

// Optional entry: sort points into internal and boundary points
//orderPoints false;

// Optional entry (experimental) - for block-by-block (blockSize &gt; 0) option:
// - sort intra-region and iter-region faces separately.
//   This will likely lead to non-upper triangular ordering between regions.
//regionFaceOrder false;


method          CuthillMcKee;
//method          RCM;  // == reverseCuthillMcKee;
//method          Sloan;        //&lt;-  libs (zoltanRenumber);
//method          manual;
//method          random;
//method          structured;
//method          spring;
//method          zoltan;       //&lt;-  libs (zoltanRenumber);

//CuthillMcKeeCoeffs
//{
//    // Plain or reverse CuthillMcKee (RCM)
//    reverse     true;
//}

manualCoeffs
{
    // In system directory: new-to-original (i.e. order) labelIOList
    dataFile    &quot;cellMap&quot;;
}


// For extruded (i.e. structured in one direction) meshes
structuredCoeffs
{
    // Patches that mesh was extruded from.
    // These determine the starting layer of cells
    patches     (movingWall);

    // Method to renumber the starting layer of cells
    method      random;

    // Renumber in columns (depthFirst) or in layers
    depthFirst  true;

    // Reverse ordering
    reverse     false;
}


springCoeffs
{
    // Maximum jump of cell indices. Is fraction of number of cells
    maxCo       0.01;

    // Limit the amount of movement; the fraction maxCo gets decreased
    // with every iteration
    freezeFraction 0.999;

    // Maximum number of iterations
    maxIter    1000;

    // Enable/disable verbosity
    verbose    true;
}


blockCoeffs
{
    method      scotch;
    //method      hierarchical;
    //hierarchicalCoeffs
    //{
    //    n           (1 2 1);
    //    delta       0.001;
    //    order       xyz;
    //}
}


zoltanCoeffs
{
    ORDER_METHOD    LOCAL_HSFC;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/renumbermesh/">renumberMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
