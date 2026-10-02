# 各类网格专题维护记录

入口：`/topics/meshes/`。原有 `/topics/meshing/` 和 `/topics/dynamic-mesh/` 保留，目录节点移动到“各类网格”下面。新增重叠、动态加密、旋转 AMI、MRF/SRF 四个子目录。

六篇课程使用同一系列“高级网格与旋转流动”，每篇的 `section_ids` 指向具体子目录。后台选择目录即可查看或添加课程；标题、正文和多位置归属仍由原有内容管理功能维护。

## 文件与重建

- `lessons/`：课程文字与文件引用模板。
- `modules/`：分类介绍。
- `sections.json`：目录节点快照。
- `validation.json`：本次 VMware v2512 运行与数值检查结果。
- `../build-advanced-mesh.py`：从固定 v2512 源码包提取并调整教学算例。
- `../check-advanced-mesh.py`：读取 VM 导出的 VTK，检查网格、字段、守恒量与参考系关系，并生成结果图。
- `../build-advanced-mesh-content.py`：把实际算例文件填入课程模板，输出内容 JSON、静态分类入口和带修订号检查的数据库草稿/发布 SQL。
- `../../check-advanced-mesh-ui.cjs`：隔离浏览器检查三级目录、阅读、下载、移动端和后台位置筛选。

首次构建采用 `.openfoam-work/replan/openfoam-v2512.tar.gz`，归档内目录为 `openfoam-OpenFOAM-v2512/`。下载包保留官方原文件版权头和 GPL 许可证，文字示例省略页眉装饰。

VM 输入、运行日志及 VTK 位于 `F:/UbuntuShareFolder/.foamlab-build/advanced-mesh/`，完整最终结果为 `results-final/`。主运行目录是 guest 的 `/home/shark/foamlab-advanced-mesh-20261003-final/`；重叠网格居中后的最终版本在 `/home/shark/foamlab-advanced-mesh-20261003-centred/02-overset/`。

## 本次计算

| 算例 | 求解器 | 结束时间或迭代数 | 单元数 |
| --- | --- | --- | --- |
| 移动锥体 | pimpleFoam | 0.003 s | 1900 |
| 居中旋转物体的重叠网格 | overPimpleDyMFoam | 0.28 s | 881 |
| 动态界面加密 | interFoam | 0.3 s | 4032 → 8834 |
| 旋转 AMI | pimpleFoam | 0.5 s | 3072 |
| MRF | simpleFoam | 500 次 | 3072 |
| SRF | SRFSimpleFoam | 1000 次 | 33600 |

六个 Allrun 均实际完成网格生成、初始场处理、求解、检查及 VTK 导出。重叠网格每次分类总数等于网格总数。MRF 与 SRF 初始和最终网格坐标相同；SRF 的 U、Urel 与角速度叉乘位置关系通过导出数据检查。

动态加密的普通网格检查通过。`-allGeometry` 检查额外把 336 个含共面分裂面的单元报告为 concaveCells；v2512 `primitiveMesh::checkConcaveCells` 中条件包含 planar face。全部 492 个导出的多面体都通过逐面半空间凸性检查，最大越界距离为 0，体积为正。课程中解释了这一具体诊断。

重新计算后更新下载包、图片和 manifest，再生成内容 JSON。数据库 SQL 为此次首次发布准备，修订号保护会阻止直接覆盖后续后台修改。未来编辑应使用后台或根据当时修订号生成增量更新。

发布顺序：计算与检查 → 页面预览 → 写入隐藏目录及草稿 → Hexo 发布静态文件 → 核对线上资源 → 发布草稿并移动原目录。
