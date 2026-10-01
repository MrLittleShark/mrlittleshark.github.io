---
title: "02 系统命令与辅助工具"
layout: reference
description: "OpenCFD v2512 系统命令与辅助工具；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>系统工具用于环境检查、字典操作、模板获取、算例复制和代码生成。目录别名见第 11 章。相关源码位于 bin 和 applications/utilities/miscellaneous。</p>
<h2>foamGetDict  复制配置字典模板  源码</h2>
<p>默认写入 system，*Properties 通常写入 constant。-target 指定目标目录，-force 覆盖已有文件。</p>
<p>用法：foamGetDict [选项] 文件名</p>
<pre><code class="language-plaintext">示例：foamGetDict decomposeParDict</code></pre>
<h2>foamHelp  查询边界条件、函数对象和求解器信息  源码</h2>
<p>查询类别包括 boundary、functionObject 和 solver。示例需在具有网格和 0/U 文件的算例中运行。</p>
<p>用法：foamHelp 类别 [选项]</p>
<pre><code class="language-plaintext">示例：foamHelp boundary -field U</code></pre>
<h2>foamDictionary  读取或修改字典条目  源码</h2>
<p>-value 读取条目值，-keywords 列出关键字，-expand 展开引用。子条目采用 solvers/p/tolerance 等路径表示。</p>
<p>用法：foamDictionary 字典 [-entry 路径] [-value/-set 值]</p>
<pre><code class="language-plaintext">示例：foamDictionary system/controlDict -entry endTime -set 100</code></pre>
<h2>foamSearch  搜索各算例字典中的指定条目  源码</h2>
<p>键路径以点号分隔，-count 统计相同配置的出现次数。</p>
<p>用法：foamSearch [目录] 键路径 文件名</p>
<pre><code class="language-plaintext">示例：foamSearch "&#36;FOAM_TUTORIALS" ddtSchemes.default fvSchemes</code></pre>
<h2>foamEtcFile  按配置层级查找 etc 文件  源码</h2>
<p>按用户、站点和安装目录搜索并输出文件路径。-all 列出全部匹配项，-list 列出搜索目录。</p>
<p>用法：foamEtcFile [选项] 相对文件</p>
<pre><code class="language-plaintext">示例：foamEtcFile caseDicts/meshQualityDict</code></pre>
<h2>foamInstallationTest  检查安装及环境设置  源码</h2>
<p>用于诊断安装路径及环境配置。</p>
<p>用法：foamInstallationTest [选项]</p>
<pre><code class="language-plaintext">示例：foamInstallationTest</code></pre>
<h2>foamSystemCheck  检查 OpenFOAM 编译环境  源码</h2>
<p>检查构建所需的系统和编译条件。</p>
<p>用法：foamSystemCheck [选项]</p>
<pre><code class="language-plaintext">示例：foamSystemCheck</code></pre>
<h2>foamCloneCase  复制算例初始场及配置  源码</h2>
<p>默认复制初始时刻、constant 和 system。-latestTime 选择最后时刻，-force 覆盖目标目录。</p>
<p>用法：foamCloneCase [选项] 源算例 目标算例</p>
<pre><code class="language-plaintext">示例：foamCloneCase ../cavity ./cavityCopy</code></pre>
<h2>foamCopySettings  复制算例配置  源码</h2>
<p>采用 rsync，按 foamCopySettings.rc 定义的规则复制，不包含网格和计算结果。</p>
<p>用法：foamCopySettings 源目录 目标目录</p>
<pre><code class="language-plaintext">示例：foamCopySettings ../baseCase ./</code></pre>
<h2>foamNewCase  按应用模板创建算例  源码</h2>
<p>模板来自用户或站点配置。-list 列出可用模板；创建命令为 foamNewCase -app simpleFoam -case newCase。</p>
<p>用法：foamNewCase [-app 应用] [-case 目录]</p>
<pre><code class="language-plaintext">示例：foamNewCase -list</code></pre>
<h2>foamRunTutorials  递归执行算例脚本  源码</h2>
<p>执行目标目录中的 Allrun 或 Alltest。-dry-run 列出待执行脚本。</p>
<p>用法：foamRunTutorials [选项] [-case 目录]</p>
<pre><code class="language-plaintext">示例：foamRunTutorials -dry-run -case ./cases</code></pre>
<h2>foamTestTutorial  执行教程测试  源码</h2>
<p>默认在临时目录运行一个时间步。-full 执行完整教程，-output=DIR 保留输出，指定目录须预先建立。</p>
<p>用法：foamTestTutorial [选项] 教程相对路径</p>
<pre><code class="language-plaintext">示例：foamTestTutorial -1 incompressible/icoFoam/cavity/cavity</code></pre>
<h2>foamNew  生成源码或模板文件  源码</h2>
<p>示例生成 MyModel.H。C、H、I、IO 和 App 等模板由 foamNewSource 配套提供。</p>
<p>用法：foamNew source 文件类型 类名</p>
<pre><code class="language-plaintext">示例：foamNew source H MyModel</code></pre>
<h2>foamNewApp  生成自定义应用代码  源码</h2>
<p>生成应用源码和 Make 文件。在生成目录运行 wmake，程序通常输出至 FOAM_USER_APPBIN。</p>
<p>用法：foamNewApp 应用名</p>
<pre><code class="language-plaintext">示例：foamNewApp myScalarFoam</code></pre>
<h2>foamNewBC  生成自定义边界条件代码  源码</h2>
<p>在生成目录运行 wmake libso，并在算例的 libs 中加载生成的库。</p>
<p>用法：foamNewBC 基类 场类型 名称</p>
<pre><code class="language-plaintext">示例：foamNewBC fixedValue scalar myTemperature</code></pre>
<h2>foamNewFunctionObject  生成函数对象代码  源码</h2>
<p>在生成目录运行 wmake libso，随后在 functions 中配置并加载该对象。</p>
<p>用法：foamNewFunctionObject 名称</p>
<pre><code class="language-plaintext">示例：foamNewFunctionObject myProbe</code></pre>
<h2>foamCalc  计算标量表达式  源码</h2>
<p>v2512 中该命令为标量计算器，旧版同名场处理程序采用不同接口。</p>
<p>用法：foamCalc [选项] 表达式</p>
<pre><code class="language-plaintext">示例：foamCalc '2*3+1'</code></pre>
<h2>foamExprParserInfo  查询表达式解析器信息  源码</h2>
<p>用于查询表达式语法及解析器支持范围。</p>
<p>用法：foamExprParserInfo [选项]</p>
<pre><code class="language-plaintext">示例：foamExprParserInfo -volume -rules</code></pre>
<h2>foamCleanPath  清理路径列表  源码</h2>
<p>删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变。</p>
<p>用法：foamCleanPath [选项] 路径 [过滤项]</p>
<pre><code class="language-plaintext">示例：foamCleanPath "&#36;PATH"</code></pre>
<h2>foamHasLibrary  检查共享库能否加载  源码</h2>
<p>-detail 输出详细信息。</p>
<p>用法：foamHasLibrary 库名列表 [选项]</p>
<pre><code class="language-plaintext">示例：foamHasLibrary libfieldFunctionObjects.so</code></pre>
<h2>foamListRegions  列出网格区域  源码</h2>
<p>可按 fluid、solid 等 regionType 筛选，-finite-area 选择有限面积区域。</p>
<p>用法：foamListRegions [区域类型]</p>
<pre><code class="language-plaintext">示例：foamListRegions</code></pre>
<h2>foamUpgradeFiniteArea  迁移旧版有限面积文件  源码</h2>
<p>将旧版文件调整为包含 finite-area 子目录的结构。-dry-run 预览迁移内容。</p>
<p>用法：foamUpgradeFiniteArea [选项]</p>
<pre><code class="language-plaintext">示例：foamUpgradeFiniteArea -dry-run -case ./legacyCase</code></pre>
<h2>foamUpgradeCyclics  将旧版循环边界转换为拆分形式  源码</h2>
<p>用于迁移旧版算例。</p>
<p>用法：foamUpgradeCyclics [选项]</p>
<pre><code class="language-plaintext">示例：foamUpgradeCyclics</code></pre>
{% endraw %}
