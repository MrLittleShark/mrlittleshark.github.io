---
title: "removeCase · 删除参数指定的整个算例目录"
layout: reference
description: "删除参数指定的整个算例目录。"
cms_slug: "command-removecase"
---

<p>删除参数指定的整个算例目录。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。函数递归移除第一个路径参数，下例只处理刚创建的独立临时目录。</p>
<h2>示例 1：移除一个空测试算例</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-remove.XXXXXX")
removeCase "$demoDir"
</code></pre>
<p>路径来自 mktemp，删除后该目录不再存在。</p>
<h2>示例 2：移除完整测试树</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-remove.XXXXXX")
mkdir -p "$demoDir"/{0,constant,system}
removeCase "$demoDir"
</code></pre>
<p>连同三个新建子目录一起移除。</p>
<h2>示例 3：只删除父目录中的一个方案</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-remove.XXXXXX")
mkdir -p "$demoDir"/{caseA,caseB}
removeCase "$demoDir/caseA"
ls "$demoDir"
</code></pre>
<p>剩余 caseB，明确路径限定删除范围。</p>
<h2>示例 4：处理包含空格的名称</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-remove.XXXXXX")
mkdir "$demoDir/test case"
removeCase "$demoDir/test case"
</code></pre>
<p>引号使含空格路径完整传递。</p>
<h2>示例 5：清除多个独立试验</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-remove.XXXXXX")
mkdir -p "$demoDir"/{trial1,trial2}
for name in trial1 trial2; do removeCase "$demoDir/$name"; done
</code></pre>
<p>函数每次只使用第一个位置参数，因此用循环分别移除两项。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
