---
title: "第 6 章　前处理命令（网格与初场）"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><p>前处理要回答三个问题：网格从哪来（生成或转换）→ 网格好不好（检查）→ 初始场怎么给（初始化）。这一章按这个顺序排。</p>
<h4>6.1 blockMesh —— 结构化网格生成器</h4>
<p>是什么：读 system/blockMeshDict，把若干个六面体块划分成网格，写进 constant/polyMesh/。</p>
<p>为什么它是入门第一课：它是 OpenFOAM 唯一”纯文本定义几何 + 网格”的工具，所有信息都摆在一个文件里，看得见摸得着。复杂几何最终要靠 snappyHexMesh，但 snappy 也需要 blockMesh 先造一个背景网格。</p>
<p>用法</p>
<pre><code>blockMesh [-dict &lt;文件&gt;] [-case &lt;目录&gt;] [-region &lt;区域&gt;] [-write-vtk] [-no-clean]</code></pre>
<div class="table-scroll"><table>
<tr><th>选项</th><th>作用</th></tr>
<tr><td>-dict &lt;文件&gt;</td><td>用别的字典（做参数扫描时指向不同文件）</td></tr>
<tr><td>-region &lt;名字&gt;</td><td>为指定区域建网格（多区域算例）</td></tr>
<tr><td>-write-vtk</td><td>额外输出 VTK，便于在 ParaView 里直接看块结构</td></tr>
</table></div>
<p>示例</p>
<pre><code>$ run
$ cp -r $FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity .
$ cd cavity
$ blockMesh
...
Mesh Information
  nPoints: 882   nCells: 400   nFaces: 1640
End
$ ls constant/polyMesh/
boundary  faces  neighbour  owner  points</code></pre>
<p>生成的五个文件就是 OpenFOAM 的网格全部内容：points（点坐标）、faces（面由哪些点组成）、owner/neighbour（面属于哪两个单元）、boundary（边界分组）。理解这五个文件，就理解了 OpenFOAM 的非结构化网格数据结构：它不存”单元由哪些点组成”，而是存”面”，单元是由面隐式定义的。这正是它能处理任意多面体网格的原因。</p>
<p>字典写法见第 15 章。</p>
<h4>6.2 surfaceFeatureExtract 与 surface 系列</h4>
<p>是什么：从 STL/OBJ 几何里提取特征边（两个面片夹角超过阈值的棱），输出 constant/extendedFeatureEdgeMesh/。</p>
<p>为什么需要它：snappyHexMesh 默认只会把网格”贴”到曲面上，尖锐的棱角会被磨圆。要保住机翼后缘、方柱棱边这类特征，必须先把特征边提出来，再在 snappy 里显式要求捕捉它们。</p>
<pre><code>$ surfaceFeatureExtract          # 读 system/surfaceFeatureExtractDict</code></pre>
<p>其他常用 surface 工具</p>
<div class="table-scroll"><table>
<tr><th>命令</th><th>作用</th><th>示例</th></tr>
<tr><td>surfaceCheck</td><td>检查 STL 是否封闭、有无自交、法向是否一致</td><td>surfaceCheck geom.stl</td></tr>
<tr><td>surfaceTransformPoints</td><td>缩放/平移/旋转几何</td><td>surfaceTransformPoints -scale &#x27;(0.001 0.001 0.001)&#x27; in.stl out.stl</td></tr>
<tr><td>surfaceConvert</td><td>格式转换（stl/obj/vtk/nas…）</td><td>surfaceConvert in.obj out.stl</td></tr>
<tr><td>surfaceOrient</td><td>统一法向朝向</td><td>surfaceOrient in.stl &#x27;(0 0 0)&#x27; out.stl</td></tr>
<tr><td>surfaceMeshTriangulate</td><td>把 OpenFOAM 边界导出为 STL</td><td>surfaceMeshTriangulate walls.stl -patches &#x27;(wall.*)&#x27;</td></tr>
<tr><td>surfaceBooleanFeatures</td><td>两个曲面的交线</td><td>复杂几何拼接时用</td></tr>
<tr><td>surfaceSplitByPatch</td><td>按 solid 名拆分 STL</td><td>一个 STL 里含多个部件时</td></tr>
</table></div>
<p>STL 文件本身不保存统一的长度单位约定。若几何按毫米导出，而算例采用米，需要进行相应缩放。应使用 surfaceCheck 核对包围盒尺寸，确认几何尺度与物性及边界条件的单位体系一致。</p>
<pre><code>$ surfaceCheck constant/triSurface/body.stl | grep -i bound
Bounding box : (0 0 0) (1200 400 300)    ← 明显是毫米，需要 -scale 0.001</code></pre>
<h4>6.3 snappyHexMesh —— 复杂几何自动网格</h4>
<p>是什么：以 blockMesh 生成的背景网格为原料，按 STL 几何做三步加工：细分切割（castellate）→ 贴合（snap）→ 加边界层（addLayers）。</p>
<p>为什么是三步而不是一步：这三步各自可能失败，分开做才能定位问题。切割阶段失败通常是 locationInMesh 点选错了；贴合阶段失败是特征边没提取或网格质量阈值太严；加层失败是几何太尖或者层数太多。分三次跑、每次看结果，是 snappy 调试的标准姿势。</p>
<p>用法</p>
<pre><code>snappyHexMesh [-overwrite] [-dict &lt;文件&gt;] [-parallel]</code></pre>
<div class="table-scroll"><table>
<tr><th>选项</th><th>作用</th></tr>
<tr><td>-overwrite</td><td>直接覆盖 constant/polyMesh，不生成 1/、2/、3/ 中间时间目录</td></tr>
<tr><td>-dict</td><td>指定字典</td></tr>
</table></div>
<p>示例：分阶段调试（强烈推荐初学者这么做）</p>
<pre><code># ① 只做切割：把 snap 和 addLayers 关掉，跑完立刻用 paraFoam 看
$ foamDictionary system/snappyHexMeshDict -entry snap -set false
$ foamDictionary system/snappyHexMeshDict -entry addLayers -set false
$ snappyHexMesh                    # 结果在 1/ 目录，可单独查看

