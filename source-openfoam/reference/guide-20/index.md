---
title: "第 20 章　OpenFOAM 运行所需的 Linux 命令"
layout: reference
description: "OpenCFD v2512 OpenFOAM 运行所需的 Linux 命令；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>OpenFOAM 没有图形界面，终端就是你的操作台。这一章只收跑算例真正会用到的命令，每条都配一个 OpenFOAM 场景的例子。</p>
<h2>20.1 走路与看路：目录操作</h2>
<div class="table-scroll"><table>
<tr><th>命令</th><th>作用</th><th>例子</th></tr>
<tr><td>pwd</td><td>我在哪</td><td>pwd</td></tr>
<tr><td>ls</td><td>列目录</td><td>ls -lh（带大小）、ls -lt（按时间排）、ls -a（含隐藏）</td></tr>
<tr><td>cd</td><td>进目录</td><td>cd system、cd ..（上一级）、cd -（回上一个待的地方）、cd（回家）</td></tr>
<tr><td>mkdir</td><td>建目录</td><td>mkdir -p a/b/c（一次建多层）</td></tr>
<tr><td>tree</td><td>树状显示</td><td>tree -L 2（只看两层，看算例结构很方便）</td></tr>
</table></div>
<pre><code class="language-plaintext">ls -lt                    # 按修改时间排序，最新的在最上面——判断"哪个文件我刚改过"
ls 0.*/ -d                # 列出所有时间目录
tree -L 1 processor0      # 看并行分区目录里有什么</code></pre>
<h2>20.2 复制、移动、删除</h2>
<div class="table-scroll"><table>
<tr><th>命令</th><th>作用</th><th>例子</th></tr>
<tr><td>cp</td><td>复制</td><td>cp -r 0.orig 0（目录要加 -r）</td></tr>
<tr><td>mv</td><td>移动/改名</td><td>mv log.txt log.simpleFoam</td></tr>
<tr><td>rm</td><td>删除</td><td>rm -rf processor*（危险，看清楚再回车）</td></tr>
<tr><td>ln -s</td><td>软链接</td><td>ln -s ../commonMesh/constant/polyMesh constant/polyMesh</td></tr>
</table></div>
<p>删除算例文件前，应先核对当前目录、匹配文件列表与保留需求。对于重复计算，优先使用可审查的算例清理脚本，并把原始几何、初始条件和自定义源码保存在生成结果之外。</p>
<pre><code class="language-bash">ls processor*             # ★ 先看
rm -rf processor*         # 再删</code></pre>
<p>软链接的用处：同一套网格给多个算例用时，不用复制几个 GB，链过去即可。</p>
<h2>20.3 看文件</h2>
<div class="table-scroll"><table>
<tr><th>命令</th><th>作用</th><th>例子</th></tr>
<tr><td>cat</td><td>全部打印</td><td>cat system/controlDict</td></tr>
<tr><td>less</td><td>分页查看（大文件用它）</td><td>less log.simpleFoam（/ 搜索，q 退出，G 到末尾）</td></tr>
<tr><td>head / tail</td><td>看头 / 看尾</td><td>head -20 0/U、tail -50 log.simpleFoam</td></tr>
<tr><td>tail -f</td><td>实时跟踪（算例跑着时用）</td><td>tail -f log.interFoam</td></tr>
<tr><td>wc -l</td><td>数行数</td><td>wc -l constant/polyMesh/points</td></tr>
<tr><td>diff</td><td>比较两个文件</td><td>diff case1/system/fvSolution case2/system/fvSolution</td></tr>
</table></div>
<pre><code class="language-plaintext">tail -f log.simpleFoam | grep -E "^Time|Courant"    # 只看时间步和 Courant 数
diff -r case1/system case2/system                   # 比较两个算例的全部设置——排查"为什么他能跑我不能"</code></pre>
<p>diff -r 是排查”两个算例结果不一样”的第一把武器。</p>
<h2>20.4 找东西：grep 与 find</h2>
<p>grep：在文件内容里找</p>
<pre><code class="language-plaintext">grep -n "endTime" system/controlDict            # -n 显示行号
grep -i "error" log.simpleFoam                  # -i 忽略大小写
grep -r "kOmegaSST" &#36;FOAM_TUTORIALS             # -r 递归搜目录
grep -rl "interFoam" &#36;FOAM_TUTORIALS --include=controlDict   # -l 只列文件名
grep -A5 -B2 "FOAM FATAL" log.simpleFoam        # 前 2 行后 5 行一起看
grep -c "Time = " log.simpleFoam                # 数一共算了多少步
grep "^Time = " log.simpleFoam | tail -1        # 算到第几步了</code></pre>
<p>find：按文件名/属性找</p>
<pre><code class="language-plaintext">find . -name "*.stl"                       # 当前目录树里所有 stl
find &#36;FOAM_SRC -name "kOmegaSST*"          # 找源码
find . -name "log.*" -delete               # 删掉所有日志
find . -type d -name "processor*"          # 只找目录
find . -size +100M                         # 找出大文件（清硬盘时用）</code></pre>
<p>两者的分工：find 找文件名，grep 找文件内容。想”在所有 fvSolution 里搜某个词”就把两者组合：</p>
<pre><code class="language-plaintext">find . -name fvSolution -exec grep -l "GAMG" {} \;</code></pre>
<h2>20.5 编辑文件</h2>
<p>vim 的最小可用集（服务器上通常只有它）</p>
<div class="table-scroll"><table>
<tr><th>键</th><th>作用</th></tr>
<tr><td>i</td><td>进入插入模式（可以打字了）</td></tr>
<tr><td>Esc</td><td>回到命令模式</td></tr>
<tr><td>:w</td><td>保存</td></tr>
<tr><td>:q</td><td>退出；:q! 不保存强制退出；:wq 保存并退出</td></tr>
<tr><td>/词</td><td>搜索，n 下一个</td></tr>
<tr><td>dd</td><td>删除一行；5dd 删 5 行</td></tr>
<tr><td>u</td><td>撤销</td></tr>
<tr><td>gg / G</td><td>到文件头 / 尾</td></tr>
<tr><td>:set number</td><td>显示行号</td></tr>
</table></div>
<p>nano 更简单（底部有提示，Ctrl+O 保存、Ctrl+X 退出），新手可以先用它。</p>
<p>不打开编辑器就改文件：</p>
<pre><code class="language-bash">sed -i 's/endTime         0.5/endTime         5/' system/controlDict
foamDictionary system/controlDict -entry endTime -set 5      # ★ OpenFOAM 里首选这个，更安全</code></pre>
<h2>20.6 进程与后台运行</h2>
<div class="table-scroll"><table>
<tr><th>命令</th><th>作用</th></tr>
<tr><td>top / htop</td><td>看 CPU、内存占用</td></tr>
<tr><td>ps aux \| grep Foam</td><td>找出正在跑的 OpenFOAM 进程</td></tr>
<tr><td>kill &lt;PID&gt;</td><td>结束进程；kill -9 &lt;PID&gt; 强制</td></tr>
<tr><td>jobs / fg / bg</td><td>前后台切换</td></tr>
<tr><td>Ctrl+C</td><td>中断当前前台命令</td></tr>
<tr><td>Ctrl+Z</td><td>暂停并放到后台，再 bg 继续</td></tr>
<tr><td>nohup ... &amp;</td><td>退出终端后继续跑</td></tr>
<tr><td>screen / tmux</td><td>可断开、可重连的会话（远程算例的标准做法）</td></tr>
</table></div>
<pre><code class="language-plaintext"># 后台跑且断网不死
nohup simpleFoam &gt; log.simpleFoam 2&gt;&amp;1 &amp;

