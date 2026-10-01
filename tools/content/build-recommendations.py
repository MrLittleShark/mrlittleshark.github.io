"""Build the curated resource directory; no network or database writes."""
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECKED_ON = "2026-10-02"
RECORDS = []


def add(slug, title, track, summary, url, source, version, verification,
        audience, use, sequence, exercise, links=(), diagram="workflow", cost_note="所列文档或公开资料可免费阅读；软件的许可条件以项目说明为准。"):
    def p(text):
        return f"<p>{escape(text)}</p>"

    body = (
        f'<p class="source-note">{escape(source)} · 核对日期：{CHECKED_ON}</p>'
        + p(summary)
        + "<h2>用途与适用对象</h2>" + p(use) + p(audience)
        + "<h2>阅读与使用顺序</h2><ol>"
        + "".join(f"<li>{escape(step)}</li>" for step in sequence) + "</ol>"
        + "<h2>建议练习</h2>" + p(exercise)
        + "<h2>版本与适用范围</h2>" + p(version) + p(cost_note)
        + "<h2>资源入口</h2><ul>"
        + "".join(f'<li><a href="{escape(link, quote=True)}">{escape(label)}</a></li>'
                  for label, link in [(title, url), *links]) + "</ul>"
        + p("链接核对：" + verification)
    )
    RECORDS.append({
        "slug": "recommend-" + slug,
        "kind": "recommendation",
        "title": title,
        "summary": summary,
        "body": body,
        "track": track,
        "series": "资源推荐",
        "status": "published",
        "sort_order": len(RECORDS) * 10,
        "cover_url": f"/assets/diagrams/reference-{diagram}.svg",
        "metadata": {
            "external_url": url,
            "resource_type": "recommendation",
            "cost": "free",
            "cost_note": cost_note,
            "source": source,
            "verification": verification,
            "checked_on": CHECKED_ON,
            "version_note": version,
            "format": "html",
        },
    })


add(
    "openfoam-v2512-release", "OpenFOAM v2512：版本发布与变更记录", "官方文档",
    "查询 v2512 的发布范围、新增功能与版本入口，用于建立明确的学习和复现基线。",
    "https://www.openfoam.com/news/main-news/openfoam-v2512", "OpenCFD / OpenFOAM 官方网站",
    "本站以 OpenCFD 的 v2512 为基准。OpenFOAM Foundation 的数字版本（如 9）属于另一发行分支，版本号、求解器组织和字典接口不能直接等同。发布页可能补充较新的下载方式，应继续选择 v2512 对应文件。",
    "官方域名搜索结果已核对发布页及正文；自动直接读取该页面受到 HTTP 403 限制。官方版本历史页的 v2512 源码和 API 链接另经 HTTP 请求核对。",
    "适合初学者确认安装版本，也适合已有算例的维护者检查升级影响。",
    "发布说明说明一个版本发生了什么变化，可用于定位后续需要阅读的模型、网格、数值方法或开发接口说明。它不能替代某个算例的配置与验证。",
    ["先确认发行方与版本号，再记录本地环境的 WM_PROJECT_VERSION。", "按正在使用的求解器或模型阅读对应变更类别。", "沿官方版本历史进入同一版本的源代码、API 和手册。"],
    "为一个现有算例建立版本记录，写明发行方、v2512、求解器、所加载的扩展库，以及运行环境；升级时以此作为对照。",
    [("官方版本历史", "https://www.openfoam.com/download/release-history")],
)

add(
    "openfoam-v2512-userguide", "OpenFOAM v2512：用户手册", "官方文档",
    "按算例文件、网格、离散格式、求解控制与后处理建立基本知识框架。",
    "https://dl.openfoam.com/source/v2512/UserGuide.pdf", "OpenCFD / 官方 v2512 下载目录",
    "入口固定在 v2512 下载目录。手册用于解释通用结构；具体模型可用的关键字和默认值仍需与 v2512 教程、运行帮助及源码相互核对。",
    "官方 v2512 目录列出了 UserGuide.pdf；下载链接 HTTP 200，可重定向至 SourceForge 文件分发服务。使用此稳定入口，不保存带时效参数的重定向地址。",
    "适合刚开始使用 OpenFOAM 的读者，以及需要系统梳理配置关系的用户。",
    "用户手册适合解释文件之间的关系：初始场在何处定义，网格如何组织，数值格式和求解控制各负责什么。阅读时应同时打开一个官方算例。",
    ["先阅读算例目录和文件语法，辨认 0、constant、system。", "随后学习网格生成、离散格式与线性求解控制。", "最后结合运行日志和后处理结果检查一个完整计算流程。"],
    "选取一个小型不可压缩算例，逐项标记 controlDict、fvSchemes、fvSolution 和初始场对计算过程的作用，并说明各自修改后应检查的日志或结果。",
    [("v2512 官方下载目录", "https://dl.openfoam.com/source/v2512/")],
    diagram="3",
)

