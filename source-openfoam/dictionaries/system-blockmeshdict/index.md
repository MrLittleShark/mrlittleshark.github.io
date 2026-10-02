---
title: "blockMeshDict"
layout: reference
description: "定义网格顶点、六面体块、单元数和边界，供 blockMesh 生成结构网格。"
dictionary: true
cms_slug: "dictionary-blockmeshdict"
---

<p>定义网格顶点、六面体块、单元数和边界，供 blockMesh 生成结构网格。</p><p>位置：<code>system/blockMeshDict</code></p><figure class="wolf-figure"><img src="/assets/wolf/wolf-mesh-smooth-transition.png" alt="网格尺寸的突变与平滑过渡" loading="lazy"><figcaption><strong>网格尺寸的突变与平滑过渡</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 19 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure><h2>配置实例</h2><p>blockMeshDict 通过 vertices 定义顶点，以 hex 后的 8 个顶点编号确定块的局部方向和体积符号。(Nx Ny Nz) 指定三个方向的单元数，scale 指定坐标缩放系数，simpleGrading 指定各方向末端与起始单元的尺寸比。</p>
<p>下例建立长 1 m、宽 0.1 m、厚 0.01 m 的二维通道。厚度方向设置一层单元，两侧边界设为 empty。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object blockMeshDict;
}
scale 1;
vertices
(
    (0 0 0) (1 0 0) (1 0.1 0) (0 0.1 0)
    (0 0 0.01) (1 0 0.01) (1 0.1 0.01) (0 0.1 0.01)
);
blocks
(
    hex (0 1 2 3 4 5 6 7) (100 20 1)
        simpleGrading (1 1 1)
);
edges ();
boundary
(
    inlet
    {
        type patch;
        faces ((0 4 7 3));
    }
    outlet
    {
        type patch;
        faces ((1 2 6 5));
    }
    walls
    {
        type wall;
        faces ((0 1 5 4) (3 7 6 2));
    }
    frontAndBack
    {
        type empty;
        faces ((0 3 2 1) (4 5 6 7));
    }
);
mergePatchPairs ();</code></pre>
<p>执行 blockMesh 生成网格，再执行 checkMesh -allTopology -allGeometry 检查拓扑和几何。边界面的顶点顺序按外法向排列；多块网格应统一局部坐标和顶点编号。</p>
<div class="table-scroll"><table>
<tr><th>参数或结构</th><th>设置方法</th><th>使用条件</th></tr>
<tr><td>scale</td><td>如 0.001 表示原坐标按毫米给出</td><td>采用 scale 统一设置坐标缩放</td></tr>
<tr><td>simpleGrading</td><td>例如 (1 10 1)</td><td>沿块的局部方向设置；反向时取对应倒数</td></tr>
<tr><td>多段 grading</td><td>某方向可写 ((0.2 0.3 4) (0.6 0.4 1) (0.2 0.3 0.25))</td><td>每段分别为长度比例、单元比例、扩张比</td></tr>
<tr><td>edgeGrading</td><td>对 12 条局部边分别指定扩张比</td><td>按块的局部边编号依次赋值</td></tr>
<tr><td>edges</td><td>arc 0 1 (中间点)，或 spline、polyLine</td><td>弧线端点与控制点应满足非退化条件</td></tr>
<tr><td>boundary/type</td><td>patch、wall、empty、symmetryPlane、wedge、cyclic 等</td><td>定义网格边界类型；场边界另行配置</td></tr>
<tr><td>defaultPatch</td><td>为未显式列出的面指定名称和类型</td><td>显式边界之外的面归入该边界</td></tr>
<tr><td>mergePatchPairs</td><td>((patchA patchB))</td><td>合并指定的块接口</td></tr>
</table></div>
<h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/icoFoam/cavity/cavity</summary><p>方腔由一个六面体块生成，配合二维 empty 边界使用。</p>
<ul>
<li><code>scale 0.1</code> 把顶点坐标乘以 0.1，得到长高各 0.1 m、厚 0.01 m 的腔体。</li>
<li><code>hex ... (20 20 1)</code> 在三个方向分成 20、20、1 个单元，共 400 个单元。</li>
<li><code>simpleGrading (1 1 1)</code> 使用均匀间距。</li>
<li><code>movingWall</code> 是顶盖，<code>fixedWalls</code> 为其余侧壁，<code>frontAndBack/type empty</code> 约束前后方向为二维。</li>
</ul>
<p>加密时可改为 (40 40 1) 并重建网格；保持二维模型时厚度方向仍取一层，同时检查时间步。</p>
<p><a href="/assets/examples/v2512/blockmeshdict/1-blockMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/blockMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      blockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

scale   0.1;

vertices
(
    (0 0 0)
    (1 0 0)
    (1 1 0)
    (0 1 0)
    (0 0 0.1)
    (1 0 0.1)
    (1 1 0.1)
    (0 1 0.1)
);

blocks
(
    hex (0 1 2 3 4 5 6 7) (20 20 1) simpleGrading (1 1 1)
);

edges
(
);

