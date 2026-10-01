---
title: "网格转换与边界分区"
layout: "lesson"
lesson_id: 11
stage: 3
description: "网格转换：fluentMeshToFoam、gmshToFoam、ideasUnvToFoam、cfMesh 简介与常见转换失败原因；②操作工具：transformPoints、mirrorMesh、mergeMeshes、refineMesh、createPatch、renumberMesh；③topoSet / setSet：按几何形状（box、sphere、cylinder）选取 cellSet / faceSet，并转为 cellZone；④用 faceSet + createPatch 从一整块壁面上切出电极面（或多个成核位点）；⑤CAD 建模要点：水密性、特征线保留、STL 导出精度与单位（微米级几何尤其要核对单位）。"
---
{% raw %}
<section class="lesson-intro"><h2>本讲学习任务</h2><p>①网格转换：fluentMeshToFoam、gmshToFoam、ideasUnvToFoam、cfMesh 简介与常见转换失败原因；②操作工具：transformPoints、mirrorMesh、mergeMeshes、refineMesh、createPatch、renumberMesh；③topoSet / setSet：按几何形状（box、sphere、cylinder）选取 cellSet / faceSet，并转为 cellZone；④用 faceSet + createPatch 从一整块壁面上切出电极面（或多个成核位点）；⑤CAD 建模要点：水密性、特征线保留、STL 导出精度与单位（微米级几何尤其要核对单位）。</p></section>
<p class="source-note">配套算例来自已有课程。下载解压后阅读其中的 README 与运行脚本，并在已加载 v2512 环境的 Linux 终端执行。本站未重新运行这些算例；原讲义中的本机路径需改为自己的实际路径。</p>
<p>配套算例位于原课程“11_网格转换与边界分区”目录。文中相对路径以该讲目录或已注明的算例目录为准。</p>
<pre><code>OpenCFD OpenFOAM v2512</code></pre>
<h2>1 网格数据与控制方程的接口</h2>
<p>有限体积方程使用单元体积、面积和邻接关系计算瞬态项与面通量。外部软件的网格格式和区域编号可能不同，转换工具将点、面、单元和分组写为求解器可读数据，物理边界仍由场文件另行定义。</p>
<p>polyMesh 中，points 保存坐标，faces 保存面顶点编号，owner 保存面所属单元，neighbour 保存内部面另一侧单元，boundary 保存边界分组。内部面通过邻接关系共享通量，边界面通过 patch 关联场条件；这些关系共同确定面值的来源。</p>
<p>几何表面定义空间形状，面集合选取已有网格面，patch 参与边界条件分配。选面操作不会自动建立入口条件，inlet 名称也不自动赋予速度。边界名称与物理条件须在场文件中明确对应。</p>
<p>gmsh_import 将 cube.msh 转换为一个六面体单元，便于逐项核对网格文件；split_boundary 从已生成网格的底面选区，建立独立边界和单元区域。两组均只处理网格，不求解流场。</p>
<h2>2 外部网格转换及单位核对</h2>
<p>gmsh_import 依次执行 gmshToFoam cube.msh、checkMesh 并创建 case.foam。转换结果为一个单元，包围盒 (0 0 0) 至 (1 1 1)，六个面归入 walls。该例用于检验格式与边界映射，不具备实际流动分辨能力。</p>
<pre><code>source /usr/lib/openfoam/openfoam2512/etc/bashrc
cd 代码/gmsh_import
./Allrun.sh
gmshToFoam cube.msh &gt; log.gmshToFoam 2&gt;&amp;1
checkMesh &gt; log.checkMesh 2&gt;&amp;1
touch case.foam</code></pre>
<p>外部网格的单位应由已知尺寸核对。若将以 mm 表示的长度误读为 m，长度放大 \(10^{3}\) 倍，面积和体积分别放大 10⁶ 与 10⁹ 倍。即使速度与黏度数值不变，Re 和通量积分也会改变，因此单位检查须在求解前完成。</p>
<p>transformPoints 可缩放点坐标，mm 转为 m 时使用 0.001。本例已采用 m，无需再次缩放。换算应在副本中进行并记录原单位及比例；后处理仅将坐标显示为 mm 时，不应再次修改计算网格。</p>
<figure><img loading="lazy" src="/assets/lessons/11/image1.png" alt="本讲配套算例图"><figcaption>配套学生讲义中的算例图</figcaption></figure>
<p>图中几何外形与包围盒一致。还需读取 boundary：walls 的类型实际为 patch，名称虽然包含 wall 含义，却没有自动变为 wall 类型。是否设置无滑移条件仍由速度场决定；需要壁面模型或壁面统计时，还应检查网格类型是否符合该模型要求。这个例子说明边界名称、网格类型和场条件必须分别读取。</p>
<h2>3 按几何条件选择边界面</h2>
<p>split_boundary 尺寸为 1 m×1 m×0.05 m，各方向 12 个单元，总计 1728。厚度方向也有 12 层，因此属于三维网格。底面已有 144 面，分区仅从中选择，不新增几何面。</p>
<p>选区分两步完成。第一步用 patchToFace 建立 sourceWallFaces，把 bottom 的全部面纳入 faceSet。第二步使用 action subset，仅保留这些面中面中心位于指定圆柱内的面。先限定底面再按几何筛选，可以避免邻近侧面或内部面同时被选入。</p>
<pre><code>actions
(
    {
        name sourceWallFaces;
        type faceSet;
        action new;
        source patchToFace;
        patches (bottom);
    }
    {
        name sourceWallFaces;
        type faceSet;
        action subset;
        source cylinderToFace;
        p1 (0.5 -0.1 0.025);
        p2 (0.5 0.1 0.025);
        radius 0.2;
    }
);</code></pre>
<p>圆柱轴沿 y 方向通过底面中心附近，半径为零点二米。筛选依据是面中心的位置，并非对圆周进行重新切割，所以分区边缘沿现有网格面呈离散近似。半径略微改变但没有跨过新的面中心时，面数可能保持不变；跨过某一排面中心后，面数会跳变。这种分段变化来自选择规则和网格分辨率。</p>
<p>实际日志先报告一百四十四个底面，随后 sourceWallFaces 减少为四十八个面。核对这一中间结果比只查看最终边界名称更有用：若第一步已为零，应检查 patch 名；若第一步正确而第二步为零，应检查圆柱轴、半径、单位及筛选范围。两种错误发生于不同阶段，修正方法也不同。</p>
<h2>4 创建 patch 与单元区域</h2>
<p>createPatch 从已有面集合创建 sourceWall。constructFrom set 指明来源为集合，set sourceWallFaces 指定集合名，patchInfo 中 type wall 指定网格边界类型。-overwrite 将修改直接写入当前 polyMesh。</p>
<pre><code>patches
(
    {
        name sourceWall;
        patchInfo { type wall; }
        constructFrom set;
        set sourceWallFaces;
    }
);</code></pre>
<p>本例分区后 sourceWall 有四十八个面，剩余底面仍名为 bottom，有九十六个面。两者面数之和等于原底面的一百四十四个面，说明操作是边界面的重新分组，并没有增加或删除底面几何。最终边界总数从五个增至六个，单元总数仍为一千七百二十八个。</p>
<p>topoSetDict 中还有 sourceCells 和 sourceZone。boxToCell 根据单元中心位于盒内的条件选择单元，范围为 x 从零点三到零点七米、y 从零到零点二米、z 从零到零点零五米。生成的 cellSet 包含九十六个单元，随后 setToCellZone 把它转换为同样包含九十六个单元的 sourceZone。</p>
<p>faceSet 与 cellZone 的用途不同。前者可用于重建边界，后者常用于指定体积源项或区域操作。局部输入若施加于面，积分单位通常包含面积；若施加于单元，积分单位通常包含体积。把边界通量直接写成体积源，除了对象类型不匹配，还会造成源项量纲错误，因此需要先根据控制方程明确输入发生在边界还是体内。</p>
<p>运行脚本还调用 renumberMesh -overwrite 重排编号，以改善后续线性系统的编号结构。重编号保留几何及物理分区，但单元和面编号可改变。任何依赖原单元编号的人工列表都需要重新核对；通常应优先使用几何或区域名称指定对象，减少对偶然编号的依赖。</p>
<h2>5 面积 法向与通量的计算</h2>
<p>底面面积为 \(1\times 0.05=0.05\,\mathrm{m}^{2}\)，均分为 144 面。sourceWall 含 48 面，面积为 \(0.016667\,\mathrm{m}^{2}\)，剩余 bottom 约为 \(0.033333\,\mathrm{m}^{2}\)。分区前后面积之和应一致。</p>
<p>本例第三方向厚度仅零点零五米，所选圆柱在薄底面内被几何范围截取。因此不能直接把选区面积写成 \(\pi r^{2}\)。圆柱半径描述选择工具的范围，实际边界面积还受到原底面尺寸和离散面中心条件限制。面对局部圆孔、薄片或曲面分区时，都应从实际网格面积计算总通量。</p>
<p>给定均匀摩尔通量密度 J，总输入率为 JA。假设另一计算题中面积为 \(4\times 10^{-6} m^{2}\)，向域内通量密度为 \(2 \mathrm{mol}/(m^{2}\cdot s)\)，则输入率为 \(8\times 10^{-6} \mathrm{mol}/s\)。OpenFOAM 边界面法向指向计算域外部，若按外向为正，总外向通量为 \(-8\times 10^{-6} \mathrm{mol}/s\)。该符号来自法向约定，与输入物质的名称无关。</p>
<p>对于 Fick 扩散，外向摩尔通量密度为 \(-D\partial c/\partial n\)。若要求向内输入为正的 J，则外法向浓度梯度应满足 \(\partial c/\partial n=J/D\)。在底部边界，外法向通常沿负 y 方向，因此外法向梯度与沿正 y 的导数符号相反。将坐标导数与外法向导数混用，是通量方向设置错误的常见原因。</p>
<h2>6 运行与结果复核</h2>
<p>进入 split_boundary 后执行 Allrun.sh，程序按建网格、初始检查、选区、创建边界、重编号和最终检查的顺序运行。各阶段均生成独立日志，便于从失败命令对应的记录定位问题。</p>
<pre><code>blockMesh &gt; log.blockMesh 2&gt;&amp;1
checkMesh &gt; log.checkMesh 2&gt;&amp;1
topoSet &gt; log.topoSet 2&gt;&amp;1
createPatch -overwrite &gt; log.createPatch 2&gt;&amp;1
renumberMesh -overwrite &gt; log.renumberMesh 2&gt;&amp;1
checkMesh &gt; log.checkMesh.2 2&gt;&amp;1
touch case.foam</code></pre>
<figure><img loading="lazy" src="/assets/lessons/11/image2.png" alt="本讲配套算例图"><figcaption>配套学生讲义中的算例图</figcaption></figure>
<p>图中网格单元分布保持规则，分区主要改变边界归属。单独显示边线时，新旧 patch 的差异未必明显，需在 ParaView 中按边界名称分别选择 sourceWall 和 bottom，并采用不同颜色检查其空间位置。随后读取 boundary 中的面数和起始编号，核对与 topoSet 日志一致。</p>
<p>最终 checkMesh 的最大非正交角为零，最大偏斜度约为 \(1.07\times 10^{-14}\)，反映本例仍为规则正交网格。这些指标没有改变，是因为创建 patch 和重编号没有移动顶点。若后续更改几何或缩放，也应重新检查，但不能用质量指标不变替代边界语义和单位核对。</p>
<p>需要继续求解时，各场文件必须为 sourceWall 增加条件，并保留 bottom 的相应条目。仅给速度补边界而遗漏压力或标量，求解器仍会在读取后续场时停止。添加条目前先确认新边界承担的约束，例如固定速度、固定梯度或无滑移，并检查各变量之间是否相容。</p>
<p>边界面积的核对还应与总体守恒联系起来。将原底面分成两部分后，若两部分仍采用相同通量密度，则两部分通量之和应等于分区前的总通量。若只在新边界施加通量，其余部分设为零梯度，则总体输入随选区面积改变。比较不同分区时，需要说明保持的是通量密度还是总输入率：保持前者时总量随面积变，保持后者时应按新面积重新计算密度。</p>
<p>内部面的守恒方式与外边界不同。内部面只存储一份几何面积及通量，面两侧单元使用相反符号，因此在全域积分中抵消。外边界没有另一侧计算单元与其抵消，其通量直接进入全域收支。边界重组本身不改变这一结构，只有随后赋予不同场条件时才改变控制方程的边界贡献。这也是需要在网格转换后重新核对全部场条件的原因。</p>
<p>曲面分区还需逐面计算法向通量。若指定的是全局方向通量向量，应与各面面积向量作点积后求和；若指定的是外法向通量密度，则直接乘各面的面积。曲面上两种输入方式一般得到不同总量。将一个全局向量的某个分量乘总表面积，会忽略法向随位置变化，只有面法向一致的平面才可按相应简化处理。</p>
<h2>7 常见错误及其原因</h2>
<p>外部网格导入失败时，先核对工具支持的文件版本、ASCII 或二进制格式及单元类型。文件能够打开但边界映射错误时，应检查外部物理分组，而非直接把所有默认边界设成同一种条件。缺失分组会使不同几何功能的面合并，后续再按名称设置就失去区分依据。</p>
<p>选区为空时，应分别确认对象类型、几何坐标和已有集合。cellSet 的选择条件作用于单元中心，faceSet 作用于面中心，二者即使使用相同盒子也会得到不同数量。边界附近很薄的选择区可能包含面中心却不包含任何单元中心，这并非工具异常，而是离散位置不同。</p>
<p>出现负体积、不闭合区域或拓扑错误时，问题通常需要在原始网格中修复。修改 boundary 文本只能重新归类已有边界面，不能补足缺失单元或修复错误的面点连接。修复后应重新转换，保存输入网格和对应日志，保证最后使用的 polyMesh 来自明确的一次处理过程。</p>
<p>对于分区扩展实验，应在副本中仅修改选择半径或盒子范围，重新建网格并执行完整流程。比较面数、面积及区域位置，解释变化来自哪组面中心被加入或移除。这样可以将集合操作、边界条件和积分守恒联系起来，为后续局部源项与通量边界设置建立基础。</p>
<h2>8 命令查询与结果复核</h2>
<p>以下命令在指定算例目录执行。运行脚本生成网格、日志及结果后，再进行结果查询；需要修改设置时，先保留完整算例副本。</p>
<h3>集合 分区与边界</h3>
<p>执行目录为 代码/split_boundary。</p>
<pre><code>cat system/topoSetDict
cat system/createPatchDict
head -n 45 log.topoSet
head -n 70 constant/polyMesh/boundary</code></pre>
<p>topoSet 按几何或拓扑条件生成集合，createPatch 根据 faceSet 等来源创建边界。</p>
<p>cellSet 和 faceSet 分别记录所选单元及面。源项需要 cellZone 时，需将单元集合转换为单元区域。</p>
<p>创建 patch 后，各场的 boundaryField 均需包含新边界名称，并设置相应条件。</p>
<h3>导入网格的长度单位</h3>
<p>执行目录为 代码/gmsh_import。</p>
<pre><code>ls *.msh
head -n 35 log.gmshToFoam
transformPoints -help
checkMesh &gt; log.importCheck 2&gt;&amp;1</code></pre>
<p>gmshToFoam 读取本目录中的 msh 文件，导入后核对物理分组、patch 类型、包围盒和单元数。</p>
<p>transformPoints -scale 按比例修改网格坐标，可在副本中用于长度单位换算。</p>
<p>本例网格采用米。缩放因子 0.001 适用于输入坐标采用毫米、目标单位为米的情况。</p>
<h2>9 网格对象与量纲传播</h2>
<p>网格转换保留的是坐标、拓扑和分组关系。有限体积离散通过 owner 和 neighbour 确定面两侧的单元，通过 boundary 确定外边界所属分组。一个几何上位于壁面的面，只有在网格分组和场条件共同正确时，才具有所需的速度或热边界约束。将名字写成 inlet 或 wall 并不自动定义相应物理条件。</p>
<p>设边界面通量密度为 j_f，单元体积源强为 s_c，则边界总量为 \(\sum j_{f} A_{f}\)，体积总量为 \(\sum s_{c} V_{c}\)。两者的积分对象、单位和选区方法不同。topoSet 的几何筛选只是把已有面或单元选入集合，不会产生新的控制方程；createPatch 和区域模型才决定后续如何使用这些对象。</p>
<p>检查 sourceWall 和 sourceZone 时，应分别显示面和单元，核对其位置、数量与积分范围。</p>
<p>尺度换算会沿计算链传播。若毫米坐标被按米解释，长度变为目标值的 1000 倍，面积和体积分别变为 10⁶、10⁹ 倍。即使字典中的速度或通量密度数值未变，Re 和总流量也已经变化。正确的核查顺序是先比较设计尺寸与网格包围盒，再计算代表面积和体积，最后检查变量量纲及边界积分。</p>
<h2>10 资料来源</h2>
<p>基本方法参考 Wolf Dynamics《OpenFOAM Introductory Training》2021 修订版，PDF 文件第 515–538 页。命令语法以本机 OpenCFD OpenFOAM v2512 的帮助和配套教程为准。本讲字典片段、网格统计及数值结果取自课程对应算例，完整输入位于代码目录，原始日志与检查记录位于测试结果目录。</p>
<section class="exercise"><h2>课后练习</h2><p>把一个 gmsh（或 Fluent）网格转入 OpenFOAM；在底面用 topoSet + createPatch 切出一个圆形电极面，并用 setFields 在电极中心放一个半球形种子气泡，用 ParaView 确认位置正确。</p><a class="button secondary" href="/assignments/">前往作业区 →</a></section>
{% endraw %}