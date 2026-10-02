---
title: "12 常用 Linux 命令"
layout: reference
description: "常用 Linux 命令：用法与配置实例。"
cms_slug: "reference-manual-12"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>本章列出 GNU/Linux 和 Bash 常用命令。“文件”和“目录”等名称表示待替换参数。命令依据见 S5 至 S12。</p>
<h3>12.1 文件管理与内容查看</h3>
<div class="table-scroll"><table>
<tr><th>命令</th><th>含义与语法</th><th>具体示例</th></tr>
<tr><td>pwd</td><td>显示当前目录：pwd [-P]</td><td>pwd -P</td></tr>
<tr><td>ls</td><td>列出目录：ls [选项] [路径]</td><td>ls -lah constant/polyMesh</td></tr>
<tr><td>cd</td><td>切换目录：cd 路径</td><td>cd "$FOAM_RUN"；cd ..；cd -</td></tr>
<tr><td>mkdir</td><td>创建目录：mkdir [-p] 目录</td><td>mkdir -p cases/cavity</td></tr>
<tr><td>cp</td><td>复制文件或目录：cp [选项] 源 目标</td><td>cp -a cavity cavity_backup</td></tr>
<tr><td>mv</td><td>移动或重命名：mv [选项] 源 目标</td><td>mv log log.simpleFoam；-i 在覆盖前询问</td></tr>
<tr><td>rm</td><td>删除文件：rm [选项] 路径</td><td>rm -i log.old；rm -r ./caseCopy 递归删除目录</td></tr>
<tr><td>rmdir</td><td>删除空目录：rmdir 目录</td><td>rmdir emptyCase</td></tr>
<tr><td>touch</td><td>创建空文件或更新时间戳：touch 文件</td><td>touch case.foam，供内置读取器识别算例</td></tr>
<tr><td>ln</td><td>建立链接：ln -s 目标 链接名</td><td>ln -s ../shared/geometry constantGeometry</td></tr>
<tr><td>realpath</td><td>解析绝对路径：realpath 路径</td><td>realpath ./constant/polyMesh</td></tr>
<tr><td>basename</td><td>取路径最后部分：basename 路径</td><td>basename /tmp/case/system/controlDict</td></tr>
<tr><td>dirname</td><td>取父路径：dirname 路径</td><td>dirname /tmp/case/system/controlDict</td></tr>
<tr><td>cat</td><td>输出文件内容：cat 文件</td><td>cat system/controlDict</td></tr>
<tr><td>less</td><td>分页浏览：less 文件</td><td>less log.simpleFoam；/关键词 搜索，q 退出</td></tr>
<tr><td>head</td><td>查看文件开头：head -n 行数 文件</td><td>head -n 30 log.simpleFoam</td></tr>
<tr><td>tail</td><td>查看文件末尾或跟踪更新：tail [-n N] [-f] 文件</td><td>tail -f log.simpleFoam；Ctrl+C 退出监控</td></tr>
<tr><td>file</td><td>判断文件类型：file 路径</td><td>file constant/polyMesh/points</td></tr>
<tr><td>stat</td><td>查看文件详细元数据：stat 路径</td><td>stat system/controlDict</td></tr>
<tr><td>wc</td><td>统计行数词数和字节数：wc [选项] 文件</td><td>wc -l log.simpleFoam</td></tr>
<tr><td>du</td><td>统计磁盘占用：du -sh 路径</td><td>du -sh processor*</td></tr>
<tr><td>df</td><td>文件系统剩余空间：df -h [路径]</td><td>df -h .</td></tr>
</table></div>
<p>rm 直接删除文件。执行前核对目标路径，并保留算例原始配置。</p>
<h3>12.2 文本检索与处理</h3>
<div class="table-scroll"><table>
<tr><th>命令</th><th>含义与语法</th><th>具体示例</th></tr>
<tr><td>find</td><td>按路径和属性查找：find 路径 条件</td><td>find "$FOAM_TUTORIALS" -name blockMeshDict</td></tr>
<tr><td>grep</td><td>匹配文本：grep [选项] 模式 文件</td><td>grep -n 'Courant Number' log.pimpleFoam</td></tr>
<tr><td>rg</td><td>递归文本检索：rg [选项] 模式 路径，需安装 ripgrep</td><td>rg -n 'maxCo' system</td></tr>
<tr><td>sort</td><td>排序：sort [选项] 文件</td><td>sort -n times.txt</td></tr>
<tr><td>uniq</td><td>合并相邻重复行：uniq [选项] 文件</td><td>sort models.txt | uniq -c</td></tr>
<tr><td>cut</td><td>按分隔符选列：cut -d 分隔符 -f 列 文件</td><td>cut -d',' -f1,3 data.csv，按逗号分列</td></tr>
<tr><td>awk</td><td>按字段和条件处理：awk '程序' 文件</td><td>awk '/ExecutionTime/ {print $3}' log.simpleFoam</td></tr>
<tr><td>sed</td><td>流式文本替换：sed '表达式' 文件</td><td>sed 's/endTime 1;/endTime 2;/' controlDict &gt; controlDict.new</td></tr>
<tr><td>tr</td><td>替换或删除字符：tr 集合1 集合2</td><td>tr -d '\r' &lt; Allrun &gt; Allrun.unix</td></tr>
<tr><td>diff</td><td>比较文本差异：diff [选项] 文件1 文件2</td><td>diff -u fvSolution.old system/fvSolution</td></tr>
<tr><td>cmp</td><td>逐字节比较：cmp 文件1 文件2</td><td>cmp meshA.gz meshB.gz</td></tr>
<tr><td>tee</td><td>同时输出至文件和终端：tee [选项] 文件</td><td>simpleFoam 2&gt;&amp;1 | tee log.simpleFoam</td></tr>
<tr><td>xargs</td><td>将输入转换为命令参数：xargs [选项] 命令</td><td>find . -name '*.log' -print0 | xargs -0 wc -l</td></tr>
</table></div>
<p>OpenFOAM 字典的结构化条目使用 foamDictionary 修改。grep 的 -r、-n、-i 和 -E 分别表示递归搜索、显示行号、忽略大小写和使用扩展正则表达式。搜索模式用引号包围，以保留括号、星号和反斜线。</p>
<pre><code class="language-bash">grep -E 'Solving for|Courant Number' log.pimpleFoam
awk '/ExecutionTime/ {print $3}' log.simpleFoam
find . -name '*.log' -print0 | xargs -0 wc -l
simpleFoam 2&gt;&amp;1 | tee log.simpleFoam</code></pre>
<h3>12.3 系统管理与帮助查询</h3>
<div class="table-scroll"><table>
<tr><th>命令</th><th>含义与语法</th><th>具体示例</th></tr>
<tr><td>ps</td><td>查看进程：ps [选项]</td><td>ps -u "$USER" -o pid,etime,cmd</td></tr>
<tr><td>pgrep</td><td>按名称查找进程：pgrep [选项] 模式</td><td>pgrep -af simpleFoam</td></tr>
<tr><td>top</td><td>实时查看 CPU、内存及进程状态</td><td>top，q 退出</td></tr>
<tr><td>htop</td><td>交互式资源监控，需安装</td><td>htop</td></tr>
<tr><td>free</td><td>内存统计：free -h</td><td>free -h</td></tr>
<tr><td>lscpu</td><td>CPU 拓扑和指令信息</td><td>lscpu</td></tr>
<tr><td>nproc</td><td>可用处理单元数</td><td>nproc</td></tr>
<tr><td>jobs</td><td>当前 shell 后台作业列表</td><td>jobs -l</td></tr>
<tr><td>bg</td><td>在后台恢复当前 shell 的挂起作业</td><td>bg %1</td></tr>
<tr><td>fg</td><td>将后台作业转至前台</td><td>fg %1</td></tr>
<tr><td>wait</td><td>等待子进程并取得返回状态</td><td>wait "$solver_pid"</td></tr>
<tr><td>kill</td><td>向进程发送信号：kill [-信号] PID</td><td>kill -TERM 12345，PID 替换为实际进程号</td></tr>
<tr><td>nohup</td><td>忽略挂断信号运行程序</td><td>nohup simpleFoam &gt; log.simpleFoam 2&gt;&amp;1 &amp;</td></tr>
<tr><td>nice</td><td>以指定优先级启动：nice -n 增量 命令</td><td>nice -n 10 simpleFoam</td></tr>
<tr><td>time</td><td>测量命令耗时</td><td>time blockMesh；/usr/bin/time -v simpleFoam 输出资源统计</td></tr>
<tr><td>chmod</td><td>修改权限：chmod 模式 文件</td><td>chmod u+x Allrun</td></tr>
<tr><td>chown</td><td>修改所有者：chown 用户:组 路径</td><td>sudo chown "$USER:$USER" ./ownedFile</td></tr>
<tr><td>umask</td><td>查看或设置新建权限掩码</td><td>umask 022；只影响此后新建对象</td></tr>
<tr><td>sudo</td><td>以获授权身份执行命令</td><td>sudo apt install gnuplot</td></tr>
<tr><td>man</td><td>查看手册：man 命令</td><td>man find</td></tr>
<tr><td>help</td><td>Bash 内置命令帮助</td><td>help cd</td></tr>
<tr><td>type</td><td>查询命令实际类型</td><td>type foam tut blockMesh</td></tr>
<tr><td>command -v</td><td>查询命令对应的程序路径</td><td>command -v simpleFoam</td></tr>
<tr><td>which</td><td>查询可执行程序路径</td><td>which simpleFoam；别名定义使用 type 查询</td></tr>
<tr><td>env</td><td>显示环境变量或按指定环境运行命令</td><td>env；<code>env FOAM_SIGFPE=true simpleFoam</code></td></tr>
<tr><td>printenv</td><td>打印环境变量</td><td>printenv WM_PROJECT_DIR</td></tr>
<tr><td>export</td><td>导出变量给子进程</td><td><code>export OMP_NUM_THREADS=1</code></td></tr>
<tr><td>unset</td><td>移除变量或函数</td><td>unset FOAM_SETNAN</td></tr>
<tr><td>source 或 .</td><td>在当前 shell 执行脚本</td><td>source ~/.bashrc</td></tr>
<tr><td>history</td><td>查看命令历史</td><td>history 20</td></tr>
<tr><td>sleep</td><td>暂停：sleep 秒数</td><td>sleep 2</td></tr>
<tr><td>date</td><td>显示日期时间</td><td>date '+%F %T'</td></tr>
<tr><td>printf</td><td>格式化输出</td><td>printf '%s\n' "$FOAM_RUN"</td></tr>
</table></div>
<p>Ctrl+C 发送中断信号，Ctrl+Z 暂停进程。需要保存结果后停止求解时，使用 stopAt 或 foamEndJob。kill -9 强制结束进程，不执行结果写出及清理操作。</p>
<h3>12.4 文件传输与远程管理</h3>
<div class="table-scroll"><table>
<tr><th>命令</th><th>含义与语法</th><th>具体示例</th></tr>
<tr><td>tar</td><td>归档或解包</td><td>tar -czf case.tar.gz case/；tar -tzf case.tar.gz 预览；tar -xzf case.tar.gz 解包</td></tr>
<tr><td>gzip</td><td>gzip 压缩或解压</td><td>gzip -k log.simpleFoam 保留原文件；gzip -d file.gz 解压</td></tr>
<tr><td>zip 和 unzip</td><td>ZIP 压缩与解包</td><td>zip -r case.zip case/；unzip -l case.zip；unzip case.zip</td></tr>
<tr><td>sha256sum</td><td>计算校验和</td><td>sha256sum case.tar.gz</td></tr>
<tr><td>curl</td><td>下载或 HTTP 请求</td><td>curl -L -o guide.pdf 'https://dl.openfoam.com/source/v2512/UserGuide.pdf'</td></tr>
<tr><td>wget</td><td>下载文件</td><td>wget -O guide.pdf 'https://dl.openfoam.com/source/v2512/UserGuide.pdf'</td></tr>
<tr><td>ssh</td><td>远程登录：ssh 用户@主机</td><td>ssh user@compute.example.org</td></tr>
<tr><td>scp</td><td>复制文件到远端</td><td>scp case.tar.gz user@compute.example.org:~/runs/</td></tr>
<tr><td>rsync</td><td>增量同步</td><td>rsync -av --dry-run case/ user@compute.example.org:~/runs/case/</td></tr>
<tr><td>tmux</td><td>建立和恢复终端会话</td><td>tmux new -s of；按 Ctrl+B 后按 D 脱离；tmux attach -t of 恢复</td></tr>
<tr><td>git</td><td>管理配置和脚本版本</td><td>git init；git status；git diff；git add system constant 0</td></tr>
<tr><td>apt</td><td>管理 Debian 和 Ubuntu 软件包</td><td>apt search openfoam；sudo apt install gnuplot</td></tr>
</table></div>
<p>rsync 源路径末尾的斜线表示同步目录内容，--dry-run 用于预览，--delete 删除目标端多余文件。算例版本管理通常跟踪配置和脚本，大型计算结果单独保存。</p>
<h3>12.5 Bash 语法与批处理</h3>
<div class="table-scroll"><table>
<tr><th>符号或结构</th><th>含义</th><th>示例</th></tr>
<tr><td>&gt;</td><td>覆盖标准输出文件</td><td>blockMesh &gt; log.blockMesh</td></tr>
<tr><td>&gt;&gt;</td><td>追加标准输出</td><td>echo done &gt;&gt; workflow.log</td></tr>
<tr><td>2&gt;</td><td>单独重定向标准错误</td><td>blockMesh 2&gt; errors.txt</td></tr>
<tr><td>2&gt;&amp;1</td><td>将标准错误并入当前标准输出</td><td>simpleFoam &gt; log.simpleFoam 2&gt;&amp;1</td></tr>
<tr><td>|</td><td>将前一命令的标准输出传给后一命令</td><td>simpleFoam 2&gt;&amp;1 | tee log.simpleFoam</td></tr>
<tr><td>&amp;</td><td>后台运行</td><td>simpleFoam &gt; log.simpleFoam 2&gt;&amp;1 &amp;</td></tr>
<tr><td>&amp;&amp;</td><td>前一命令成功才继续</td><td>blockMesh &amp;&amp; checkMesh</td></tr>
<tr><td>||</td><td>前一命令失败时执行后一命令</td><td>见下方错误分支示例</td></tr>
<tr><td>单引号</td><td>保留字面文本</td><td>echo '$FOAM_RUN' 输出变量名</td></tr>
<tr><td>双引号</td><td>展开变量并保持路径整体</td><td>cd "$FOAM_RUN"</td></tr>
<tr><td>$(命令)</td><td>命令替换</td><td><code>app=$(getApplication)</code></td></tr>
<tr><td>$?</td><td>上一条命令退出状态</td><td>echo "$?"；0 通常表示成功</td></tr>
<tr><td>$!</td><td>最近后台任务 PID</td><td><code>solver_pid=$!</code></td></tr>
<tr><td>for</td><td>批量遍历</td><td>见下方多个算例循环</td></tr>
<tr><td>if 与 test</td><td>条件判断</td><td>if [ -f system/controlDict ]; then ...; fi</td></tr>
<tr><td>set -e 与 pipefail</td><td>-e 控制失败时退出，pipefail 启用管道失败状态检测</td><td>set -euo pipefail，具体退出行为取决于 Bash 控制结构</td></tr>
</table></div>
<pre><code class="language-bash">set -o pipefail
simpleFoam 2&gt;&amp;1 | tee log.simpleFoam
blockMesh || { echo 'blockMesh failed' &gt;&amp;2; exit 1; }

for case_dir in caseA caseB caseC; do
    blockMesh -case "$case_dir" &gt; "$case_dir/log.blockMesh" 2&gt;&amp;1
done

cat &gt; system/localSettings &lt;&lt;'EOF'
// 保留字典引用
pFinal { $p; relTol 0; }
EOF</code></pre>
<p>批量执行前建立各算例目录，并通过退出状态判断各步骤是否成功。</p>
