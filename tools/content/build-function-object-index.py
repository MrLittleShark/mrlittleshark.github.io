"""Build the index with one independent reference route per functionObject."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXT = (ROOT / 'tools/content/function-objects/lessons/16.md').read_text(encoding='utf-8')
CATEGORIES = {
    2: '场运算', 3: '采样与统计', 4: '湍流与声学',
    5: '力与物理量', 6: '颗粒与两相', 7: '文件与控制',
}
LESSONS = {}
for line in TEXT.splitlines():
    match = re.search(r'/read/\?slug=function-objects-(\d+)', line)
    if match:
        for name in re.findall(r'`([^`]+)`', line):
            LESSONS[name] = match.group(1)
for chapter, names in {
    '07': 'magSqr components add subtract multiply div flowType enstrophy LambVector surfaceInterpolate',
    '13': 'writeCellCentres writeCellVolumes',
    '14': 'PecletNo MachNo processorField timeInfo AMIWeights caseInfo',
}.items():
    LESSONS.update({name: chapter for name in names.split()})

# Grouped rows in the course index become one card for each type.
DESCRIPTIONS = {
    'mag': '计算场的模，例如速度大小。',
    'magSqr': '计算场的模平方。',
    'add': '将多个场相加，生成结果场。',
    'subtract': '将场相减，用于计算差值。',
    'multiply': '将多个场相乘，生成结果场。',
    'grad': '计算标量场或向量场的梯度。',
    'div': '计算场的散度。',
    'vorticity': '由速度场计算涡量。',
    'enstrophy': '由速度场计算拟涡能。',
    'LambVector': '计算涡量与速度的叉积。',
    'Q': '计算 Q 判据，用于观察旋转与应变的关系。',
    'Lambda2': '计算 Lambda2，用于识别涡结构。',
    'flowType': '根据速度梯度区分局部流动类型。',
    'probes': '记录指定空间位置上的场值。',
    'patchProbes': '记录边界面上指定位置的场值。',
    'sets': '沿线或点集采样，输出场值剖面。',
    'surfaces': '在截面、等值面或指定表面上采样。',
    'streamLine': '从种子点出发追踪流线。',
    'wallBoundedStreamLine': '追踪受壁面约束的流线。',
    'volFieldValue': '对体区域计算平均、积分或其他归约值。',
    'surfaceFieldValue': '计算选定表面的流量、平均值或积分。',
    'fieldMinMax': '记录场的最小值、最大值及其位置。',
    'fieldStatistics': '统计场值的空间分布特征。',
    'forces': '计算指定边界上的合力和力矩。',
    'forceCoeffs': '计算升力、阻力与力矩系数。',
    'yPlus': '计算壁面的 y+，检查近壁网格。',
    'wallShearStress': '输出壁面剪切应力。',
    'wallHeatFlux': '计算壁面热流密度与热流积分。',
    'heatTransferCoeff': '按所选模型计算换热系数。',
    'interfaceHeight': '监测两相流的等效液位。',
    'regionSizeDistribution': '统计连通相区域的等效直径分布。',
    'readFields': '将指定场读入对象数据库。',
    'writeObjects': '将对象数据库中的指定对象写入文件。',
    'writeCellCentres': '输出单元中心坐标。',
    'writeCellVolumes': '输出单元体积。',
    'processorField': '用场值标记单元所属的并行分区。',
    'vtkWrite': '将指定字段导出为 VTK 格式。',
    'ensightWrite': '将指定字段导出为 EnSight 格式。',
    'solverInfo': '记录线性求解器的残差与迭代信息。',
    'continuityError': '监测连续性误差。',
    'CourantNo': '计算 Courant 数，检查时间步与流速的关系。',
    'PecletNo': '计算 Peclet 数，比较对流与扩散的强弱。',
    'MachNo': '计算 Mach 数。',
    'AMIWeights': '检查 AMI 接口的插值权重。',
    'runTimeControl': '根据残差、场值等条件控制计算过程。',
    'setTimeStep': '按指定规则设置时间步。',
    'abort': '通过外部停止文件结束计算。',
    'caseInfo': '输出算例与网格等概要信息。',
    'timeInfo': '记录时间与运行消耗。',
}
PARAMETERS = {
    'probes': '`fields`、`probeLocations`、`fixedLocations`、`interpolationScheme`',
    'patchProbes': '`patches`、`fields`、`probeLocations`、`writeControl`',
    'sets': '`fields`、`setFormat`、`interpolationScheme`、`sets`',
    'surfaces': '`fields`、`surfaceFormat`、`interpolationScheme`、`surfaces`',
    'volFieldValue': '`regionType`、`name`、`operation`、`fields`、`weightField`',
    'surfaceFieldValue': '`regionType`、`name`、`operation`、`fields`、`weightField`',
    'forces': '`patches`、`rho`、`rhoInf`、`CofR`',
    'forceCoeffs': '`patches`、`rho`、`rhoInf`、`CofR`、`liftDir`、`dragDir`、`magUInf`、`Aref`、`lRef`',
}
rows = []
section = 0
for line in TEXT.splitlines():
    heading = re.match(r'## (\d+)\.', line)
    if heading:
        section = int(heading.group(1))
    if section not in CATEGORIES or not line.startswith('| `'):
        continue
    columns = [v.strip() for v in line.strip('|').split('|')]
    for name in re.findall(r'`([^`]+)`', columns[0]):
        chapter = LESSONS.get(name, '16')
        rows.append({
            'name': name, 'category': CATEGORIES[section],
            'description': DESCRIPTIONS.get(name, columns[1]),
            'parameters': PARAMETERS.get(name, columns[2] if len(columns) > 2 else ''),
            'url': '/read/?slug=function-objects-' + chapter,
            'linkLabel': '参数与用法' if chapter != '16' else '分类与选用',
        })
# Time statistics is taught separately from the grouped expansion index.
for name, description, parameters in [
    ('fieldAverage', '计算场的时间平均值与脉动二阶矩。', '`fields`、`mean`、`prime2Mean`、`base`、`window`'),
    ('valueAverage', '对其他功能对象输出的数值做时间平均。', '`functionObject`、`fields`、`window`'),
]:
    rows.append({'name': name, 'category': '采样与统计', 'description': description,
                 'parameters': parameters, 'url': '/read/?slug=function-objects-08', 'linkLabel': '参数与用法'})
assert len({row['name'] for row in rows}) == len(rows), 'Duplicate type'
profiles = json.loads((ROOT / 'tools/content/function-object-reference/profiles.json').read_text(encoding='utf-8'))
for row in rows:
    row['url'] = '/function-objects/' + row['name'].lower() + '/'
    row['description'] = profiles[row['name']]['description']
    row['linkLabel'] = '配置与示例'
    row['lessonUrl'] = profiles[row['name']]['lesson']
output = ROOT / 'source-openfoam/assets/function-objects.json'
output.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(rows)} functionObject types -> {output}')
