---
title: "system/renumberMeshDict · renumberMeshDict"
layout: reference
description: "renumberMethod 指定网格编号算法，如 CuthillMcKee；算法参数置于对应系数字典。运行 renumberMesh -list-renumber 可查询可用方法。重新编号用于调整稀疏矩阵带宽，网格几何分辨率保持不变。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>renumberMethod 指定网格编号算法，如 CuthillMcKee；算法参数置于对应系数字典。运行 renumberMesh -list-renumber 可查询可用方法。重新编号用于调整稀疏矩阵带宽，网格几何分辨率保持不变。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/renumberMeshDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>renumberMethod</code> · <code>CuthillMcKee</code></p><h2>关联命令</h2><p><a href="/commands/?q=renumberMesh">renumberMesh</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/renumberMeshDict -keywords
renumberMesh -help</code></pre><h2>8.5 system/renumberMeshDict 与文件处理器</h2><p>renumberMethod 指定网格编号算法，如 CuthillMcKee；算法参数置于对应系数字典。运行 renumberMesh -list-renumber 可查询可用方法。重新编号用于调整稀疏矩阵带宽，网格几何分辨率保持不变。</p>
<p>FOAM_FILEHANDLER 设置默认文件处理器，常用值为 uncollated 和 collated；命令行 -fileHandler 可覆盖该设置。collated 通过合并并行 I/O 减少文件数量，其性能取决于文件系统、MPI 和缓冲策略。结果读取及重分配应使用支持该格式的工具。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>method</td><td>所采用的分区、插值或模型方法；含义由该字典的读取程序决定。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>writeMaps</td><td>libs        (SloanRenumber); libs        (zoltanRenumber); Optional entry: write maps from renumbered back to original mesh</td></tr><tr><td>sortCoupledFaceCells</td><td>Optional entry: sort cells on coupled boundaries to last for use with e.g. nonBlockingGaussSeidel.</td></tr><tr><td>manualCoeffs</td><td>// Plain or reverse CuthillMcKee (RCM) reverse     true; }</td></tr><tr><td>dataFile</td><td>In system directory: new-to-original (i.e. order) labelIOList</td></tr><tr><td>structuredCoeffs</td><td>For extruded (i.e. structured in one direction) meshes</td></tr><tr><td>depthFirst</td><td>Renumber in columns (depthFirst) or in layers</td></tr><tr><td>reverse</td><td>Reverse ordering</td></tr><tr><td>maxCo</td><td>Maximum jump of cell indices. Is fraction of number of cells</td></tr><tr><td>freezeFraction</td><td>Limit the amount of movement; the fraction maxCo gets decreased with every iteration</td></tr><tr><td>maxIter</td><td>Maximum number of iterations</td></tr><tr><td>verbose</td><td>Enable/disable verbosity</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 1 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><p>该文件族在本次固定版本源码中仅选到一份不同的完整配置；不重复同一个文件充当多个案例。</p><h3>示例 1 · etc/caseDicts/annotated</h3><p>原始路径：<code>etc/caseDicts/annotated/renumberMeshDict</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/renumberMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/renumbermeshdict/1-renumberMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/renumbermesh/">renumberMesh</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;renumberMeshDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;renumberMeshDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
