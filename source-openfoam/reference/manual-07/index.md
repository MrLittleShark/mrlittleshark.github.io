---
title: "07 网格生成与前处理配置"
layout: reference
description: "OpenCFD v2512 网格生成与前处理配置；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h3>7.1 system/blockMeshDict</h3>
<p>blockMeshDict 通过 vertices 定义顶点，以 hex 后的 8 个顶点编号确定块的局部方向和体积符号。(Nx Ny Nz) 指定三个方向的单元数，scale 指定坐标缩放系数，simpleGrading 指定各方向末端与起始单元的尺寸比。</p>
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
<h3>7.2 system/snappyHexMeshDict</h3>
<p>snappyHexMesh 包括切割细化、表面贴合和边界层生成三个阶段。运行 foamGetDict snappyHexMeshDict 获取带注释模板，在已建立的背景网格上配置几何和各阶段参数。</p>
<div class="table-scroll"><table>
<tr><th>参数</th><th>含义</th><th>设置方法</th></tr>
<tr><td>castellatedMesh、snap、addLayers</td><td>分别控制切割细化、贴体和边界层生成</td><td>先检查切割细化和贴体，再配置边界层</td></tr>
<tr><td>geometry</td><td>表面及可搜索几何体</td><td>body.stl { type triSurfaceMesh; name body; }</td></tr>
<tr><td>maxLocalCells、maxGlobalCells</td><td>局部及全局细化控制限额</td><td>根据可用内存设置单元数量上限</td></tr>
<tr><td>minRefinementCells</td><td>停止继续细化的候选单元阈值</td><td>设为 0 时继续处理剩余细化单元，计算量相应增加</td></tr>
<tr><td>nCellsBetweenLevels</td><td>相邻细化级别间的过渡层数</td><td>例如 3</td></tr>
<tr><td>features</td><td>显式特征文件和细化等级</td><td>({ file "body.eMesh"; level 2; })</td></tr>
<tr><td>refinementSurfaces</td><td>表面的最小最大细化等级</td><td>body { level (2 3); patchInfo { type wall; } }</td></tr>
<tr><td>resolveFeatureAngle</td><td>区分尖锐表面特征的角度</td><td>示例为 30，按表面几何特征确定</td></tr>
<tr><td>refinementRegions</td><td>体积或距离带细化</td><td>mode inside、outside 或 distance；levels 定义等级</td></tr>
<tr><td>locationInMesh</td><td>标记需要保留的连通流体区域</td><td>取目标流体区域内部点，避开边界面</td></tr>
<tr><td>allowFreeStandingZoneFaces</td><td>是否允许独立区域面</td><td>与 zone 生成方式匹配</td></tr>
<tr><td>snapControls</td><td>贴体松弛和迭代</td><td>nSmoothPatch、tolerance、nSolveIter、nRelaxIter</td></tr>
<tr><td>显式特征贴合</td><td>explicitFeatureSnap 与 nFeatureSnapIter</td><td>与 features 中的 eMesh 配合</td></tr>
<tr><td>layers</td><td>各 patch 的层数</td><td>"body.*" { nSurfaceLayers 3; }</td></tr>
<tr><td>relativeSizes</td><td>层厚是否相对外层网格尺寸</td><td>true 相对尺寸；false 绝对长度</td></tr>
<tr><td>expansionRatio</td><td>层间厚度增长比</td><td>例如 1.2</td></tr>
<tr><td>finalLayerThickness、firstLayerThickness、thickness</td><td>不同的层厚约束</td><td>按层厚参数关系选取相容组合</td></tr>
<tr><td>minThickness</td><td>允许保留的最小总层厚指标</td><td>阈值过大时，局部边界层将被取消</td></tr>
<tr><td>nGrow、nBufferCellsNoExtrude</td><td>尖角附近的非挤出区域及过渡缓冲</td><td>控制未生成边界层区域的过渡</td></tr>
<tr><td>featureAngle、slipFeatureAngle</td><td>层网格遇尖角时的行为</td><td>按几何特征及边界层覆盖率调整</td></tr>
<tr><td>nLayerIter、nRelaxedIter</td><td>边界层生成迭代及质量阈值放宽迭代</td><td>几何有效性满足要求后设置迭代上限</td></tr>
<tr><td>meshQualityControls</td><td>质量约束</td><td>通常包含系统 meshQualityDict</td></tr>
<tr><td>mergeTolerance</td><td>点合并相对容差</td><td>常用 1e-6，以几何包围盒尺度为基准</td></tr>
</table></div>
<pre><code class="language-openfoam">// 片段：放入对应的 snappyHexMeshDict
geometry
{
    body.stl { type triSurfaceMesh; name body; }
    refineBox
    {
        type searchableBox;
        min (-0.2 -0.2 -0.2);
        max (1.2 0.2 0.2);
    }
}
castellatedMeshControls
{
    maxLocalCells 1000000;
    maxGlobalCells 3000000;
    minRefinementCells 0;
    nCellsBetweenLevels 3;
    features ({ file "body.eMesh"; level 2; });
    refinementSurfaces
    {
        body { level (2 3); patchInfo { type wall; } }
    }
    resolveFeatureAngle 30;
    refinementRegions
    {
        refineBox { mode inside; levels ((1e15 2)); }
    }
    locationInMesh (2 0 0);
    allowFreeStandingZoneFaces true;
}
snapControls
{
    nSmoothPatch 3; tolerance 2.0;
    nSolveIter 30; nRelaxIter 5;
    nFeatureSnapIter 10;
    implicitFeatureSnap false;
    explicitFeatureSnap true;
    multiRegionFeatureSnap false;
}</code></pre>
<p>locationInMesh 中的 (2 0 0) 表示待保留流体区域内的一点，该点须位于背景网格范围内及物体外部。网格生成前应消除 STL 自相交，统一长度单位，并检查背景网格。</p>
<p>边界层生成配置如下。snapControls 和质量控制参数保留模板中的完整设置。将 addLayers 设为 false，可单独检查切割细化和表面贴合结果。</p>
<pre><code class="language-openfoam">castellatedMesh true;
snap true;
addLayers true;
addLayersControls
{
    relativeSizes true;
    layers { body { nSurfaceLayers 3; } }
    expansionRatio 1.2;
    finalLayerThickness 0.3;
    minThickness 0.1;
    nGrow 0;
    featureAngle 60;
    nRelaxIter 5;
    nSmoothSurfaceNormals 1;
    nSmoothNormals 3;
    nSmoothThickness 10;
    maxFaceThicknessRatio 0.5;
    maxThicknessToMedialRatio 0.3;
    minMedialAxisAngle 90;
    nBufferCellsNoExtrude 0;
    nLayerIter 50;
}
meshQualityControls
{
    #includeEtc "caseDicts/meshQualityDict"
}
mergeTolerance 1e-6;</code></pre>
<h3>7.3 system/surfaceFeatureExtractDict</h3>
<pre><code class="language-openfoam">FoamFile
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
<h3>7.4 system/meshQualityDict</h3>
<p>运行 foamGetDict meshQualityDict 获取模板，或通过 #includeEtc "caseDicts/meshQualityDict" 引入。下表列出常用质量指标及示例阈值，阈值应结合网格尺度和求解要求确定。</p>
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
<h3>7.5 system/setFieldsDict</h3>
<p>setFields 首先按 defaultFieldValues 设置全域初值，再依次执行 regions 中的区域赋值。区域重叠时，后续赋值覆盖先前结果。目标场文件须预先建立，并设置相应的 class 和 dimensions。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object setFieldsDict;
}
defaultFieldValues
(
    volScalarFieldValue alpha.water 0
    volVectorFieldValue U (0 0 0)
);
regions
(
    boxToCell
    {
        box (0 0 -1) (0.2 0.3 1);
        fieldValues (volScalarFieldValue alpha.water 1);
    }
);</code></pre>
<p>boxToCell 按单元位置选取长方体区域；sphereToCell 通过 centre 和 radius 定义球形区域；cylinderToCell 通过 p1、p2 和 radius 定义圆柱区域。边界面可采用 boxToFace 等选择器。</p>
<p>赋值后检查 alpha.water 的极值与空间分布，边界条件在场文件中另行设置。需采用数学表达式赋值时，使用 setExprFields。</p>
<h3>7.6 system/setExprFieldsDict</h3>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object setExprFieldsDict;
}
expressions
(
    setTemperature
    {
        field T;
        expression "300 + 10*pos().x()";
    }
);</code></pre>
<p>下例在已有温度场 T 上设置随坐标变化的温度，运行 setExprFields 后生效。fieldMask 限定赋值区域，create 和 dimensions 用于新建场。表达式语法可通过 foamExprParserInfo 查询。边界表达式使用 setExprBoundaryFieldsDict，其结构按边界场接口配置。</p>
<h3>7.7 system/topoSetDict</h3>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object topoSetDict;
}
actions
(
    {
        name heaterCells;
        type cellSet;
        action new;
        source boxToCell;
        box (0.2 0 0) (0.4 0.1 0.01);
    }
    {
        name heater;
        type cellZoneSet;
        action new;
        source setToCellZone;
        set heaterCells;
    }
);</code></pre>
<div class="table-scroll"><table>
<tr><th>条目</th><th>含义</th><th>设置方法与取值</th></tr>
<tr><td>name</td><td>输出集合或区域名称</td><td>与源项中的 cellZone 匹配</td></tr>
<tr><td>type</td><td>对象类别</td><td>cellSet、faceSet、pointSet、cellZoneSet、faceZoneSet</td></tr>
<tr><td>action</td><td>集合操作</td><td>new、add、subtract、subset、invert、clear、remove</td></tr>
<tr><td>source</td><td>选择算法</td><td>boxToCell、sphereToCell、cylinderToCell、patchToFace、fieldToCell 等</td></tr>
<tr><td>sourceInfo</td><td>选择源参数子字典</td><td>多数选择源可将参数直接写入动作字典；名称冲突时采用 sourceInfo</td></tr>
</table></div>
<h3>7.8 system/createPatchDict</h3>
<pre><code class="language-openfoam">FoamFile
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
<h3>7.9 system/createBafflesDict</h3>
<p>createBaffles 将内部面转换为成对边界面。internalFacesOnly 控制选面范围，baffles 定义各挡板的 type、zoneName 和 patches。下例采用预先建立的 interfaceZone 面区域。</p>
<pre><code class="language-openfoam">internalFacesOnly true;
baffles
{
    interface
    {
        type faceZone;
        zoneName interfaceZone;
        patches
        {
            master { name sideA; type wall; }
            slave  { name sideB; type wall; }
        }
    }
}</code></pre>
<p>运行 createBaffles -overwrite 生成挡板边界。两侧的传热和流动耦合由场边界条件及物理模型确定。</p>
<h3>7.10 system/refineMeshDict</h3>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object refineMeshDict;
}
set heaterCells;
coordinateSystem global;
globalCoeffs
{
    tan1 (1 0 0);
    tan2 (0 1 0);
}
directions (tan1 tan2);
useHexTopology true;
geometricCut false;
writeMesh false;</code></pre>
<p>set 指定待细化的单元集合，directions 指定细化方向。二维网格仅沿面内方向细化，厚度方向保持 empty 边界要求的单层结构。运行 refineMesh -overwrite 后，检查场、区域和边界与新网格的对应关系。</p>
<h3>7.11 system/extrudeMeshDict</h3>
<p>constructFrom 指定挤出来源，sourceCase 和 sourcePatches 指定源算例及边界，exposedPatchName 定义新暴露边界。extrudeModel 选择挤出模型，nLayers 和 expansionRatio 控制层数及层厚比，mergeFaces 和 mergeTol 控制合并。linearNormal 通过 linearNormalCoeffs/thickness 设置总厚度；其他模型采用各自的系数字典。</p>
<pre><code class="language-plaintext">// 片段：沿已有 patch 外法向挤出
constructFrom patch;
sourceCase ".";
sourcePatches (front);
exposedPatchName back;
extrudeModel linearNormal;
nLayers 5;
expansionRatio 1;
linearNormalCoeffs { thickness 0.01; }
mergeFaces false;
mergeTol 0;</code></pre>
<h3>7.12 system/mapFieldsDict</h3>
<p>mapFieldsDict 用于源算例与目标算例边界不一致时的场映射。patchMap 中每组名称依次为目标边界和源边界。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object mapFieldsDict;
}
patchMap
(
    inlet sourceInlet
    outlet sourceOutlet
);
cuttingPatches (newCutBoundary);</code></pre>
<p>在目标算例中执行 mapFields ../sourceCase -sourceTime latestTime。cuttingPatches 指定切穿源计算域的目标边界，其数值由源域内部插值得到。-consistent 适用于边界拓扑匹配的算例。映射体积分数等守恒量后，应检查有界性及积分守恒。</p>
<h3>7.13 system/changeDictionaryDict</h3>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object changeDictionaryDict;
}
dictionaryReplacement
{
    U
    {
        boundaryField
        {
            inlet { type fixedValue; value uniform (2 0 0); }
        }
    }
}</code></pre>
<p>dictionaryReplacement 按目标文件名组织替换条目，运行 changeDictionary 后写回相应文件。-instance 指定目标实例目录。单个键值可直接通过 foamDictionary 修改。</p>
{% endraw %}
