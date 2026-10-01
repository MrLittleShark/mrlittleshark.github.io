---
title: "system/PDRMeshDict · PDRMeshDict"
layout: reference
description: "PDR 网格处理工作流中的专用配置。按对应教程的 Allrun 确定读取程序及前处理次序，不把该文件当作通用 blockMeshDict。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>PDR 网格处理工作流中的专用配置。按对应教程的 Allrun 确定读取程序及前处理次序，不把该文件当作通用 blockMeshDict。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>blockedFaces</td><td>faceSet 与封闭挡板 patch 的映射。</td></tr><tr><td>coupledFaces</td><td>耦合挡板的面集合及相关壁面/周期边界配置。</td></tr><tr><td>wallPatch</td><td>用于挡板壁面的 patch 名称。</td></tr><tr><td>cyclicMasterPatch</td><td>周期耦合主边界名称。</td></tr><tr><td>blockedCells</td><td>需要从网格中移除的单元集合。</td></tr><tr><td>defaultPatch</td><td>新暴露且没有明确指定去向的面归入此边界。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>blockedFaces</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // Per faceSet the patch the faces should go into blocked baffles</td></tr><tr><td>coupledFaces</td><td>Per faceSet the patch the faces should go into coupled baffles</td></tr><tr><td>blockedCells</td><td>Name of cellSet that holds the cells to fully remove</td></tr><tr><td>defaultPatch</td><td>All exposed faces that are not specified in blockedFaces go into this patch</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 2 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · combustion/PDRFoam/flamePropagationWithObstacles</h3><p>原始路径：<code>tutorials/combustion/PDRFoam/flamePropagationWithObstacles/system/PDRMeshDict</code>；求解器：<code>PDRFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/PDRFoam/flamePropagationWithObstacles/system/PDRMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/pdrmeshdict/1-PDRMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/PDRFoam/flamePropagationWithObstacles">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      PDRMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

//- Per faceSet the patch the faces should go into blocked baffles
blockedFaces ((blockedFacesSet blockedFaces));

//- Per faceSet the patch the faces should go into coupled baffles
coupledFaces
{

    coupledFacesSet
    {
        wallPatch                   baffleWall;
        cyclicMasterPatch           baffleCyclic_half0;
    }
}

//- Name of cellSet that holds the cells to fully remove
blockedCells blockedCellsSet;

//- All exposed faces that are not specified in blockedFaces go into
//  this patch
defaultPatch outer;


// ************************************************************************* //</code></pre><h3>示例 2 · etc/caseDicts/annotated</h3><p>原始路径：<code>etc/caseDicts/annotated/PDRMeshDict</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/PDRMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/pdrmeshdict/2-PDRMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      PDRMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

//- Per faceSet the patch the faces should go into blocked baffles
blockedFaces ((blockedFacesSet blockedFaces));

//- Per faceSet the duplicate baffles to generate (one &#x27;normal&#x27;, wall baffle,
//  one cyclic baffle). For use with active baffle boundary conditions.
coupledFaces
{
    coupledFacesSet
    {
        wallPatchName               baffleWall;
        cyclicMasterPatchName       baffleCyclic_half0;
    }
}

//- Name of cellSet that holds the cells to fully remove
blockedCells blockedCellsSet;

//- All exposed faces that are not specified in blockedFaces go into
//  this patch
defaultPatch outer;

// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/pdrmesh/">PDRMesh</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/PDRMeshDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/PDRMeshDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
