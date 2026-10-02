---
title: "makeFiles · 扫描源码并生成 Make/files"
layout: reference
description: "扫描源码并生成 Make/files。"
cms_slug: "command-makefiles"
---

<p>扫描源码并生成 Make/files。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 下列每例建立一个新的独立目录；空源文件仅用于演示清单生成，编译前须填写有效源码。对应 Make/files 已存在时脚本会退出。 默认 files 目标是 FOAM_APPBIN，个人开发应改为 FOAM_USER_APPBIN。</p>
<h2>示例 1：平面源码目录</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-make-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p flat
    touch flat/main.C
    cd flat
    "$WM_PROJECT_DIR/wmake/scripts/makeFiles"
    cat Make/files
)
</code></pre>
<p>扫描 main.C 并生成 EXE 清单。 末行显示实际生成内容。</p>
<h2>示例 2：带模型子目录</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-make-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p nested nested/models
    touch nested/main.C nested/models/model.C
    cd nested
    "$WM_PROJECT_DIR/wmake/scripts/makeFiles"
    cat Make/files
)
</code></pre>
<p>源码分组位于 models，清单为子目录生成变量并引用源文件。 末行显示实际生成内容。</p>
<h2>示例 3：多文件工具</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-make-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p multi
    touch multi/main.C multi/readData.C multi/writeData.C
    cd multi
    "$WM_PROJECT_DIR/wmake/scripts/makeFiles"
    cat Make/files
)
</code></pre>
<p>三份实现进入同一编译清单，最终只应有一个 main 入口。 末行显示实际生成内容。</p>
<h2>示例 4：带头文件的目录</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-make-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p headers
    touch headers/main.C headers/model.H
    cd headers
    "$WM_PROJECT_DIR/wmake/scripts/makeFiles"
    cat Make/files
)
</code></pre>
<p>头文件不作为独立编译源加入 files，main.C 被收录。 末行显示实际生成内容。</p>
<h2>示例 5：准备个人目标路径</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-make-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p user-target
    touch user-target/main.C
    cd user-target
    "$WM_PROJECT_DIR/wmake/scripts/makeFiles"
    sed -i 's/FOAM_APPBIN/FOAM_USER_APPBIN/g' Make/files
    cat Make/files
)
</code></pre>
<p>生成后把 EXE 输出路径改为 FOAM_USER_APPBIN，适合个人开发。 末行显示实际生成内容。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: makeFiles
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeFiles

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Scan the current directory for source files and construct Make/files Usage : makeFiles</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeFiles">源码与说明</a> · <a href="/assets/command-help/makefiles.txt">帮助文本</a></p>
