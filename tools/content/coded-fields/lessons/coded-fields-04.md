上一节在文件读取时生成了一组固定入口速度。这一节把相同公式放进 `codedFixedValue`，让 OpenFOAM 在更新边界时计算面上的速度。公式暂时保持不随时间变化，先熟悉这个边界类型的基本写法。

[下载 codedFixedValue 固定剖面算例](/downloads/programming/coded-fields-04-v2512.zip) · [上一节：codeStream 固定入口](/read/?slug=coded-fields-03)

## 1. 先把两种写法对应起来

| 项目 | `fixedValue` + `value #codeStream` | `codedFixedValue` |
| --- | --- | --- |
| 代码放置位置 | value 的内容中 | patch 的 code 条目中 |
| 代码执行时机 | 读取该字典条目时 | 需要更新边界系数时 |
| 获取当前边界 | 从网格按名称查找 | 直接调用 `patch()` |
| 设置边界值 | 写入 `os`，供字典读取 | 调用 `operator==(...)` 赋值 |
| 适用例子 | 固定空间分布、初值生成 | 固定或随时间变化的边界公式 |

`codedFixedValue` 会自动生成一个固定值边界类，编译成共享库，再交给求解器使用。完整类的构造、复制等常规接口由模板提供，你主要编写面值怎样计算。

<figure class="lesson-figure"><img src="/assets/science/coded-fields-steady.png" alt="两种入口实现的速度剖面与计算结果对比" loading="lazy"><figcaption>两种写法生成相同的固定入口剖面。<small>FoamLab，配套两组 v2512 计算。</small></figcaption></figure>

## 2. 在相同通道中更换入口类型

下载包的 `06-coded-steady` 沿用上一课网格、物性、初值、压力边界和求解设置。入口仍高 0.01 m，最大速度仍为 0.15 m/s。

打开 `0/U`，定位 `boundaryField/inlet`。完整入口块如下：

{{boundary:06-coded-steady}}

`type codedFixedValue` 选择动态编译边界。`name foamLabSteadyProfile` 是生成类型的名称，给这段边界代码一个明确标识。它与网格 patch 的名称不同：网格入口仍叫 `inlet`。

`value uniform (0 0 0)` 提供边界对象创建时的初始数值。进入边界更新过程后，下面的代码将按公式覆盖它。计算结果文件会写出边界的当前值及代码配置，供后续读取和重启使用。

## 3. `patch().Cf()` 直接取得当前面中心

代码开头是：

```cpp
const vectorField& centres = patch().Cf();
vectorField velocity(patch().size(), vector::zero);
```

此时正在执行的代码属于一个边界对象，这个对象已经知道自己附着在哪个 patch 上。因此可以直接使用 `patch()`，获得面数量、面中心、面积等信息。

`centres` 引用面中心列表；`velocity` 新建同样长度的向量字段，用来装计算结果。每个元素的编号都对应当前 patch 的局部面编号。

接下来的循环与上一节相同：

{{snippet:STEADY}}

每个面先计算相对高度 eta，再计算速度 x 分量。左右或上下换了 patch 名称时，这段代码仍通过 `patch()` 使用当前所附着的边界；剖面公式中的坐标方向和高度需要与新几何对应。

## 4. `operator==` 为什么写成这个样子

代码末尾的

```cpp
operator==(velocity);
```

调用了 OpenFOAM patch 字段的赋值接口，把整个向量列表写入当前边界。这里是在显式调用重载的运算符函数。普通 C++ 表达式 `a == b` 通常用于比较；本处这个接口由 OpenFOAM 定义为强制赋值。

当传入一个向量时，例如 `operator==(vector(0.1, 0, 0))`，所有面得到同一个值；当传入 `vectorField` 时，每个面得到列表中的对应值。本例使用后者表示非均匀剖面。

这也解释了与 `codeStream` 的输出方式差异：`codeStream` 要生成能被字典读取的文本；这里已经存在边界字段对象，可以直接更新数值。

