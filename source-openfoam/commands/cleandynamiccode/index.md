---
title: "cleanDynamicCode · 清理动态编译生成的 dynamicCode 目录"
layout: reference
description: "清理动态编译生成的 dynamicCode 目录。"
cms_slug: "command-cleandynamiccode"
---

<p>清理动态编译生成的 dynamicCode 目录。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。下列空文件用于观察范围；每例先创建独立临时目录，然后只在该目录操作。</p>
<h2>示例 1：移除动态编译缓存</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'dynamicCode'
    touch 'system/controlDict' 'dynamicCode/cache'
    cleanDynamicCode
    find . -type f
)
</code></pre>
<p>存在 system 时移除 dynamicCode；下次 coded 功能执行会按需重新编译。 末行列出剩余文件。</p>
<h2>示例 2：清理多个生成类</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'dynamicCode/classA' 'dynamicCode/classB'
    touch 'dynamicCode/classA/a.C' 'dynamicCode/classB/b.C'
    cleanDynamicCode
    find . -type f
)
</code></pre>
<p>两个动态类缓存均清除。 末行列出剩余文件。</p>
<h2>示例 3：保留物理配置</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'dynamicCode' 'constant'
    touch 'dynamicCode/cache' 'constant/transportProperties'
    cleanDynamicCode
    find . -type f
)
</code></pre>
<p>只处理动态代码目录，物性配置保留。 末行列出剩余文件。</p>
<h2>示例 4：检查算例识别条件</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'dynamicCode'
    touch 'dynamicCode/cache'
    cleanDynamicCode
    find . -type f
)
</code></pre>
<p>缺少 system 时不会移除目录。 末行列出剩余文件。</p>
<h2>示例 5：仅刷新一个算例</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'caseA/system' 'caseA/dynamicCode' 'caseB/dynamicCode'
    touch 'caseA/dynamicCode/a' 'caseB/dynamicCode/b'
    cd caseA
    cleanDynamicCode
    find . -type f
)
</code></pre>
<p>通过工作目录限定缓存所属算例。 末行列出剩余文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