boundary
(
    movingWall
    {
        type wall;
        faces
        (
            (3 7 6 2)
        );
    }
    fixedWalls
    {
        type wall;
        faces
        (
            (0 4 7 3)
            (2 6 5 1)
            (1 5 4 0)
        );
    }
    frontAndBack
    {
        type empty;
        faces
        (
            (0 3 2 1)
            (4 5 6 7)
        );
    }
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/simpleFoam/pitzDaily</summary><p>pitzDaily 的后台阶及下游通道由五个六面体块拼接，以便在台阶、剪切层和壁面附近分配不同分辨率。</p>
<ul>
<li><code>scale 0.001</code> 将毫米量级坐标换算为米。</li>
<li>入口块 <code>(18 30 1)</code>、下游块 <code>(180 27 1)</code> 与 <code>(180 30 1)</code> 等分别控制不同分区的单元数。</li>
<li><code>negY</code>、<code>posY</code>、<code>posYR</code> 被 grading 条目引用，使单元向需要分辨的区域渐变。</li>
<li><code>inlet</code>、<code>outlet</code>、上下壁面与 <code>frontAndBack empty</code> 分开命名，随后由场文件设置物理边界。</li>
</ul>
<p>移动台阶或改变高度时保持相邻块共享面的单元数相容；比较回流长度时优先加密台阶后的剪切层。</p>
<p><a href="/assets/examples/v2512/blockmeshdict/2-blockMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/system/blockMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      blockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

scale   0.001;

vertices
(
    (-20.6 0 -0.5)
    (-20.6 25.4 -0.5)
    (0 -25.4 -0.5)
    (0 0 -0.5)
    (0 25.4 -0.5)
    (206 -25.4 -0.5)
    (206 0 -0.5)
    (206 25.4 -0.5)
    (290 -16.6 -0.5)
    (290 0 -0.5)
    (290 16.6 -0.5)

    (-20.6 0 0.5)
    (-20.6 25.4 0.5)
    (0 -25.4 0.5)
    (0 0 0.5)
    (0 25.4 0.5)
    (206 -25.4 0.5)
    (206 0 0.5)
    (206 25.4 0.5)
    (290 -16.6 0.5)
    (290 0 0.5)
    (290 16.6 0.5)
);

negY
(
    (2 4 1)
    (1 3 0.3)
);

posY
(
    (1 4 2)
    (2 3 4)
    (2 4 0.25)
);

posYR
(
    (2 1 1)
    (1 1 0.25)
);


blocks
(
    hex (0 3 4 1 11 14 15 12)
    (18 30 1)
    simpleGrading (0.5 $posY 1)

    hex (2 5 6 3 13 16 17 14)
    (180 27 1)
    edgeGrading (4 4 4 4 $negY 1 1 $negY 1 1 1 1)

    hex (3 6 7 4 14 17 18 15)
    (180 30 1)
    edgeGrading (4 4 4 4 $posY $posYR $posYR $posY 1 1 1 1)

    hex (5 8 9 6 16 19 20 17)
    (25 27 1)
    simpleGrading (2.5 1 1)

    hex (6 9 10 7 17 20 21 18)
    (25 30 1)
    simpleGrading (2.5 $posYR 1)
);

edges
(
);

boundary
(
    inlet
    {
        type patch;
        faces
        (
            (0 1 12 11)
        );
    }
    outlet
    {
        type patch;
        faces
        (
            (8 9 20 19)
            (9 10 21 20)
        );
    }
    upperWall
    {
        type wall;
        faces
        (
            (1 4 15 12)
            (4 7 18 15)
            (7 10 21 18)
        );
    }
    lowerWall
    {
        type wall;
        faces
        (
            (0 3 14 11)
            (3 2 13 14)
            (2 5 16 13)
            (5 8 19 16)
        );
    }
    frontAndBack
    {
        type empty;
        faces
        (
            (0 3 4 1)
            (2 5 6 3)
            (3 6 7 4)
            (5 8 9 6)
            (6 9 10 7)
            (11 14 15 12)
            (13 16 17 14)
            (14 17 18 15)
            (16 19 20 17)
            (17 20 21 18)
        );
    }
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · compressible/acousticFoam/obliqueAirJet/main</summary><p>倾斜射流声学算例的 main 区先建立规则背景网格，后续数据与边界处理需结合配套流程。</p>
<ul>
<li><code>scale 1</code> 表示坐标直接按米使用，包围范围是 x: −0.2～2.2、y: −0.3～1.3、z: −0.2～2.2。</li>
<li>单块 <code>(15 10 15)</code> 对应 2250 个单元，各方向间距均约 0.16 m。</li>
<li><code>simpleGrading (1 1 1)</code> 使用均匀分布，<code>edges ()</code> 没有额外曲边。</li>
<li><code>patches ()</code> 未在本文件细分边界，边界划分应继续对照算例的其他预处理配置。</li>
</ul>
<p>研究更高频的声学扰动时，需要按目标波长检查每波长网格数，并同步检查采样与时间步。</p>
<p><a href="/assets/examples/v2512/blockmeshdict/3-blockMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/main/system/blockMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/main">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      blockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

scale    1;

vertices
(
  (-.2  -.3   -.2)
  (2.2  -.3  -.2)
  (2.2  1.3  -.2)
  (-.2  1.3  -.2)

  (-.2  -.3  2.2)
  (2.2  -.3  2.2)
  (2.2  1.3  2.2)
  (-.2  1.3  2.2)
);

blocks
(
    hex (0 1 2 3 4 5 6 7) (15 10 15) simpleGrading (1 1 1)
);

edges
(
);

patches
(
);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/blockmesh/">blockMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
