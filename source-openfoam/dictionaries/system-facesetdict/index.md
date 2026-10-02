---
title: "faceSetDict"
layout: reference
description: "教程中面集合生成或筛选使用的配置。"
dictionary: true
cms_slug: "dictionary-facesetdict"
---

<p>教程中面集合生成或筛选使用的配置。</p><p>位置：<code>system/faceSetDict</code></p><h2>配置实例</h2><p>mesh/foamyHexMesh/flange 中的 faceSetDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      faceSetDict;
}

// Name of set to operate on
name facesToBeRemoved;

// One of (add | subtract | subset | clear | new | invert | list)
action  new;

// Actions to apply to pointSet. These are all the topoSetSource&#x27;s ending
// in ..ToFace (see the meshTools library).
topoSetSources
(
    //  Select by explicitly providing face labels
    labelToFace
    {
        value #include &quot;../facesToBeRemoved&quot;;
    }
);</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>name</td><td>要创建或修改的面集合名称。</td></tr><tr><td>action</td><td>集合操作，例如 new、add、subtract 或 subset。</td></tr><tr><td>topoSetSources</td><td>面选择源列表，示例利用 labelToFace 按面编号选择。</td></tr><tr><td>value</td><td>此处由 #include 读取外部面编号列表。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · mesh/foamyHexMesh/flange</summary><p>flange 算例用显式面编号建立 facesToBeRemoved 集合，后续网格处理据此选择要移除的面。</p>
<ul>
<li><code>name facesToBeRemoved</code> 指定输出面集合名。</li>
<li><code>action new</code> 创建新的集合内容，替换同名集合的原有选择。</li>
<li><code>labelToFace</code> 按面编号选取；<code>value #include "../facesToBeRemoved"</code> 从外部文件读入编号列表。</li>
</ul>
<p>重新生成网格后面编号可能变化，应重新生成这份列表，并在显示面集合后确认选中区域与预期一致。</p>
<p><a href="/assets/examples/v2512/facesetdict/1-faceSetDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/flange/system/faceSetDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/flange">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      faceSetDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Name of set to operate on
name facesToBeRemoved;

// One of (add | subtract | subset | clear | new | invert | list)
action  new;

// Actions to apply to pointSet. These are all the topoSetSource&#x27;s ending
// in ..ToFace (see the meshTools library).
topoSetSources
(
    //  Select by explicitly providing face labels
    labelToFace
    {
        value #include &quot;../facesToBeRemoved&quot;;
    }
);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/toposet/">topoSet</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
