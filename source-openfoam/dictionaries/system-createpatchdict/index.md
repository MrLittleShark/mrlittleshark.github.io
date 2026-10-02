---
title: "createPatchDict"
layout: reference
description: "从现有边界或 faceSet 创建、合并和重命名网格边界。"
dictionary: true
cms_slug: "dictionary-createpatchdict"
---

<p>从现有边界或 faceSet 创建、合并和重命名网格边界。</p><p>位置：<code>system/createPatchDict</code></p><h2>配置实例</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object createPatchDict;
}
pointSync false;
patches
(
    {
        name walls;
        patchInfo { type wall; }
        constructFrom patches;
        patches (wallA wallB);
    }
);</code></pre>
<p>constructFrom patches 从已有边界选面；constructFrom set 从指定 faceSet 选面。pointSync 控制耦合点同步。执行 createPatch -overwrite 后，将 0/U、0/p 等场文件中的边界条目与新建 walls 对应。</p>
<h2>17.5 createPatchDict</h2><pre><code class="language-openfoam">pointSync false;

patches
(
    {
        name            cyclicLeft;
        patchInfo       { type cyclic; neighbourPatch cyclicRight; }
        constructFrom   patches;
        patches         (left);
    }
);</code></pre>
<p>用途：把网格转换器生成的一堆零散 patch 合并；把两个面配成周期边界；改 patch 类型。</p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr><tr><td>constructFrom</td><td>指定挤出源来自已有网格、表面或其他受支持的输入。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/overInterDyMFoam/rigidBodyHull/background</summary><p>船体背景网格将已有边界重组为 overset 接口，供重叠网格插值使用。</p>
<ul>
<li><code>name oversetPatch</code> 给新边界命名，<code>patchInfo/type overset</code> 设定重叠接口类型。</li>
<li><code>constructFrom patches</code>、<code>patches (MRF_REGION)</code> 指明从已有 MRF_REGION 边界收集面。</li>
<li><code>pointSync false</code> 关闭额外的点同步步骤，<code>value uniform 0</code> 是该配置附带的初始化条目。</li>
</ul>
<p>表面名称改变时更新来源列表，并在各场文件中同步设置新的 oversetPatch 条件。</p>
<p><a href="/assets/examples/v2512/createpatchdict/1-createPatchDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/rigidBodyHull/background/system/createPatchDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/rigidBodyHull/background">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      createPatchDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

pointSync false;

patches
(
    {
        name oversetPatch;

        patchInfo
        {
            type    overset;
            value   uniform 0;
        }

        constructFrom patches;

        patches (MRF_REGION);
    }
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · mesh/foamyHexMesh/mixerVessel</summary><p>mixerVessel 提供了一份空的 createPatch 配置入口。</p>
<ul>
<li><code>patches ()</code> 没有列出新边界的构造任务，因此当前文件不会按清单生成额外 patch。</li>
<li><code>pointSync false</code> 指定不执行额外的耦合点同步。</li>
<li>真正分组边界时需在 patches 列表中增加名称、类型和来源。</li>
</ul>
<p>可先由 topoSet 选出面集合，再用 constructFrom set 引用它，避免依靠模糊的几何猜测分组。</p>
<p><a href="/assets/examples/v2512/createpatchdict/2-createPatchDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel/system/createPatchDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      createPatchDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Do a synchronisation of coupled points after creation of any patches.
// Note: this does not work with points that are on multiple coupled patches
//       with transformations (i.e. cyclics).
pointSync false;

// Patches to create.
patches
(
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · heatTransfer/buoyantSimpleFoam/comfortHotRoom</summary><p>comfortHotRoom 把预先选好的面集合分别变成房间入口和出口。</p>
<ul>
<li><code>constructFrom set</code> 表示来源是面集合，两项分别引用 <code>set inlet</code> 和 <code>set outlet</code>。</li>
<li>新边界同名为 inlet、outlet，<code>patchInfo/type patch</code> 定义一般边界类型，具体速度和温度条件在场文件中设置。</li>
<li><code>pointSync false</code>、<code>writeCyclicMatch false</code> 控制点同步和周期匹配诊断输出。</li>
</ul>
<p>改变开口位置时先重新生成面集合，再运行 createPatch，最后检查边界面数与场条目。</p>
<p><a href="/assets/examples/v2512/createpatchdict/3-createPatchDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/comfortHotRoom/system/createPatchDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/comfortHotRoom">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      createPatchDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

pointSync         false;

writeCyclicMatch  false;

patches
(
    {
        name inlet;

        patchInfo
        {
            type patch;
        }

        constructFrom set;
        set inlet;
    }
    {
        name outlet;

        patchInfo
        {
            type patch;
        }

        constructFrom set;
        set outlet;
    }
);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/createpatch/">createPatch</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
