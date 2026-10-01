---
title: "system/blockMeshDict · blockMeshDict"
layout: reference
description: "blockMeshDict 通过 vertices 定义顶点，以 hex 后的 8 个顶点编号确定块的局部方向和体积符号。(Nx Ny Nz) 指定三个方向的单元数，scale 指定坐标缩放系数，simpleGrading 指定各方向末端与起始单元的尺寸比。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>blockMeshDict 通过 vertices 定义顶点，以 hex 后的 8 个顶点编号确定块的局部方向和体积符号。(Nx Ny Nz) 指定三个方向的单元数，scale 指定坐标缩放系数，simpleGrading 指定各方向末端与起始单元的尺寸比。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/blockMeshDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>vertices</code> · <code>blocks</code> · <code>edges</code> · <code>boundary</code> · <code>scale</code> · <code>convertToMeters</code> · <code>simpleGrading</code></p><h2>关联命令</h2><p><a href="/commands/?q=blockMesh">blockMesh</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/blockMeshDict -keywords
blockMesh -help</code></pre><h2>7.1 system/blockMeshDict</h2><p>blockMeshDict 通过 vertices 定义顶点，以 hex 后的 8 个顶点编号确定块的局部方向和体积符号。(Nx Ny Nz) 指定三个方向的单元数，scale 指定坐标缩放系数，simpleGrading 指定各方向末端与起始单元的尺寸比。</p>
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
<h2>补充说明</h2><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>scale</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/icoFoam/cavity/cavity</h3><p>原始路径：<code>tutorials/incompressible/icoFoam/cavity/cavity/system/blockMeshDict</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/blockMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/blockmeshdict/1-blockMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/simpleFoam/pitzDaily</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/pitzDaily/system/blockMeshDict</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/system/blockMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/blockmeshdict/2-blockMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    simpleGrading (0.5 &#36;posY 1)

    hex (2 5 6 3 13 16 17 14)
    (180 27 1)
    edgeGrading (4 4 4 4 &#36;negY 1 1 &#36;negY 1 1 1 1)

    hex (3 6 7 4 14 17 18 15)
    (180 30 1)
    edgeGrading (4 4 4 4 &#36;posY &#36;posYR &#36;posYR &#36;posY 1 1 1 1)

    hex (5 8 9 6 16 19 20 17)
    (25 27 1)
    simpleGrading (2.5 1 1)

    hex (6 9 10 7 17 20 21 18)
    (25 30 1)
    simpleGrading (2.5 &#36;posYR 1)
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


// ************************************************************************* //</code></pre><h3>示例 3 · compressible/acousticFoam/obliqueAirJet/main</h3><p>原始路径：<code>tutorials/compressible/acousticFoam/obliqueAirJet/main/system/blockMeshDict</code>；求解器：<code>acousticFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/main/system/blockMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/blockmeshdict/3-blockMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/acousticFoam/obliqueAirJet/main">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/blockmesh/">blockMesh</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/blockMeshDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/blockMeshDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
