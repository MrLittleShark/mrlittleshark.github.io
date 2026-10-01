---
title: "system/surfaceFeatureExtractDict · surfaceFeatureExtractDict"
layout: reference
description: "输入表面 body.stl 存放于 constant/triSurface。includedAngle 按特征提取器的包含角定义取值，其定义与 resolveFeatureAngle 不同。writeObj 控制可视化文件输出。运行 surfaceFeatureExtract 后，将生成的 eMesh 文件名用于后续特征线配置。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>输入表面 body.stl 存放于 constant/triSurface。includedAngle 按特征提取器的包含角定义取值，其定义与 resolveFeatureAngle 不同。writeObj 控制可视化文件输出。运行 surfaceFeatureExtract 后，将生成的 eMesh 文件名用于后续特征线配置。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/surfaceFeatureExtractDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>extractionMethod</code> · <code>extractFromSurfaceCoeffs</code> · <code>includedAngle</code> · <code>writeObj</code></p><h2>关联命令</h2><p><a href="/commands/?q=surfaceFeatureExtract">surfaceFeatureExtract</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/surfaceFeatureExtractDict -keywords
surfaceFeatureExtract -help</code></pre><h2>7.3 system/surfaceFeatureExtractDict</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object surfaceFeatureExtractDict;
}
body.stl
{
    extractionMethod extractFromSurface;
    extractFromSurfaceCoeffs { includedAngle 150; }
    writeObj yes;
}</code></pre>
<p>输入表面 body.stl 存放于 constant/triSurface。includedAngle 按特征提取器的包含角定义取值，其定义与 resolveFeatureAngle 不同。writeObj 控制可视化文件输出。运行 surfaceFeatureExtract 后，将生成的 eMesh 文件名用于后续特征线配置。</p>
<h2>17.7 surfaceFeatureExtractDict</h2><pre><code class="language-openfoam">body.stl
{
    extractionMethod    extractFromSurface;
    includedAngle       150;          // 夹角超过它的棱视为特征边
    subsetFeatures      { nonManifoldEdges no; openEdges yes; }
    writeObj            yes;          // 输出 obj 方便在 ParaView 里检查
}</code></pre>
<p>includedAngle 越大，提取的边越多。150 是常用起点：太小会漏掉圆角过渡处的特征，太大会把曲面上的三角片棱也当成特征。</p><h2>从真实配置理解关键条目</h2><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>buildings.obj</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>HULL.obj</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>MRF_region.obj</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/simpleFoam/windAroundBuildings</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/windAroundBuildings/system/surfaceFeatureExtractDict</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/windAroundBuildings/system/surfaceFeatureExtractDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/surfacefeatureextractdict/1-surfaceFeatureExtractDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/windAroundBuildings">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFeatureExtractDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

buildings.obj
{
    #includeEtc &quot;caseDicts/surface/surfaceFeatureExtractDict.cfg&quot;
}


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/surface/surfaceFeatureExtractDict.cfg&quot;。下载单个文件不会自动取得这些依赖。</p><h3>示例 2 · multiphase/overInterDyMFoam/rigidBodyHull/overset-1</h3><p>原始路径：<code>tutorials/multiphase/overInterDyMFoam/rigidBodyHull/overset-1/system/surfaceFeatureExtractDict</code>；求解器：<code>snappyHexMesh</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/rigidBodyHull/overset-1/system/surfaceFeatureExtractDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/surfacefeatureextractdict/2-surfaceFeatureExtractDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/rigidBodyHull/overset-1">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFeatureExtractDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

HULL.obj
{
    extractionMethod extractFromSurface;
    writeObj        yes;

    extractFromSurfaceCoeffs
    {
        includedAngle   150;
    }
}


// ************************************************************************* //</code></pre><h3>示例 3 · heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet</h3><p>原始路径：<code>tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet/system/surfaceFeatureExtractDict</code>；求解器：<code>chtMultiRegionSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet/system/surfaceFeatureExtractDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/surfacefeatureextractdict/3-surfaceFeatureExtractDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFeatureExtractDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

MRF_region.obj
{
    extractionMethod extractFromSurface;
    writeObj        yes;

    extractFromSurfaceCoeffs
    {
        includedAngle   150;
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/surfacefeatureextract/">surfaceFeatureExtract</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/surfaceFeatureExtractDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/surfaceFeatureExtractDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