# tmux 用法（推荐）
tmux new -s case1        # 新建会话
  ... 在里面跑算例 ...
  Ctrl+B 然后按 D          # 断开（detach），算例继续跑
tmux ls                  # 看有哪些会话
tmux attach -t case1     # 重新连上</code></pre>
<p>tmux 会话在服务器端维持终端任务，可减少客户端断线对交互会话的影响。批量或共享集群计算仍应遵守作业调度方式，并独立记录日志、任务状态与退出码。</p>
<pre><code class="language-plaintext">ps aux | grep interFoam            # 找到 PID
kill 12345                         # 温和地停
pkill -f interFoam                 # 按名字停所有相关进程</code></pre>
<h2>20.7 输出重定向与管道</h2>
<div class="table-scroll"><table>
<tr><th>写法</th><th>含义</th></tr>
<tr><td>&gt; file</td><td>标准输出覆盖写入文件</td></tr>
<tr><td>&gt;&gt; file</td><td>追加写入</td></tr>
<tr><td>2&gt;&amp;1</td><td>把错误输出也并进去</td></tr>
<tr><td>\|</td><td>管道：把上一条的输出交给下一条</td></tr>
<tr><td>tee</td><td>同时输出到屏幕和文件</td></tr>
</table></div>
<pre><code class="language-bash">simpleFoam &gt; log.simpleFoam 2&gt;&amp;1 &amp;            # 最常用
simpleFoam 2&gt;&amp;1 | tee log.simpleFoam          # 想同时看屏幕
grep "^Time = " log.simpleFoam | wc -l        # 算了多少个时间步
ls -lh 0.*/U | awk '{print $5, $9}'           # 只看大小和文件名</code></pre>
<h2>20.8 磁盘与文件大小</h2>
<pre><code class="language-plaintext">df -h                       # 各分区剩余空间（算例跑满硬盘是常事）
du -sh *                    # 当前目录下每一项占多大
du -sh * | sort -h          # 排序，找出谁最大
du -sh 0.* | tail -5</code></pre>
<p>长计算前应估计结果输出量并检查磁盘空间。磁盘写满可能产生不完整时间目录；重启前应确认待读取文件完整。</p>
<h2>20.9 压缩与传输</h2>
<pre><code class="language-plaintext">tar -czf case.tar.gz myCase/            # 打包压缩
tar -xzf case.tar.gz                    # 解压
tar -czf case.tar.gz --exclude='processor*' --exclude='[0-9]*' myCase/   # 只打包设置文件

