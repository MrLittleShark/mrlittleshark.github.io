"""Explain the v2512 shell helpers from their actual function definitions."""
from pathlib import Path
import json,re,tarfile

ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).parent
commands=json.loads((ROOT/'source-openfoam/assets/commands.json').read_text(encoding='utf-8'))
source={}
with tarfile.open(ROOT/'.openfoam-work/replan/openfoam-v2512.tar.gz') as archive:
    for suffix in ['bin/tools/RunFunctions','bin/tools/CleanFunctions','etc/config.sh/aliases']:
        name=next(x for x in archive.getnames() if x.endswith('/'+suffix))
        source[suffix]=archive.extractfile(name).read().decode()
NOTES={
'canCompile':('检查 make、wmake 和 C++ 编译器是否可用。','canCompile\necho $?','退出码 0 表示检查通过。缺少工具时，函数在错误输出中说明缺项。'),
'cloneCase':('复制算例的 constant、system 和初始场目录。','cloneCase cavity cavity-study','第一个参数是源算例，第二个是尚不存在的目标目录。已有目标目录时函数返回错误，便于脚本避免混合两套输入。'),
'cloneParallelCase':('复制已分区的算例及选定时间数据。','cloneParallelCase sourceCase parallel-copy 0.5','两个目录参数之后可给出要复制的时间；省略时间时复制完整 processor 目录。'),
'compileApplication':('通过 wmake 编译指定目录中的应用程序。','compileApplication ./mySolver','目标目录包含 Make/files 与 Make/options。函数打印目标名称，再把目录传给 wmake。'),
'getApplication':('读取 controlDict 中的 application。','getApplication','返回求解器名称，常与 runApplication 的命令替换配合。'),
'getNumberOfPatchFaces':('读取指定网格边界的面数。','getNumberOfPatchFaces movingWall','读取 constant/polyMesh/boundary。第二个位置参数可指定多区域网格的区域名称。'),
'getNumberOfProcessors':('读取 decomposeParDict 中的 numberOfSubdomains。','getNumberOfProcessors\ngetNumberOfProcessors system/decomposeParDict','省略参数时使用 system/decomposeParDict。输出可用作 mpirun 的进程数。'),
'isParallel':('检查参数列表是否包含 -parallel。','isParallel -parallel\necho $?','匹配到 -parallel 时返回 0，否则返回 1；用于脚本条件判断。'),
'isTest':('检查参数列表是否包含 -test。','isTest -test\necho $?','返回码表示是否启用测试模式。'),
'notTest':('检查参数列表是否省略 -test。','notTest -parallel\necho $?','参数中没有 -test 时返回 0，可用于选择正常运行分支。'),
'isTrue':('把 on、yes、true 等开关值转换为 shell 返回码。','isTrue on\necho $?\nisTrue -dict system/controlDict -entry runTimeModifiable','真值返回 0，假值返回 1，无法识别的值返回 2。-dict 方式通过 foamDictionary 读取条目。'),
'remove0DirFields':('删除 0 目录中指定名称的场文件。','remove0DirFields Ux Uy Uz','仅用于准备好的练习副本；三个参数分别指定场名。多区域场可使用 -region 区域名。'),
'restore0Dir':('从 0.orig 恢复初始场目录。','restore0Dir','已有 0 目录会由模板替换。-processor 作用于分区，-all 同时处理主算例和分区。'),
'cleanAdiosOutput':('清理算例中的 adiosData 输出。','cleanAdiosOutput','函数同时检查 adiosData 与 system 目录是否存在。'),
'cleanApplication':('调用 wclean 清理当前应用的编译中间文件。','cleanApplication','在应用源码目录调用；后续可重新运行 wmake。'),
'cleanAuxiliary':('清理求解日志、ParaView 入口和辅助输出。','cleanAuxiliary','本函数会删除 log.*、*.foam 等匹配文件，适合已保存所需日志的算例副本。'),
'cleanCase':('清理时间结果、网格、分区和后处理输出，保留主要输入配置。','cleanCase','会删除生成的 polyMesh 和 processor 数据。适合从网格生成步骤重新开始的练习副本。'),
'cleanCase0':('清理算例结果，并删除 0 目录。','cleanCase0','通常与 0.orig 模板配合，随后用 restore0Dir 重建初始场。'),
'cleanDynamicCode':('清理动态编译生成的 dynamicCode 目录。','cleanDynamicCode','后续读到相应 coded 条目时会重新生成和编译动态代码。'),
'cleanFaMesh':('清理有限面积网格 faMesh。','cleanFaMesh -region film','区域名称决定 constant/finite-area 下的目标位置。'),
'cleanOptimisation':('清理优化结果和控制点输出。','cleanOptimisation','清理 optimisation 与 constant/controlPoints，重新计算前保留所需的优化历史。'),
'cleanPolyMesh':('清理体网格 polyMesh。','cleanPolyMesh -region fluid','省略 -region 时处理 constant/polyMesh；给出区域时处理该区域的网格。'),
'cleanPostProcessing':('清理后处理、VTK 和表面采样输出。','cleanPostProcessing','包括 postProcessing、VTK、EnSight 等目录，随后可重新执行后处理。'),
'cleanSamples':('清理 sets、samples 和 sampleSurfaces 采样结果。','cleanSamples','适合更改采样设置后重新输出，避免旧文件与新文件混合。'),
'cleanSnappyFiles':('清理 snappyHexMesh 的细化历史和辅助字段。','cleanSnappyFiles','包含 cellLevel、pointLevel 和 refinementHistory 等数据；需要继续自适应细化时应保留这些文件。'),
'cleanTimeDirectories':('清理非零数值时间目录。','cleanTimeDirectories','运行前在练习副本中用 ls 查看时间目录，并保存需要比较的结果。'),
'cleanUcomponents':('删除 0/Ux、0/Uy 和 0/Uz 三个速度分量文件。','cleanUcomponents','完整速度矢量场 0/U 保持原样。'),
'removeCase':('删除参数指定的整个算例目录。','removeCase ./discarded-practice','参数应指向已确认可以删除的练习副本。该函数递归删除整个目标目录。'),
'foamPV':('重新加载 ParaView 版本配置。','foamPV','读取当前 OpenFOAM 的 ParaView 环境设置；指定版本时会按安装配置寻找相应程序。'),
'foamPwd':('用 OpenFOAM 环境变量缩写显示当前路径。','foamPwd','例如把用户算例路径的公共前缀显示为 $FOAM_RUN，便于写入说明和日志。'),
'wmRefresh':('按当前设置重新加载 OpenFOAM 环境。','wmRefresh','先清理旧环境变量，再读取同一项目的 etc/bashrc。')}
ALIASES={
'app':('应用程序源码目录','$WM_PROJECT_DIR/applications'),
'foam':('OpenFOAM 安装根目录','$WM_PROJECT_DIR'),
'lib':('已编译的库目录','$FOAM_LIBBIN'),
'run':('个人算例目录','$FOAM_RUN'),
'src':('C++ 库源码目录','$WM_PROJECT_DIR/src'),
'sol':('求解器源码目录','$WM_PROJECT_DIR/applications/solvers'),
'tut':('官方教程目录','$FOAM_TUTORIALS'),
'util':('工具程序源码目录','$WM_PROJECT_DIR/applications/utilities'),
'ufoam':('个人 OpenFOAM 工作目录','$WM_PROJECT_USER_DIR'),
'uapp':('个人应用源码目录','$WM_PROJECT_USER_DIR/applications'),
'usol':('个人求解器源码目录','$WM_PROJECT_USER_DIR/applications/solvers'),
'uutil':('个人工具源码目录','$WM_PROJECT_USER_DIR/applications/utilities')}
for name,(label,location) in ALIASES.items():NOTES[name]=('切换到'+label+'。',name+'\npwd','这是 cd 的别名，对应目录为 `'+location+'`。先创建尚不存在的个人目录，再使用相应别名。')
for name,option in [('wmDP','WM_PRECISION_OPTION=DP'),('wmSP','WM_PRECISION_OPTION=SP'),('wmSPDP','WM_PRECISION_OPTION=SPDP'),('wmInt32','WM_LABEL_SIZE=32'),('wmInt64','WM_LABEL_SIZE=64')]:
    NOTES[name]=('重新加载环境并设置 '+option+'。',name+'\necho "$WM_OPTIONS"','这会选择对应的精度或标签长度环境。该配置需要匹配的程序与库，可从源码构建。')
