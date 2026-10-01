---
title: "第 17 章　system/ 下的其他字典"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><h4>17.1 decomposeParDict（并行分区）</h4>
<pre><code>numberOfSubdomains  8;          // 必须等于 mpirun -np 的数字

method              scotch;     // 分区算法

// 各算法的参数（只需写你用的那个）
simpleCoeffs    { n (2 2 2); delta 0.001; }        // 按 x/y/z 均分
hierarchicalCoeffs { n (2 2 2); delta 0.001; order xyz; }
manualCoeffs    { dataFile &quot;decompositionData&quot;; }</code></pre>
<div class="table-scroll"><table>
<tr><th>method</th><th>说明</th><th>何时用</th></tr>
<tr><td>scotch</td><td>自动最小化交界面，默认首选</td><td>绝大多数情况</td></tr>
<tr><td>hierarchical</td><td>按指定顺序在 x/y/z 上依次均分</td><td>规则区域、想控制分区形状</td></tr>
<tr><td>simple</td><td>直接三向均分</td><td>简单几何</td></tr>
<tr><td>kahip / metis</td><td>其他图分区库</td><td>有装才有</td></tr>
<tr><td>multiLevel</td><td>多级分区（跨节点/节点内分别优化）</td><td>大规模集群</td></tr>
<tr><td>structured</td><td>沿某方向不切（保持结构）</td><td>边界层方向不切分</td></tr>
<tr><td>manual</td><td>读文件指定每个单元归谁</td><td>特殊需求</td></tr>
</table></div>
<p>约束条件（保证某些面不被切开）：</p>
<pre><code>constraints
{
    baffles       { type preserveBaffles; }
    cyclics       { type preservePatches; patches (cyc1 cyc2); }
    faces         { type singleProcessorFaceSets; sets ((f0 -1)); }
}</code></pre>
<p>n (2 2 2) 的乘积必须等于 numberOfSubdomains，写不一致会直接报错。</p>
<h4>17.2 setFieldsDict（区域初始化）</h4>
<pre><code>defaultFieldValues              // 先把全场设成默认值
(
    volScalarFieldValue alpha.water 0
    volVectorFieldValue U (0 0 0)
);

regions                          // 再覆盖指定区域
(
    boxToCell
    {
        box (0 0 -1) (0.1461 0.292 1);
        fieldValues ( volScalarFieldValue alpha.water 1 );
    }

    cylinderToCell
    {
        p1 (0 0 0);  p2 (0 0 0.1);  radius 0.05;
        fieldValues ( volScalarFieldValue T 500 );
    }

    sphereToCell
    {
        origin (0 0 0);  radius 0.1;
        fieldValues ( volScalarFieldValue p 1e6 );
    }
);</code></pre>
<p>常用区域类型：boxToCell、sphereToCell、cylinderToCell、rotatedBoxToCell、surfaceToCell（用 STL 划区）、cellToCell（用已有 cellSet）、zoneToCell。</p>
<p>注意：setFields 直接修改 0/ 里的文件。跑之前先 cp -r 0.orig 0，否则第二次运行是在被改过的场上再改一次。</p>
<h4>17.3 topoSetDict（选择集合）</h4>
<pre><code>actions
(
    {
        name    c0;
        type    cellSet;        // cellSet / faceSet / pointSet / cellZoneSet / faceZoneSet
        action  new;            // new / add / subtract / subset / invert / clear / remove
        source  boxToCell;
        box     (0 0 0) (1 1 1);
    }
    {
        name    porous;
        type    cellZoneSet;
        action  new;
        source  setToCellZone;
        set     c0;
    }
);</code></pre>
<p>常用 source 一览</p>
<div class="table-scroll"><table>
<tr><th>类别</th><th>source</th><th>关键参数</th></tr>
<tr><td>几何选单元</td><td>boxToCell</td><td>box (min) (max) 或 boxes ((..)(..))</td></tr>
<tr><td></td><td>rotatedBoxToCell</td><td>origin, i, j, k</td></tr>
<tr><td></td><td>sphereToCell</td><td>origin, radius</td></tr>
<tr><td></td><td>cylinderToCell</td><td>p1, p2, radius</td></tr>
<tr><td></td><td>surfaceToCell</td><td>file &quot;x.stl&quot;, outsidePoints, includeCut</td></tr>
<tr><td>拓扑选单元</td><td>zoneToCell / setToCell / labelToCell</td><td>zone/set/value</td></tr>
<tr><td></td><td>cellToCell</td><td>set</td></tr>
<tr><td>选面</td><td>boxToFace、patchToFace、normalToFace、cellToFace</td><td></td></tr>
<tr><td></td><td>boundaryToFace</td><td>全部边界面</td></tr>
<tr><td>选点</td><td>boxToPoint、labelToPoint、surfaceToPoint</td><td></td></tr>
<tr><td>转 zone</td><td>setToCellZone、setsToFaceZone、setToPointZone</td><td></td></tr>
</table></div>
<p>Set 与 Zone 的区别（重要）：Set 是临时选择结果，写在 constant/polyMesh/sets/；Zone 是网格的正式组成部分，写进 cellZones/faceZones。求解器里的多孔介质、MRF、fvOptions、动网格全都认 Zone 不认 Set，所以典型流程是”先 xxxToCell 造 Set，再 setToCellZone 转 Zone”。</p>
<h4>17.4 fvOptions（源项与区域模型）</h4>
<p>放在 system/fvOptions（或 constant/fvOptions）。它让你不改求解器就能加源项。</p>
<pre><code>momentumSource
{
    type            meanVelocityForce;      // 恒定流量驱动（周期性槽道流必用）
    active          yes;
    selectionMode   all;
    fields          (U);
    Ubar            (0.1335 0 0);
}