# ② 确认切割正确后，打开 snap
$ foamDictionary system/snappyHexMeshDict -entry snap -set true
$ snappyHexMesh

# ③ 最后打开边界层
$ foamDictionary system/snappyHexMeshDict -entry addLayers -set true
$ snappyHexMesh -overwrite
$ checkMesh -allGeometry -allTopology</code></pre>
<p>并行加密（大网格必须并行，单核会内存爆掉）：</p>
<pre><code>$ decomposePar
$ mpirun -np 8 snappyHexMesh -overwrite -parallel
$ reconstructParMesh -constant</code></pre>
<p>字典写法见第 16 章。</p>
<h4>6.4 extrudeMesh 与 extrudeToRegionMesh</h4>
<p>是什么：把一个面（或一个已有的 patch）沿法向/轴向拉伸成三维网格。</p>
<p>为什么需要它：二维算例、轴对称楔形（wedge）算例常用；也用来从已有网格的某个边界”长出”一层新区域（如固体壁面区）。</p>
<pre><code>$ extrudeMesh                       # 读 system/extrudeMeshDict
$ extrudeToRegionMesh -overwrite    # 从 faceZone 生成新 region（共轭传热常用）</code></pre>
<h4>6.5 checkMesh —— 网格体检（每次建完网格必跑）</h4>
<p>是什么：检查网格拓扑与几何质量，报告非正交角、歪斜度、纵横比、负体积等。</p>
<p>为什么必须每次都跑：OpenFOAM 不会因为网格差就拒绝计算，它会算，然后给你一个错误的结果或者中途发散。网格问题是初学者算例失败的头号原因，而 checkMesh 是唯一能在开算前发现它们的工具。</p>
<p>用法</p>
<pre><code>checkMesh [-allGeometry] [-allTopology] [-meshQuality] [-writeSets vtk] [-latestTime] [-region &lt;名&gt;] [-parallel]</code></pre>
<div class="table-scroll"><table>
<tr><th>选项</th><th>作用</th></tr>
<tr><td>-allGeometry / -allTopology</td><td>做全部几何/拓扑检查（默认只做基础检查）</td></tr>
<tr><td>-meshQuality</td><td>用 system/meshQualityDict 的阈值判定</td></tr>
<tr><td>-writeSets vtk</td><td>把有问题的单元/面导出成 VTK，可在 ParaView 里直接看到坏在哪</td></tr>
</table></div>
<p>示例与读法</p>
<pre><code>$ checkMesh -allGeometry -allTopology
...
Checking geometry...
    Max cell openness = 1.6e-16 OK.
    Max aspect ratio = 5.2 OK.
    Mesh non-orthogonality Max: 42.7 average: 8.6      ← 关注这个
    Max skewness = 1.8 OK.                             ← 和这个
