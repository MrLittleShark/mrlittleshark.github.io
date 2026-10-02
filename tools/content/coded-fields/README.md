# codeStream 与可编程边界课程源文件

公开入口：`/programming/coded-fields/`。目录键 `coded-fields`，父目录 `programming`。
六篇课程的 slug 为 `coded-fields-01` 至 `coded-fields-06`，正文模板位于 `lessons/`。

编辑顺序：

1. `tools/content/build-coded-fields.py` 生成九个干净算例及下载 ZIP；输出到独立的 `.foamlab-build/coded-fields/source`，保留用户提供的原资料。
2. 将算例复制到加载了 OpenFOAM v2512 的 Linux 个人目录，运行各例 `bash Allrun`。分别保留初始 VTK、求解日志、保存场与 postProcessing。
3. `tools/content/check-coded-fields.py` 读取此次虚拟机计算结果，检查初值、均值、通量、重启、并行差异，生成六张图、CSV、验证记录并重新打包。
4. `tools/content/build-coded-fields-content.py` 把正文中的 `file`、`boundary`、`snippet` 占位符替换为已运行的代码，生成 `tools/content/coded-fields-content.json`。不要直接发布未展开的 Markdown 模板。
5. `node tools/check-rebuild.cjs` 检查链接与内容，构建后运行 `tools/check-coded-fields-ui.cjs` 检查目录、正文、下载和后台位置。

数据库中的正文可在管理后台直接维护。重新导入前先读取当前 revision，保留后台修改。内容生成器输出的 SQL 仅用于首次创建隐藏目录与草稿，不会自动执行，也不覆盖已有页面。发布顺序为先上线图片与附件，再将六篇草稿及目录一并公开。

固定剖面与脉动剖面的图使用真实计算值；空间图保留 x/y 坐标的实际比例。案例初值的 VTK 为浮点文本，公式检查按其输出精度设置容差；计算中的入口均值使用高精度函数对象数据。