NOTES['wmSet']=('按给定变量重新加载 OpenFOAM 环境。','wmSet WM_LABEL_SIZE=64','参数传给 etc/bashrc，用于选择编译和运行配置。')
NOTES['wmUnset']=('清除当前 shell 中的 OpenFOAM 环境设置。','wmUnset','随后可重新 source 所需版本的 etc/bashrc。')
result={}
for item in commands:
    name=item['name']
    if name not in NOTES:continue
    summary,usage,explanation=NOTES[name];file=item.get('sourcePath','')
    pre='source "$WM_PROJECT_DIR/'+file+'"' if file else 'source "$WM_PROJECT_DIR/etc/config.sh/aliases"'
    example=pre+'\n'+usage
    text=source.get(file,source['etc/config.sh/aliases'])
    match=re.search(r'(?m)^'+re.escape(name)+r'\(\)\s*\n\{[\s\S]*?^\}',text)
    if not match:match=re.search(r'(?m)^alias '+re.escape(name)+r'=.*$',text)
    body='## 调用示例\n\n```bash\n'+example+'\n```\n\n'+explanation+'\n\n## 在脚本中查看定义\n\n```bash\ntype '+name+'\n```\n\n`type` 显示函数定义或别名展开，可用于确认当前终端加载的实现。'
    if match:body+='\n\n<details><summary>v2512 实现</summary>\n\n```bash\n'+match.group()+'\n```\n\n</details>'
    result[name]={'summary':summary,'example':example,'body':body,'examples':[{'title':'调用示例','code':example,'explanation':explanation},{'title':'查看定义','code':'type '+name,'explanation':'查看当前终端中的函数或别名定义。'}]}
(HERE/'shell-command-guides.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Shell guides:',len(result))