## 5. 运行，比较两份结果

```bash
cd ~/OpenFOAM/foamLabCodedFields/06-coded-steady
bash Allrun
```

首次读取边界会生成 `dynamicCode/foamLabSteadyProfile` 中的代码。编译完成后，`icoFoam` 从 0 计算到 1 s，时间步 0.001 s，每 0.05 s 写出结果。

查看 `1/U` 的 inlet 部分。它包含 20 个面上的速度：最靠近壁面的面为 0.014625 m/s，中间两个面为 0.149625 m/s。入口面积平均速度为 0.100125 m/s，与上一节的离散剖面一致。

在 ParaView 中同时打开两组算例，选中相同时间、相同字段和色标范围。还可将两份 `inletMean/0/surfaceFieldValue.dat` 画在同一张图上，检查入口平均值。

若查看 0 时刻的边界，某些后处理读取路径会先显示 `value` 提供的初值。要看代码更新后的边界，可使用求解器保存的 0.05 s 及以后时间；本课的对比图取计算结果中的边界值。

## 6. 怎样由固定值变成时变值

当前 code 每次被调用时都会重新计算，但公式只使用面坐标，因此静止网格上结果保持相同。

加入当前时间后，就可以生成时间函数：

```cpp
const scalar t = this->db().time().value();
```

`db()` 访问所属对象注册表，`time()` 得到模拟时间对象，`value()` 返回当前物理时间数值。它对应 `controlDict` 中推进的时间，单位为秒。

下一课把这个 t 代入斜坡函数和正弦函数。每次边界更新读取当时的 t，得到当时应施加的入口速度。

## 7. 三个小修改，熟悉赋值方式

### 均匀速度入口

把 code 内全部内容改成：

```cpp
operator==(vector(0.1, 0, 0));
```

所有入口面均为 0.1 m/s。这里给出均匀写法是为了练习接口；固定均匀边界日常也可直接用 `fixedValue`。

### 固定线性剖面

在原来的循环中把计算式改为：

```cpp
velocity[faceI] = vector(0.1*eta, 0, 0);
```

入口速度从下缘的零逐渐增加到上缘的 0.1 m/s。若保持上壁面 `noSlip`，入口上缘附近会出现较强速度变化，内部流场将对此作出调整。用它做一个对照，可以看清入口与相邻壁面条件之间的关系。

### 标量温度边界

在一个温度场文件中，对应的赋值改为标量即可：

```foam
heatedWall
{
    type codedFixedValue;
    value uniform 300;
    name foamLabWarmWall;
    code
    #{
        operator==(320.0);
    #};
}
```

这段放在 `T` 的 `boundaryField` 下，`heatedWall` 应替换为实际网格边界名。求解器需要读取并求解温度场，例如前两课的热扩散算例。边界所在字段决定模板使用标量还是向量。

## 8. 编译错误从哪里看

| 日志中的信息 | 对应处理 |
| --- | --- |
| 找不到 `g++` 或 `wmake` | 加载完整 v2512 开发环境，安装系统 C++ 编译工具 |
| `fvCFD.H: No such file or directory` | 核对 codeOptions 的头文件目录与环境变量 |
| 提示某行 C++ 语法错误 | 打开日志指定的生成源码，对照 0/U 中相应 code 代码 |
| `Unknown patchField type` | 检查 type 的拼写，入口应为 codedFixedValue |
| 参数改了，旧结果仍相同 | 在独立新工况中从 0 开始计算，再读取新生成的时间目录 |

日志先报告尝试加载动态库，接着报告创建和编译库，这是首次运行的正常步骤。出现真正的编译错误时，查看 `Failed wmake` 之前的第一条编译器报错，通常会给出文件和行号。

## 参考

[v2512 codedFixedValue 接口](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/finiteVolume/fields/fvPatchFields/derived/codedFixedValue/codedFixedValueFvPatchField.H) · [动态边界代码模板](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/codeTemplates/dynamicCode/fixedValueFvPatchFieldTemplate.C)。
