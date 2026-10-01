---
title: "system/meshQualityDict · meshQualityDict"
layout: reference
description: "运行 foamGetDict meshQualityDict 获取模板，或通过 #includeEtc \"caseDicts/meshQualityDict\" 引入。下表列出常用质量指标及示例阈值，阈值应结合网格尺度和求解要求确定。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>运行 foamGetDict meshQualityDict 获取模板，或通过 #includeEtc &quot;caseDicts/meshQualityDict&quot; 引入。下表列出常用质量指标及示例阈值，阈值应结合网格尺度和求解要求确定。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/meshQualityDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>maxNonOrtho</code> · <code>maxBoundarySkewness</code> · <code>maxInternalSkewness</code> · <code>minVol</code> · <code>minDeterminant</code></p><h2>关联命令</h2><p><a href="/commands/?q=checkMesh">checkMesh</a> · <a href="/commands/?q=snappyHexMesh">snappyHexMesh</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/meshQualityDict -keywords
checkMesh -help</code></pre><h2>7.4 system/meshQualityDict</h2><p>运行 foamGetDict meshQualityDict 获取模板，或通过 #includeEtc &quot;caseDicts/meshQualityDict&quot; 引入。下表列出常用质量指标及示例阈值，阈值应结合网格尺度和求解要求确定。</p>
<div class="table-scroll"><table>
<tr><th>参数</th><th>含义</th><th>示例值</th></tr>
<tr><td>maxNonOrtho</td><td>最大非正交角</td><td>65</td></tr>
<tr><td>maxBoundarySkewness</td><td>边界偏斜限制</td><td>20</td></tr>
<tr><td>maxInternalSkewness</td><td>内部偏斜限制</td><td>4</td></tr>
<tr><td>maxConcave</td><td>最大凹角</td><td>80</td></tr>
<tr><td>minVol</td><td>最小单元体积</td><td>示例为 1e-13，按实际网格尺度确定</td></tr>
<tr><td>minTetQuality</td><td>最小分解四面体质量</td><td>1e-15</td></tr>
<tr><td>minArea</td><td>最小面面积</td><td>负值可关闭相应面积检查</td></tr>
<tr><td>minTwist、minTriangleTwist</td><td>面扭曲限制</td><td>以模板值为初值，按不合格面分布调整</td></tr>
<tr><td>minDeterminant</td><td>单元几何行列式限制</td><td>0.001</td></tr>
<tr><td>minFaceWeight</td><td>面插值权重下限</td><td>0.05</td></tr>
<tr><td>minVolRatio</td><td>相邻单元体积比下限</td><td>0.01</td></tr>
<tr><td>nSmoothScale、errorReduction</td><td>质量失败时缩放处理参数</td><td>4、0.75</td></tr>
</table></div>
<h2>17.11 meshQualityDict</h2><pre><code class="language-openfoam">#includeEtc &quot;caseDicts/meshQualityDict&quot;     // 直接用官方默认阈值
maxNonOrtho 65;                             // 再局部覆盖</code></pre>
<p>供 checkMesh -meshQuality 与 snappyHexMesh 共用。</p><h2>从真实配置理解关键条目</h2><p>该专用配置的字段由对应程序决定。阅读下面完整文件时，应把同一层的大括号块作为一个模型实例，并从 Allrun 和 #include 追踪输入关系；本页不为缺少直接证据的键杜撰默认值。</p><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · combustion/reactingFoam/RAS/membrane</h3><p>原始路径：<code>tutorials/combustion/reactingFoam/RAS/membrane/system/meshQualityDict</code>；求解器：<code>reactingFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/membrane/system/meshQualityDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/meshqualitydict/1-meshQualityDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/membrane">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      meshQualityDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#includeEtc &quot;caseDicts/meshQualityDict&quot;


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/meshQualityDict&quot;。下载单个文件不会自动取得这些依赖。</p><h3>示例 2 · incompressible/simpleFoam/rotorDisk</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/rotorDisk/system/meshQualityDict</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/rotorDisk/system/meshQualityDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/meshqualitydict/2-meshQualityDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/rotorDisk">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      meshQualityDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#includeEtc &quot;caseDicts/mesh/generation/meshQualityDict.cfg&quot;


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/mesh/generation/meshQualityDict.cfg&quot;。下载单个文件不会自动取得这些依赖。</p><h3>示例 3 · combustion/XiDyMFoam/annularCombustorTurbine</h3><p>原始路径：<code>tutorials/combustion/XiDyMFoam/annularCombustorTurbine/system/meshQualityDict</code>；求解器：<code>XiDyMFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/XiDyMFoam/annularCombustorTurbine/system/meshQualityDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/meshqualitydict/3-meshQualityDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/XiDyMFoam/annularCombustorTurbine">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      meshQualityDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Include defaults parameters from master dictionary
#includeEtc &quot;caseDicts/meshQualityDict&quot;

maxNonOrtho 55;


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/meshQualityDict&quot;。下载单个文件不会自动取得这些依赖。</p><h2>配套命令与验证次序</h2><p><a href="/commands/checkmesh/">checkMesh</a> · <a href="/commands/snappyhexmesh/">snappyHexMesh</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/meshQualityDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/meshQualityDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
