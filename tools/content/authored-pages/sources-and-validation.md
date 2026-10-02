本站课程使用 **OpenFOAM v2512**。

| 资料 | 内容与入口 |
| --- | --- |
| OpenFOAM 官方文档 | [v2512 下载目录](https://dl.openfoam.com/source/v2512/)、[源码与教程](https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512) |
| Wolf Dynamics 培训 | [基础培训讲义与算例](https://www.wolfdynamics.com/tutorials.html?id=181&layout=edit)，用于有限体积方法、网格和流动模型教学 |
| Basic OpenFOAM Programming Tutorials | Artur K. Lidtke 及贡献者编写的 C++ 实例，见[编程资料](/read/?slug=resource-basic-programming) |
| OF_material | 网格、求解器和边界条件实例，见[资料目录](/read/?slug=resource-of-material-catalog) |

## 图片与源码

Wolf 基础培训配图在图下标注原作者、页码和 CC BY-SA 4.0 许可；裁剪仅用于突出相关内容。OpenFOAM 和 BasicOFProgramming 的源码包保留原版权头与 GPL 许可证。

方腔、标量输运等计算图在相应课程中给出计算设置。封面为 CFD 主题插画。

## 本站方腔示例

![方腔网格](/assets/science/cavity-mesh.png)

采用 `icoFoam`，网格为 $20\times20\times1$，计算至 $t=0.5\,\mathrm{s}$。顶盖速度为 $1\,\mathrm{m/s}$，边长为 $0.1\,\mathrm{m}$，运动黏度为 $0.01\,\mathrm{m^2/s}$，因此 $\mathrm{Re}=10$。

[课程与配置](/read/?slug=first-cavity-result) · [日志与绘图脚本](/read/?slug=resource-cavity-evidence)

## 引用与纠错

引用本站内容时，请附文章名称和链接。反馈示例问题时，可在评论区提供相关文件、运行命令和错误日志。
