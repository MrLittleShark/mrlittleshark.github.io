---
title: "第 2 章　安装与环境激活"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><h4>2.1 三条安装路线怎么选</h4>
<div class="table-scroll"><table>
<tr><th>路线</th><th>适合谁</th><th>代价</th></tr>
<tr><td>deb 二进制包</td><td>只想用、不改源码</td><td>5 分钟装完，但装在 /usr/lib/openfoam 下，改源码需要 root</td></tr>
<tr><td>源码编译</td><td>要读源码、写自己的求解器（推荐给做科研的）</td><td>首次编译 1–3 小时</td></tr>
<tr><td>Docker / WSL2</td><td>主力系统是 Windows 或 macOS</td><td>多一层容器，图形界面（ParaView）配置略麻烦</td></tr>
</table></div>
<h4>2.2 路线一：deb 包安装（Ubuntu）</h4>
<pre><code># ① 添加官方软件源（只需一次）
curl -s https://dl.openfoam.com/add-debian-repo.sh | sudo bash

# ② 安装 v2512
sudo apt update
sudo apt install openfoam2512-default

# ③ 激活环境
source /usr/lib/openfoam/openfoam2512/etc/bashrc
foamVersion</code></pre>
<p>为什么第 ③ 步不能省：OpenFOAM 不是一个程序，而是几百个可执行文件 + 几十个库 + 一大堆环境变量。etc/bashrc 这个脚本做的事就是把它们的路径塞进 PATH、LD_LIBRARY_PATH 和一系列 $FOAM_* 变量里。没 source 过，终端根本不知道 blockMesh 在哪儿。</p>
<h4>2.3 路线二：源码编译（Ubuntu 26.04，装到家目录）</h4>
<p>装到 ~/OpenFOAM 而不是 /usr/lib 的理由：改源码、加自己的求解器都不需要 sudo，多版本共存也干净。</p>
<pre><code># ① 装编译依赖
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
cd $WM_PROJECT_DIR
./Allwmake -j -s -l

# ⑥ 编译后自检
foamInstallationTest</code></pre>
<p>关于 ThirdParty：里面是 scotch（并行分区）、CGAL、FFTW 等第三方库。ESI 版在 Ubuntu 上大多能直接用系统自带的这些库，所以 ThirdParty 常常只需要解压、不需要单独编译。若 foamSystemCheck 提示某个库缺失，再进 ThirdParty 目录跑 ./Allwmake。</p>
<p>编译要多久：8 核虚拟机大约 1–2 小时。中途断了不要紧，./Allwmake 可以重复执行，已编译好的不会重来。</p>
<h4>2.4 让 source 变得省事（同时支持多版本共存）</h4>
<p>不要把 source .../etc/bashrc 直接写进 ~/.bashrc。原因：以后你多半会同时装 v2512 和别的版本，两个环境的变量会互相污染，出现”命令找得到但库版本对不上”这类极难排查的问题。</p>
<p>正确做法是在 ~/.bashrc 末尾加别名，用哪个版本就敲哪个别名：</p>
<pre><code># ~/.bashrc 末尾
alias of2512=&#x27;source $HOME/OpenFOAM/OpenFOAM-v2512/etc/bashrc&#x27;
alias of2506=&#x27;source $HOME/OpenFOAM/OpenFOAM-v2506/etc/bashrc&#x27;
$ source ~/.bashrc     # 让别名立即生效
$ of2512               # 从此每开一个终端，敲一次这个
$ foamVersion</code></pre>
<h4>2.5 路线三：Docker / WSL2（Windows 用户）</h4>
<pre><code># WSL2：先在 PowerShell 里装 Ubuntu，之后一切按 2.2 / 2.3 操作
wsl --install -d Ubuntu

# Docker：官方镜像
docker run -it --rm -v $HOME/OpenFOAM:/data opencfd/openfoam-default:2512</code></pre>
<p>WSL2 里跑 ParaView 有两种方式：装 Windows 版 ParaView，然后在 Windows 里打开 WSL 路径（\\wsl$\Ubuntu\home\你的用户名\...）；或在 WSL 里装 Linux 版 ParaView（Windows 11 的 WSLg 已内置图形支持）。推荐前者，更流畅。</p>
<h4>2.6 ParaView 怎么装</h4>
<p>deb 包 openfoam2512-default 会带一个 ParaView。如果想用新版（例如 6.x），去 paraview.org 下官方二进制包解压到家目录，然后把它的 bin 加进 PATH：</p>
<pre><code>echo &#x27;export PATH=$HOME/ParaView-6.1.1/bin:$PATH&#x27; &gt;&gt; ~/.bashrc</code></pre>
<p>注意顺序问题：如果你既装了 OpenFOAM 自带的 ParaView 又装了官方包，paraFoam 命令会去调用 $ParaView_DIR 指向的那个。想强制用自己装的，直接用 paraview 打开算例里的 .foam 文件即可（见第 8 章）。</p>
{% endraw %}