add(
    "openfoam-v2512-source", "OpenFOAM v2512：固定版本源代码", "源码与开发",
    "从固定标签阅读应用程序、库、运行时选择表和教程，避免在不同版本之间混用接口。",
    "https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512", "OpenFOAM 官方 GitLab 仓库",
    "链接固定为 OpenFOAM-v2512 标签，而非随开发持续变化的主分支。第三方模块、个人补丁和另行安装的扩展库需要独立记录版本。",
    "官方 GitLab 标签入口可访问；本站命令与配置目录另已依据该标签的源码归档清点应用程序并提取教程示例。",
    "适合准备修改求解器、边界条件或函数对象的用户；初学者也可用它确认一个关键字的真实读取位置。",
    "源代码是核对类型名称、字典读取和执行顺序的主要依据。阅读时先从正在运行的应用程序出发，再进入调用到的库，通常比从整个源码树顺序浏览更有效。",
    ["在 applications 中找到求解器的入口文件和 Make 配置。", "在 src 中追踪相关类、运行时注册以及字典读取代码。", "返回 tutorials，观察同一模型在完整算例中的使用方式。"],
    "追踪一个已知边界条件：找到类型注册、构造函数、字典条目和更新系数方法，画出从配置到执行的调用关系，并记录源码路径。",
    diagram="9",
)

add(
    "openfoam-v2512-api", "OpenFOAM v2512：C++ API 文档", "源码与开发",
    "通过类、成员函数、继承关系与源码链接定位开发接口。",
    "https://api.openfoam.com/2512/", "OpenCFD / OpenFOAM 官方 API 文档",
    "使用路径中的 2512 确认 API 版本。API 页面描述编译接口，不保证复制其他发行分支的代码后即可编译；应同时核对头文件、链接库和运行时注册方式。",
    "该入口由官方版本历史页链接；本地 HTTP 请求返回 200。网页检索工具未能解析其正文，因此未据此推断未核实的具体 API 行为。",
    "适合具有基本 C++ 知识的求解器、边界条件和后处理工具开发者。",
    "API 文档可缩小源码搜索范围，帮助区分类所属命名空间、基类与接口。接口的数值或物理意义仍需结合实现代码与模型文献判断。",
    ["先确定要寻找的类或函数名称。", "查看其声明、基类与成员函数，再进入实现文件。", "在固定版本教程或应用程序中查找实际调用示例。"],
    "选择一个体积场相关类型，记录声明位置、所属命名空间及一个实际调用它的求解器；说明该类型所表示的数据及其所在网格位置。",
    [("v2512 固定版本源代码", "https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512")],
    diagram="9",
)

add(
    "openfoam-v2512-tutorials", "OpenFOAM v2512：官方算例库", "教程与课程",
    "查找完整、可追溯的模型配置与算例脚本，作为学习和修改算例的起点。",
    "https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials", "OpenFOAM 官方 GitLab 仓库",
    "固定标签中的配置与本站 v2512 基线一致，但算例仍可能依赖外部网格工具、额外模块、并行环境或较长计算时间。教程的存在不表示本站已经完整运行了每个算例。",
    "官方 GitLab 教程目录入口可访问；本站已从同一标签归档提取完整配置文件，并记录算例路径与文件校验值。",
    "适合需要查看真实配置的所有学习者，尤其适合准备从相近物理问题修改算例的用户。",
    "官方算例包含文件之间的依赖关系。仅复制一个字典通常不足以重建算例，还应检查初始场、包含文件、网格来源以及运行脚本。",
    ["根据物理模型和求解器选择相近的小型算例。", "复制到自己的工作目录，阅读 README、Allrun 和初始文件。", "先运行原始配置并保存日志，再逐项修改并比较结果。"],
    "为一个小型算例整理执行依赖表：网格生成、初始化、求解和后处理各读取哪些文件、生成哪些输出；不要直接在安装目录中修改原始教程。",
    diagram="workflow",
)

