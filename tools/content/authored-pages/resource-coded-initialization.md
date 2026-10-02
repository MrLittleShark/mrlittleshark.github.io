![从初值到时间推进](/assets/diagrams/programming-13.svg)

复杂初值不一定需要开发独立求解器。`OF_material/101programming/codeStream_INIT/elliptical_IC` 在 `internalField` 中使用 `#codeStream`，读取网格中心后生成标量列表。这一机制在字典读取期间编译并执行代码，与时间循环中反复更新的边界条件不同。

## 从几何定义到单元判断

椭圆内域满足

$$\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}\leq1.$$

原例取中心 `(0.5,0.5)`、半轴 `0.3` 与 `0.15`。对每个单元中心计算该判据，内部赋 1，外部赋 0。示意实现为：

```cpp
scalarField alpha(mesh.nCells(), 0);
forAll(alpha, celli)
{
    const vector& c = mesh.C()[celli];
    scalar q = sqr((c.x()-0.5)/0.3) + sqr((c.y()-0.5)/0.15);
    alpha[celli] = q <= 1 ? 1 : 0;
}
alpha.writeEntry("", os);
```

这里的 `writeEntry("", os)` 将结果作为当前字典条目的值输出，不是在磁盘上创建另一份独立场文件。原例的 `codeInclude` 提供头文件，`codeOptions` 提供编译包含目录，`codeLibs` 提供链接库，三者分别对应编译依赖中的不同阶段。

## 为什么初始化仍然有离散误差

单元中心判据把每个单元整体设为 0 或 1，不等于精确计算椭圆与单元的交叠体积分数。因此边界呈现阶梯形，积分 $\sum_P\alpha_PV_P$ 与几何体积存在网格误差。加密网格后比较积分与 $\pi ab$ 乘实际厚度，才能定量评估初值表示。

若需要平滑过渡，可令 $\alpha$ 随带符号距离平滑变化，但这会改变初始界面厚度和体积，需要重新归一化或评估。不能把平滑图像直接等同于更准确的几何体积分数。

## v2512 使用注意

检查相名称与场名称是否一致。该材料保留部分旧文件头，例如文件名为 `alpha.phase1` 而头中的 `object` 仍可能写 `alpha.water`；运行前应与 `transportProperties` 中 phases、求解器读取字段及边界名称交叉核对，而不是只改一个文件名。

动态代码需要可写的编译目录和完整开发环境。应只执行可信算例中的 C++；这类条目是程序代码，不是纯数值配置。原资料脚本会恢复 `0_org` 并清理旧结果，因此使用独立副本。

## 三种初始化方法怎样选择

| 方法 | 合适情形 | 主要检查 |
| --- | --- | --- |
| uniform / nonuniform | 直接给定场值 | 列表长度、量纲和 patch |
| setFields | 基于已有几何选择规则赋值 | 区域覆盖顺序及字段名 |
| codeStream | 自定义解析几何或空间函数 | 编译接口、网格引用和输出类型 |

[下载含 cylinder、elliptical_IC、rayleigh_taylor 的精选源包](/downloads/programming/OF_material-v2512-selected-examples.zip)。本页依据 v2512 适配材料解释代码，目录内历史迁移报告与本次逐例编译证据应分别阅读。
