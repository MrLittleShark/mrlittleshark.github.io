---
title: "snappyHexMesh 原理"
layout: "lesson"
lesson_id: 9
stage: 3
description: "前提：背景网格 blockMesh + 水密 STL + surfaceFeatures 特征线提取；②castellation：refinementSurfaces / refinementRegions / 细化层级 / locationInMesh；③snap：贴体迭代、特征线捕捉、nSmoothPatch / tolerance / nSolveIter；④addLayers：expansionRatio、finalLayerThickness、minThickness、relativeSizes 与覆盖率；⑤meshQualityControls 在三个阶段中的作用。"
---
{% raw %}
<section class="lesson-intro"><h2>本讲学习任务</h2><p>①前提：背景网格 blockMesh + 水密 STL + surfaceFeatures 特征线提取；②castellation：refinementSurfaces / refinementRegions / 细化层级 / locationInMesh；③snap：贴体迭代、特征线捕捉、nSmoothPatch / tolerance / nSolveIter；④addLayers：expansionRatio、finalLayerThickness、minThickness、relativeSizes 与覆盖率；⑤meshQualityControls 在三个阶段中的作用。</p></section>
<p class="source-note">配套算例来自已有课程。下载解压后阅读其中的 README 与运行脚本，并在已加载 v2512 环境的 Linux 终端执行。本站未重新运行这些算例；原讲义中的本机路径需改为自己的实际路径。</p>
<p>配套算例位于原课程“09_snappyHexMesh原理”目录。文中相对路径以该讲目录或已注明的算例目录为准。</p>
<pre><code>OpenCFD OpenFOAM v2512</code></pre>
<h2>1 表面几何与背景网格</h2>
<p>snappyHexMesh 由背景体网格和表面几何出发，经局部细化、区域保留、贴体及加层生成网格，适合三角面片描述的曲面和多凸起结构。本讲以四个凸起表面为例，分别用 castellated、snap、layers 独立目录比较各阶段的实际结果。</p>
<p>constant/triSurface/posts.stl 通过三角面片及其顶点坐标描述物体表面。求解所需体单元由后续网格生成过程建立，表面三角形数与体单元数没有固定比例关系。</p>
<p>surfaceCheck 显示 512 个三角形、1 个命名区域和 4 个不连通部分。各部分包含 128 个三角形，均为闭合表面，每条边连接两个面。四个独立凸起共同归于 posts 名称，说明一个命名区域可包含多个分离实体。</p>
<p>表面包围盒为 (−0.0011,−0.0002,−0.0011)～(0.0011,0.0015,0.0011) m。背景网格从 \(y=0\) 开始，凸起底部延伸至 \(y=-0.0002\,\mathrm{m}\)，与底边界相交。保留区域应依据表面与背景网格的相对位置确定。</p>
<p>表面检查应同时核对法向、连接关系及闭合性。法向不一致会影响内外区域识别，重复三角形、非流形边和缝隙可能改变连通关系。本例的四个法向一致部分分别对应四个凸起。新几何应先修复表面问题，再调整网格参数。</p>
<h2>2 三阶段的输入与处理顺序</h2>
<p>三组背景域相同：x、z 为 −0.002～0.002 m，y 为 0～0.004 m。各方向 16 个单元，总计 4096，初始边长 0.25 mm。该网格覆盖目标域，并确定后续细化的基准尺度。</p>
<p>snappyHexMeshDict 的三个开关分别控制执行阶段：castellatedMesh 负责切割、细化和区域选择，snap 负责顶点贴合，addLayers 负责壁面层生成。三组目录的设置如下。</p>
<div class="table-scroll"><table>
<tr><th>目录</th><th>castellatedMesh</th><th>snap</th><th>addLayers</th></tr>
<tr><td>castellated</td><td>true</td><td>false</td><td>false</td></tr>
<tr><td>snap</td><td>true</td><td>true</td><td>false</td></tr>
<tr><td>layers</td><td>true</td><td>true</td><td>true</td></tr>
</table></div>
<p>每个目录都从自己的 blockMesh 结果开始执行，因此可以单独复制运行。snap 目录会重新完成细化，再进行贴合；layers 目录会重新完成细化和贴合，再尝试加层。比较三个结果时，前面各阶段的设置相同，便于识别后续操作的影响。</p>
<p>几何在字典中按如下方式声明：</p>
<pre><code>geometry
{
    posts.stl
    {
        type triSurfaceMesh;
        name posts;
    }
}</code></pre>
<p>posts.stl 是输入文件名，triSurfaceMesh 指定三角面片几何，posts 是后续 refinementSurfaces 等字典引用的名称。文件名、几何名称和最终边界名称彼此有关，但应分别核对，尤其是在一个 STL 含有多个命名区域时。</p>
<h2>3 castellated 细化与区域选择</h2>
<p>六面体每细化一级，各方向边长通常减半，形成八个子单元，等级 l 的名义尺度为 \(h_{0}/2\)ˡ。本例表面 level (1 1) 对应 0.125 mm。粗细交界含过渡单元，最终数量以日志为准。</p>
<pre><code>refinementSurfaces
{
    posts
    {
        level (1 1);
        patchInfo { type wall; }
    }
}
nCellsBetweenLevels 3;
locationInMesh (0.0018 0.0038 0.0018);</code></pre>
<p>level 的两个值规定表面细化的最小和最大等级；本例二者相同，均为一级。nCellsBetweenLevels 为相邻细化等级之间的缓冲单元层数，用于限制尺寸过渡过于集中。它与表面细化等级不同，数值三不表示把整个表面细化三级。</p>
<p>细化和切割将背景网格划分为不同区域后，locationInMesh 指定需要保留的连通区域。本例选点位于计算域上部、远离四个实体内部。该点应处于目标流体区域内部，避开几何表面和网格面；选入固体内部可能保留错误的一侧，导致流体域外形和体积异常。</p>
<p><code>maxLocalCells=100000</code>、<code>maxGlobalCells=200000</code> 用于控制细化过程的规模。它们不是要求达到的单元数。实际日志从初始 4096 个单元开始，经过细化一度达到 9854 个单元，区域选择后保留 9066 个单元。这一过程包含增加和删除单元，不能只把初始数量乘以八预测最终结果。</p>
<figure><img loading="lazy" src="/assets/lessons/09/image1.png" alt="本讲配套算例图"><figcaption>配套学生讲义中的算例图</figcaption></figure>
<p>图 1 为 castellated 的结果。靠近凸起的单元更细，几何边界仍呈阶梯状。总体积为 \(6.203125\times 10^{-8} m^{3}\)，小于原背景长方体的 \(6.4\times 10^{-8} m^{3}\)，差值对应当前网格对实体占据区域的离散表示。</p>
<p>细化等级的代价可以用一个局部区域估算。若一百个规则六面体全部细化一级，它们将由八百个子单元替代，总数净增加七百个；再细化一级，局部单元数量还会继续增加。实际流程为维持等级过渡，可能同时细化邻近区域。因此选择局部加密范围时，应将表面分辨率、缓冲区宽度和允许单元规模一并记录。</p>
<h2>4 snap 顶点移动与贴体</h2>
<p>snap 移动边界顶点并平滑邻近位移，使离散边界接近输入表面。网格面仍为平面多边形，贴体后仍存在曲面近似误差，应结合轮廓、局部截面及质量指标评价。</p>
<pre><code>snapControls
{
    nSmoothPatch 3;
    tolerance 2;
    nSolveIter 30;
    nRelaxIter 5;
    nFeatureSnapIter 10;
    implicitFeatureSnap true;
    explicitFeatureSnap false;
    multiRegionFeatureSnap false;
}</code></pre>
<p>nSmoothPatch 控制表面平滑迭代，nSolveIter 和 nRelaxIter 控制位移求解及相关松弛过程。tolerance 是结合局部网格尺度确定搜索距离的系数，本例的二没有米的单位。nFeatureSnapIter 给出特征贴合迭代次数，几何棱边附近的点移动与这些控制共同有关。</p>
<p>本例采用隐式特征处理，implicitFeatureSnap 为 true，explicitFeatureSnap 为 false，细化控制中的 features 列表为空。显式特征处理需要先提取特征边，在字典中引用相应 eMesh 文件，并启用对应设置。</p>
<p>本例 Allrun.sh 没有执行 surfaceFeatureExtract，阅读其他版本教程时应先确认其所用方式。</p>
<p>贴合后单元数仍为 9066，但点数由 11627 减少到 11435，面数由 29712 减少到 29520。日志记录了面合并，因此单元数不变并不表示网格完全没有改变。posts 边界面数也由 1044 降到 852，点坐标和边界面组织均发生调整。</p>
<figure><img loading="lazy" src="/assets/lessons/09/image2.png" alt="本讲配套算例图"><figcaption>配套学生讲义中的算例图</figcaption></figure>
<p>图 2 显示 snap 结果。流体域总体积变为 \(6.23610186612\times 10^{-8} m^{3}\)，反映贴合改变了离散边界位置。最大非正交角从约 25.2394°增至 28.6383°，最大偏斜度从约 0.33333 增至 0.35869。表面几何表示改善的同时，内部单元形状也需要重新检查。</p>
<h2>5 addLayers 层数与厚度</h2>
<p>壁面法向常存在显著速度、温度或浓度梯度，薄层单元可提高其分辨率。加层先移动现有近壁网格腾出空间，再沿指定壁面挤出单元，最后依据质量条件保留或撤回新增层。</p>
<pre><code>relativeSizes true;
layers
{
    &quot;posts.*&quot;
    {
        nSurfaceLayers 2;
    }
}
expansionRatio 1.2;
finalLayerThickness 0.3;
minThickness 0.05;</code></pre>
<p>这些条目位于 addLayersControls。&quot;posts.*&quot; 按名称匹配目标边界；本例生成的 posts 边界被匹配。<code>nSurfaceLayers=2</code> 是目标层数，<code>expansionRatio=1.2</code> 表示向外相邻层厚度的增长关系。</p>
<p><code>relativeSizes=true</code> 表示厚度参数相对于局部网格尺度定义，<code>finalLayerThickness=0.3</code> 对应最外层的目标相对厚度，minThickness 给出允许保留的最小相对总厚度。</p>
<p>可用规则网格作厚度估算。若局部基准尺寸 \(h=0.125 \mathrm{mm}\)，则最外层目标厚度为 \(0.3h=37.5 \mu m\)，两层按 1.2 的比值排列，第一层约为 \(31.25 \mu m\)，总厚度约为 \(68.75 \mu m\)。实际贴合后各位置的尺度、法向和约束不同，应以生成场及日志统计检查最终厚度。</p>
<p>层数、厚度和覆盖面积必须分别评价。某些表面位置可能因尖角、狭缝、法向冲突或质量限制而停止挤出，最终层数也可能低于目标值。读取 nSurfaceLayers、thickness 和 thicknessFraction 可以检查实际层数、总厚度及其相对目标的比例。本例启用了 layerFields 和 layerSets，以保存这些诊断结果。</p>
<h2>6 本例加层失败的实际过程</h2>
<p>layers 目录已启用加层阶段，但最终没有成功生成壁面层。其最终单元数、点数、面数及体积均与 snap 相同，仍为 9066 个单元。log.snappyHexMesh 最后的加层统计为：</p>
<pre><code>Extruding 0 out of 852 faces (0%).
Added 0 out of 1704 cells (0%).
Writing 0 faces inside added layer to faceSet layerFaces
Layer mesh : cells:9066  faces:29520  points:11435</code></pre>
<p>直接原因可以在此前迭代中找到。第一次检查候选加层网格时，日志报告 4808 个面的面金字塔体积小于 \(1\times 10^{-13} m^{3}\)，随后撤销相关挤出。面金字塔体积由单元中心与单元面构成的几何体计算，是局部质量检查量，不等于整个单元体积。第二次迭代最终没有保留新增单元。</p>
<p>本例 meshQualityControls 引用了安装目录的 caseDicts/meshQualityDict，其中 <code>minVol=1e-13</code>。这个阈值带有体积尺度；毫米级几何中的薄层可能形成很小的面金字塔体积，需要结合目标网格尺寸评价阈值。其他几何上的经验数值直接用于本例时，可能限制本来计划生成的薄层。</p>
<p>日志在中间迭代曾出现 Added 1576 out of 1704 cells 的信息，但随后质量检查与挤出撤销改变了结果。应顺序读取候选网格检查、撤销信息和最终写出统计，不能从中间一行提取“加层成功率”。本例最终 layerFaces 数量为零，才是交付网格的实际状态。</p>
<figure><img loading="lazy" src="/assets/lessons/09/image3.png" alt="本讲配套算例图"><figcaption>配套学生讲义中的算例图</figcaption></figure>
<p>图 3 为 layers 最终网格。其壁面附近没有保留下来的新增层单元。该结果用于学习如何区分目标设置、过程尝试和最终输出；字典中的“两层”应表述为目标参数，不能写成已经获得两层壁面网格。</p>
<p>加层诊断文件本身也是结果。nSurfaceLayers 记录实际生成层数，区别于字典中同名目标条目；layerFaces 是最终新增层内部相关面的集合。检查时先确认读取的是网格生成后写出的文件，再与最终日志对应。本例这些输出与零新增层的结论一致，图片上没有出现薄层也由此获得了数量依据。</p>
<h2>7 完整操作与命令说明</h2>
<p>在本讲目录打开终端，加载本机环境，然后进入 castellated 算例即可运行：</p>
<pre><code>source /usr/lib/openfoam/openfoam2512/etc/bashrc
cd 代码/castellated
./Allrun.sh</code></pre>
<p>每个算例均包含自己的 Allrun.sh，内容为简单命令。脚本先生成背景网格，再检查输入表面，随后执行网格细化与所启用的后续阶段，最后检查生成网格。</p>
<pre><code>#!/bin/sh
set -e
blockMesh &gt; log.blockMesh 2&gt;&amp;1
checkMesh &gt; log.checkMesh 2&gt;&amp;1
surfaceCheck constant/triSurface/posts.stl &gt; log.surfaceCheck 2&gt;&amp;1
snappyHexMesh -overwrite &gt; log.snappyHexMesh 2&gt;&amp;1
checkMesh &gt; log.checkMesh.2 2&gt;&amp;1
touch case.foam</code></pre>
<p>第一次 checkMesh 检查背景网格，第二次检查最终网格，日志分别保存为 log.checkMesh 与 log.checkMesh.2。比较单元数量或质量时，应读取后者。-overwrite 将最终网格写回输入网格位置，使 case.foam 打开后使用本次结果；不用该选项时，应检查新产生的网格时间目录。</p>
<p>完成一个目录后，可以进入相邻的 snap 或 layers 目录执行各自脚本。运行前查看三个开关，有助于确认目录中的实际设置：</p>
<pre><code>foamDictionary system/snappyHexMeshDict -entry castellatedMesh -value
foamDictionary system/snappyHexMeshDict -entry snap -value
foamDictionary system/snappyHexMeshDict -entry addLayers -value</code></pre>
<p>surfaceCheck 输出几何尺寸、三角形、边连接和闭合性；surfaceFeatureExtract -help 用于查看显式特征提取帮助；snappyHexMesh -help 用于查看本机支持的选项。-help 只显示说明，不生成特征文件或网格。当前案例以本机 v2512 帮助和实际字典为准。</p>
<h2>8 结果对比与网格质量判断</h2>
<p>三个算例的脚本均正常结束，最终网格均通过本次 checkMesh 检查。测试中的 PASS 表示执行及相应网格检查通过；加层目标仍需依据上一节的实际层数评价。本讲没有执行流场求解，不包含阻力、速度或传热结果。</p>
<div class="table-scroll"><table>
<tr><th>结果</th><th>castellated</th><th>snap</th><th>layers</th></tr>
<tr><td>单元数</td><td>9066</td><td>9066</td><td>9066</td></tr>
<tr><td>点数</td><td>11627</td><td>11435</td><td>11435</td></tr>
<tr><td>posts 边界面数</td><td>1044</td><td>852</td><td>852</td></tr>
<tr><td>总体积\(/m^{3}\)</td><td>\(6.203125\times 10^{-8}\)</td><td>\(6.236102\times 10^{-8}\)</td><td>\(6.236102\times 10^{-8}\)</td></tr>
<tr><td>最大非正交角/°</td><td>25.2394</td><td>28.6383</td><td>28.6383</td></tr>
<tr><td>最终新增壁面层面数</td><td>未启用</td><td>未启用</td><td>0</td></tr>
</table></div>
<p>在 ParaView 中打开各自 case.foam，选择 Surface With Edges，并设置相同视角。外表面用于检查几何贴合，穿过凸起的截面用于检查内部尺寸过渡和壁面法向网格。若同时显示 STL 与网格，应选择不同颜色或透明度，避免两个表面重叠后掩盖局部偏差。</p>
<p>单元数相同而几何质量不同，是本例的重要观察。snap 改变点的位置并合并部分面，几何体积和质量指标均随之变化；layers 则因最终挤出全部撤销而保持与 snap 相同。解释结果时，应同时列出开关、拓扑数量、几何量和阶段日志。</p>
<p>若需要进一步量化几何误差，可以在多个固定高度提取凸起截面，把网格边界位置与输入 STL 的截面比较，并报告局部距离或截面面积差。只比较流体域总体积可能掩盖局部误差，因为不同位置的边界偏移可能相互抵消。几何比较的坐标、截面位置和误差单位应保持一致，才能判断加密或贴合设置是否改善了目标部位。</p>
<h2>9 错误原因与参数比较方法</h2>
<p>如果生成区域明显偏离预期，先核对 STL 与背景网格的包围盒、坐标单位及 locationInMesh。几何完全位于背景网格之外时，调整细化等级不能解决位置问题；选点落入错误连通区域时，应先修正区域选择，再比较网格尺寸。</p>
<p>若表面仍出现较明显阶梯，可分别检查是否启用 snap、表面附近网格是否足以表达曲率、特征处理是否与几何相符。过粗的网格缺少描述小尺度结构所需的自由度；单纯增加点移动迭代次数，无法代替这些空间分辨率。</p>
<p>针对本例的加层问题，应先定位未通过 minVol 检查的区域，估算当地面面积和目标层厚度，再审查该绝对阈值与毫米级网格的关系。参数比较可以在完整副本中一次修改一项，例如厚度设置或有依据的质量阈值，并重新记录最终层数、覆盖面积、最小体积和非正交角。</p>
<p>减小层厚会减少所需挤出空间，却也可能进一步减小面金字塔体积；增加层厚可能改善体积尺度，又可能在狭窄区域导致挤出冲突。因此调整方向需要由实际失败指标决定。关闭检查项目仅改变接受规则，不能说明新增单元已经具有足够质量。</p>
<p>最后还需区分几何分辨率与近壁流动分辨率。获得两层网格后，仍要根据后续流动物性、雷诺数和壁面处理方法确定第一层高度是否合适。当前阶段先完成可靠的几何与网格检查，再在对应流动课程中评价梯度和壁面量。</p>
<h2>10 几何分辨率 体网格分辨率与质量阈值</h2>
<p>STL近似曲面的误差可以先作几何估算。将半径R的圆周离散为N段，弦与圆弧的最大径向差为\(R[1-\cos (\pi /N)]\)。本例\(R=0.3\mathrm{mm}\)、\(N=32\)，弦高约\(1.44\mu m\)；当前一级细化体网格尺度约\(125\mu m\)。该比较说明几何面片与体单元控制不同的误差来源，增加其中一类分辨率不能自动消除另一类误差。</p>
<p>生成边界首先应与输入STL在相同截面比较，核对柱顶、柱侧与间隙位置。随后再评价STL相对设计几何的误差。若只观察流场云图，很难区分边界几何误差与方程离散误差；两者都可能改变局部梯度和通量。</p>
<p>细化等级还会改变绝对体积尺度。边长减半，体积缩小八倍，因此minVol等绝对阈值需要结合目标最小单元重新判断。非正交角、偏斜度和相邻体积比属于不同类型的条件。第10讲以正的minVol阈值修复毫米尺度层生成失败，并用实际覆盖与扩展几何检查评价结果，形成从参数估算到真实网格检查的完整训练。</p>
<h2>11 资料来源</h2>
<p>本讲依据 castellated、snap、layers 的完整字典、surfaceCheck 日志、snappyHexMesh 日志和最终 checkMesh 结果编写。质量阈值取自本机 v2512 安装目录中的 caseDicts/meshQualityDict。</p>
<p>继续阅读可查阅本机 snappyHexMesh、surfaceCheck、surfaceFeatureExtract 帮助，以及《OpenFOAM 命令与文件大全 v2512》第 6.2—6.3、16.1—16.4、17.7、18.7 章，并对照实际三阶段结果理解各参数作用。</p>
<section class="exercise"><h2>课后练习</h2><p>通读一份完整 snappyHexMeshDict 注释，按三个阶段分类标出关键参数并注明各自控制什么。</p><a class="button secondary" href="/assignments/">前往作业区 →</a></section>
{% endraw %}