add(
    "wolf-introductory-training", "Wolf Dynamics：OpenFOAM 入门培训资料", "教程与课程",
    "配合讲义、视频和算例学习 Linux、算例操作与有限体积法，并对照 v2512 完成版本迁移。",
    "https://www.wolfdynamics.com/tutorials.html?id=181&layout=edit", "Wolf Dynamics / Joel Guerrero",
    "官方页面明确说明这套公开培训材料基于 OpenFOAM 9，来自 2021 年课程。概念、方法与许多操作思路可参考，命令选项、模型名、字典结构和源码接口需要逐项对照 v2512。",
    "官方培训资料页面已直接读取，已核对 OpenFOAM 9 版本说明、视频入口、讲义与算例的 figshare 链接。",
    "适合希望按照课程顺序学习、同时愿意完成版本核对的初学者。",
    "这套资料适合将演示、理论和上机练习结合起来。建议把讲义作为学习路线，把 v2512 官方教程与源码作为实际运行的配置依据。",
    ["先补充 Linux 终端与基本文件操作。", "按讲义完成算例结构、网格、求解和后处理练习。", "再学习数值方法与编程内容，并为每个迁移练习记录差异。"],
    "从讲义选取一个基础算例，与 v2512 中相近的官方算例并排比较：记录求解器、文件名、关键字和日志差异，最后用同一组物理量检查结果。",
    [("培训资料存档与 DOI", "https://doi.org/10.6084/m9.figshare.16783657")],
    cost_note="此处推荐官方公开的自学资料与视频；网站另行提供的现场培训、辅导等服务不包含在免费资源说明中。",
)

add(
    "paraview-documentation", "ParaView：科学可视化与后处理文档", "可视化与数据",
    "学习场数据读取、切片、曲线、色标与结果导出，建立可重复的后处理过程。",
    "https://docs.paraview.org/en/latest/", "ParaView 官方文档 / Kitware",
    "该链接指向持续更新的文档，应选择与本机 ParaView 对应的版本。OpenFOAM 读取器、插件和 VTK 版本影响可读取的数据及选项；应核对实际读取器，不能仅凭文件后缀判断兼容性。",
    "官方文档主页已读取，已核对用户指南、参考手册、自学教程与 Python 相关文档入口。",
    "适合需要分析速度、压力、温度等场量，或制作报告图件的用户。",
    "ParaView 文档帮助区分数据选择与显示操作。云图应保留量纲、时间、空间位置与色标范围，比较不同工况时尤其需要统一这些条件。",
    ["先学习读取数据、选择时间和区分单元数据与点数据。", "再学习 Slice、曲线提取、色标与相机控制。", "最后保存状态和导出图表，必要时学习 Python 批处理。"],
    "对同一算例的两个时刻制作同位置切片，固定色标范围与相机视角，并保存状态文件；比较结果时注明采样位置、时间和单位。",
    diagram="8",
)

add(
    "gmsh-manual", "Gmsh：几何建模与网格生成手册", "几何网格",
    "通过官方教程学习几何、物理分组与网格尺寸控制，为外部网格导入准备可检查的边界定义。",
    "https://gmsh.info/doc/texinfo/", "Gmsh 官方参考手册",
    "当前在线手册随 Gmsh 更新。导入 OpenFOAM 前应确认导出格式与 v2512 转换工具支持范围，并检查物理分组到边界名称的映射；不能假定所有最新网格格式均可直接读取。",
    "官方完整参考手册已读取，已核对基础几何、物理分组、网格尺寸场及 OpenCASCADE 相关教程目录。",
    "适合规则几何建模、参数化网格生成，以及需要用脚本复现网格的用户。",
    "Gmsh 将几何、网格和物理分组关联起来。对 CFD 算例而言，入口、出口、壁面等边界标识与单元质量同样重要。",
    ["先阅读基础几何与 physical groups 教程。", "再学习局部尺寸控制，观察过渡区域的单元质量。", "最后选择合适的导出格式，转换后检查边界与网格。"],
    "建立一个简单通道并明确命名入口、出口和壁面；导出后用 v2512 的 gmshToFoam 转换，再用 checkMesh 检查网格，同时核对 boundary 文件。",
    diagram="0",
)

add(
    "salome-platform", "SALOME：几何处理与网格工作平台", "几何网格",
    "了解几何建模、几何分组与网格模块的配合方式，建立外部网格准备流程。",
    "https://www.salome-platform.org/", "SALOME 官方网站与文档",
    "SALOME 的模块与导出能力随版本变化。应先确定所用模块、网格格式和 OpenFOAM 转换路径；几何或网格能在 SALOME 中打开，并不代表可不经检查直接用于 v2512。",
    "官方主页已读取，已核对 SHAPER、SMESH 等模块说明和 Documentation 入口；文档域名可访问，但自动读取未返回正文。",
    "适合需要图形化处理复杂几何、创建边界组或比较网格策略的用户。",
    "SALOME 提供用于数值计算前处理的几何与网格工具。实际学习宜围绕一个完整几何模型展开，避免只生成网格而遗漏边界组、单位和实体连通性。",
    ["先理解几何实体、组与网格对象的关系。", "再学习局部划分策略及网格质量检查。", "最后确定导出与转换方式，核对导入后的区域和边界。"],
    "对一个带孔几何建立命名边界组，记录几何单位和网格参数；转换进入 OpenFOAM 后逐一对照面组数量、位置及网格质量报告。",
    [("官方文档目录", "https://docs.salome-platform.org/")],
    diagram="0",
)

