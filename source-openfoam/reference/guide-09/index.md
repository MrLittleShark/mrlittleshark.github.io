---
title: "第 9 章　并行计算与集群作业"
layout: reference
description: "并行计算与集群作业：用法与配置实例。"
cms_slug: "reference-guide-09"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>9.1 并行的三步骤</h2>
<p>OpenFOAM 的并行是区域分解：把网格切成 N 块，每块交给一个进程，进程之间在交界面上交换数据。所以流程固定为三步：</p>
<pre><code class="language-bash">decomposePar                              # ① 切分：生成 processor0/ … processorN-1/
mpirun -np 8 simpleFoam -parallel         # ② 并行求解（-parallel 不能漏）
reconstructPar                            # ③ 合并结果回主目录</code></pre>
<p>-parallel 漏了会怎样：8 个进程各自把整个算例独立算一遍，互相覆盖对方的输出。日志看起来”正常”但结果是错的，而且慢 8 倍。这是初学者最隐蔽的错误之一。</p>
<h2>9.2 decomposePar</h2>
<pre><code class="language-plaintext">decomposePar [-force] [-copyZero] [-fields] [-latestTime] [-time &lt;范围&gt;] [-cellDist] [-dry-run]</code></pre>
<div class="table-scroll"><table>
<tr><th>选项</th><th>作用</th></tr>
<tr><td>-force</td><td>先删掉已有的 processor* 再分（改了网格重新分时必用）</td></tr>
<tr><td>-fields</td><td>只分场，不分网格（网格已分好、只是换了初场时用，快很多）</td></tr>
<tr><td>-copyZero</td><td>原样复制 0/ 而不做插值分解</td></tr>
<tr><td>-latestTime</td><td>只分解最新时刻（续算时用）</td></tr>
<tr><td>-cellDist</td><td>输出 cellDist 场，可在 ParaView 里看分区效果</td></tr>
</table></div>
<p>示例</p>
<pre><code class="language-bash">decomposePar -force
decomposePar -cellDist        # 想检查分区是否合理时
paraFoam                      # 在 ParaView 里显示 cellDist，看分块是否均匀</code></pre>
<p>配置文件 system/decomposeParDict 见第 17 章。</p>
<h2>9.3 mpirun 的常用写法</h2>
<pre><code class="language-bash">mpirun -np 8 simpleFoam -parallel &gt; log.simpleFoam 2&gt;&amp;1 &amp;
mpirun -np 16 interFoam -parallel -fileHandler collated &gt; log 2&gt;&amp;1 &amp;
mpirun --hostfile hosts -np 32 pimpleFoam -parallel &gt; log 2&gt;&amp;1 &amp;   # 多机</code></pre>
<p>-np 必须等于 decomposeParDict 里的 numberOfSubdomains，不一致会直接报错退出。</p>
<p>核数怎么选：经验值是每个核 5 万–10 万网格。核给太多，每核网格太少，通信时间超过计算时间，反而更慢。100 万网格的算例，用 8–16 核通常就是最优区间。</p>
<h2>9.4 reconstructPar / reconstructParMesh</h2>
<pre><code class="language-plaintext">reconstructPar                        # 合并所有时刻
reconstructPar -latestTime            # 只合并最后一个时刻（最常用）
reconstructPar -newTimes              # 只合并尚未合并过的时刻
reconstructPar -fields '(U p)'        # 只合并部分场
reconstructParMesh -constant          # 合并网格（并行 snappyHexMesh 之后必须做）</code></pre>
<p>什么时候可以不合并：只是想在 ParaView 里看结果的话，直接用 Decomposed Case 模式读 processor*（见 8.5），省下大量时间和磁盘。需要合并的场景：要做 mapFields、要把结果交给别人、要用串行工具处理。</p>
<h2>9.5 redistributePar —— 变更核数而不重新分解</h2>
<pre><code class="language-bash">mpirun -np 16 redistributePar -overwrite -parallel      # 8 核结果改到 16 核继续算
mpirun -np 8  redistributePar -reconstruct -parallel    # 相当于并行版 reconstructPar，大算例快得多
mpirun -np 8  redistributePar -decompose -parallel      # 并行版 decomposePar</code></pre>
<p>大规模结果可评估 redistributePar -reconstruct 的并行重构流程。是否优于串行重构取决于文件处理器、并行文件系统、进程数和字段数量，应在代表性数据上比较内存与耗时。</p>
<h2>9.6 collated 文件模式（大规模并行必备）</h2>
<p>默认情况下 1000 核会生成 1000 个目录、每个目录里一堆小文件。文件系统（尤其是集群的并行文件系统）会被这种小文件海拖垮。</p>
<pre><code class="language-bash">mpirun -np 256 simpleFoam -parallel -fileHandler collated</code></pre>
<p>所有进程的数据写进 processors256/ 下的少量合并文件。也可以在 etc/controlDict 或算例 controlDict 的 OptimisationSwitches 里全局设定：</p>
<pre><code class="language-plaintext">OptimisationSwitches
{
    fileHandler collated;
    maxThreadFileBufferSize 2e9;    // 用后台线程写，计算不必等 I/O
}</code></pre>
<p>转换回普通格式：foamFormatConvert -fileHandler uncollated。</p>
<h2>9.7 并行时的常见操作</h2>
<pre><code class="language-bash">mpirun -np 8 checkMesh -parallel                 # 并行查网格
mpirun -np 8 snappyHexMesh -overwrite -parallel  # 并行生成网格
mpirun -np 8 renumberMesh -overwrite -parallel
mpirun -np 8 postProcess -func Q -latestTime -parallel
foamListTimes -rm -processor                     # 清理 processor* 里的时间目录</code></pre>
<h2>9.8 集群作业脚本模板</h2>
<p>SLURM</p>
<pre><code class="language-bash">#!/bin/bash
#SBATCH --job-name=of_case
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=32
#SBATCH --time=24:00:00
#SBATCH --output=slurm-%j.out

