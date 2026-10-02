`snappyHexMesh` 从背景六面体网格出发，围绕 STL 或 OBJ 表面生成贴体网格。它适合复杂外形，主要通过局部细化、表面贴合和近壁层生成控制网格。

## 三个阶段分别做什么

| 阶段 | 开关 | 作用 |
| --- | --- | --- |
| 局部细化与区域选择 | `castellatedMesh` | 细分表面和加密区域附近的单元，保留目标流体域 |
| 表面贴合 | `snap` | 将边界网格点移动到目标几何表面附近 |
| 近壁层生成 | `addLayers` | 沿选定壁面添加薄层单元 |

<figure class="wolf-figure"><img src="/assets/wolf/wolf-snappy-workflow.png" alt="snappyHexMesh 的几何与背景网格输入" loading="lazy"><figcaption><strong>snappyHexMesh 的几何与背景网格输入</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 71 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

对应的开关位于 `system/snappyHexMeshDict` 顶部：

```foam
castellatedMesh true;
snap            true;
addLayers       true;
```

本课使用 motorBike 的完整字典，分段解释主要设置。下面出现的配置片段用于修改对应子字典；完整文件还包含其他控制项及质量设置。

## 准备 motorBike 算例

从官方教程复制完整算例，在新副本中运行：

```bash
mkdir -p "$HOME/OpenFOAM/learning-v2512"
cd "$HOME/OpenFOAM/learning-v2512"
cp -r "$FOAM_TUTORIALS/incompressible/simpleFoam/motorBike" motorBike-mesh
cd motorBike-mesh
mkdir -p constant/triSurface
cp "$FOAM_TUTORIALS/resources/geometry/motorBike.obj.gz" \
    constant/triSurface/
```

下载包包含相同的算例与表面资源。使用下载包时，将包内 `tutorials/resources/geometry/motorBike.obj.gz` 复制到本例 `constant/triSurface`。

主要文件的作用如下：

| 文件 | 内容 |
| --- | --- |
| `blockMeshDict` | 外部背景域与初始网格 |
| `surfaceFeatureExtractDict` | 从表面提取需要保留的特征边 |
| `snappyHexMeshDict` | 表面、细化等级、贴合与层网格设置 |
| `meshQualityDict` | 网格质量约束 |
| `0.orig` | 求解阶段需要的初始场模板 |

官方 `Allrun` 包含六分区并行网格生成、场恢复、初始化和流动求解。本课先采用串行网格流程，便于观察各阶段；复杂网格的并行运行将在并行计算章节介绍。

## 几何与背景网格

motorBike 的几何定义包含物体表面和一个空间加密盒：

```foam
geometry
{
    motorBike.obj
    {
        type triSurfaceMesh;
        name motorBike;
    }
    refinementBox
    {
        type box;
        min (-1.0 -0.7 0.0);
        max ( 8.0  0.7 2.5);
    }
}
```

物体表面参与切割、细化与贴合；`refinementBox` 用两个角点定义空间范围，后面用于局部体积加密。它在这里是加密控制区域，流动边界来自实际网格的 patch。

背景网格有 $20\times8\times8=1280$ 个单元，覆盖范围为 $x\in[-5,15]$、$y\in[-4,4]$、$z\in[0,8]$。先执行：

```bash
blockMesh > log.blockMesh 2>&1
```

背景网格应覆盖需要保留的外流区域。表面几何和背景域采用相同坐标系与长度单位。

## 特征边怎样提取

`surfaceFeatureExtractDict` 的关键部分为：

```foam
motorBike.obj
{
    extractionMethod extractFromSurface;
    includedAngle 150;
    subsetFeatures
    {
        nonManifoldEdges no;
        openEdges yes;
    }
    writeObj yes;
}
```

`extractFromSurface` 根据表面三角面之间的夹角提取特征；`includedAngle 150` 用于识别较明显的折角。按这一角度约定，平滑相接接近 $180^\circ$，较小夹角更容易被选为特征。`openEdges yes` 保留开放边，`writeObj yes` 额外写出便于查看的几何文件。

执行：

```bash
surfaceFeatureExtract > log.surfaceFeatureExtract 2>&1
```

生成的 `motorBike.eMesh` 被 `snappyHexMeshDict` 引用：