add(
    "freecad-project", "FreeCAD：参数化几何建模", "几何网格",
    "为 CFD 前处理建立具有明确尺寸和参数关系的几何模型。",
    "https://github.com/FreeCAD/FreeCAD", "FreeCAD 官方项目仓库",
    "FreeCAD 是几何建模工具，CFD 网格生成与求解需要后续流程。工作台、导出选项和插件随版本变化；向网格工具传递模型时应核对单位、封闭性和曲面离散精度。",
    "官方 GitHub 仓库及项目说明已读取。官网和 Wiki 在自动访问时受到访问控制，因此以可核对的官方仓库作为主入口。",
    "适合需要参数化尺寸、重复修改几何或保留可编辑 CAD 模型的用户。",
    "参数化建模可将长度、直径和位置等设计变量保存在可追溯的模型中。面向 CFD 时，还需判断输出的是固体几何还是流体计算域。",
    ["从项目说明进入官方文档，学习草图与几何约束。", "构建参数化特征并检查几何有效性。", "按下游网格工具要求选择 STEP 或 STL 等输出，并复核尺度。"],
    "建立一个尺寸可调的通道模型，保存原始 CAD 文件及导出文件；改变一个尺寸后重新导出，并在网格工具中确认几何尺度和边界位置。",
    diagram="0",
)

add(
    "pyvista-documentation", "PyVista：Python 科学数据处理与绘图", "可视化与数据",
    "使用 Python 组织 VTK 数据读取、采样和图像输出，便于重复执行相同的后处理步骤。",
    "https://docs.pyvista.org/", "PyVista 官方文档",
    "PyVista 与其依赖的 VTK 版本共同影响读取器和数据接口。处理 OpenFOAM 结果时，应确认读取到的区域、时间、网格块和场名称，不能仅以脚本成功退出判断数据正确。",
    "官方文档主页已读取，已核对项目文档入口；此推荐不预设某个未经本机验证的读取器参数组合。",
    "适合已经掌握基础 Python，希望批量生成图件或整理多个工况数据的用户。",
    "PyVista 适合把读取、筛选、采样和输出写成脚本。脚本应同时记录输入数据位置与处理参数，使图件可以在相同条件下重新生成。",
    ["先理解网格对象、点数据与单元数据。", "使用简单数据练习切片、采样和绘图。", "再处理 OpenFOAM 输出，明确时间选择和多区域数据结构。"],
    "对一个已经在 ParaView 中检查过的算例，用 Python 提取同一条测线的数据，并比较坐标、场值及插值差异；随后再扩展到批处理。",
    diagram="8",
)

add(
    "pyfoam-package", "PyFoam：OpenFOAM 工作流辅助工具", "源码与开发",
    "了解运行组织、日志处理与参数化工作流的 Python 辅助工具，并先在小型算例中检查兼容性。",
    "https://pypi.org/project/pyfoam/", "PyFoam 项目维护者 / PyPI 发布页",
    "PyFoam 是独立于 OpenFOAM 核心发行版的第三方工具。包版本、Python 版本和 OpenFOAM 的日志或字典格式变化均可能影响功能；本站不将其全部功能声明为已通过 v2512 测试。",
    "PyPI 项目页已读取，已核对维护者、发布记录与项目说明入口。",
    "适合已有稳定算例，希望整理批量运行或减少重复操作的用户。",
    "PyFoam 提供围绕 OpenFOAM 的脚本与库。它处理工作流层面的任务，物理模型、离散格式和求解器行为仍由实际运行的 OpenFOAM 程序决定。",
    ["先阅读项目说明与当前版本发布记录。", "在独立 Python 环境中确认安装版本和命令帮助。", "选取一个可快速完成的算例，逐项测试需要使用的功能。"],
    "选择一个已保存基准日志的小型算例，比较直接运行与辅助工具组织运行后的命令、日志、退出状态和结果文件，确认工作流没有改变预期配置。",
    diagram="9",
)

