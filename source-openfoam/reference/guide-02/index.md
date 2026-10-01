---
title: "第 2 章　安装与环境激活"
layout: reference
description: "OpenCFD v2512 安装与环境激活；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>2.1 三条安装路线怎么选</h2>
<div class="table-scroll"><table>
<tr><th>路线</th><th>适合谁</th><th>代价</th></tr>
<tr><td>deb 二进制包</td><td>只想用、不改源码</td><td>5 分钟装完，但装在 /usr/lib/openfoam 下，改源码需要 root</td></tr>
<tr><td>源码编译</td><td>要读源码、写自己的求解器（推荐给做科研的）</td><td>首次编译 1–3 小时</td></tr>
<tr><td>Docker / WSL2</td><td>主力系统是 Windows 或 macOS</td><td>多一层容器，图形界面（ParaView）配置略麻烦</td></tr>
</table></div>
<h2>2.2 路线一：deb 包安装（Ubuntu）</h2>
<pre><code class="language-bash"># ① 添加官方软件源（只需一次）
curl -s https://dl.openfoam.com/add-debian-repo.sh | sudo bash

# ② 安装 v2512
sudo apt update
sudo apt install openfoam2512-default

# ③ 激活环境
source /usr/lib/openfoam/openfoam2512/etc/bashrc
printf '%s\n' "&#36;WM_PROJECT_VERSION"  # 版本变量不依赖交互式别名</code></pre>
<p>激活 etc/bashrc 会设置可执行程序、共享库和教程等路径。环境未激活时，终端可能找不到 blockMesh，或者错误调用其他版本的程序。激活后应同时检查 WM_PROJECT_VERSION、WM_PROJECT_DIR 和 command -v blockMesh。</p>
<h2>2.3 路线二：源码编译（Ubuntu 26.04，装到家目录）</h2>
<p>装到 ~/OpenFOAM 而不是 /usr/lib 的理由：改源码、加自己的求解器都不需要 sudo，多版本共存也干净。</p>
<pre><code class="language-bash"># ① 装编译依赖
sudo apt update
sudo apt install -y build-essential autoconf autotools-dev cmake gawk gnuplot \
  flex libfl-dev libreadline-dev zlib1g-dev openmpi-bin libopenmpi-dev \
  mpi-default-bin mpi-default-dev libgmp-dev libmpfr-dev libmpc-dev

# ② 建目录并下载源码（OpenFOAM 本体 + ThirdParty 第三方库）
mkdir -p ~/OpenFOAM &amp;&amp; cd ~/OpenFOAM
wget https://dl.openfoam.com/source/v2512/OpenFOAM-v2512.tgz
wget https://dl.openfoam.com/source/v2512/ThirdParty-v2512.tgz
tar -xzf OpenFOAM-v2512.tgz
tar -xzf ThirdParty-v2512.tgz

# ③ 激活环境（编译前必须先 source，编译脚本靠环境变量找路径）
source ~/OpenFOAM/OpenFOAM-v2512/etc/bashrc

# ④ 编译前体检：检查 gcc、mpi、flex 等是否齐全
foamSystemCheck

# ⑤ 编译（-j 用满所有核心；-s 静默；-l 写日志，出错时好排查）
cd &#36;WM_PROJECT_DIR
./Allwmake -j -s -l

# ⑥ 编译后自检
foamInstallationTest</code></pre>
<p>关于 ThirdParty：里面是 scotch（并行分区）、CGAL、FFTW 等第三方库。ESI 版在 Ubuntu 上大多能直接用系统自带的这些库，所以 ThirdParty 常常只需要解压、不需要单独编译。若 foamSystemCheck 提示某个库缺失，再进 ThirdParty 目录跑 ./Allwmake。</p>
<p>编译要多久：8 核虚拟机大约 1–2 小时。中途断了不要紧，./Allwmake 可以重复执行，已编译好的不会重来。</p>
<h2>2.4 让 source 变得省事（同时支持多版本共存）</h2>
<p>不要把 source .../etc/bashrc 直接写进 ~/.bashrc。原因：以后你多半会同时装 v2512 和别的版本，两个环境的变量会互相污染，出现”命令找得到但库版本对不上”这类极难排查的问题。</p>
<p>可在 ~/.bashrc 中为不同安装定义别名，并在使用时显式激活所需版本。别名中的路径必须与实际安装位置一致：</p>
<pre><code class="language-bash"># ~/.bashrc 末尾
alias of2512='source &#36;HOME/OpenFOAM/OpenFOAM-v2512/etc/bashrc'
alias of2506='source &#36;HOME/OpenFOAM/OpenFOAM-v2506/etc/bashrc'
source ~/.bashrc     # 让别名立即生效
of2512               # 从此每开一个终端，敲一次这个
printf '%s\n' "&#36;WM_PROJECT_VERSION"  # 版本变量不依赖交互式别名</code></pre>
<h2>2.5 路线三：Docker / WSL2（Windows 用户）</h2>
<pre><code class="language-plaintext"># WSL2：先在 PowerShell 里装 Ubuntu，之后一切按 2.2 / 2.3 操作
wsl --install -d Ubuntu

# Docker：官方镜像
docker run -it --rm -v &#36;HOME/OpenFOAM:/data opencfd/openfoam-default:2512</code></pre>
<p>WSL2 里跑 ParaView 有两种方式：装 Windows 版 ParaView，然后在 Windows 里打开 WSL 路径（\\wsl$\Ubuntu\home\你的用户名\...）；或在 WSL 里装 Linux 版 ParaView（Windows 11 的 WSLg 已内置图形支持）。推荐前者，更流畅。</p>
<h2>2.6 ParaView 怎么装</h2>
<p>deb 包 openfoam2512-default 会带一个 ParaView。如果想用新版（例如 6.x），去 paraview.org 下官方二进制包解压到家目录，然后把它的 bin 加进 PATH：</p>
<pre><code class="language-bash">echo 'export PATH=&#36;HOME/ParaView-6.1.1/bin:&#36;PATH' &gt;&gt; ~/.bashrc</code></pre>
<p>v2512 的 paraFoam 最终调用 PATH 中的 paraview。-vtk（与 -builtin 等价）使用 ParaView 内置 OpenFOAM 读取器；-block 需要匹配的 blockReader 插件。可以用 command -v paraview 核对实际程序，使用 .foam 标记文件并不能保证所有版本都支持全部场与网格功能。</p><h2>环境函数与安装程序的区别</h2><p><code>foamVersion</code>、<code>tut</code>、<code>run</code> 等可由环境脚本定义为函数或别名，并非所有打包环境和非交互式 shell 都加载它们。<code>type foamVersion</code> 用于诊断当前 shell；查询版本可直接输出 <code>WM_PROJECT_VERSION</code>，查找实际程序用 <code>command -v blockMesh</code>。</p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">v2512 的函数与别名定义</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamExec">foamExec 的位置和环境激活实现</a></p>
{% endraw %}