heatSource
{
    type            scalarSemiImplicitSource;
    active          yes;
    selectionMode   cellZone;
    cellZone        heater;
    volumeMode      absolute;               // absolute / specific
    sources         { h (500 0); }          // (显式部分 隐式部分)
}

porous
{
    type            explicitPorositySource;
    active          yes;
    selectionMode   cellZone;
    cellZone        porousZone;
    type            DarcyForchheimer;
    d   (5e7 -1000 -1000);
    f   (0 0 0);
    coordinateSystem { ... }
}

MRF1
{
    type            MRFSource;             // 旋转参考系（风机、搅拌器）
    selectionMode   cellZone;
    cellZone        rotor;
    origin          (0 0 0);
    axis            (0 0 1);
    omega           constant 104.72;       // rad/s
}</code></pre>
<p>常用类型还有：limitTemperature（限温，防发散）、limitVelocity、fixedTemperatureConstraint、buoyancyEnergy、radiation、solidificationMeltingSource（相变）、atmAmbientTurbSource（大气边界层）。</p>
<p>为什么它重要：初学者遇到”我要在某个区域加个热源/阻力/旋转”，第一反应常是去改求解器源码。用 fvOptions 一个字典就能解决，且不影响可维护性。</p>
<h4>17.5 createPatchDict</h4>
<pre><code>pointSync false;

patches
(
    {
        name            cyclicLeft;
        patchInfo       { type cyclic; neighbourPatch cyclicRight; }
        constructFrom   patches;
        patches         (left);
    }
);</code></pre>
<p>用途：把网格转换器生成的一堆零散 patch 合并；把两个面配成周期边界；改 patch 类型。</p>
<h4>17.6 extrudeMeshDict</h4>
<pre><code>constructFrom   patch;              // mesh / patch / surface
sourceCase      &quot;../base&quot;;
sourcePatches   (front);
exposedPatchName back;

extrudeModel    linearNormal;       // linearNormal/linearDirection/wedge/sector/plane
linearNormalCoeffs { thickness 0.01; }
sectorCoeffs   { axisPt (0 0 0); axis (0 0 1); angle 5; }

nLayers         1;
expansionRatio  1.0;
mergeFaces      false;</code></pre>
<p>典型用途：把一个二维面拉伸成一层网格做二维算例；用 sector 模型做轴对称（wedge）算例。</p>
<h4>17.7 surfaceFeatureExtractDict</h4>
<pre><code>body.stl
{
    extractionMethod    extractFromSurface;
    includedAngle       150;          // 夹角超过它的棱视为特征边
    subsetFeatures      { nonManifoldEdges no; openEdges yes; }
    writeObj            yes;          // 输出 obj 方便在 ParaView 里检查
}</code></pre>
<p>includedAngle 越大，提取的边越多。150 是常用起点：太小会漏掉圆角过渡处的特征，太大会把曲面上的三角片棱也当成特征。</p>
<h4>17.8 refineMeshDict</h4>
<pre><code>set             c0;                 // 对哪个 cellSet 加密
coordinateSystem global;
globalCoeffs    { tan1 (1 0 0); tan2 (0 1 0); }
directions      ( tan1 tan2 );      // 只在这两个方向加密（各向异性）
useHexTopology  yes;
geometricCut    no;
writeMesh       no;
$ topoSet &amp;&amp; refineMesh -overwrite -dict system/refineMeshDict</code></pre>
<h4>17.9 mapFieldsDict</h4>
<pre><code>patchMap        ( inlet1 inlet );   // 源算例 patch → 目标算例 patch
cuttingPatches  ( outlet );         // 被切开的 patch（源网格不覆盖的部分）</code></pre>
<p>网格边界一致时可以完全不用这个文件，直接 mapFields ../src -consistent。</p>
<h4>17.10 changeDictionaryDict</h4>
<pre><code>dictionaryReplacement
{
    boundary
    {
        minZ { type wall; }
    }
    U
    {
        boundaryField
        {
            &quot;(inlet|outlet)&quot; { type zeroGradient; }
        }
    }
}</code></pre>
<p>多区域算例（chtMultiRegionFoam）里，每个 region 一份，放在 system/&lt;region&gt;/changeDictionaryDict。</p>
<h4>17.11 meshQualityDict</h4>
<pre><code>#includeEtc &quot;caseDicts/meshQualityDict&quot;     // 直接用官方默认阈值
maxNonOrtho 65;                             // 再局部覆盖</code></pre>
<p>供 checkMesh -meshQuality 与 snappyHexMesh 共用。</p>
<h4>17.12 setAlphaFieldDict</h4>
<pre><code>field       alpha.water;
type        sphere;            // sphere / plane / cylinder / sin
origin      (0.5 0.5 0);
radius      0.15;
direction   (1 0 0);</code></pre>
<p>比 setFields 精细：界面所在单元会得到精确的部分体积分数（而不是 0 或 1），用于界面收敛性验证。</p>
{% endraw %}