add(
    "openfoamwiki", "OpenFOAMwiki：社区经验与扩展索引", "学术社区",
    "查找社区整理的使用经验、扩展项目与历史资料，再回到对应版本的原始来源核对。",
    "https://openfoamwiki.net/index.php/Main_Page", "OpenFOAMwiki 社区；非 OpenCFD 官方文档",
    "社区条目可能面向不同发行分支或较早版本。使用前检查更新时间、OpenFOAM 版本、依赖与原作者链接；页面可访问或有人使用过，并不能证明它适配 v2512。",
    "入口由已核对的第三方项目资料交叉确认；站点自动读取受到浏览器验证限制，未将其具体技术条目视为已审校内容。",
    "适合寻找历史问题线索、第三方工具名称或其他用户实践记录的读者。",
    "Wiki 可作为检索线索的起点。对影响数值结果的配置建议，应进一步查找版本一致的源码、正式说明或可重复的算例证据。",
    ["先用具体工具名或错误信息查找相关条目。", "记录条目的发行分支、版本和更新时间。", "沿原始项目链接核对，再在独立小算例中验证。"],
    "选取一个与当前任务相关的条目，为其中一个操作建立核对记录：原文版本、v2512 中的对应工具、实际帮助输出和小型测试结果。",
)

add(
    "cfd-online-openfoam", "CFD Online：OpenFOAM 讨论论坛", "学术社区",
    "按安装、网格、求解、后处理与编程等主题检索社区讨论和问题线索。",
    "https://www.cfd-online.com/Forums/openfoam/", "CFD Online 社区；非 OpenCFD 官方技术支持",
    "论坛帖子可能跨越多个 OpenFOAM 分支与版本，回答的上下文十分重要。旧帖中的命令、边界条件名称或数值建议不能未经核对直接用于 v2512。",
    "OpenFOAM 论坛目录已直接读取，已核对其安装、网格、运行、后处理、编程及验证相关分区。",
    "适合遇到具体错误、需要对照相似问题，或希望参与技术讨论的用户。",
    "论坛的价值在于保留问题、尝试过程和讨论背景。使用回答时应区分可以通过日志验证的事实与需要进一步检验的经验建议。",
    ["搜索完整错误片段、工具名与发行版本。", "阅读原问题和后续回复，检查几何、边界条件及运行环境是否相近。", "提问时提供最小复现资料与已经完成的检查。"],
    "整理一份可复现的问题说明：发行方与 v2512、运行命令、关键日志、网格检查结果、相关字典片段和预期行为；避免仅发布截图而省略文本错误。",
    cost_note="公开帖子可免费阅读；外部论坛的注册、发帖与附件规则以该论坛当前规定为准。本站 GitHub 登录不会自动登录外部论坛。",
)

add(
    "openfoam-journal", "OpenFOAM Journal：论文与可复现研究", "学术社区",
    "结合论文、代码和算例学习模型开发与数值验证，区分方法描述和适用范围。",
    "https://journal.openfoam.com/index.php/ofj", "OpenFOAM Journal 期刊网站",
    "论文可能使用不同发行分支、版本或定制代码。复现前需确认软件版本、修改内容、网格、时间步长与验证数据；发表结果不代表能直接迁移到 v2512。",
    "期刊主页及办刊说明已读取，已核对开放获取、可复现性要求与论文讨论入口说明。",
    "适合已掌握基础算例，准备研究模型、开发求解器或开展验证工作的读者。",
    "论文提供从控制方程、数值方法到验证证据的完整论证。阅读时应分别判断物理假设、离散误差、实现方式与实验或解析对照。",
    ["先阅读问题定义、控制方程与模型假设。", "再整理数值设置、网格与时间步长研究。", "最后检查公开代码和算例，选择最小验证问题进行复现。"],
    "为一篇论文建立复现表：版本与依赖、边界条件、网格规模、时间步长、比较指标、数据来源及尚未公开的信息；先复现一个关键图表再扩展研究。",
    cost_note="期刊说明提供开放获取阅读且不收取发表费用；具体论文、代码与数据的复用许可应分别查阅。",
)


def main():
    assert len(RECORDS) == 15
    assert len({record["slug"] for record in RECORDS}) == len(RECORDS)
    for record in RECORDS:
        cover = ROOT / "source-openfoam" / record["cover_url"].lstrip("/")
        assert cover.is_file(), cover
        assert record["metadata"]["external_url"].startswith("https://")
    output = ROOT / "tools/content/recommendations-content.json"
    output.write_text(json.dumps(RECORDS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = {}
    for record in RECORDS:
        counts[record["track"]] = counts.get(record["track"], 0) + 1
    print(json.dumps({"records": len(RECORDS), "categories": counts, "output": str(output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
