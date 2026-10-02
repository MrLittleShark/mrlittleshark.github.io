---
title: "extrude2DMeshDict"
layout: reference
description: "extrude2DMesh 将二维网格转为具有厚度或角度的三维网格。"
dictionary: true
cms_slug: "dictionary-extrude2dmeshdict"
---

<p>extrude2DMesh 将二维网格转为具有厚度或角度的三维网格。</p><p>位置：<code>system/extrude2DMeshDict</code></p><h2>配置实例</h2><p>mesh/foamyQuadMesh/square 中的 extrude2DMeshDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      extrude2DMeshDict;
}

extrudeModel    wedge;

patchInfo
{}

patchType       wedge;

sectorCoeffs    //&lt;- Also used for wedge
{
    point       (0 0 0);
    axis        (1 0 0);
    angle       10;
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>extrudeModel</td><td>挤出几何模型，例如平移、旋转或法向挤出；各模型需要不同系数。</td></tr><tr><td>axis</td><td>旋转轴或方向向量；需明确是否要求单位向量。</td></tr><tr><td>nLayers</td><td>挤出或边界层生成的层数；同时检查层厚与总厚度。</td></tr><tr><td>expansionRatio</td><td>相邻挤出层的厚度增长比例。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · mesh/foamyQuadMesh/square</summary><p>square 的 extrude2DMeshDict 把平面网格沿圆周方向拉伸成薄楔体，用于轴对称几何表示。</p>
<ul>
<li><code>extrudeModel wedge</code> 选择楔形拉伸，<code>patchType wedge</code> 设置两侧边界类型。</li>
<li><code>point (0 0 0)</code> 给出旋转轴经过的点，<code>axis (1 0 0)</code> 将轴线设为 x 方向。</li>
<li><code>angle 10</code> 指定楔形开角为 10°，sectorCoeffs 同时供 wedge 模型读取。</li>
</ul>
<p>拉伸前检查平面网格与旋转轴的位置关系，拉伸后检查楔形两侧法向及轴线附近单元质量。</p>
<p><a href="/assets/examples/v2512/extrude2dmeshdict/1-extrude2DMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/square/system/extrude2DMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/square">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      extrude2DMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

extrudeModel    wedge;

patchInfo
{}

patchType       wedge;

sectorCoeffs    //&lt;- Also used for wedge
{
    point       (0 0 0);
    axis        (1 0 0);
    angle       10;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · mesh/foamyQuadMesh/OpenCFD</summary><p>OpenCFD 字样网格采用直线拉伸，把平面形状转换为只有一层单元的二维计算网格。</p>
<ul>
<li><code>extrudeModel linearDirection</code> 选择固定方向拉伸，<code>direction (0 0 1)</code> 指定 z 方向。</li>
<li><code>thickness 0.1</code> 设置厚度为 0.1 m，<code>nLayers 1</code> 在厚度方向只生成一层。</li>
<li><code>patchType empty</code> 配合这一层网格用于二维求解，<code>expansionRatio 1</code> 表示均匀层厚。</li>
<li>同文件中的 sectorCoeffs 是另一种拉伸方式的参数；当前由 linearDirectionCoeffs 决定生成形状。</li>
</ul>
<p>需要三维厚度分辨率时增加层数，同时将前后边界改为实际物理边界类型。</p>
<p><a href="/assets/examples/v2512/extrude2dmeshdict/2-extrude2DMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/OpenCFD/system/extrude2DMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/OpenCFD">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      extrude2DMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

extrudeModel        linearDirection;

patchInfo
{}

patchType           empty;

nLayers             1;

expansionRatio      1.0;

linearDirectionCoeffs
{
    direction       (0 0 1);
    thickness       0.1;
}

sectorCoeffs    //&lt;- Also used for wedge
{
    point       (0 0 0);
    axis        (1 0 0);
    angle       10;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · etc/caseDicts/annotated</summary><p>这个模板给出沿 z 方向拉伸二维网格的基本写法，可作为创建薄层网格的起点。</p>
<ul>
<li><code>linearDirection</code> 使用指定的直线方向，<code>direction (0 0 1)</code> 沿正 z 方向延伸。</li>
<li><code>nLayers 1</code>、<code>thickness 0.1</code> 生成厚度 0.1 m 的单层网格，<code>expansionRatio 1</code> 表示等距分层。</li>
<li><code>patchType empty</code> 表明前后面用于二维计算；sectorCoeffs 保留了旋转拉伸所需的另一组参数。</li>
</ul>
<p>如果实际问题需要解析厚度方向的速度或温度变化，应增加单元层数，并为两侧面配置对应物理条件。</p>
<p><a href="/assets/examples/v2512/extrude2dmeshdict/3-extrude2DMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/extrude2DMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

FoamFile
{
    version         2.0;
    format          ascii;
    class           dictionary;
    object          extrude2DMeshDict;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

extrudeModel        linearDirection;
//extrudeModel        wedge;

patchType           empty;
//patchType           wedge;

nLayers             1;

expansionRatio      1.0;

linearDirectionCoeffs
{
    direction       (0 0 1);
    thickness       0.1;
}

sectorCoeffs    //&lt;- Also used for wedge
{
    point       (0 0 0);
    axis        (1 0 0);
    angle       10;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</code></pre></details><h2>相关命令</h2><p><a href="/commands/extrude2dmesh/">extrude2DMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
