---
title: "extrudeToRegionMeshDict"
layout: reference
description: "从已有网格的面或面区挤出独立区域，用于薄壁或液膜等区域耦合。"
dictionary: true
cms_slug: "dictionary-extrudetoregionmeshdict"
---

<p>从已有网格的面或面区挤出独立区域，用于薄壁或液膜等区域耦合。</p><p>位置：<code>system/extrudeToRegionMeshDict</code></p><h2>配置实例</h2><p>combustion/fireFoam/LES/simplePMMApanel 中的 extrudeToRegionMeshDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      extrudeToRegionMeshDict;
}

region          panelRegion;

faceZones       (panel);

oneD            true;

sampleMode      nearestPatchFace;

extrudeModel    linearNormal;

oneDPolyPatchType empty;

nLayers         8;

expansionRatio  1;

adaptMesh       true;

linearNormalCoeffs
{
    thickness       0.0234;
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>region</td><td>目标网格区域名称；多区域场与网格路径中应保持一致。</td></tr><tr><td>extrudeModel</td><td>挤出几何模型，例如平移、旋转或法向挤出；各模型需要不同系数。</td></tr><tr><td>nLayers</td><td>挤出或边界层生成的层数；同时检查层厚与总厚度。</td></tr><tr><td>expansionRatio</td><td>相邻挤出层的厚度增长比例。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · combustion/fireFoam/LES/simplePMMApanel</summary><p>PMMA 板燃烧算例从已有 panel 面区向厚度方向拉伸，建立固体板区域 panelRegion。</p>
<ul>
<li><code>faceZones (panel)</code> 选定起始面区，<code>region panelRegion</code> 给新网格命名。</li>
<li><code>extrudeModel linearNormal</code> 沿局部法向拉伸，<code>thickness 0.0234</code> 给出板厚 23.4 mm。</li>
<li><code>nLayers 8</code>、<code>expansionRatio 1</code> 使用 8 层等厚单元，每层约 2.925 mm。</li>
<li><code>oneD true</code> 与 <code>oneDPolyPatchType empty</code> 将板内主要传热方向设为厚度方向；<code>sampleMode nearestPatchFace</code> 用于界面映射。</li>
<li><code>adaptMesh true</code> 同步调整原始网格的相关边界。</li>
</ul>
<p>改变板厚时同时更新材料热物性与层数，比较板面温度和厚度方向温度梯度。</p>
<p><a href="/assets/examples/v2512/extrudetoregionmeshdict/1-extrudeToRegionMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/simplePMMApanel/system/extrudeToRegionMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/simplePMMApanel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      extrudeToRegionMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

region          panelRegion;

faceZones       (panel);

oneD            true;

sampleMode      nearestPatchFace;

extrudeModel    linearNormal;

oneDPolyPatchType empty;

nLayers         8;

expansionRatio  1;

adaptMesh       true;

linearNormalCoeffs
{
    thickness       0.0234;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · lagrangian/reactingParcelFoam/cylinder</summary><p>cylinder 算例从 wallFilmFaces 面区生成 wallFilmRegion，为壁面液膜计算提供附着区域。</p>
<ul>
<li><code>faceZones (wallFilmFaces)</code> 选定壁面集合，<code>region wallFilmRegion</code> 是后续液膜模型查找的区域名称。</li>
<li><code>linearNormal</code> 沿壁面法向拉伸，<code>thickness 0.01</code>、<code>nLayers 1</code> 生成 0.01 m 的单层区域。</li>
<li><code>sampleMode nearestPatchFace</code> 选择界面采样映射方式，<code>adaptMesh yes</code> 更新原有网格的连接边界。</li>
<li><code>oneD false</code> 保留该区域的多方向拓扑处理，<code>expansionRatio 1</code> 采用均匀层厚。</li>
</ul>
<p>修改壁面区域名称后同步修改 surfaceFilmProperties 中的 region，使液膜模型能找到对应网格。</p>
<p><a href="/assets/examples/v2512/extrudetoregionmeshdict/2-extrudeToRegionMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/cylinder/system/extrudeToRegionMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/cylinder">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      extrudeToRegionMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

region          wallFilmRegion;

faceZones       (wallFilmFaces);

sampleMode      nearestPatchFace;

oneD            false;

extrudeModel    linearNormal;

nLayers         1;

expansionRatio  1;

adaptMesh       yes; // apply mapped to both regions

linearNormalCoeffs
{
    thickness       0.01;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/reactingParcelFoam/rivuletPanel</summary><p>rivuletPanel 从板面创建壁膜区域，随后在其上计算液膜沿板面的运动。</p>
<ul>
<li><code>wallFilmFaces</code> 指定要拉伸的面区，输出区域名称为 wallFilmRegion。</li>
<li><code>linearNormal</code>、<code>thickness 0.01</code> 沿板法向生成厚 0.01 m 的网格区域，<code>nLayers 1</code> 只保留一层。</li>
<li><code>nearestPatchFace</code> 用最近面映射连接壁膜区域与主流区域，<code>adaptMesh yes</code> 调整主网格相关边界。</li>
<li><code>oneD false</code>、<code>expansionRatio 1</code> 给出区域生成方式和均匀层厚。</li>
</ul>
<p>这里的几何拉伸厚度与液膜场中的局部液膜厚度分别配置；查看液膜结果时应读取模型计算的厚度场。</p>
<p><a href="/assets/examples/v2512/extrudetoregionmeshdict/3-extrudeToRegionMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/rivuletPanel/system/extrudeToRegionMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/rivuletPanel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      extrudeToRegionMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

region          wallFilmRegion;

faceZones       (wallFilmFaces);

oneD            false;

sampleMode      nearestPatchFace;

extrudeModel    linearNormal;

nLayers         1;

expansionRatio  1;

adaptMesh       yes; // apply mapped to both regions

linearNormalCoeffs
{
    thickness       0.01;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/extrudetoregionmesh/">extrudeToRegionMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