source $HOME/OpenFOAM/OpenFOAM-v2512/etc/bashrc

cd $SLURM_SUBMIT_DIR
decomposePar -force &gt; log.decomposePar 2&gt;&amp;1
srun --mpi=pmi2 simpleFoam -parallel -fileHandler collated &gt; log.simpleFoam 2&gt;&amp;1
reconstructPar -latestTime &gt; log.reconstructPar 2&gt;&amp;1</code></pre>
<p>提交与查看：</p>
<pre><code class="language-plaintext">sbatch job.sh          # 提交
squeue -u $USER        # 查看排队/运行状态
scancel &lt;作业号&gt;       # 取消
sacct -j &lt;作业号&gt;      # 查看资源使用</code></pre>
<p>PBS / Torque</p>
<pre><code class="language-bash">#!/bin/bash
#PBS -N of_case
#PBS -l nodes=2:ppn=32
#PBS -l walltime=24:00:00
#PBS -j oe

source $HOME/OpenFOAM/OpenFOAM-v2512/etc/bashrc
cd $PBS_O_WORKDIR
decomposePar -force &gt; log.decomposePar 2&gt;&amp;1
mpirun -np 64 simpleFoam -parallel &gt; log.simpleFoam 2&gt;&amp;1
qsub job.sh      $ qstat -u $USER      $ qdel &lt;作业号&gt;</code></pre>
<p>集群运行中常见的两类环境问题：① 计算节点没 source 环境 —— 脚本里必须显式 source .../etc/bashrc（或用 foamExec）；② 集群的 MPI 与编译 OpenFOAM 时用的 MPI 不是同一个 —— 表现为一跑就 mpirun 报符号错误，解决办法是用集群的 module load 加载与编译时一致的 MPI。</p>
