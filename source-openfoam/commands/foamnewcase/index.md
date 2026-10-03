---
title: "foamNewCase · 根据指定求解器的模板创建新算例"
layout: reference
description: "根据指定求解器的模板创建新算例。"
cms_slug: "command-foamnewcase"
---

<p>根据指定求解器的模板创建新算例。</p><h2>开始前</h2>
<p>需要 rsync 和用户/站点应用模板。先执行 mkdir -p "$HOME/.OpenFOAM/appTemplates/2512"，再将完整初始算例复制为该目录下的 cavityStarter，保证其含 constant 和 system。</p>
<h2>示例 1：查看可用模板</h2>
<pre><code class="language-bash">foamNewCase -list
</code></pre>
<p>列出用户和站点 appTemplates 中具有算例结构的模板名。</p>
<h2>示例 2：创建指定算例</h2>
<pre><code class="language-bash">foamNewCase -app cavityStarter -case case-new
</code></pre>
<p>目标不存在时自动建立，rsync 同步模板并建立 postPro 目录。</p>
<h2>示例 3：在空目录生成</h2>
<pre><code class="language-bash">mkdir -p case-local
cd case-local
foamNewCase -app cavityStarter
</code></pre>
<p>省略 -case 时使用当前目录。</p>
<h2>示例 4：显式指定 API</h2>
<pre><code class="language-bash">foamNewCase -with-api=2512 -app cavityStarter -case case-api2512
</code></pre>
<p>优先匹配 2512 目录内的同名模板，再查通用模板。</p>
<h2>示例 5：建立三组试验</h2>
<pre><code class="language-bash">for tag in coarse medium fine; do foamNewCase -app cavityStarter -case "grid-$tag"; done
</code></pre>
<p>从同一模板建立不同网格试验，后续分别调整 blockMeshDict。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-app NAME</code></td><td>指定使用的应用程序。</td></tr><tr><td><code>-case DIR</code></td><td>指定算例目录；默认使用当前目录。</td></tr><tr><td><code>-list</code></td><td>列出可用的应用程序。</td></tr><tr><td><code>-with-api=NUM</code></td><td>指定 API 版本值，默认使用 $FOAM_API。</td></tr><tr><td><code>-version VER</code></td><td>已废弃的兼容选项。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewCase">源码与说明</a> · <a href="/assets/command-help/foamnewcase.txt">帮助文本</a></p>
