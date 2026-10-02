`checkMesh` 检查网格的连接关系、几何尺寸和单元质量。生成网格、导入其他软件的网格，或进行网格变形后，都可以用它查找负体积、错误连接、非正交和偏斜等问题。

## 先运行基本检查

在算例根目录执行：

```bash
checkMesh > log.checkMesh 2>&1
less log.checkMesh
```

日志通常依次给出网格统计、拓扑检查、几何检查和最终汇总。对于基础方腔，应先核对 400 个单元、正确的包围盒和二维求解方向，再阅读质量指标。

需要更完整的几何与拓扑检查时运行：

```bash
checkMesh -allGeometry -allTopology > log.checkMesh-full 2>&1
```

`-allGeometry` 增加几何相关检查，`-allTopology` 增加拓扑相关检查。日志较长，可以先搜索关键条目：

```bash
grep -nE 'cells:|Bounding box|non-orthogonality|skewness|Failed|Mesh OK' \
    log.checkMesh-full
```

`grep -E` 将竖线分隔的多个模式作为“或”处理；`-n` 输出行号，方便回到完整日志阅读上下文。

## 网格统计告诉我们什么

| 项目 | 关注内容 |
| --- | --- |
| 点、面、单元数量 | 是否符合预期分辨率，有无异常增长或大量单元丢失 |
| 包围盒 | 几何单位、位置和计算域范围 |
| patch 列表 | 入口、出口、壁面是否完整，名称是否与场文件一致 |
| 单元类型 | 六面体、棱柱、四面体和一般多面体的数量 |
| 连通区域数量 | 流体域是否按预期连通 |
| 有效几何方向与求解方向 | 二维、轴对称或三维设置是否一致 |

外流网格中单元总数减少可能来自固体内部单元被移除；内流网格出现两个连通区域则可能意味着通道被意外封堵。应结合所建物理域解释统计，而不是仅看数量大小。

## 单元体积与拓扑

单元必须具有正体积，面与单元的连接也必须一致。负体积意味着局部网格翻转或顶点顺序错误，零体积常见于点重合或单元塌缩。这类问题会破坏离散方程的几何基础，应回到网格生成步骤修复。

对于 `blockMesh`，优先检查顶点顺序和坐标；对于贴体网格，检查尖角、狭窄缝隙及表面吸附造成的畸变；对于动网格，检查位移幅度及网格运动后的局部单元形状。

## 非正交角

两个相邻单元的中心连线为 $\mathbf d$，公共面的面积向量为 $\mathbf S_f$。非正交角可表示为：

$$
\theta=\cos^{-1}\left(
\frac{\mathbf S_f\cdot\mathbf d}
{|\mathbf S_f|\,|\mathbf d|}
\right).
$$

面积向量垂直于面，方向由面法向决定。理想正交网格中，单元中心连线与它平行，因此 $\theta=0$。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-mesh-nonorthogonality.png" alt="非正交角的几何定义" loading="lazy"><figcaption><strong>非正交角的几何定义</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 16 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

有限体积方法需要计算面上的法向梯度。正交网格可直接利用两个单元中心的差分；非正交网格需要额外修正，角度越大，修正项通常越重要，离散误差与求解困难也可能增加。

日志会给出最大角和平均角。平均值反映整体状况，最大值指出最差局部；少量高非正交面如果集中在分离点、界面或壁面附近，仍可能影响目标结果。

## 偏斜与非正交有什么区别

偏斜关注单元中心连线与面的交点，相对于实际面心的偏移。即使面法向与中心连线夹角很小，面心也可能偏离插值位置。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-mesh-skewness.png" alt="面心偏斜与非正交性的区别" loading="lazy"><figcaption><strong>面心偏斜与非正交性的区别</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 17 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

非正交主要影响法向梯度和扩散项处理；偏斜还会影响从单元中心插值到面心的精度。两者描述不同的几何特征，需要分别查看。

`checkMesh` 报告的偏斜度是按相应尺度归一化的指标。比较不同网格时应采用相同工具和定义，避免把其他网格软件采用的偏斜指标直接套用到这里。

## 长宽比与尺寸过渡

高长宽比表示某个方向的单元尺度显著大于其他方向。近壁层通常沿壁面较长、沿壁面法向较薄，这与边界层的物理梯度分布相适应。判断时还要看单元方向是否与主要梯度相匹配，以及非正交、偏斜是否保持合理。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-mesh-wall-alignment.png" alt="近壁单元方向与面值插值" loading="lazy"><figcaption><strong>近壁单元方向与面值插值</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 20 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

相邻单元尺寸突变会使插值与梯度重构更困难。可以用 `blockMesh` 的渐变控制或 `snappyHexMesh` 的等级过渡层，让网格从细区逐步过渡到粗区。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-mesh-smooth-transition.png" alt="网格尺寸的突变与平滑过渡" loading="lazy"><figcaption><strong>网格尺寸的突变与平滑过渡</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 19 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

因此同样的单元总数，分布方式和几何质量可能带来不同的结果。网格设计应同时考虑关注区域的分辨率与相邻单元的平滑过渡。

## 把问题位置写出来

只看最大值难以判断问题在哪，可以输出质量场：

```bash
checkMesh -constant -writeFields '(nonOrthoAngle)' \
    > log.checkMesh-fields 2>&1
```

`-constant` 选择基础网格；`-writeFields` 指定要写出的质量场列表。`nonOrthoAngle` 可用于查看非正交问题在空间中的分布。多个质量指标可按工具帮助提供的字段名配置。

希望输出全部可用质量场，可以使用：

```bash
checkMesh -constant -writeAllFields > log.checkMesh-allFields 2>&1
```

检查失败时，工具还可能生成相应的点、面或单元集合。使用下面的选项将所生成的诊断集合导出为 VTK：

```bash
checkMesh -allGeometry -allTopology -writeSets vtk \
    > log.checkMesh-sets 2>&1
```

在 ParaView 中打开日志提示的输出文件，叠加显示几何和网格，确定问题集中在哪些部位。诊断文件名和数量取决于实际触发的检查。

## 使用自己的质量标准

`checkMesh -meshQuality` 会读取 `system/meshQualityDict` 中的质量标准。motorBike 等官方网格算例提供了这份字典，可以在相近案例的完整配置上调整。

```bash
checkMesh -meshQuality > log.checkMesh-quality 2>&1
```

这类标准用于网格质量控制。合适的阈值取决于方程、离散格式、计算目标和网格生成方法。把标准放宽只会改变检查是否通过，单元几何本身仍需由网格操作改善。

## 网格质量与数值格式的配合

基础方腔采用正交网格，因此 `fvSchemes` 使用：

```foam
laplacianSchemes
{
    default Gauss linear orthogonal;
}
snGradSchemes
{
    default orthogonal;
}
```

对于具有明显非正交性的网格，需要选择适合的法向梯度处理，例如在相应算例中使用 `corrected` 或受限修正，并配合压力方程的非正交校正设置。网格改善和数值修正共同决定计算表现；强烈畸变时，优先修复几何质量通常更有效。

## 动手练习

对上一课的三份方腔网格分别运行完整检查。把单元数、包围盒、最大非正交角、最大偏斜度和长宽比整理在同一张表中。

均匀加密会增加单元数，正交性仍应保持。沿坐标方向进行渐变也可以保持正交，但最小尺寸和长宽比会变化。随后显示网格与质量场，观察这些指标对应的实际几何。

最终还需要比较中心线速度等目标量随网格加密的变化。`Mesh OK` 表示网格通过了本次启用的检查；结果对网格分辨率的敏感性由这种计算对比给出。
