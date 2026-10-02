---
title: "makeOptions · 生成 Make/options 文件"
layout: reference
description: "生成 Make/options 文件。"
cms_slug: "command-makeoptions"
---

<p>生成 Make/options 文件。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 下列每例建立一个新的独立目录；空源文件仅用于演示清单生成，编译前须填写有效源码。对应 Make/options 已存在时脚本会退出。 默认 files 目标是 FOAM_APPBIN，个人开发应改为 FOAM_USER_APPBIN。</p>
<h2>示例 1：平面源码目录</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-make-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p flat
    touch flat/main.C
    cd flat
    "$WM_PROJECT_DIR/wmake/scripts/makeOptions"
    cat Make/options
)
</code></pre>
<p>生成 finiteVolume、meshTools 的默认 include 和链接项。 末行显示实际生成内容。</p>
<h2>示例 2：带模型子目录</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-make-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p nested nested/models
    touch nested/main.C nested/models/model.C
    cd nested
    "$WM_PROJECT_DIR/wmake/scripts/makeOptions"
    cat Make/options
)
</code></pre>
<p>源码分组位于 models，默认选项仍需补充项目自定义 include。 末行显示实际生成内容。</p>
<h2>示例 3：多文件工具</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-make-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p multi
    touch multi/main.C multi/readData.C multi/writeData.C
    cd multi
    "$WM_PROJECT_DIR/wmake/scripts/makeOptions"
    cat Make/options
)
</code></pre>
<p>三份实现共享该默认选项，所需额外库再补入 EXE_LIBS。 末行显示实际生成内容。</p>
<h2>示例 4：带头文件的目录</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-make-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p headers
    touch headers/main.C headers/model.H
    cd headers
    "$WM_PROJECT_DIR/wmake/scripts/makeOptions"
    cat Make/options
)
</code></pre>
<p>为已有头文件项目生成默认编译依赖设置。 末行显示实际生成内容。</p>
<h2>示例 5：准备个人目标路径</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-make-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p user-target
    touch user-target/main.C
    cd user-target
    "$WM_PROJECT_DIR/wmake/scripts/makeOptions"
    cat Make/options
)
</code></pre>
<p>生成的 EXE_LIBS 提供基础库，可在此后添加自编库。 末行显示实际生成内容。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeOptions">源码与说明</a> · <a href="/assets/command-help/makeoptions.txt">帮助文本</a></p>
