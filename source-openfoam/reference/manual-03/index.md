---
title: "03 前处理命令"
layout: reference
description: "前处理命令：用法与配置实例。"
cms_slug: "reference-manual-03"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>前处理依次完成几何处理、网格生成或导入、质量检查、区域划分及初始场设置。改变网格拓扑后，应同步检查场文件中的边界和区域。配置方法见第 7 至 9 章。</p>
<h3>3.1 网格生成与检查</h3>
<h2>checkFaMesh  检查有限面积网格  源码</h2>
<p>检查对象为有限面积网格。</p>
<p>用法：checkFaMesh [选项]</p>
<pre><code class="language-plaintext">示例：checkFaMesh</code></pre>
<h2>makeFaMesh  从体网格面生成有限面积网格  源码</h2>
<p>v2512 的常用字典位置为 system/finite-area/faMeshDefinition。</p>
<p>用法：makeFaMesh [-dict 文件]</p>
<pre><code class="language-plaintext">示例：makeFaMesh</code></pre>
<h2>PDRblockMesh  生成 PDR 专用直角单块网格  源码</h2>
<p>读取 PDRblockMeshDict。</p>
<p>用法：PDRblockMesh [-dict 文件]</p>
<pre><code class="language-plaintext">示例：PDRblockMesh</code></pre>
<h2>blockMesh  根据块拓扑生成六面体网格  源码</h2>
<p>读取 system/blockMeshDict，生成后使用 checkMesh 检查。</p>
<p>用法：blockMesh [-dict 文件] [-case 目录]</p>
<pre><code class="language-plaintext">示例：blockMesh</code></pre>
<h2>extrudeMesh  沿指定模型挤出网格或表面  源码</h2>
<p>读取 extrudeMeshDict。</p>
<p>用法：extrudeMesh [-dict 文件]</p>
<pre><code class="language-plaintext">示例：extrudeMesh</code></pre>
<h2>extrudeToRegionMesh  将面集合挤出为独立区域  源码</h2>
<p>用于薄层或膜区域，源面和目标区域名称由字典指定。</p>
<p>用法：extrudeToRegionMesh [-dict 文件]</p>
<pre><code class="language-plaintext">示例：extrudeToRegionMesh</code></pre>
<h2>extrude2DMesh  将二维网格挤出为三维网格  源码</h2>
<p>读取 system/extrude2DMeshDict。polyMesh2D 输入为仅含顶点和边的二维网格。</p>
<p>用法：extrude2DMesh polyMesh2D 或 MeshedSurface [选项]</p>
<pre><code class="language-plaintext">示例：extrude2DMesh polyMesh2D -overwrite</code></pre>
<h2>cellSizeAndAlignmentGrid  生成网格尺寸和方向辅助场  源码</h2>
<p>用于 foamyMesh 网格生成流程。</p>
<p>用法：cellSizeAndAlignmentGrid [选项]</p>
<pre><code class="language-plaintext">示例：cellSizeAndAlignmentGrid</code></pre>
<h2>foamyHexMesh  生成共形 Voronoi 体网格  源码</h2>
<p>读取 foamyHexMeshDict 和相关几何，运行需具备对应编译依赖。</p>
<p>用法：foamyHexMesh [选项]</p>
<pre><code class="language-plaintext">示例：foamyHexMesh</code></pre>
<h2>foamyHexMeshBackgroundMesh  生成 foamyHexMesh 背景网格  源码</h2>
<p>为 foamyHexMesh 提供背景网格。</p>
<p>用法：foamyHexMeshBackgroundMesh [选项]</p>
<pre><code class="language-plaintext">示例：foamyHexMeshBackgroundMesh</code></pre>
<h2>foamyHexMeshSurfaceSimplify  为 foamyHexMesh 简化表面  源码</h2>
<p>输出用于 triSurface 表面处理。</p>
<p>用法：foamyHexMeshSurfaceSimplify 输出表面名</p>
<pre><code class="language-plaintext">示例：foamyHexMeshSurfaceSimplify simplified.stl</code></pre>
<h2>foamyQuadMesh  生成以四边形为主的二维 Voronoi 网格  源码</h2>
<p>参数由专用字典定义，-pointsFile 可指定初始点。</p>
<p>用法：foamyQuadMesh [选项]</p>
<pre><code class="language-plaintext">示例：foamyQuadMesh</code></pre>
<h2>snappyHexMesh  细化背景网格并生成贴体网格和边界层  源码</h2>
<p>输入包括背景网格及 constant/triSurface 中的表面。并行运行通过 mpirun 启动，并使用 -parallel。</p>
<p>用法：snappyHexMesh [-dict 文件] [-overwrite]</p>
<pre><code class="language-plaintext">示例：snappyHexMesh -overwrite</code></pre>
<h2>checkMesh  检查网格拓扑和几何质量  源码</h2>
<p>-meshQuality 读取网格质量约束。</p>
<p>用法：checkMesh [选项]</p>
<pre><code class="language-plaintext">示例：checkMesh -allTopology -allGeometry</code></pre>
<h3>3.2 表面处理</h3>
<h2>surfaceAdd  合并表面数据  源码</h2>
<p>连接两个表面数据集，不执行几何布尔并集。</p>
<p>用法：surfaceAdd 表面1 表面2 输出</p>
<pre><code class="language-plaintext">示例：surfaceAdd a.stl b.stl combined.stl</code></pre>
<h2>surfaceBooleanFeatures  提取表面布尔运算特征线  源码</h2>
<p>支持 intersection、union 和 difference，相关构建可依赖 CGAL。</p>
<p>用法：surfaceBooleanFeatures 操作 表面1 表面2</p>
<pre><code class="language-plaintext">示例：surfaceBooleanFeatures intersection a.stl b.stl</code></pre>
<h2>surfaceCheck  检查表面网格闭合性和相交情况  源码</h2>
<p>用于检查 snappyHexMesh 等工具的输入表面。</p>
<p>用法：surfaceCheck 表面文件 [选项]</p>
<pre><code class="language-plaintext">示例：surfaceCheck constant/triSurface/body.stl -checkSelfIntersection</code></pre>
<h2>surfaceClean  清理短边及低质量三角形  源码</h2>
<p>长度和质量阈值按几何尺度设置；清理会改变局部表面细节。</p>
<p>用法：surfaceClean 输入 最短边 最低质量 输出</p>
<pre><code class="language-plaintext">示例：surfaceClean body.stl 1e-6 0.01 bodyClean.stl</code></pre>
<h2>surfaceCoarsen  简化表面三角网格  源码</h2>
<p>简化因子取值范围为 [0,1)，简化后检查几何完整性。</p>
<p>用法：surfaceCoarsen 输入 简化因子 输出</p>
<pre><code class="language-plaintext">示例：surfaceCoarsen body.stl 0.5 coarse.stl</code></pre>
<h2>surfaceConvert  转换三角表面文件格式  源码</h2>
<p>-scale 指定几何缩放系数，按输入与输出长度单位换算。</p>
<p>用法：surfaceConvert 输入 输出 [选项]</p>
<pre><code class="language-plaintext">示例：surfaceConvert body.obj body.stl</code></pre>
<h2>surfaceFeatureConvert  转换边线和特征线文件格式  源码</h2>
<p>输入和输出采用该程序支持的边线格式。</p>
<p>用法：surfaceFeatureConvert 输入 输出</p>
<pre><code class="language-plaintext">示例：surfaceFeatureConvert body.eMesh body.obj</code></pre>
<h2>surfaceFeatureExtract  提取几何表面特征线  源码</h2>
<p>读取 surfaceFeatureExtractDict，生成 eMesh 等特征文件。</p>
<p>用法：surfaceFeatureExtract [-dict 文件]</p>
<pre><code class="language-plaintext">示例：surfaceFeatureExtract</code></pre>
<h2>surfaceFind  按坐标查询表面信息  源码</h2>
<p>用于定位和检查表面坐标。</p>
<p>用法：surfaceFind 输入 [-x X] [-y Y] [-z Z]</p>
<pre><code class="language-plaintext">示例：surfaceFind body.stl -x 0.1</code></pre>
<h2>surfaceHookUp  按容差连接表面  源码</h2>
<p>连接规则和输入表面由相应字典指定。</p>
<p>用法：surfaceHookUp 连接容差 [-dict 文件]</p>
<pre><code class="language-plaintext">示例：surfaceHookUp 1e-5</code></pre>
<h2>surfaceInertia  计算封闭表面的惯性参数  源码</h2>
<p>按选项采用实体或薄壳模型，密度单位与几何长度单位保持一致。</p>
<p>用法：surfaceInertia 输入 [选项]</p>
<pre><code class="language-plaintext">示例：surfaceInertia body.stl -density 1000</code></pre>
<h2>surfaceInflate  沿法向膨胀表面  源码</h2>
<p>安全因子范围为 [1,10]，膨胀后检查表面自相交。</p>
<p>用法：surfaceInflate 输入 距离 安全因子</p>
<pre><code class="language-plaintext">示例：surfaceInflate body.stl 0.001 2</code></pre>
<h2>surfaceLambdaMuSmooth  采用 lambda mu 算法平滑表面  源码</h2>
<p>lambda 和 mu 均采用该程序定义的 [0,1] 系数。</p>
<p>用法：surfaceLambdaMuSmooth 输入 lambda mu 迭代数 输出</p>
<pre><code class="language-plaintext">示例：surfaceLambdaMuSmooth body.stl 0.5 0.5 10 smooth.stl</code></pre>
<h2>surfaceMeshConvert  转换 surfaceMesh 格式和坐标  源码</h2>
<p>采用 surfaceMesh 读写接口。</p>
<p>用法：surfaceMeshConvert 输入 输出 [选项]</p>
<pre><code class="language-plaintext">示例：surfaceMeshConvert body.obj body.stl</code></pre>
<h2>surfaceMeshExport  导出算例中的 surfaceMesh  源码</h2>
<p>输入为算例中已有的 surfaceMesh。</p>
<p>用法：surfaceMeshExport 输出 [选项]</p>
<pre><code class="language-plaintext">示例：surfaceMeshExport body.obj</code></pre>
<h2>surfaceMeshExtract  提取体网格边界表面  源码</h2>
<p>-patches 指定网格中已有的边界名称。</p>
<p>用法：surfaceMeshExtract 输出 [选项]</p>
<pre><code class="language-plaintext">示例：surfaceMeshExtract walls.stl -patches '(walls)'</code></pre>
<h2>surfaceMeshImport  导入表面至算例的 surfaceMesh  源码</h2>
<p>导入对象为表面网格，-name 指定名称。</p>
<p>用法：surfaceMeshImport 输入 [选项]</p>
<pre><code class="language-plaintext">示例：surfaceMeshImport body.stl</code></pre>
<h2>surfaceMeshInfo  输出表面网格统计信息  源码</h2>
<p>-areas 输出面积统计，可用于核查几何尺度。</p>
<p>用法：surfaceMeshInfo 输入 [选项]</p>
<pre><code class="language-plaintext">示例：surfaceMeshInfo body.stl -areas</code></pre>
<h2>surfaceOrient  统一表面法向  源码</h2>
<p>默认按物体外部观察点定向，-inside 将指定点按内部点处理。</p>
<p>用法：surfaceOrient 输入 外部点 输出</p>
<pre><code class="language-plaintext">示例：surfaceOrient body.stl '(10 10 10)' bodyOriented.stl</code></pre>
<h2>surfacePatch  按几何规则重划表面区域  源码</h2>
<p>读取 surfacePatchDict。</p>
<p>用法：surfacePatch [-dict 文件]</p>
<pre><code class="language-plaintext">示例：surfacePatch</code></pre>
<h2>surfacePointMerge  按距离阈值合并表面点  源码</h2>
<p>距离阈值采用表面坐标的长度单位。</p>
<p>用法：surfacePointMerge 输入 距离 输出</p>
<pre><code class="language-plaintext">示例：surfacePointMerge body.stl 1e-6 merged.stl</code></pre>
<h2>surfaceRedistributePar  并行重分配三角表面  源码</h2>
<p>示例采用 4 个进程，并读取 constant/triSurface/body.stl。分配方式包括 follow、independent、distributed 和 frozen；follow 按网格包围盒划分。</p>
<p>用法：surfaceRedistributePar 表面名 分配方式 -parallel</p>
<pre><code class="language-plaintext">示例：mpirun -np 4 surfaceRedistributePar body.stl follow -parallel</code></pre>
<h2>surfaceRefineRedGreen  采用红绿细分加密三角表面  源码</h2>
<p>-steps 指定细分次数。</p>
<p>用法：surfaceRefineRedGreen 输入 输出 [-steps N]</p>
<pre><code class="language-plaintext">示例：surfaceRefineRedGreen body.stl fine.stl -steps 1</code></pre>
<h2>surfaceSplitByPatch  按区域拆分表面文件  源码</h2>
<p>-patches 指定待拆分区域。</p>
<p>用法：surfaceSplitByPatch 输入 [选项]</p>
<pre><code class="language-plaintext">示例：surfaceSplitByPatch body.stl</code></pre>
<h2>surfaceSplitByTopology  按连通关系拆分表面  源码</h2>
<p>用于分离拓扑不连通的部件。</p>
<p>用法：surfaceSplitByTopology 输入 输出</p>
<pre><code class="language-plaintext">示例：surfaceSplitByTopology body.stl split.stl</code></pre>
<h2>surfaceSplitNonManifolds  拆分表面非流形连接  源码</h2>
<p>拆分后使用 surfaceCheck 检查表面。</p>
<p>用法：surfaceSplitNonManifolds 输入 输出</p>
<pre><code class="language-plaintext">示例：surfaceSplitNonManifolds body.stl manifold.stl</code></pre>
<h2>surfaceSubset  按字典选取表面子集  源码</h2>
<p>选择规则由输入字典定义。</p>
<p>用法：surfaceSubset 字典 输入 输出</p>
<pre><code class="language-plaintext">示例：surfaceSubset system/surfaceSubsetDict body.stl subset.stl</code></pre>
<h2>surfaceToPatch  按给定表面重划体网格边界  源码</h2>
<p>修改后同步检查场文件中的边界条目。</p>
<p>用法：surfaceToPatch 表面文件 [选项]</p>
<pre><code class="language-plaintext">示例：surfaceToPatch body.stl</code></pre>
<h2>surfaceTransformPoints  对表面进行平移旋转和缩放  源码</h2>
<p>-read-scale 和 -write-scale 分别指定读取和写出时的缩放系数。</p>
<p>用法：surfaceTransformPoints [选项] 输入 输出</p>
<pre><code class="language-plaintext">示例：surfaceTransformPoints -translate '(0 0 1)' body.stl bodyMoved.stl</code></pre>
<h3>3.3 网格转换</h3>
<h2>ansysToFoam  导入 ANSYS 网格输入文件  源码</h2>
<p>输入采用转换器支持的 ANSYS 文件格式。</p>
<p>用法：ansysToFoam ANSYS文件</p>
<pre><code class="language-plaintext">示例：ansysToFoam mesh.ans</code></pre>
<h2>ccmToFoam  导入 CCM 网格及数据  源码</h2>
<p>需编译 CCM 支持。-list 列出文件内容，移除该选项后执行转换。</p>
<p>用法：ccmToFoam 输入.ccm [选项]</p>
<pre><code class="language-plaintext">示例：ccmToFoam mesh.ccm -list</code></pre>
<h2>foamToCcm  导出 CCM 网格或结果  源码</h2>
<p>需编译 CCM 库支持。</p>
<p>用法：foamToCcm [选项]</p>
<pre><code class="language-plaintext">示例：foamToCcm</code></pre>
<h2>cfx4ToFoam  导入 CFX4 几何网格  源码</h2>
<p>-scale 指定长度缩放系数。</p>
<p>用法：cfx4ToFoam CFX几何文件 [选项]</p>
<pre><code class="language-plaintext">示例：cfx4ToFoam mesh.geo</code></pre>
<h2>datToFoam  导入特定 DAT 网格格式  源码</h2>
<p>输入内容须符合该转换器定义的 DAT 网格结构。</p>
<p>用法：datToFoam DAT文件</p>
<pre><code class="language-plaintext">示例：datToFoam mesh.dat</code></pre>
<h2>ensightToFoam  导入 EnSight 几何网格  源码</h2>
<p>转换范围为几何网格，物理模型在目标算例中配置。</p>
<p>用法：ensightToFoam 几何.geo [选项]</p>
<pre><code class="language-plaintext">示例：ensightToFoam mesh.geo</code></pre>
<h2>fireToFoam  导入 AVL FIRE 多面体网格  源码</h2>
<p>转换后检查长度单位。</p>
<p>用法：fireToFoam FIRE网格 [选项]</p>
<pre><code class="language-plaintext">示例：fireToFoam mesh.fpma</code></pre>
<h2>fluent3DMeshToFoam  导入 Fluent 三维网格  源码</h2>
<p>用于 Fluent 三维网格的专用转换，按输入格式选择。</p>
<p>用法：fluent3DMeshToFoam 网格.msh</p>
<pre><code class="language-plaintext">示例：fluent3DMeshToFoam mesh.msh</code></pre>
<h2>fluentMeshToFoam  导入 Fluent 网格  源码</h2>
<p>输入采用 Fluent mesh 格式；Gmsh 文件使用 gmshToFoam 转换。</p>
<p>用法：fluentMeshToFoam 网格.msh</p>
<pre><code class="language-plaintext">示例：fluentMeshToFoam mesh.msh</code></pre>
<h2>foamMeshToFluent  导出 Fluent 格式网格  源码</h2>
<p>导出范围为网格数据，求解配置在 Fluent 中设置。</p>
<p>用法：foamMeshToFluent [选项]</p>
<pre><code class="language-plaintext">示例：foamMeshToFluent</code></pre>
<h2>foamToFireMesh  导出 AVL FIRE 网格  源码</h2>
<p>-scale 指定长度缩放系数。</p>
<p>用法：foamToFireMesh [选项]</p>
<pre><code class="language-plaintext">示例：foamToFireMesh</code></pre>
<h2>foamToStarMesh  导出 STARCD PROSTAR 网格  源码</h2>
<p>输出 bnd、cel 和 vrt 等文件。</p>
<p>用法：foamToStarMesh [选项]</p>
<pre><code class="language-plaintext">示例：foamToStarMesh</code></pre>
<h2>foamToSurface  将体网格边界导出为表面文件  源码</h2>
<p>用于几何检查及外部软件数据交换。</p>
<p>用法：foamToSurface 输出 [选项]</p>
<pre><code class="language-plaintext">示例：foamToSurface boundary.stl</code></pre>
<h2>gambitToFoam  导入 GAMBIT 中性网格  源码</h2>
<p>转换后运行 checkMesh。</p>
<p>用法：gambitToFoam 中性网格文件</p>
<pre><code class="language-plaintext">示例：gambitToFoam mesh.neu</code></pre>
<h2>gmshToFoam  导入 Gmsh 网格  源码</h2>
<p>常用输入为 ASCII MSH2。转换后检查物理组与边界名称。</p>
<p>用法：gmshToFoam 网格.msh</p>
<pre><code class="language-plaintext">示例：gmshToFoam mesh.msh</code></pre>
<h2>ideasUnvToFoam  导入 I-DEAS 通用网格  源码</h2>
<p>转换后检查边界、长度单位和单元类型。</p>
<p>用法：ideasUnvToFoam 网格.unv</p>
<pre><code class="language-plaintext">示例：ideasUnvToFoam mesh.unv</code></pre>
<h2>kivaToFoam  导入 KIVA3v 网格  源码</h2>
<p>输入为 KIVA3v 发动机网格。</p>
<p>用法：kivaToFoam [-file 文件] [-version 版本]</p>
<pre><code class="language-plaintext">示例：kivaToFoam -file otape17</code></pre>
<h2>mshToFoam  导入该转换器支持的 MSH 网格  源码</h2>
<p>输入须符合该转换器定义的 MSH 结构；Gmsh 网格使用 gmshToFoam。</p>
<p>用法：mshToFoam 输入.msh</p>
<pre><code class="language-plaintext">示例：mshToFoam mesh.msh</code></pre>
<h2>netgenNeutralToFoam  导入 Netgen 中性网格  源码</h2>
<p>转换后检查边界划分。</p>
<p>用法：netgenNeutralToFoam 中性网格文件</p>
<pre><code class="language-plaintext">示例：netgenNeutralToFoam mesh.neutral</code></pre>
<h2>plot3dToFoam  导入 PLOT3D 块网格  源码</h2>
<p>-singleBlock 和 -2D 等选项用于指定输入网格形式。</p>
<p>用法：plot3dToFoam 几何文件 [选项]</p>
<pre><code class="language-plaintext">示例：plot3dToFoam mesh.xyz</code></pre>
<h2>star4ToFoam  导入 PROSTAR v4 网格  源码</h2>
<p>按文件名前缀读取 mesh.vrt、mesh.cel 等配套文件。</p>
<p>用法：star4ToFoam 文件名前缀</p>
<pre><code class="language-plaintext">示例：star4ToFoam mesh</code></pre>
<h2>tetgenToFoam  导入 TetGen 网格  源码</h2>
<p>按前缀读取配套的 node、ele 和 face 等文件。</p>
<p>用法：tetgenToFoam 文件名前缀</p>
<pre><code class="language-plaintext">示例：tetgenToFoam mesh</code></pre>
<h2>vtkUnstructuredToFoam  导入旧式 ASCII 非结构 VTK 网格  源码</h2>
<p>输入采用旧式 ASCII VTK 格式。</p>
<p>用法：vtkUnstructuredToFoam 输入.vtk</p>
<pre><code class="language-plaintext">示例：vtkUnstructuredToFoam mesh.vtk</code></pre>
<h2>writeMeshObj  将网格几何信息导出为 OBJ  源码</h2>
<p>-cell、-face、-point 和 -cellSet 等选项指定诊断对象。</p>
<p>用法：writeMeshObj [选项]</p>
<pre><code class="language-plaintext">示例：writeMeshObj -cell 10</code></pre>
<h3>3.4 网格修改及区域选择</h3>
<h2>PDRMesh  为 PDR 模型准备网格和区域  源码</h2>
<p>输入包括 blockedCells、blockedFaces 等集合。</p>
<p>用法：PDRMesh [选项]</p>
<pre><code class="language-plaintext">示例：PDRMesh</code></pre>
<h2>collapseEdges  按字典折叠短边和低质量面  源码</h2>
<p>读取 collapseDict 或指定字典，折叠操作可改变网格拓扑。</p>
<p>用法：collapseEdges [-dict 文件]</p>
<pre><code class="language-plaintext">示例：collapseEdges</code></pre>
<h2>combinePatchFaces  合并近共面的边界面  源码</h2>
<p>通过 concaveAngle 及质量约束控制合并。</p>
<p>用法：combinePatchFaces 特征角 [选项]</p>
<pre><code class="language-plaintext">示例：combinePatchFaces 5 -overwrite</code></pre>
<h2>modifyMesh  移动拆分或折叠网格元素  源码</h2>
<p>按配置字典执行拓扑修改。</p>
<p>用法：modifyMesh [-dict 文件]</p>
<pre><code class="language-plaintext">示例：modifyMesh</code></pre>
<h2>refineHexMesh  加密指定六面体集合  源码</h2>
<p>待细化集合可通过 topoSet 建立。</p>
<p>用法：refineHexMesh cellSet [选项]</p>
<pre><code class="language-plaintext">示例：refineHexMesh refineCells -overwrite</code></pre>
<h2>refineWallLayer  细化近壁网格  源码</h2>
<p>输入比例指定边的细分位置。</p>
<p>用法：refineWallLayer patch列表 边比例 [选项]</p>
<pre><code class="language-plaintext">示例：refineWallLayer '(walls)' 0.3 -overwrite</code></pre>
<h2>refinementLevel  估计笛卡尔网格细化级别  源码</h2>
<p>用于贴体变形前的网格。</p>
<p>用法：refinementLevel [选项]</p>
<pre><code class="language-plaintext">示例：refinementLevel</code></pre>
<h2>removeFaces  删除指定面集合中的面  源码</h2>
<p>输入为预先建立的 faceSet。</p>
<p>用法：removeFaces faceSet [选项]</p>
<pre><code class="language-plaintext">示例：removeFaces removeFacesSet</code></pre>
<h2>selectCells  按表面选取内部外部或相交单元  源码</h2>
<p>读取选择字典，生成 selected 集合。</p>
<p>用法：selectCells [选项]</p>
<pre><code class="language-plaintext">示例：selectCells</code></pre>
<h2>snappyRefineMesh  在表面附近加密体网格  源码</h2>
<p>输入为待处理表面及细化字典。</p>
<p>用法：snappyRefineMesh [选项]</p>
<pre><code class="language-plaintext">示例：snappyRefineMesh</code></pre>
<h2>splitCells  按边角度拆分单元  源码</h2>
<p>用于网格单元的拓扑修复。</p>
<p>用法：splitCells 边角度 [选项]</p>
<pre><code class="language-plaintext">示例：splitCells 90</code></pre>
<h2>attachMesh  通过网格修改器连接分离网格  源码</h2>
<p>用于相应的拓扑连接流程。</p>
<p>用法：attachMesh [选项]</p>
<pre><code class="language-plaintext">示例：attachMesh</code></pre>
<h2>autoPatch  按面夹角自动划分边界  源码</h2>
<p>重划边界后更新对应场边界。</p>
<p>用法：autoPatch 特征角 [选项]</p>
<pre><code class="language-plaintext">示例：autoPatch 45 -overwrite</code></pre>
<h2>createBaffles  将内部面转换为成对边界  源码</h2>
<p>读取 createBafflesDict。边界面生成与点拆分属于不同操作。</p>
<p>用法：createBaffles [-dict 文件] [-overwrite]</p>
<pre><code class="language-plaintext">示例：createBaffles -overwrite</code></pre>
<h2>createPatch  创建或重组网格边界  源码</h2>
<p>读取 createPatchDict，修改后使场边界与新网格对应。</p>
<p>用法：createPatch [-dict 文件] [-overwrite]</p>
<pre><code class="language-plaintext">示例：createPatch -overwrite</code></pre>
<h2>deformedGeom  按位移场生成缩放后的变形几何  源码</h2>
<p>输入为已有位移结果场。</p>
<p>用法：deformedGeom 缩放倍数</p>
<pre><code class="language-plaintext">示例：deformedGeom 1</code></pre>
<h2>flattenMesh  压平二维网格前后平面  源码</h2>
<p>适用于相应的二维笛卡尔网格。</p>
<p>用法：flattenMesh [选项]</p>
<pre><code class="language-plaintext">示例：flattenMesh</code></pre>
<h2>insideCells  选取封闭表面内部单元  源码</h2>
<p>输入表面应具备明确的内外区域。</p>
<p>用法：insideCells 表面文件 cellSet</p>
<pre><code class="language-plaintext">示例：insideCells body.stl innerCells</code></pre>
<h2>mergeMeshes  合并两个算例网格  源码</h2>
<p>接合处需共形连接时，合并后继续执行缝合。</p>
<p>用法：mergeMeshes 主算例 附加算例 [选项]</p>
<pre><code class="language-plaintext">示例：mergeMeshes ./mainCase ./extraCase -overwrite</code></pre>
<h2>mergeOrSplitBaffles  检测合并或拆分挡板面  源码</h2>
<p>-detectOnly 执行检测，-split 执行拆分。</p>
<p>用法：mergeOrSplitBaffles [选项]</p>
<pre><code class="language-plaintext">示例：mergeOrSplitBaffles -detectOnly</code></pre>
<h2>mirrorMesh  按平面对称复制网格  源码</h2>
<p>读取 mirrorMeshDict。</p>
<p>用法：mirrorMesh [-dict 文件]</p>
<pre><code class="language-plaintext">示例：mirrorMesh</code></pre>
<h2>moveDynamicMesh  执行网格运动  源码</h2>
<p>读取 dynamicMeshDict，可用于独立检查网格运动过程。</p>
<p>用法：moveDynamicMesh [选项]</p>
<pre><code class="language-plaintext">示例：moveDynamicMesh</code></pre>
<h2>moveEngineMesh  执行发动机网格运动  源码</h2>
<p>读取发动机网格及运动设置。</p>
<p>用法：moveEngineMesh [选项]</p>
<pre><code class="language-plaintext">示例：moveEngineMesh</code></pre>
<h2>moveMesh  求解网格运动  源码</h2>
<p>输入包括网格运动方程及边界条件。</p>
<p>用法：moveMesh [-deltaT 值] [-endTime 值]</p>
<pre><code class="language-plaintext">示例：moveMesh -deltaT 0.01 -endTime 1</code></pre>
<h2>objToVTK  将 OBJ 线文件转成 VTK  源码</h2>
<p>用于线几何可视化。</p>
<p>用法：objToVTK 输入.obj 输出.vtk</p>
<pre><code class="language-plaintext">示例：objToVTK edges.obj edges.vtk</code></pre>
<h2>orientFaceZone  按外部参考点统一面区域方向  源码</h2>
<p>面方向用于通量计算及挡板处理。</p>
<p>用法：orientFaceZone faceZone 外部点</p>
<pre><code class="language-plaintext">示例：orientFaceZone interface '(10 0 0)'</code></pre>
<h2>polyDualMesh  生成多面体对偶网格  源码</h2>
<p>生成后检查网格拓扑及场映射。</p>
<p>用法：polyDualMesh 特征角 [选项]</p>
<pre><code class="language-plaintext">示例：polyDualMesh 60 -overwrite</code></pre>
<h2>refineMesh  全局或按集合定向加密体网格  源码</h2>
<p>缺少 refineMeshDict 时可执行全域细化。</p>
<p>用法：refineMesh [-dict 文件] [-overwrite]</p>
<pre><code class="language-plaintext">示例：refineMesh -overwrite</code></pre>
<h2>renumberMesh  重排网格编号以降低矩阵带宽  源码</h2>
<p>-write-maps 输出新旧编号映射，供外部编号关联使用。</p>
<p>用法：renumberMesh [选项]</p>
<pre><code class="language-plaintext">示例：renumberMesh -overwrite</code></pre>
<h2>rotateMesh  按两个方向向量旋转网格  源码</h2>
<p>与几何方向关联的场和参数应同步检查。</p>
<p>用法：rotateMesh 起始向量 目标向量</p>
<pre><code class="language-plaintext">示例：rotateMesh '(1 0 0)' '(0 1 0)'</code></pre>
<h2>setSet  交互编辑单元面和点集合  源码</h2>
<p>批处理文件逐行定义集合操作。</p>
<p>用法：setSet [-batch 文件]</p>
<pre><code class="language-plaintext">示例：setSet -batch system/sets.batch</code></pre>
<h2>setsToZones  将集合转换为同名网格区域  源码</h2>
<p>转换面集合时需处理面方向信息。</p>
<p>用法：setsToZones [选项]</p>
<pre><code class="language-plaintext">示例：setsToZones</code></pre>
<h2>singleCellMesh  构建保留边界数据的单单元网格  源码</h2>
<p>用于边界数据处理。</p>
<p>用法：singleCellMesh [选项]</p>
<pre><code class="language-plaintext">示例：singleCellMesh</code></pre>
<h2>splitMesh  按面集合生成成对边界  源码</h2>
<p>输入为预先建立的 cutFaces 等面集合。</p>
<p>用法：splitMesh faceSet 主patch 从patch</p>
<pre><code class="language-plaintext">示例：splitMesh cutFaces sideA sideB</code></pre>
<h2>splitMeshRegions  按连通性或 cellZone 拆分网格区域  源码</h2>
<p>各目标区域分别配置字典和场文件。</p>
<p>用法：splitMeshRegions [选项]</p>
<pre><code class="language-plaintext">示例：splitMeshRegions -cellZones -overwrite</code></pre>
<h2>stitchMesh  缝合两个网格边界  源码</h2>
<p>-perfect 要求几何匹配；其余接口可按相应条件采用 -partial 或 -integral。</p>
<p>用法：stitchMesh [选项] 主patch 从patch</p>
<pre><code class="language-plaintext">示例：stitchMesh -perfect sideA sideB -overwrite</code></pre>
<h2>subsetMesh  提取指定单元集合或区域的子网格  源码</h2>
<p>默认读取已有单元集合，如 fluidCells；-zone 改为选择 cellZone。</p>
<p>用法：subsetMesh 选择名 [选项]</p>
<pre><code class="language-plaintext">示例：subsetMesh fluidCells -overwrite</code></pre>
<h2>topoSet  按规则创建或修改集合及区域  源码</h2>
<p>读取 topoSetDict，按 type 选择 cellSet、cellZoneSet 等对象。</p>
<p>用法：topoSet [-dict 文件]</p>
<pre><code class="language-plaintext">示例：topoSet</code></pre>
<h2>transformPoints  对体网格进行平移旋转和缩放  源码</h2>
<p>示例将毫米坐标换算为米。外部源项位置和参考点需同步换算。</p>
<p>用法：transformPoints 变换选项</p>
<pre><code class="language-plaintext">示例：transformPoints -scale '(0.001 0.001 0.001)'</code></pre>
<h2>zipUpMesh  修复悬挂顶点引起的单元不闭合  源码</h2>
<p>适用于网格转换产生的相应拓扑缺陷。</p>
<p>用法：zipUpMesh [选项]</p>
<pre><code class="language-plaintext">示例：zipUpMesh</code></pre>
<h3>3.5 初始化与映射</h3>
<h2>PDRsetFields  生成 PDRFoam 所需初始场  源码</h2>
<p>输入为 PDR 阻塞模型等专用数据。</p>
<p>用法：PDRsetFields [-dict 文件]</p>
<pre><code class="language-plaintext">示例：PDRsetFields</code></pre>
<h2>applyBoundaryLayer  按七分之一次方律设置边界层初值  源码</h2>
<p>用于符合该速度分布近似的初始场设置。</p>
<p>用法：applyBoundaryLayer [-ybl 厚度] [-writeTurbulenceFields]</p>
<pre><code class="language-plaintext">示例：applyBoundaryLayer -ybl 0.01</code></pre>
<h2>boxTurb  生成给定能谱的无散度湍流盒  源码</h2>
<p>通过专用配置指定湍流能谱。</p>
<p>用法：boxTurb [选项]</p>
<pre><code class="language-plaintext">示例：boxTurb</code></pre>
<h2>changeDictionary  批量修改场和边界条目  源码</h2>
<p>读取 changeDictionaryDict，并将替换结果写回文件。</p>
<p>用法：changeDictionary [-dict 文件]</p>
<pre><code class="language-plaintext">示例：changeDictionary</code></pre>
<h2>createBoxTurb  生成各向同性合成湍流盒  源码</h2>
<p>按配套配置生成湍流盒，并可输出 blockMesh 输入。</p>
<p>用法：createBoxTurb [选项]</p>
<pre><code class="language-plaintext">示例：createBoxTurb -createBlockMesh</code></pre>
<h2>createExternalCoupledPatchGeometry  输出外部耦合边界几何  源码</h2>
<p>组名和通信目录与耦合配置对应。</p>
<p>用法：createExternalCoupledPatchGeometry patch组 [选项]</p>
<pre><code class="language-plaintext">示例：createExternalCoupledPatchGeometry coupledWalls</code></pre>
<h2>createViewFactors  生成辐射视角因子  源码</h2>
<p>读取 constant/viewFactorsDict 等辐射配置。</p>
<p>用法：createViewFactors [选项]</p>
<pre><code class="language-plaintext">示例：createViewFactors</code></pre>
<h2>createZeroDirectory  按模板创建初始场  源码</h2>
<p>按 solver、boundary 等配置生成初始目录和场文件。</p>
<p>用法：createZeroDirectory [-templateDir 目录]</p>
<pre><code class="language-plaintext">示例：createZeroDirectory</code></pre>
<h2>dsmcInitialise  初始化 DSMC 粒子算例  源码</h2>
<p>读取 system/dsmcInitialise。</p>
<p>用法：dsmcInitialise [选项]</p>
<pre><code class="language-plaintext">示例：dsmcInitialise</code></pre>
<h2>engineSwirl  生成发动机旋流初场  源码</h2>
<p>读取发动机几何及旋流参数。</p>
<p>用法：engineSwirl [选项]</p>
<pre><code class="language-plaintext">示例：engineSwirl</code></pre>
<h2>faceAgglomerate  聚合辐射边界面并输出映射  源码</h2>
<p>用于视角因子计算的前处理。</p>
<p>用法：faceAgglomerate [-dict 文件]</p>
<pre><code class="language-plaintext">示例：faceAgglomerate</code></pre>
<h2>mapFields  将源算例场映射至目标算例  源码</h2>
<p>-consistent 适用于边界拓扑匹配的情形；边界不一致时配置 mapFieldsDict。</p>
<p>用法：mapFields 源算例 [选项]</p>
<pre><code class="language-plaintext">示例：mapFields ../coarseCase -sourceTime latestTime -consistent</code></pre>
<h2>mapFieldsPar  执行并行算例场映射  源码</h2>
<p>通过 mpirun 启动，并添加 -parallel。其参数按自身接口设置。</p>
<p>用法：mapFieldsPar 源算例 [选项]</p>
<pre><code class="language-plaintext">示例：mapFieldsPar ../sourceCase -sourceTime latestTime -consistent</code></pre>
<h2>mdInitialise  初始化分子动力学算例  源码</h2>
<p>读取分子动力学初值字典。</p>
<p>用法：mdInitialise [选项]</p>
<pre><code class="language-plaintext">示例：mdInitialise</code></pre>
<h2>writeMorpherCPs  导出 NURBS 变形控制点  源码</h2>
<p>读取 dynamicMeshDict 中的 NURBS3DVolume 配置。</p>
<p>用法：writeMorpherCPs [选项]</p>
<pre><code class="language-plaintext">示例：writeMorpherCPs</code></pre>
<h2>setAlphaField  按几何切割设置体积分数  源码</h2>
<p>可用于平面、球面和圆柱面等界面的初始化。</p>
<p>用法：setAlphaField [-dict 文件]</p>
<pre><code class="language-plaintext">示例：setAlphaField</code></pre>
<h2>setExprBoundaryFields  按表达式设置边界场  源码</h2>
<p>读取边界表达式字典，-backup 保留原场。</p>
<p>用法：setExprBoundaryFields [-dict 文件]</p>
<pre><code class="language-plaintext">示例：setExprBoundaryFields</code></pre>
<h2>setExprFields  按表达式设置体场  源码</h2>
<p>示例修改已有 T 场；采用 -create 新建场时需设置 dimensions。</p>
<p>用法：setExprFields [-dict 文件] 或表达式选项</p>
<pre><code class="language-plaintext">示例：setExprFields -field T -expression '300 + 10*pos().x()'</code></pre>
<h2>setFields  按几何区域初始化场  源码</h2>
<p>读取 setFieldsDict，通常在网格生成后、分区前执行。</p>
<p>用法：setFields [-dict 文件]</p>
<pre><code class="language-plaintext">示例：setFields</code></pre>
<h2>setTurbulenceFields  按经验关系初始化湍流量  源码</h2>
<p>模型和场名采用所用求解器的定义。</p>
<p>用法：setTurbulenceFields [-dict 文件]</p>
<pre><code class="language-plaintext">示例：setTurbulenceFields</code></pre>
<h2>smoothSurfaceData  平滑表面数据字段  源码</h2>
<p>输入采用程序支持的表面数据格式。</p>
<p>用法：smoothSurfaceData 输入 [选项]</p>
<pre><code class="language-plaintext">示例：smoothSurfaceData sample.vtp -radius 0.01</code></pre>
<h2>viewFactorsGen  采用面积和线积分生成视角因子  源码</h2>
<p>参数由对应辐射模型及字典定义。</p>
<p>用法：viewFactorsGen [选项]</p>
<pre><code class="language-plaintext">示例：viewFactorsGen</code></pre>
<h2>wallFunctionTable  生成表格式壁面函数数据  源码</h2>
<p>由字典指定壁面模型及数据范围。</p>
<p>用法：wallFunctionTable [选项]</p>
<pre><code class="language-plaintext">示例：wallFunctionTable</code></pre>
