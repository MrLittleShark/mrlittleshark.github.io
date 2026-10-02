---
title: "meshQualityDict"
layout: reference
description: "设置非正交角、偏斜、体积等网格质量限制。snappyHexMesh 可在生成网格时用这些阈值调整局部操作。"
dictionary: true
cms_slug: "dictionary-meshqualitydict"
---

<p>设置非正交角、偏斜、体积等网格质量限制。snappyHexMesh 可在生成网格时用这些阈值调整局部操作。</p><p>位置：<code>system/meshQualityDict</code></p><figure class="wolf-figure"><img src="/assets/wolf/wolf-mesh-nonorthogonality.png" alt="非正交角的几何定义" loading="lazy"><figcaption><strong>非正交角的几何定义</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 16 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure><h2>配置实例</h2><p>运行 foamGetDict meshQualityDict 获取模板，或通过 #includeEtc "caseDicts/meshQualityDict" 引入。下表列出常用质量指标及示例阈值，阈值应结合网格尺度和求解要求确定。</p>
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
<h2>17.11 meshQualityDict</h2><pre><code class="language-openfoam">#includeEtc "caseDicts/meshQualityDict"     // 直接用官方默认阈值
maxNonOrtho 65;                             // 再局部覆盖</code></pre>
<p>供 checkMesh -meshQuality 与 snappyHexMesh 共用。</p><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · combustion/reactingFoam/RAS/membrane</summary><p>膜分离反应流算例把网格质量阈值集中放在公共配置中。</p>
<ul>
<li>这里唯一的有效条目是 <code>#includeEtc "caseDicts/meshQualityDict"</code>，它从当前 OpenFOAM 安装展开质量约束。</li>
<li>实际阈值取决于被包含文件；阅读本例时应连同该文件查看非正交、倾斜与体积等要求。</li>
<li>本文件没有局部覆盖值，调整某项可在 include 后显式添加同名条目。</li>
</ul>
<p>网格被拒绝时先定位具体质量项和坏单元位置，再判断是改善几何、网格参数，还是调整适当阈值。</p>
<p><a href="/assets/examples/v2512/meshqualitydict/1-meshQualityDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/membrane/system/meshQualityDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/membrane">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/simpleFoam/rotorDisk</summary><p>rotorDisk 的网格质量设置引用生成器用的公共阈值，供网格生成与质量判断使用。</p>
<ul>
<li><code>#includeEtc "caseDicts/mesh/generation/meshQualityDict.cfg"</code> 指向安装内的生成配置。</li>
<li>本地文件没有再定义数值，因此完整配置由 include 展开取得。</li>
<li>需要定制时可在文件后部增加明确的质量阈值，并保留与求解离散格式的对应。</li>
</ul>
<p>旋转盘附近的高纵横比或局部细化需要查看坏单元分布；单独放宽阈值不会改变网格本身。</p>
<p><a href="/assets/examples/v2512/meshqualitydict/2-meshQualityDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/rotorDisk/system/meshQualityDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/rotorDisk">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · combustion/XiDyMFoam/annularCombustorTurbine</summary><p>环形燃烧器网格沿用公共质量标准，并对非正交角作了更明确的限制。</p>
<ul>
<li><code>#includeEtc "caseDicts/meshQualityDict"</code> 提供基础质量约束。</li>
<li><code>maxNonOrtho 55</code> 将允许的最大非正交角设为 55°，本地值覆盖包含文件中的同名项。</li>
<li>角度描述单元中心连线与面法向的偏离，直接影响法向梯度离散。</li>
</ul>
<p>若局部超限，先在几何上定位单元并调整网格；修改阈值后仍需选择与非正交程度相适应的数值修正。</p>
<p><a href="/assets/examples/v2512/meshqualitydict/3-meshQualityDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/XiDyMFoam/annularCombustorTurbine/system/meshQualityDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/XiDyMFoam/annularCombustorTurbine">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/checkmesh/">checkMesh</a> · <a href="/commands/snappyhexmesh/">snappyHexMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
