---
title: "system/createPatchDict · createPatchDict"
layout: reference
description: "constructFrom patches 从已有边界选面；constructFrom set 从指定 faceSet 选面。pointSync 控制耦合点同步。执行 createPatch -overwrite 后，将 0/U、0/p 等场文件中的边界条目与新建 walls 对应。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>constructFrom patches 从已有边界选面；constructFrom set 从指定 faceSet 选面。pointSync 控制耦合点同步。执行 createPatch -overwrite 后，将 0/U、0/p 等场文件中的边界条目与新建 walls 对应。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/createPatchDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>pointSync</code> · <code>patches</code> · <code>name</code> · <code>patchInfo</code> · <code>constructFrom</code> · <code>set</code></p><h2>关联命令</h2><p><a href="/commands/?q=createPatch">createPatch</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/createPatchDict -keywords
createPatch -help</code></pre><h2>7.8 system/createPatchDict</h2><pre><code class="language-openfoam">FoamFile
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
<p>用途：把网格转换器生成的一堆零散 patch 合并；把两个面配成周期边界；改 patch 类型。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>constructFrom</td><td>指定挤出源来自已有网格、表面或其他受支持的输入。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>pointSync</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · multiphase/overInterDyMFoam/rigidBodyHull/background</h3><p>原始路径：<code>tutorials/multiphase/overInterDyMFoam/rigidBodyHull/background/system/createPatchDict</code>；求解器：<code>overInterDyMFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/rigidBodyHull/background/system/createPatchDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/createpatchdict/1-createPatchDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/rigidBodyHull/background">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · mesh/foamyHexMesh/mixerVessel</h3><p>原始路径：<code>tutorials/mesh/foamyHexMesh/mixerVessel/system/createPatchDict</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel/system/createPatchDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/createpatchdict/2-createPatchDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · heatTransfer/buoyantSimpleFoam/comfortHotRoom</h3><p>原始路径：<code>tutorials/heatTransfer/buoyantSimpleFoam/comfortHotRoom/system/createPatchDict</code>；求解器：<code>buoyantSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/comfortHotRoom/system/createPatchDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/createpatchdict/3-createPatchDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/comfortHotRoom">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/createpatch/">createPatch</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/createPatchDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/createPatchDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
