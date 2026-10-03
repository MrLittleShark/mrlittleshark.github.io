---
title: "source · 在当前终端执行脚本，使脚本设置的环境变量和函数立即生效"
layout: reference
description: "在当前终端执行脚本，使脚本设置的环境变量和函数立即生效。"
cms_slug: "command-source"
---

<p>在当前终端执行脚本，使脚本设置的环境变量和函数立即生效。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：加载环境</h2>
<pre><code class="language-bash">source /usr/lib/openfoam/openfoam2512/etc/bashrc
command -v blockMesh
</code></pre>
<p>按实际安装位置修改路径。脚本在当前终端配置程序和库的搜索路径；末行给出 blockMesh 的位置。</p>
<h2>示例 2：加载运行函数</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
cd caseA
getApplication
</code></pre>
<p>source 后可在当前终端调用函数；getApplication 读取 controlDict 并输出求解器名。</p>
<h2>示例 3：阅读清理函数</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
declare -f cleanCase
</code></pre>
<p>加载后展开函数定义，查看清理范围；此例只阅读代码。</p>
<h2>示例 4：加载项目变量</h2>
<pre><code class="language-bash">printf 'CASE_ROOT="%s/cases"\n' "$PWD" &gt; project.env
source ./project.env
mkdir -p "$CASE_ROOT"
</code></pre>
<p>自己创建的变量文件在当前 shell 中生效，mkdir 随后建立对应目录。</p>
<h2>示例 5：限定环境作用范围</h2>
<pre><code class="language-bash">(source /usr/lib/openfoam/openfoam2512/etc/bashrc; blockMesh -case caseA)
</code></pre>
<p>圆括号建立子 shell；网格写入 caseA，外层终端环境保持原值。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/bash/manual/">源码与说明</a></p>