```foam
features
(
    {
        file "motorBike.eMesh";
        level 6;
    }
);
```

这段位于 `castellatedMeshControls`，使特征边附近达到指定细化等级。检查提取结果时，重点观察真正需要保留的尖角与轮廓是否完整，以及是否产生了大量无关细碎边。

## 表面与空间细化

motorBike 表面采用：

```foam
refinementSurfaces
{
    motorBike
    {
        level (5 6);
        patchInfo
        {
            type wall;
            inGroups (motorBikeGroup);
        }
    }
}
resolveFeatureAngle 30;
```

`level (5 6)` 给出最小和最大表面细化等级。一般表面交切位置细化到较低等级，遇到满足特征判据的角度变化时可采用更高等级。`patchInfo` 指定生成边界的网格类型与分组。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-snappy-refinement-level.png" alt="加密等级与单元尺度" loading="lazy"><figcaption><strong>加密等级与单元尺度</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 72 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

每增加一级，典型单元边长约减半，单个三维六面体可细分成 8 个子单元。若背景边长约为 $h_0$，第 $l$ 级对应：

$$
h_l\approx\frac{h_0}{2^l}.
$$

因此提高等级时，局部单元数增长很快。实际总量还取决于细化区域大小以及固体内部单元的移除。

空间加密设置为：

```foam
refinementRegions
{
    refinementBox
    {
        mode inside;
        levels ((1E15 4));
    }
}
nCellsBetweenLevels 3;
```

`mode inside` 表示加密盒内部达到 4 级；该模式使用条目中的等级，前面的距离值采用占位写法。`nCellsBetweenLevels 3` 在不同等级之间安排过渡，避免尺寸过于突变。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-snappy-surface-refinement.png" alt="几何表面附近的局部网格加密" loading="lazy"><figcaption><strong>几何表面附近的局部网格加密</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 76 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

本例用加密盒提高物体周围与下游区域的分辨率。分析尾迹时，可以按实际尾迹范围延长或调整加密区域，随后比较速度亏损、阻力等目标量的变化。

## 保留正确的流体区域

`castellatedMeshControls` 中还包含：

```foam
locationInMesh (3.0001 3.0001 0.43);
maxLocalCells 100000;
maxGlobalCells 2000000;
```

`locationInMesh` 指向应保留的流体区域内部。对于外流，点放在物体外部的背景域内。`maxGlobalCells` 是细化过程中的大致总单元上限，达到上限可能导致目标等级未完成；最终移除固体内部单元后，总量还会减少。`maxLocalCells` 主要影响并行细化时的负载平衡策略。

如果最终只剩物体内部网格，优先检查区域选择点；如果表面某处加密不足，检查单元上限、特征定义与细化日志。

## 分阶段生成并查看

第一阶段先关闭贴合与层网格：

```bash
foamDictionary system/snappyHexMeshDict -entry snap -set false
foamDictionary system/snappyHexMeshDict -entry addLayers -set false
snappyHexMesh -overwrite > log.snappy-castellated 2>&1
checkMesh > log.check-castellated 2>&1
touch motorBike.foam
```

`-overwrite` 将结果写回当前网格。此时在 ParaView 中查看流体域是否正确、物体轮廓是否完整，以及加密区域是否覆盖目标位置。表面呈阶梯状是这一阶段的典型特征。

然后关闭重复细化，启用贴合：

```bash
foamDictionary system/snappyHexMeshDict -entry castellatedMesh -set false
foamDictionary system/snappyHexMeshDict -entry snap -set true
snappyHexMesh -overwrite > log.snappy-snap 2>&1
checkMesh > log.check-snap 2>&1
```

第二次运行接着使用第一阶段的网格。修改几何或细化等级后，应重新从背景网格开始这一流程。

## 表面贴合的参数

motorBike 的 `snapControls` 中包含：

```foam
nSmoothPatch         3;
tolerance            2.0;
nSolveIter           30;
nRelaxIter           5;
nFeatureSnapIter     10;
implicitFeatureSnap  false;
explicitFeatureSnap  true;
```