Mesh OK.</code></pre>
<div class="table-scroll"><table>
<tr><th>指标</th><th>安全范围</th><th>超标了怎么办</th></tr>
<tr><td>non-orthogonality（非正交角）</td><td>&lt; 70 好；70–80 需处理；&gt; 80 危险</td><td>在 fvSolution 里加 nNonOrthogonalCorrectors 1~2，fvSchemes 的 laplacianSchemes 用 limited corrected 0.33</td></tr>
<tr><td>skewness（歪斜度）</td><td>&lt; 4</td><td>改网格，数值上没有好办法救</td></tr>
<tr><td>aspect ratio（纵横比）</td><td>&lt; 100（边界层区域可放宽）</td><td>检查边界层加密是否过分</td></tr>
<tr><td>negative volume（负体积）</td><td>必须为 0</td><td>网格是坏的，必须重建</td></tr>
</table></div>
<p>看到 ***Number of severely non-orthogonal faces: N 这种带 *** 的行，一定要处理，它是错误不是提示。</p>
<h4>6.6 renumberMesh —— 重排单元编号提速</h4>
<p>是什么：用 Cuthill-McKee 等算法重新编号单元，让相邻单元的编号也相邻。</p>
<p>为什么能提速：矩阵带宽变窄 → 缓存命中率提高。大网格上通常能省 10%–30% 的求解时间，代价只是几秒钟。大算例开跑前顺手跑一下，是性价比最高的优化。</p>
<pre><code>$ renumberMesh -overwrite
$ mpirun -np 8 renumberMesh -overwrite -parallel     # 并行网格也能做</code></pre>
<h4>6.7 transformPoints —— 缩放 / 平移 / 旋转网格</h4>
<pre><code>$ transformPoints -scale &#x27;(0.001 0.001 0.001)&#x27;          # mm → m
$ transformPoints -translate &#x27;(0 0 -0.5)&#x27;               # 平移
$ transformPoints -rotate-angle &#x27;((0 0 1) 30)&#x27;          # 绕 z 轴转 30°
$ transformPoints -rollPitchYaw &#x27;(0 10 0)&#x27;              # 按滚转/俯仰/偏航角</code></pre>
<p>最常见用途：从 CAD 导来的网格单位是毫米，用第一条命令一次性换算。注意它直接改 constant/polyMesh/points，是不可撤销的，做之前先备份或确认命令没写错。</p>
<h4>6.8 topoSet —— 造集合（cellSet / faceSet / pointSet / zone）</h4>
<p>是什么：按几何条件（盒子、球、圆柱、曲面内外）或拓扑关系挑出一批单元/面/点，命名保存。</p>
<p>为什么需要它：很多操作都要先”选中一部分网格”再作用：局部加密、设多孔介质区、加源项、造挡板、分区域。topoSet 就是 OpenFOAM 的”选择工具”。</p>
<pre><code>$ topoSet                       # 读 system/topoSetDict
$ topoSet -dict system/topoSetDict.refine
$ topoSet -constant             # 作用在 constant 时刻的网格上</code></pre>
<p>示例：选出一个盒子区域的单元，再转成 cellZone</p>
<pre><code>// system/topoSetDict
actions
(
    { name c0;  type cellSet;  action new;
      source boxToCell;  box (0 0 0) (0.1 0.1 0.1); }

    { name porousZone;  type cellZoneSet;  action new;
      source setToCellZone;  set c0; }
);</code></pre>
<p>cellSet 与 cellZone 的区别：Set 是临时的选择结果（存在 constant/polyMesh/sets/），Zone 是网格的正式组成部分（写进 constant/polyMesh/cellZones），求解器里的多孔介质、MRF、fvOptions 认的是 Zone。所以流程通常是”先 Set 后 Zone”。</p>
<p>常用 source 类型见第 17 章。</p>
<h4>6.9 setFields —— 分区域给初始场赋值</h4>
<p>是什么：把某个几何区域内的场设成指定值。溃坝算例里”左下角一柱水”就是它做出来的。</p>
<p>为什么不用手改 0/alpha.water：场文件里是按单元编号排列的几万个数，人手改不现实。setFields 让你用几何语言描述初始条件。</p>
<pre><code>$ setFields                     # 读 system/setFieldsDict</code></pre>
<p>完整示例（溃坝）</p>
<pre><code>$ cp -r $FOAM_TUTORIALS/multiphase/interFoam/laminar/damBreak/damBreak .
$ cd damBreak
$ ./Allrun.pre        # 或手动：
$ blockMesh
$ cp -r 0.orig 0      # ★ 先恢复干净的初始场
$ setFields
$ interFoam</code></pre>
<p>字典写法见第 17 章。</p>
<p>兄弟命令</p>
<div class="table-scroll"><table>
<tr><th>命令</th><th>作用</th><th>示例</th></tr>
<tr><td>setExprFields</td><td>用表达式给场赋值，比 setFields 灵活得多</td><td>setExprFields -field U -expression &quot;vector(4*pos().y()*(1-pos().y()),0,0)&quot;（抛物线入口）</td></tr>
<tr><td>setExprBoundaryFields</td><td>同上，但作用在边界上</td><td>给非均匀边界条件用</td></tr>
<tr><td>setAlphaField</td><td>按解析形状（球、平面）精确初始化相分数，界面处给出部分填充的体积分数</td><td>配合 interIsoFoam 做界面收敛性研究</td></tr>
</table></div>
<p>setExprFields 值得单独说一句：它让你不写代码就能给出解析初场（剪切层、涡、扰动），做验证算例时极其省事。表达式里可用 pos()（单元中心坐标）、vol()、time()、rand() 等。</p>
<h4>6.10 网格操作类命令一览</h4>
<div class="table-scroll"><table>
<tr><th>命令</th><th>作用</th><th>典型用法</th></tr>
<tr><td>createPatch</td><td>合并/拆分/新建边界 patch，把 cyclic 配对起来</td><td>createPatch -overwrite（读 system/createPatchDict）</td></tr>
<tr><td>mergeMeshes</td><td>把两套网格合成一套</td><td>mergeMeshes . ../otherCase -overwrite</td></tr>
<tr><td>stitchMesh</td><td>把两个 patch 缝合成内部面</td><td>stitchMesh -perfect patchA patchB -overwrite</td></tr>
<tr><td>mirrorMesh</td><td>按平面镜像网格</td><td>mirrorMesh -overwrite（读 mirrorMeshDict）</td></tr>
<tr><td>subsetMesh</td><td>只保留某个 cellSet 的网格</td><td>subsetMesh c0 -patch newPatch -overwrite</td></tr>
<tr><td>splitMeshRegions</td><td>按 cellZone 拆成多个 region</td><td>splitMeshRegions -cellZones -overwrite（共轭传热必用）</td></tr>
<tr><td>refineMesh</td><td>各向同性/指定方向加密</td><td>refineMesh -overwrite -dict system/refineMeshDict</td></tr>
<tr><td>createBaffles</td><td>在内部面上造零厚度挡板</td><td>createBaffles -overwrite（读 createBafflesDict）</td></tr>
<tr><td>checkMesh</td><td>见 6.5</td><td></td></tr>
<tr><td>polyDualMesh</td><td>生成对偶多面体网格</td><td>polyDualMesh 60 -overwrite</td></tr>
<tr><td>collapseEdges</td><td>折叠过短的边，修补差网格</td><td>collapseEdges -overwrite</td></tr>
<tr><td>moveDynamicMesh</td><td>只跑动网格运动，不解流场（检查运动设置）</td><td>moveDynamicMesh -checkAMI</td></tr>
<tr><td>zeroDimensionalMesh</td><td>生成单单元网格（做化学反应零维验证）</td><td>zeroDimensionalMesh</td></tr>
</table></div>
<h4>6.11 mapFields / mapFieldsPar —— 把结果映射到另一套网格</h4>
<p>是什么：把一个算例的场插值到另一个（网格不同的）算例上。</p>
<p>为什么需要它：粗网格先算到基本收敛，再把结果映射到细网格做初场，比细网格从均匀初场算快得多——尤其是稳态 RANS。</p>
<pre><code># 网格边界完全一致（只是加密）时用 -consistent
$ mapFields ../coarseCase -consistent -sourceTime latestTime

