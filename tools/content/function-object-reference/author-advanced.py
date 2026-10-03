"""Tool-specific context and variants for the remaining reference entries."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
d=json.loads((P/'profiles.json').read_text(encoding='utf-8'))
contexts='''pow|对标量场做幂运算，随后缩放和偏移。本例的结果为 0.5×k^0.25+2.5，field、n、scale、offset 分别指定输入和运算系数。用于数值变换时可明确关闭量纲检查。
log|对标量场取自然对数。先用 clip 截断过小的输入，再取对数、乘 scale 并加 offset；本例对湍动能 k 做变换，用于比较跨越多个数量级的数值。
norm|按选定范数归一化输入场，生成一个新场。本例输入 U，norm L1 选择 L1 范数；换用不同范数会改变归一化后的分量数值。
ddt|计算瞬态体场对时间的一阶导数。本例对 U 求导得到 ddtU，需要连续时间步中的历史值；计算采用 fvSchemes 中的时间离散格式。
ddt2|计算一阶时间导数的模或模平方。mag false 输出模平方，mag true 输出模；fields 可包含多个场，result 中的 @@ 会被输入场名替换。
fieldCoordinateSystemTransform|把向量或张量转换到指定局部坐标系。本例用 U 演示字段选择，coordinateSystem 中的 origin 和 rotation 决定坐标系；rotation none 保持原轴向。
reference|从输入场减去参考值，再加 offset 并乘 scale。示例 refValue sample 从指定 position 采样压力，输出整个区域相对于该点的压力差。
randomise|为输入场加入给定幅值的随机扰动。本例以 U 为输入、magPerturbation 0.1 为扰动尺度，可用于准备带扰动的初始流动。
zeroGradient|生成采用零梯度边界的派生场，保留输入场内部数值，便于某些后处理计算。fields 可用精确名称或匹配表达式选择多个场。
limitFields|在内存中把指定场限制到选定范围。limit both 同时启用 min 和 max；该操作会参与后续计算，应把上下限设为物理问题允许的范围。
derivedFields|从求解器当前字段生成预定义派生量。本例 derived (rhoU pTotal) 分别生成动量密度和总压，供后续采样或写出对象使用。
nearWallFields|沿壁面法向在给定距离处采样，把结果保存在新的字段中。本例距离为 0.001 m，输入 U、输出 UNear，供沿壁面流线追踪使用。
streamLine|从 seedSampleSet 指定的种子点沿 U 追踪流线。本例在方腔中线放置五个点，双向追踪并保存沿线的 U 与 p；nSubCycle 控制单元内的追踪细分。
wallBoundedStreamLine|在壁面附近追踪受壁面约束的流线。本例使用 nearWallFields 先生成的 UNear 作为追踪速度，并从 motorBikeGroup 边界布置种子。
surfaceDistance|计算到指定几何表面的距离。示例的 pending.obj 放在 constant/triSurface，geometry 定义其类型和名称，calculateCells 决定是否计算单元中心距离。
fieldExtents|求字段超过 threshold 的区域在空间中的包围范围。本例在 wallFilmRegion 中以 alpha>0.5 识别液膜覆盖区域，fields、region 和 threshold 共同决定统计对象。
columnAverage|沿结构化网格柱方向平均场值。本例选择 front 以及对应的并行周期边界，将 p、U 和已有时间统计场沿该方向平均。
binField|按空间位置把场值分箱。本例使用 singleDirectionUniformBin，沿 x 方向分成 20 箱，对 motorBikeGroup 上已生成的 forceCoeff 统计，cumulative 控制累计和。
fluxSummary|汇总指定面区域的通量，并可按方向区分流入和流出。本例由 porosity 单元区域及参考方向识别统计面，scaleFactor 对最终通量统一缩放。
momentum|统计线动量和角动量。本例对整个区域计算，并使用以 x 轴为轴向的圆柱坐标；相关开关决定是否同时保存动量、位置和速度的分量场。
momentumError|根据当前速度、压力和动量输运模型计算动量方程的不平衡场，适合定位离散方程误差较大的区域。本例与求解器写出时刻同步更新和保存。
DESModelRegions|从 DES 模型提取 RANS 与 LES 工作区域的指示场。算例需要采用支持这一接口的 DES 类模型；result 指定保存该指示量的名称。
energySpectrum|用速度场计算能量随波数的分布。本例来自各向同性湍流衰减算例，依赖适合频谱计算的规则网格；结果用于比较不同尺度上的动能。
DMD|对连续时刻的场快照进行动态模态分解。DMDModel STDMD 选择流式算法，field U 指定快照变量，executeInterval 决定快照间隔，计算结束时输出模态信息。
Curle|根据固体表面的非定常载荷估算声压。本例选 cylinder 边界、343 m/s 的声速和四个观察点，适合查看载荷变化在不同观察方向上的声学响应。
proudmanAcousticPower|按各向同性湍流假设估算局部声功率。需要湍动能、耗散率及声速等数据，alphaEps 为模型经验系数，结果用来识别潜在噪声源区域。
blendingFactor|输出混合对流格式使用的局部混合因子。本例选择速度 U，配合 fvSchemes 中对应的混合格式使用，以查看计算在不同区域更偏向哪一种格式。
stabilityBlendingFactor|根据网格质量、残差或 Courant 数生成局部格式混合因子。result 命名的面场交给 localBlended 格式使用；switch 开关分别启用各项判据。
propellerInfo|对推进器载荷和尾流进行统计。origin、axis、n 定义转轴与转速，radius 和参考速度用于性能系数，sampleDisk 规定尾流采样圆盘。
bladeForces|分析旋转叶片上的载荷分布。本例以 x 轴为转轴、25 转/秒为转速，并沿半径分段；nearCellValue 选择从邻近流体单元读取速度的方式。
thermoCoupleProbes|在探针位置求解热电偶温度响应，同时考虑对流与辐射。rho、Cp、d、epsilon 是热电偶材料和几何参数，G 为辐射模型提供的辐射场。
comfort|根据速度、温度、湿度及人体参数计算热舒适度。本例 clothing 0.5、metabolicRate 1.2 描述衣着与活动水平，relHumidity 60 表示相对湿度为 60%。
XiReactionRate|从 b–Xi 预混燃烧模型计算火焰传播和反应率相关输出。它使用对应燃烧求解器创建的模型与字段，适合比较火焰区的反应强度。
reactingEulerHtcModel|在 Euler 多相传热框架中计算壁面换热系数。本例选择 water 区域的 T.liquid，在 water_to_solid 边界使用 373 K 的固定参考温度。
multiphaseInterHtcModel|在相应界面捕捉多相框架中计算壁面换热系数。本例对 bottom 壁面使用 T 和 373 K 的固定参考温度，结合该模型的热流得到换热系数。
electricPotential|在现有流场上求解电势方程，并可输出电场等派生量。示例为两相分别设置电导率和介电常数；算例还要准备电势边界及对应的线性求解配置。
scalarTransport|在已有速度或通量场中额外求解被动标量。本例对 tracer0 使用 0.001 的扩散系数；算例需要 tracer0 的初始与边界条件，以及离散和求解设置。
energyTransport|在现有流动上求解附加能量输运。本例对 T 使用质量通量 rhoPhi，各相的 Cp 和 kappa 决定热容与导热，并可通过 fvOptions 加入热源。
age|求解流体平均年龄，用来评估通风、停留时间和流体更新。本例启用扩散项，schemesField age 对应离散与求解设置，nCorr 决定附加校正次数。
regionSizeDistribution|按相分数阈值识别连通区域，计算等效直径和分布。本例用 alpha.air>0.5 识别区域，并通过 inlet 区分与入口相连的核心区域；统计范围由直径上下限和箱数决定。
extractEulerianParticles|在指定 faceZone 上从相分数输运记录颗粒事件，用于把欧拉界面数据转成后续拉格朗日注入数据。本例选择 collector，alphaThreshold 定义液相事件识别阈值。
cloudInfo|统计颗粒云的数量、质量等信息。示例选择 reactingCloud1，并按温度、组分、粒径及速度筛选颗粒；selection 各操作按顺序缩小或调整统计对象。
particleDistribution|对颗粒属性分箱统计。本例对 sprayCloud 的粒径 d 使用 10⁻⁵ m 箱宽，对速度使用 10 的箱宽，输出分布数据供绘图使用。
sizeDistribution|从群体平衡模型输出粒径分布。populationBalance 选择模型，selectionMode 选择统计区域，functionType 和 abszissaType 分别决定纵轴统计方式与横轴粒径定义。
vtkCloud|将颗粒位置与属性写为 VTK。本例选择全部云，并导出 U、T、d 以及匹配 Y.* 的组分字段，便于在 ParaView 中查看颗粒温度与粒径分布。
dsmcFields|把 DSMC 统计得到的密度、动量和能量等量组合为宏观物理场。使用已完成统计的 DSMC 算例，可得到速度、温度等结果。
writeObjects|将内存中选定对象写到时间目录。objects 控制名称筛选，writeOption 控制选择的写出属性；log 模式用于查看匹配到的对象信息。
areaWrite|导出有限面积网格上的场。本例的 Uf_film、hf_film、pf_film 是液膜速度、厚度和压力，surfaceFormat ensight 指定表面结果格式。
mapFields|在同一次运行中把场映射到另一个网格区域。本例映射 U、p 到 coarseMesh，cellVolumeWeight 使用单元体积重叠关系进行插值。
caseInfo|把算例、网格、字典和功能对象结果汇总为信息文件。本例选择 JSON，dictionaries 的 include 列表可以精确选择需要记录的配置路径。
PecletNo|根据面通量、网格尺度和扩散相关模型计算局部 Peclet 数，比较对流与扩散的强弱。示例读取 phi，并把输出场命名为 PecletNoField。
MachNo|由速度大小与局部声速计算马赫数。算例需要可压缩热物性模型提供声速相关数据；可在结果中查看接近或超过音速的区域。
AMIWeights|统计 AMI 接口的插值权重，并可把权重写成 VTK 场。适合检查旋转接口覆盖情况，以及几何运动时权重的变化。
timeActivatedFileUpdate|在指定模拟时刻把预先准备的文件复制到目标位置。本例先采用 fvSolution.0，到 0.02 时改用 fvSolution.5，用于分阶段调整求解设置。
multiRegion|把同一个子功能对象应用到多个网格区域。本例对子区域分别运行 fieldMinMax，统计温度 T 的范围，适合共轭传热算例。
externalCoupled|通过通信目录与外部程序交换边界数据。本例交换温度 T，由外部程序提供初始数据，regions 定义参与耦合的区域和边界组。
syncObjects|把本地对象数据库中的 IOFields 分发到其他进程或区域，常与 mapped 边界及松耦合计算配合使用。root 定位用于发送和接收数据的子对象数据库。
setFlow|按解析规则设置速度和通量。本例绕 y 轴以 2π rad/s 旋转，origin 定义转动中心，reverseTime 1 使流动在 1 s 时反向，适合界面输运测试。
foamReport|用计算数据填充一个文本模板，生成报告。template 指定模板，substitutions 从字典或日志抽取数值并替换对应占位符；本例使用 motorBike 的配套模板。
graphFunctionObject|将其他功能对象的数值结果绘制为 SVG 曲线。本例从 forceCoeffs1 读取 Cd、Cl 等系数，functions 中每个子字典定义一条曲线。
dataCloud|把选定颗粒云的单个属性写出为数据集合。本例读取 coalCloud1 的粒径 d，可进一步用于颗粒分布分析。'''
for line in contexts.splitlines():
    name,text=line.split('|',1);d[name]['explanation']=text
d['ddt2']['description']='计算体场一阶时间导数的模或模平方。'
d['ddt']['description']='计算体场对时间的一阶导数。'
d['syncObjects']['description']='在进程或区域之间分发对象数据库中的 IOFields 数据。'
d['reference']['description']='将输入场转换为相对于指定参考值的场。'
d['writeDictionary']['description']='监测并输出指定字典的内容。'
# Specific parameter changes use the original case's geometry and models.
variants={
'pow':[('取平方根',{'n':'0.5','scale':'1','offset':'0'},'单独观察 k 的平方根，先去掉缩放与偏移，便于核对运算。'),('线性放大平方',{'n':'2','scale':'2','offset':'0'},'先平方再乘二，输出量纲和数值范围随之改变。')],
'log':[('降低截断下限',{'clip':'1e-6'},'保留更小正值之间的差异，对数结果在低值区会出现更负的数值。'),('调整显示尺度',{'scale':'2','offset':'1'},'在取对数后作线性变换，便于与其他诊断量比较。')],
'norm':[('采用欧氏范数',{'norm':'L2','result':'normalisedU'},'按 L2 范数归一化速度，保存为独立结果场。'),('采用三阶范数',{'norm':'Lp','p':'3','result':'normalisedU3'},'Lp 模式下用 p 指定指数，比较不同范数对各分量权重的影响。')],
'ddt':[('计算压力变化率',{'field':'p','result':'ddtP'},'跟踪压力随时间的变化率，使用同一套连续时间步数据。'),('每步更新导数',{'executeControl':'timeStep','executeInterval':'1'},'让导数计算与时间推进同步，之后按需要降低文件保存频率。')],
'ddt2':[('保存变化率的模',{'mag':'true'},'结果与一阶导数具有相同量纲，适合直接比较变化率大小。'),('只分析速度变化',{'fields':'(U)'},'只对速度执行时间导数统计，减少输出字段。')],
'fieldCoordinateSystemTransform':[('同时转换速度与应力',{'fields':'(U UPrime2Mean)'},'在已保存 UPrime2Mean 的算例中，将向量和二阶张量放在同一坐标系解释。'),('只处理平均速度',{'fields':'(UMean)'},'使用已有时间平均速度，获得局部坐标下的平均分量。')],
'reference':[('改用固定参考值',{'refValue':'constant 0'},'以固定零值为参考，便于核对输入与输出。'),('放大相对压力',{'scale':'1000'},'对减去参考值后的结果统一乘以 1000；使用运动压力时可结合参考密度解释实际压差。')],
'randomise':[('减小扰动',{'magPerturbation':'0.01'},'把扰动幅值缩小十倍，观察初始扰动强度对后续流动的影响。'),('增大扰动',{'magPerturbation':'0.2'},'增加初始扰动幅值，比较流动响应时保持其他计算条件相同。')],
'zeroGradient':[('只生成压力派生场',{'fields':'(p)'},'保留原压力内部值，并为派生场配置零梯度边界。'),('处理压力与速度',{'fields':'(p U)'},'同时生成两类派生场，用于后续几何或场运算。')],
'limitFields':[('仅限制压力下限',{'fields':'(p)','limit':'min','min':'0'},'仅对所选标量设置下限；物理问题允许负表压时应据其压力定义选择阈值。'),('仅限制速度上限',{'fields':'(U)','limit':'max','max':'2'},'把速度限制到给定上界，可用于特定数值控制流程。')],
'derivedFields':[('只生成动量密度',{'derived':'(rhoU)'},'重点观察密度变化对动量分布的影响。'),('只生成总压',{'derived':'(pTotal)'},'供下游采样或写出对象读取总压。')],
'nearWallFields':[('靠近壁面采样',{'distance':'0.0005'},'把采样高度从 1 mm 改为 0.5 mm，分析更近壁面的速度。'),('远离壁面采样',{'distance':'0.002'},'把采样高度增至 2 mm，与较低采样高度的结果对照。')],
'streamLine':[('只向下游追踪',{'direction':'forward'},'从种子点沿速度方向积分，适合观察流体之后经过的区域。'),('增加单元内追踪步数',{'nSubCycle':'10'},'提高轨迹在单元内的分辨率，代价是更多追踪计算。')],
'wallBoundedStreamLine':[('反向追踪',{'direction':'backward'},'从壁面种子点逆速度方向追踪，观察流线来自何处。'),('延长追踪',{'lifeTime':'200'},'允许更多追踪步数，以观察更长的近壁路径。')],
'surfaceDistance':[('只计算边界距离',{'calculateCells':'false'},'省去内部单元的距离计算，保留边界相关结果。'),('同时计算单元距离',{'calculateCells':'true'},'保存计算域内的距离分布，便于按距离筛选区域。')],
'fieldExtents':[('放宽识别阈值',{'threshold':'0.1'},'把较薄的液膜也纳入范围统计。'),('收紧识别阈值',{'threshold':'0.9'},'聚焦相分数更高的连续液体区域。')],
'columnAverage':[('只平均速度',{'fields':'(U)'},'减少统计字段，观察网格柱方向平均后的速度分布。'),('只平均压力',{'fields':'(p)'},'输出同一方向上的平均压力。')],
'binField':[('保留完整向量贡献',{'decomposePatchValues':'false'},'不再拆分法向与切向贡献，直接统计字段本身。'),('保留分量分解',{'decomposePatchValues':'true'},'分别观察沿壁面法向和切向的贡献。')],
'fluxSummary':[('取消比例缩放',{'scaleFactor':'1'},'按输入通量的原量纲输出，便于与边界通量直接核对。'),('按十步间隔保存',{'writeControl':'timeStep','writeInterval':'10'},'连续监测区域通量，同时减少日志与文本行数。')],
'momentum':[('只统计总量',{'writeMomentum':'false','writePosition':'false','writeVelocity':'false'},'关闭附加分量场，以较小文件保留整体动量信息。'),('输出动量场',{'writeMomentum':'true'},'在总量之外查看动量的空间分布。')],
'momentumError':[('每步计算误差',{'executeControl':'timeStep','executeInterval':'1'},'更密集地检查误差随迭代或时间推进的变化。'),('每十步保存误差场',{'writeControl':'timeStep','writeInterval':'10'},'把保存频率与主结果输出分开设置。')],
'DESModelRegions':[('为指示场重新命名',{'result':'RANSLESIndicator'},'用容易识别的场名区分不同模型的结果。'),('每二十步记录区域变化',{'writeControl':'timeStep','writeInterval':'20'},'观察模型工作区域随非定常流动变化的过程。')],
'energySpectrum':[('每十步输出频谱',{'writeControl':'timeStep','writeInterval':'10'},'更密集地观察湍动能向小尺度传递的变化。'),('从指定时刻开始统计',{'timeStart':'0.1'},'跳过最初的启动阶段，再保存频谱。')],
'DMD':[('提高快照采样频率',{'executeInterval':'1'},'每个计算步都纳入快照，能够覆盖更高的时间频率，同时增加分解工作量。'),('分析压力模态',{'field':'p'},'从速度快照切换到压力快照，查看主要压力变化模式。')],
'Curle':[('只保留一个观察点',{'observerPositions':'((0.20 0.17 -0.01))'},'先检查一个测点的声压时序，再增加方向分布。'),('提高载荷采样频率',{'executeControl':'timeStep','executeInterval':'1'},'保留每步载荷变化，时间分辨率由求解器时间步决定。')],
'proudmanAcousticPower':[('使用空气参考值',{'rhoInf':'1.225','aRef':'343'},'按研究条件选择参考密度和声速，保持其与物理工况一致。'),('调整经验系数',{'alphaEps':'0.2'},'比较经验系数对声功率估计的敏感性。')],
'blendingFactor':[('打开统计日志',{'log':'true'},'在日志中查看格式混合相关信息。'),('每十步保存混合场',{'writeControl':'timeStep','writeInterval':'10'},'观察局部格式选择随迭代的变化。')],
'stabilityBlendingFactor':[('只启用非正交判据',{'switchResiduals':'false'},'保留示例中的网格非正交控制，单独观察其作用。'),('同时考虑 Courant 数',{'switchCo':'true','Co1':'1','Co2':'2'},'在 Courant 数由 1 增至 2 的区间调整格式权重。')],
'propellerInfo':[('只保存性能指标',{'writeWakeFields':'false'},'关闭尾流数据，重点监测推力、转矩及相关性能。'),('同时保存尾流',{'writeWakeFields':'true'},'保留采样圆盘上的流场信息，与推进器性能曲线对照。')],
'bladeForces':[('减少径向分段',{'nRadial':'5'},'较少分段便于先观察沿半径的总体变化。'),('加密径向分段',{'nRadial':'20'},'在几何与网格分辨率允许的条件下观察更细的叶片载荷分布。')],
'thermoCoupleProbes':[('采用更细热电偶',{'d':'0.0005'},'减小直径会改变热惯性与对流换热响应，可对照流体温度检查响应延迟。'),('降低发射率',{'epsilon':'0.5'},'观察热电偶表面辐射性质对测量温度的影响。')],
'comfort':[('比较较厚衣着',{'clothing':'1'},'衣着热阻提高后，比较相同环境下的舒适度变化。'),('比较较高活动水平',{'metabolicRate':'2'},'代谢率增大，人体产热相应变化；其余环境条件保持一致。')],
'XiReactionRate':[('逐步保存反应率',{'writeControl':'timeStep','writeInterval':'1'},'保留火焰发展过程中的密集时间数据。'),('只保存结束结果',{'writeControl':'onEnd'},'用于只关注最终状态的计算对比。')],
'reactingEulerHtcModel':[('改变参考温度',{'TRef':'353'},'参考温度决定换热系数所用温差，应与对应的物理定义一致。'),('单独命名换热结果',{'result':'liquidHtc'},'把液相换热系数与其他区域的结果分开。')],
'multiphaseInterHtcModel':[('改变参考温度',{'TRef':'353'},'在相同壁面热流下比较参考温差定义对换热系数的影响。'),('设置独立输出名',{'result':'bottomHtc'},'便于在结果中识别底部壁面的换热系数。')],
'electricPotential':[('只保存电势',{'writeDerivedFields':'false'},'先检查电势边界与分布，减少派生字段。'),('增加电势校正',{'nCorr':'3'},'增加外层校正次数，观察电势方程的迭代变化。')],
'scalarTransport':[('减小分子扩散',{'D':'0.0001'},'降低扩散后，标量分布更受对流支配；应同时检查网格和对流格式。'),('启动时清零标量',{'resetOnStartUp':'true'},'以新的零初始分布开始标量输运，入口注入条件仍由场边界决定。')],
'energyTransport':[('增加温度校正',{'nCorr':'2'},'对相同流场多执行校正，改善附加能量方程的代数求解。'),('设置明确的停止容差',{'tolerance':'1e-6'},'根据温度方程的初始残差控制校正过程。')],
'age':[('关闭扩散项',{'diffusion':'false'},'比较纯对流年龄与包含扩散时的更新差异。'),('增加附加校正',{'nCorr':'10'},'对同一流场更充分地迭代年龄方程。')],
'regionSizeDistribution':[('减少粒径箱数',{'nBins':'50'},'在相同直径范围内使用更宽的箱，观察总体分布。'),('聚焦小尺度区域',{'maxDiameter':'0.1','nBins':'50'},'收窄直径统计范围，并保留较细的分箱。')],
'extractEulerianParticles':[('提高相分数阈值',{'alphaThreshold':'0.5'},'以液相更集中的区域识别事件，比较阈值对提取结果的影响。'),('增加注入分箱',{'nLocations':'40'},'更细地组织收集面上的事件位置。')],
'cloudInfo':[('输出更多颗粒统计信息',{'verbose':'true'},'在日志中保留更详细的统计。'),('每步更新内存统计',{'sampleOnExecute':'true'},'让下游对象可以读取本步更新后的结果。')],
'particleDistribution':[('粒径采用更细箱宽',{'nameVsBinWidth':'((d 5e-6))'},'只分析粒径，并将分箱宽度减半。'),('只统计速度分布',{'nameVsBinWidth':'((U 5))'},'选择速度属性，便于比较颗粒速度的离散程度。')],
'sizeDistribution':[('输出归一化分布',{'normalize':'true'},'比较不同总颗粒数量下的分布形状。'),('扩大到整个网格',{'selectionMode':'all'},'统计全域分布，并与指定 cellZone 的局部分布比较。')],
'vtkCloud':[('只导出速度与粒径',{'fields':'(U d)'},'减少组分和温度属性，便于快速查看颗粒运动。'),('省略空颗粒云',{'prune':'true'},'避免生成没有颗粒位置的空输出。')],
'dsmcFields':[('每十步输出宏观场',{'writeControl':'timeStep','writeInterval':'10'},'观察统计量随采样积累的变化。'),('只在结束时输出',{'writeControl':'onEnd'},'将输出集中到统计结束后的状态。')],
'writeObjects':[('保存指定对象',{'writeOption':'anyWrite','objects':'(U p)'},'选择 U 和 p，按本对象的写出时刻保存。'),('仅保存自动写出对象',{'writeOption':'autoWrite','objects':'(".*")'},'按对象自身 AUTO_WRITE 属性筛选。')],
'areaWrite':[('只导出膜厚',{'fields':'(hf_film)'},'重点分析薄膜厚度变化。'),('改用 VTK 表面格式',{'surfaceFormat':'vtk'},'将有限面积结果交给 VTK 可视化流程。')],
'mapFields':[('只映射速度',{'fields':'(U)'},'将目标区域用于速度分析，减少其他字段的传递。'),('只映射压力',{'fields':'(p)'},'检查压力映射的平滑程度及边界处理。')],
'caseInfo':[('遇到缺项时发出提示',{'lookupMode':'warn'},'收集现有信息，同时在日志中指出未找到的条目。'),('每次完整输出同步汇总',{'writeControl':'writeTime','writeInterval':'1'},'使信息文件与主计算结果对应。')],
'PecletNo':[('单独命名诊断场',{'result':'Pe'},'在可视化列表中使用较短名称。'),('每十步保存',{'writeControl':'timeStep','writeInterval':'10'},'观察随速度或有效扩散变化的局部 Peclet 数。')],
'MachNo':[('单独命名马赫数场',{'result':'Ma'},'区分其他速度相关诊断量。'),('逐步保存马赫数',{'writeControl':'timeStep','writeInterval':'1'},'用于观察快速传播的压缩波或激波变化。')],
'AMIWeights':[('只记录统计值',{'writeFields':'false'},'保留权重范围等信息，减少接口场文件。'),('保存接口权重场',{'writeFields':'true'},'在 ParaView 中定位覆盖或插值质量变化的具体区域。')],
'timeActivatedFileUpdate':[('把切换延后到 0.05',{'timeVsFile':'((-1 "<system>/fvSolution.0") (0.05 "<system>/fvSolution.5"))'},'让初始求解设置维持更长时间，再进入下一阶段。'),('每步检查更新',{'executeControl':'timeStep','executeInterval':'1'},'让文件更新及时对应指定的模拟时间。')],
'multiRegion':[('只处理一个区域',{'regions':'(heater)'},'在包含 heater 的共轭传热算例中单独统计该区域。'),('选择两个区域',{'regions':'(heater topAir)'},'在同一配置中对固体和上部空气区域分别执行温度统计。')],
'externalCoupled':[('缩短等待轮询',{'waitInterval':'0.5'},'更频繁地检查外部响应文件，适合交互延迟较短的耦合。'),('限定最长等待时间',{'timeOut':'60'},'外部程序在一分钟内响应，超时后由工具反馈通信问题。')],
'syncObjects':[('每步同步',{'executeControl':'timeStep','executeInterval':'1'},'在每次推进时更新耦合数据。'),('每五步同步',{'executeControl':'timeStep','executeInterval':'5'},'在较松的耦合流程中降低数据交换频率。')],
'setFlow':[('将角速度减半',{'omega':'3.14159265359'},'相同半径处的切向速度相应减半。'),('延后反转时刻',{'reverseTime':'2'},'维持原旋转方向到 2 s，再反向输运。')],
'foamReport':[('显示可用替换键',{'debugKeys':'true'},'先检查数据来源与模板占位符的对应关系。'),('只生成结束报告',{'writeControl':'onEnd'},'让报告集中保存最终设置和结果。')],
'graphFunctionObject':[('扩大图像尺寸',{'width':'1200','height':'800'},'为多条曲线和图例提供更多像素。'),('限定系数显示范围',{'yMin':'-0.5','yMax':'0.5','drawGrid':'true'},'聚焦较小的系数变化，并使用网格辅助读数。')],
'dataCloud':[('导出颗粒温度',{'field':'T'},'在具有 T 属性的煤颗粒云中读取温度数据。'),('导出颗粒速度',{'field':'U'},'将数据属性改为颗粒速度，便于分析运动分布。')],
}
for name,vs in variants.items():d[name]['variants']=[dict(title=t,patch=p,explanation=e) for t,p,e in vs]
# Correct source example spelling to the actual reader used by v2512.
d['graphFunctionObject']['code']=d['graphFunctionObject']['code'].replace('xlabel','xLabel').replace('ylabel','yLabel')
(P/'profiles.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Contexts',sum(bool(p['explanation']) for p in d.values()),'specific examples',sum(len(p['variants']) for p in d.values()))