scp -r myCase user@server:~/run/        # 上传到服务器
scp user@server:~/run/case/log.* .      # 下载日志
rsync -avz --progress user@server:~/run/case/ ./case/    # ★ 断点续传、只传变化的部分
rsync -avz --exclude 'processor*' server:~/run/case/ ./case/</code></pre>
<p>rsync 可以按变化传输并支持指定排除规则，适用于重复同步大型结果。与 scp 比较时，应同时考虑连接方式、文件数量、权限以及断点恢复选项。</p>
<h2>20.10 环境变量与 .bashrc</h2>
<pre><code class="language-bash">echo &#36;PATH
export FOAM_SIGFPE=true            # 只对当前终端生效
source ~/.bashrc                   # 让改动立即生效（等价于 . ~/.bashrc）
which simpleFoam                   # 这条命令实际在哪
type run                           # 看某个名字是命令还是别名</code></pre>
<p>在 ~/.bashrc 末尾加自己的别名，是长期效率的来源：</p>
<pre><code class="language-plaintext">alias of2512='source &#36;HOME/OpenFOAM/OpenFOAM-v2512/etc/bashrc'
alias ll='ls -lh'
alias cl='foamListTimes -rm'
alias t='tail -f'</code></pre>
<h2>20.11 其他高频小命令</h2>
<pre><code class="language-bash">history | grep blockMesh      # 我上次那条长命令怎么敲的
!!                            # 重复上一条命令
sudo !!                       # 用 sudo 重跑上一条
watch -n 5 'ls 0.* -d | tail -3'   # 每 5 秒刷新一次，盯着输出目录
time simpleFoam               # 统计耗时
nproc                         # 这台机器有几个核（决定 mpirun -np 用多少）
free -h                       # 剩多少内存
ssh user@server               # 登服务器
man ls                        # 看手册（q 退出）</code></pre>
<p>Tab 补全可减少命令和路径的拼写错误。输入名称前缀后按 Tab，查看当前 shell 提供的候选项；补全结果也可用于检查路径是否存在。</p>
<h2>第五部分　排错与附录</h2>
{% endraw %}