`nSmoothPatch` 控制贴合前的边界平滑；`tolerance` 以局部最大边长为尺度确定吸附搜索距离；`nSolveIter` 与 `nRelaxIter` 控制网格位移求解与松弛。`explicitFeatureSnap true` 使用已提供的特征边，`nFeatureSnapIter` 控制特征贴合迭代。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-snappy-surface-snapping.png" alt="网格顶点向几何表面贴合" loading="lazy"><figcaption><strong>网格顶点向几何表面贴合</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 79 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

贴合后检查尖角是否保留、表面误差是否减小，以及局部单元质量是否恶化。背景分辨率不足时，应优先提高相应区域的细化等级；迭代次数主要影响已有网格点如何移动。

## 近壁层厚度怎样设置

官方例的 `addLayersControls` 包含：

```foam
relativeSizes true;
layers
{
    "(lowerWall|motorBike).*"
    {
        nSurfaceLayers 1;
    }
}
expansionRatio      1.0;
finalLayerThickness 0.3;
minThickness       0.1;
```

`layers` 按最终 patch 名匹配需要加层的壁面。正则表达式选中以 `lowerWall` 或 `motorBike` 开头的 patch。这里请求添加一层。

`relativeSizes true` 表示厚度参数相对于层外未变形的局部细化单元尺寸。`finalLayerThickness 0.3` 表示最外侧层厚度取该尺度的 0.3 倍；`minThickness 0.1` 是局部允许的最小厚度。`relativeSizes false` 则使用绝对长度。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-snappy-relative-layer-size.png" alt="相对与绝对层厚设置的网格对比" loading="lazy"><figcaption><strong>相对与绝对层厚设置的网格对比</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 139 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

需要多层时，可增加 `nSurfaceLayers`，并用 `expansionRatio` 控制相邻层厚度比。若首层厚度为 $h_1$，层数为 $n$，增长率为 $r$，总厚度为：

$$
H=h_1\frac{r^n-1}{r-1}\qquad(r\ne1).
$$

当 $r=1$ 时，$H=nh_1$。近壁分辨率最终还要结合所用湍流模型与计算后的 $y^+$ 评估；层数、首层中心距离和覆盖范围都要一起考虑。

## 添加层网格并检查

在已贴合的网格上执行：

```bash
foamDictionary system/snappyHexMeshDict -entry snap -set false
foamDictionary system/snappyHexMeshDict -entry addLayers -set true
snappyHexMesh -overwrite > log.snappy-layers 2>&1
checkMesh -allGeometry -allTopology > log.check-final 2>&1
```

<figure class="wolf-figure"><img src="/assets/wolf/wolf-snappy-layer-stage.png" alt="贴体网格中的边界层生成阶段" loading="lazy"><figcaption><strong>贴体网格中的边界层生成阶段</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 80 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

层网格可能在尖角、狭缝或质量约束较强的位置停止生长。查看日志中的实际加层情况，并在关键位置显示截面。本例的 `writeFlags` 包含 `layerSets` 和 `layerFields`，可辅助查看层数与覆盖分布。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-snappy-layer-coverage.png" alt="边界层厚度、层数与覆盖范围" loading="lazy"><figcaption><strong>边界层厚度、层数与覆盖范围</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 148 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

## 常见问题与调整顺序

| 现象 | 优先检查 |
| --- | --- |
| 找不到 `motorBike.eMesh` | 是否运行特征提取，表面名和路径是否一致 |
| 保留区域错误或网格几乎为空 | `locationInMesh`、表面封闭性和背景域范围 |
| 细化等级未达到设定值 | 单元上限、细化停止信息、目标区域定义 |
| 表面贴合不足 | 局部分辨率、几何细节尺度、特征提取及吸附参数 |
| 部分壁面没有层 | patch 名匹配、狭缝、局部曲率、厚度与质量限制 |
| 层添加后质量变差 | 降低局部厚度或增长率，改善层外网格和尖角处理 |

练习时，将三阶段的网格截面、单元数和质量统计分别保存。先比较 `level (5 6)` 与较低细化等级对几何细节的影响，再试着把一层改为三层并检查实际覆盖。这两项练习分别改变表面分辨率和近壁分辨率，能够看出参数在网格中的具体作用。

更多条目可对照 [v2512 注释版 snappyHexMeshDict](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/snappyHexMeshDict)。
