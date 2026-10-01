---
title: "system/faceSetDict · faceSetDict"
layout: reference
description: "教程中面集合生成或筛选使用的配置。现代通用选择工作流通常使用 topoSetDict；此文件的读入方式须以配套 Allrun 和工具参数为准。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>教程中面集合生成或筛选使用的配置。现代通用选择工作流通常使用 topoSetDict；此文件的读入方式须以配套 Allrun 和工具参数为准。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>name</td><td>要创建或修改的面集合名称。</td></tr><tr><td>action</td><td>集合操作，例如 new、add、subtract 或 subset。</td></tr><tr><td>topoSetSources</td><td>面选择源列表，示例利用 labelToFace 按面编号选择。</td></tr><tr><td>value</td><td>此处由 #include 读取外部面编号列表。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>name</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // Name of set to operate on</td></tr><tr><td>action</td><td>One of (add | subtract | subset | clear | new | invert | list)</td></tr><tr><td>topoSetSources</td><td>Actions to apply to pointSet. These are all the topoSetSource&#x27;s ending in ..ToFace (see the meshTools library).</td></tr><tr><td>labelToFace</td><td>Select by explicitly providing face labels</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 1 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><p>该文件族在本次固定版本源码中仅选到一份不同的完整配置；不重复同一个文件充当多个案例。</p><h3>示例 1 · mesh/foamyHexMesh/flange</h3><p>原始路径：<code>tutorials/mesh/foamyHexMesh/flange/system/faceSetDict</code>；求解器：<code>foamyHexMesh</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/flange/system/faceSetDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/facesetdict/1-faceSetDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/flange">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/toposet/">topoSet</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/faceSetDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/faceSetDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