# 网格区域不一致时，需要 system/mapFieldsDict 指定 patch 对应关系
$ mapFields ../otherCase -sourceTime 0.5

# 并行算例用 mapFieldsPar（能直接处理 processor* 数据）
$ mpirun -np 8 mapFieldsPar ../coarseCase -consistent -sourceTime latestTime -parallel</code></pre>
<h4>6.12 网格转换命令（从其他软件导入）</h4>
<div class="table-scroll"><table>
<tr><th>命令</th><th>来源格式</th><th>示例</th></tr>
<tr><td>fluentMeshToFoam</td><td>Fluent .msh（2D/3D）</td><td>fluentMeshToFoam mesh.msh -writeZones -scale 0.001</td></tr>
<tr><td>fluent3DMeshToFoam</td><td>Fluent 3D .msh</td><td>fluent3DMeshToFoam mesh.msh</td></tr>
<tr><td>gmshToFoam</td><td>Gmsh .msh</td><td>gmshToFoam model.msh</td></tr>
<tr><td>ideasUnvToFoam</td><td>I-DEAS / Salome .unv</td><td>ideasUnvToFoam mesh.unv</td></tr>
<tr><td>cfx4ToFoam</td><td>CFX .geo</td><td>cfx4ToFoam mesh.geo</td></tr>
<tr><td>starToFoam / ccm26ToFoam</td><td>STAR-CD / STAR-CCM+</td><td>ccm26ToFoam mesh.ccm</td></tr>
<tr><td>ansysToFoam</td><td>ANSYS .ans</td><td>ansysToFoam mesh.ans -scale 0.001</td></tr>
<tr><td>plot3dToFoam</td><td>Plot3D</td><td>plot3dToFoam mesh.xyz</td></tr>
<tr><td>netgenNeutralToFoam</td><td>Netgen</td><td>netgenNeutralToFoam mesh.vol</td></tr>
<tr><td>kivaToFoam</td><td>KIVA</td><td>kivaToFoam</td></tr>
<tr><td>foamMeshToFluent</td><td>反向导出到 Fluent</td><td>foamMeshToFluent</td></tr>
<tr><td>foamToStarMesh</td><td>反向导出到 STAR</td><td>foamToStarMesh</td></tr>
</table></div>
<p>转换后必做三件事：① checkMesh 查质量；② 看 constant/polyMesh/boundary，把各 patch 的 type 改对（转换器常把所有边界都设成 patch，壁面必须改成 wall，否则壁面函数不起作用）；③ 确认单位（必要时 transformPoints -scale）。</p>
<h4>6.13 changeDictionary —— 批量改字典（适用于多区域算例）</h4>
<p>是什么：按规则批量修改字典条目，支持正则匹配 patch 名。</p>
<p>为什么需要它：共轭传热算例有 5 个区域、每个区域十几个 patch，手改要改上百处。</p>
<pre><code>$ changeDictionary -region solid          # 读 system/solid/changeDictionaryDict
$ changeDictionary -literalRE             # 关键字里的正则按字面处理</code></pre>
{% endraw %}