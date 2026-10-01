---
title: "05 后处理及其他命令"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 1
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM_v2512命令与配置参考手册（GPT整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><p>后处理包括场数据转换、日志分析、统计计算和结果清理。函数对象的配置见第 10 章。ParaView、Gnuplot 和 ffmpeg 分别用于可视化、曲线绘制和视频生成，使用前需完成相应安装。</p>
<h4>postProcess  执行函数对象后处理  源码</h4>
<p>-list 列出预配置函数。依赖湍流或热物性的函数通过相应求解器的 -postProcess 选项执行。</p>
<p>用法：postProcess [-func 名称] [-time 范围] [-latestTime]</p>
<pre><code>示例：postProcess -func &#x27;mag(U)&#x27; -latestTime</code></pre>
<h4>paraFoam  在 ParaView 中打开算例  源码</h4>
<p>-builtin 选择 ParaView 内置 OpenFOAM 读取器，运行需具备 ParaView 和图形环境。</p>
<p>用法：paraFoam [选项]</p>
<pre><code>示例：paraFoam -builtin</code></pre>
<h4>foamLog  提取日志中的残差等数值记录  源码</h4>
<p>结果写入 logs/。-list 列出可提取的变量。</p>
<p>用法：foamLog [选项] 日志文件</p>
<pre><code>示例：foamLog log.simpleFoam</code></pre>
<h4>foamMonitor  实时绘制数值文件曲线  源码</h4>
<p>调用 Gnuplot 读取数值列文件。-r 2 将刷新间隔设为 2 s。</p>
<p>用法：foamMonitor [选项] 数据文件</p>
<pre><code>示例：foamMonitor -l postProcessing/residuals/0/residuals.dat</code></pre>
<h4>foamSolverSweeps  统计求解迭代次数及耗时  源码</h4>
<p>启动后交互输入日志名，如 log.simpleFoam。脚本按预设的旧式日志行格式提取统计量。</p>
<p>用法：foamSolverSweeps 随后输入日志文件名</p>
<pre><code>示例：foamSolverSweeps</code></pre>
<h4>foamToVTK  将网格与场导出为 VTK  源码</h4>
<p>支持 XML VTK 输出，-legacy 选择旧式格式，-ascii 选择文本格式。</p>
<p>用法：foamToVTK [选项]</p>
<pre><code>示例：foamToVTK -latestTime -fields &#x27;(U p)&#x27;</code></pre>
<h4>foamToEnsight  导出 EnSight 数据集  源码</h4>
<p>选项可控制区域、粒子及场数据的输出范围。</p>
<p>用法：foamToEnsight [选项]</p>
<pre><code>示例：foamToEnsight -latestTime -fields &#x27;(U p)&#x27;</code></pre>
<h4>foamToGMV  导出 GMV 后处理数据  源码</h4>
<p>结果供支持 GMV 格式的软件读取。</p>
<p>用法：foamToGMV [选项]</p>
<pre><code>示例：foamToGMV</code></pre>
<h4>foamDataToFluent  将 OpenFOAM 场转换为 Fluent 数据  源码</h4>
<p>转换范围为场数据，求解设置在目标软件中配置。</p>
<p>用法：foamDataToFluent [选项]</p>
<pre><code>示例：foamDataToFluent</code></pre>
<h4>foamToTetDualMesh  将结果转换为四面体对偶网格形式  源码</h4>
<p>用于相应的后处理流程。</p>
<p>用法：foamToTetDualMesh [选项]</p>
<pre><code>示例：foamToTetDualMesh</code></pre>
<h4>smapToFoam  导入 SMAP 格式数据  源码</h4>
<p>输入采用程序支持的 SMAP 数据结构。</p>
<p>用法：smapToFoam SMAP文件</p>
<pre><code>示例：smapToFoam input.smap</code></pre>
<h4>patchSummary  汇总网格边界及场条件  源码</h4>
<p>用于检查网格边界与场配置的对应关系。</p>
<p>用法：patchSummary [选项]</p>
<pre><code>示例：patchSummary -latestTime -expand</code></pre>
<h4>foamListTimes  列出或删除指定时间目录  源码</h4>
<p>foamListTimes -time &#x27;0.1:0.5&#x27; -rm 删除指定时段目录；移除 -rm 可预览，-noZero 排除 0 目录。</p>
<p>用法：foamListTimes [选项]</p>
<pre><code>示例：foamListTimes -latestTime</code></pre>
<h4>foamFormatConvert  按指定格式重写场和网格  源码</h4>
<p>输出格式由 controlDict 中的 writeFormat 指定，可设为 ascii 或 binary。</p>
<p>用法：foamFormatConvert [选项]</p>
<pre><code>示例：foamFormatConvert -latestTime</code></pre>
<h4>foamRestoreFields  恢复备份或转换后的场  源码</h4>
<p>从已有备份恢复，method 按命令帮助指定。</p>
<p>用法：foamRestoreFields [选项] 场名列表</p>
<pre><code>示例：foamRestoreFields U p</code></pre>
<h4>foamSequenceVTKFiles  为 VTK 文件建立连续编号链接  源码</h4>
<p>生成的符号链接供 ParaView 识别时间序列。</p>
<p>用法：foamSequenceVTKFiles [选项]</p>
<pre><code>示例：foamSequenceVTKFiles -dir postProcessing -out sequencedVTK</code></pre>
<h4>foamCreateVideo  将 PNG 图像序列合成为视频  源码</h4>
<p>通过 ffmpeg 等工具处理图像序列，默认名称为 image.0000.png 等。-image 指定图像前缀。</p>
<p>用法：foamCreateVideo [选项]</p>
<pre><code>示例：foamCreateVideo -dir frames -fps 20 -out flow</code></pre>
<h4>foamCleanPolyMesh  清理体网格文件  源码</h4>
<p>-dry-run 预览清理范围，移除该选项后执行删除。</p>
<p>用法：foamCleanPolyMesh [-case 目录] [-dry-run]</p>
<pre><code>示例：foamCleanPolyMesh -dry-run</code></pre>
<h4>foamCleanFaMesh  清理有限面积网格文件  源码</h4>
<p>对应 constant/finite-area/faMesh，-area-region 指定有限面积区域。</p>
<p>用法：foamCleanFaMesh [-case 目录] [-dry-run]</p>
<pre><code>示例：foamCleanFaMesh -dry-run</code></pre>
<h4>foamCleanTutorials  递归清理教程结果  源码</h4>
<p>按规则删除结果并执行相关 Allclean；存在 0.orig 时，默认清理过程可移除 0 目录。</p>
<p>用法：foamCleanTutorials [选项] [目录]</p>
<pre><code>示例：foamCleanTutorials -case ./caseCopy</code></pre>
<h3>5.1 其他专用工具</h3>
<h4>addr2line  将程序地址映射到源码行  源码</h4>
<p>源码包提供 macOS 兼容实现；Linux 通常使用 GNU Binutils 同名工具。地址解析需具备调试符号。</p>
<p>用法：addr2line -e 可执行文件 地址</p>
<pre><code>示例：addr2line -e mySolver 0x1234</code></pre>
<h4>particleTracks  根据粒子记录重建轨迹  源码</h4>
<p>输入包括粒子标识信息和轨迹输出字典。</p>
<p>用法：particleTracks [-dict 文件]</p>
<pre><code>示例：particleTracks</code></pre>
<h4>steadyParticleTracks  导出稳态粒子轨迹为旧式 VTK  源码</h4>
<p>并行结果通常先重构，再导出轨迹。</p>
<p>用法：steadyParticleTracks [-dict 文件]</p>
<pre><code>示例：steadyParticleTracks</code></pre>
<h4>lumpedPointForces  提取集中点运动模型的力和力矩  源码</h4>
<p>读取集中点运动模型数据。</p>
<p>用法：lumpedPointForces [选项]</p>
<pre><code>示例：lumpedPointForces</code></pre>
<h4>lumpedPointMovement  测试集中点运动及响应文件  源码</h4>
<p>采用对应耦合模型配置。</p>
<p>用法：lumpedPointMovement 响应文件 [选项]</p>
<pre><code>示例：lumpedPointMovement response.dat</code></pre>
<h4>lumpedPointZones  输出集中点压力积分区域  源码</h4>
<p>通常生成用于可视化的 lumpedPointZones.vtp。</p>
<p>用法：lumpedPointZones [选项]</p>
<pre><code>示例：lumpedPointZones</code></pre>
<h4>createROMfields  根据降阶模型重建指定时刻的场  源码</h4>
<p>输入为已有 ROM 数据。</p>
<p>用法：createROMfields [-dict 文件]</p>
<pre><code>示例：createROMfields</code></pre>
<h4>engineCompRatio  根据发动机几何计算压缩比  源码</h4>
<p>适用范围由所采用的几何容积模型确定。</p>
<p>用法：engineCompRatio [选项]</p>
<pre><code>示例：engineCompRatio</code></pre>
<h4>pdfPlot  输出概率密度分布曲线  源码</h4>
<p>按字典配置概率密度函数。</p>
<p>用法：pdfPlot [选项]</p>
<pre><code>示例：pdfPlot</code></pre>
<h4>postChannel  统计通道流结果  源码</h4>
<p>按程序规定的周期方向及平均场定义进行统计。</p>
<p>用法：postChannel [选项]</p>
<pre><code>示例：postChannel</code></pre>
<h4>profilingSummary  汇总并行性能统计  源码</h4>
<p>读取启用 profiling 后生成的性能统计文件。</p>
<p>用法：profilingSummary [选项]</p>
<pre><code>示例：profilingSummary</code></pre>
<h4>temporalInterpolate  对已有时刻的场进行时间插值  源码</h4>
<p>根据离散时刻结果生成中间时刻的场。</p>
<p>用法：temporalInterpolate [选项]</p>
<pre><code>示例：temporalInterpolate -divisions 3 -fields &#x27;(U p)&#x27;</code></pre>
<h4>noise  分析压力时序或表面压力频谱  源码</h4>
<p>读取 noiseDict。采样频率决定有效频率上限，采样时长决定频率分辨率。</p>
<p>用法：noise [-dict 文件]</p>
<pre><code>示例：noise</code></pre>
<h4>computeSensitivities  依据优化字典计算灵敏度  源码</h4>
<p>读取 optimisationDict 及相应原始场和伴随场。</p>
<p>用法：computeSensitivities [选项]</p>
<pre><code>示例：computeSensitivities</code></pre>
<h4>cumulativeDisplacement  计算相对初始网格的累计位移  源码</h4>
<p>读取各时刻点坐标及 constant 中的初始网格。</p>
<p>用法：cumulativeDisplacement [选项]</p>
<pre><code>示例：cumulativeDisplacement</code></pre>
<h4>adiabaticFlameT  计算绝热火焰温度  源码</h4>
<p>输入包括热物性和组分配置。</p>
<p>用法：adiabaticFlameT 控制文件</p>
<pre><code>示例：adiabaticFlameT adiabaticFlameTDict</code></pre>
<h4>chemkinToFoam  转换 CHEMKIN 反应机理和热物性文件  源码</h4>
<p>反应、热力学和输运输入文件采用一致的物种名称。</p>
<p>用法：chemkinToFoam 反应文件 热力学文件 输运文件 输出反应 输出热物性</p>
<pre><code>示例：chemkinToFoam chem.inp therm.dat tran.dat reactions thermo</code></pre>
<h4>equilibriumCO  计算平衡一氧化碳浓度  源码</h4>
<p>按所用热化学平衡模型计算。</p>
<p>用法：equilibriumCO [选项]</p>
<pre><code>示例：equilibriumCO</code></pre>
<h4>equilibriumFlameT  计算平衡火焰温度  源码</h4>
<p>物种数据与热力学模型保持一致。</p>
<p>用法：equilibriumFlameT 控制文件</p>
<pre><code>示例：equilibriumFlameT equilibriumFlameTDict</code></pre>
<h4>mixtureAdiabaticFlameT  计算混合物绝热火焰温度  源码</h4>
<p>由输入字典指定混合物组成。</p>
<p>用法：mixtureAdiabaticFlameT 控制文件</p>
<pre><code>示例：mixtureAdiabaticFlameT mixtureFlameTDict</code></pre>
{% endraw %}