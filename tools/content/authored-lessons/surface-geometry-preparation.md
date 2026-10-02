复杂几何通常从 CAD 导出为 STL 或 OBJ 表面，再用 `snappyHexMesh` 生成流体体网格。准备表面时，最重要的是尺寸正确、目标流体区域明确，以及表面连接满足网格生成要求。

## CAD、表面网格与体网格

| 数据 | 描述内容 | 常见格式 |
| --- | --- | --- |
| CAD 几何 | 曲线、曲面、实体及其拓扑关系 | STEP、IGES 等 |
| 离散表面 | 用三角形或多边形近似物体表面 | STL、OBJ |
| 流体体网格 | 填充流体区域的单元及其连接关系 | `constant/polyMesh` |

`snappyHexMesh` 利用表面的位置对背景体网格进行细分、切割和贴合。表面三角形决定几何近似，体网格单元决定流场的空间离散，二者的分辨率需要相互配合。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-snappy-background.png" alt="表面几何与背景六面体网格" loading="lazy"><figcaption><strong>表面几何与背景六面体网格</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 74 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

例如外流绕过摩托车时，表面文件描述摩托车，背景网格描述周围空气。流体域是背景域中位于物体外部的部分。内流问题则需要保留管道内部的流体空间，并区分入口、出口和壁面。

## 读取 motorBike 的表面

课程网格案例包中包含 `tutorials/incompressible/simpleFoam/motorBike`，以及位于 `tutorials/resources/geometry` 中的表面资源。若使用本机官方教程，在 motorBike 工作副本内执行：

```bash
mkdir -p constant/triSurface
cp "$FOAM_TUTORIALS/resources/geometry/motorBike.obj.gz" \
    constant/triSurface/
surfaceCheck constant/triSurface/motorBike.obj.gz \
    > log.surfaceCheck 2>&1
less log.surfaceCheck
```

`constant/triSurface` 是本例存放表面的目录。`.gz` 表示压缩文件，相关读取程序可处理这种压缩表面。`snappyHexMeshDict` 中使用 `motorBike.obj` 作为几何条目名，与这个表面对应。

`surfaceCheck` 报告点和面的数量、包围盒、表面连通情况及几何问题。先核对尺寸，再查看边和面的连接检查。

## 单位错误怎样影响计算

STL 文件通常只保存坐标数值，不提供可靠的物理单位。假设某管道内径在 CAD 中为 $10\,\mathrm{mm}$，导出的坐标跨度为 10，而 OpenFOAM 按米使用坐标，就会得到内径 $10\,\mathrm{m}$ 的模型。

在相同速度和运动黏度下，雷诺数与特征长度成正比：

$$
Re=\frac{UD}{\nu}.
$$

几何长度放大 1000 倍，雷诺数也会放大 1000 倍，面积和体积分别放大 $10^6$ 与 $10^9$ 倍。压力损失、流量和计算成本都会受到影响。

对于确认采用毫米坐标的 `pipe-mm.stl`，可以生成以米为单位的新文件：

```bash
surfaceTransformPoints -write-scale '(0.001 0.001 0.001)' \
    pipe-mm.stl pipe-m.stl
surfaceCheck pipe-m.stl
```

`-write-scale` 的三个数分别缩放 $x$、$y$、$z$ 坐标；输入和输出使用不同文件名，原始表面得以保留。这是毫米管道的换算示例。motorBike 已有自己的尺度，应根据实际包围盒判断是否需要变换。

`blockMeshDict` 的 `scale` 只缩放该字典中的背景网格坐标。表面文件需要独立采用相同的长度单位。背景域和表面分别检查后，再放到同一视图中对齐。

## 怎样判断表面是否封闭

对普通封闭三角表面，每条边应由两个三角形共享。只有一个相邻三角形的边称为开放边；超过两个相邻三角形的边属于非流形连接。

| 问题 | 常见来源 | 对网格的影响 |
| --- | --- | --- |
| 意外开放边 | CAD 曲面缝隙、缺失面 | 流体区域可能通过裂缝连通 |
| 重复面 | 重复导出或重叠零件 | 表面求交与区域判断可能异常 |
| 退化三角形 | 点重合、极短边 | 法向与几何交点计算困难 |
| 非流形边 | 多块表面不正确拼接 | 内外关系不明确 |
| 自交 | 曲面穿插或低质量修补 | 表面包围区域可能不一致 |

可以启用自交检查：

```bash
surfaceCheck -checkSelfIntersection constant/triSurface/motorBike.obj.gz \
    > log.surfaceCheck-intersection 2>&1
```

开放边是否有问题取决于建模方式。内流管道的入口可能在 CAD 导出时有意开口，随后通过端面形成计算域边界；几何上的随机裂缝则需要修补。修补时保留设计的入口、出口和必要的区域划分。

## 选择流体域

motorBike 的背景域由 `blockMeshDict` 给出，范围为：

```text
x: -5 到 15
y: -4 到 4
z:  0 到 8
```

长度单位为米，地面位于 $z=0$。`snappyHexMeshDict` 中使用以下条目指定保留区域中的一个点：

```foam
locationInMesh (3.0001 3.0001 0.43);
```

这个点位于背景域内、物体外部的流体区域。算法保留与它连通的区域。内流算例应把点放在管道内部；存在多个互不连通的流体区域时，需要按多区域建模要求处理。

选点时在 ParaView 中同时显示表面和背景网格，再用点坐标确认位置。点应位于单元内部，并与物体表面保持明确间距，避免正好落在面上。

## 几何细节保留到什么程度

几何简化应围绕要计算的量展开。控制分离的尖角、狭缝和喷口会明显改变流动，需要保留；远离关注区域、远小于网格尺度的装饰倒角，通常可以考虑简化。

表面三角化时，曲率较大处需要较小三角形，以控制曲面与离散表面的距离误差。平坦区域可以使用较大三角形，减少文件体积和几何求交成本。

若一个窄缝的宽度为 $g$，而局部体网格宽度接近或大于 $g$，单纯增加表面三角形数仍难以解析缝内流动。应同时考虑缝内需要多少体单元、是否需要局部加密，以及该细节在物理模型中是否应保留。

## 表面名称与边界划分

STL 可以包含多个区域，OBJ 也可通过分组区分表面部分。这些区域有助于生成不同 patch，例如壁面、入口或不同材料表面。

motorBike 的几何定义片段为：

```foam
geometry
{
    motorBike.obj
    {
        type triSurfaceMesh;
        name motorBike;
    }
}
```

`motorBike.obj` 对应表面文件，`type triSurfaceMesh` 选择三角表面读取，`name motorBike` 给这个可搜索表面命名。后续 `refinementSurfaces` 使用同一个名称配置表面细化。最终 patch 名还可能包含原表面区域名，应以生成后的 `constant/polyMesh/boundary` 为准。

## 动手练习

先运行 motorBike 的 `surfaceCheck`，记录包围盒和表面区域名，再生成背景网格，在 ParaView 中叠加显示两者。观察物体与入口、出口、侧面和顶部的距离，并定位 `locationInMesh`。

接着用自己的一份 CAD 表面进行同样检查：记录 CAD 单位、导出坐标范围和背景网格范围。如果进行了缩放，核对缩放后的已知尺寸，例如管径、翼弦或物体高度。

几何准备结束时，应能明确指出流体位于表面的哪一侧、各边界的物理含义，以及最需要加密的部位。下一课将把这些信息写入 `snappyHexMeshDict`。
