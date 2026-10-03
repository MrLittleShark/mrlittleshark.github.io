---
title: "foamCopySettings · 将一个算例的配置文件复制到另一个算例"
layout: reference
description: "将一个算例的配置文件复制到另一个算例。"
cms_slug: "command-foamcopysettings"
---

<p>将一个算例的配置文件复制到另一个算例。</p><h2>开始前</h2>
<p>先加载 v2512 环境，在个人工作目录中准备 caseA 算例副本。新目标目录使用未占用的名称。 需要 rsync；源和目标目录都须存在。脚本排除 polyMesh、processor* 与常见数字时间目录；匹配规则不涵盖所有自定义后处理目录。</p>
<h2>示例 1：向空目录复制设置</h2>
<pre><code class="language-bash">mkdir -p new-settings
foamCopySettings caseA new-settings
</code></pre>
<p>复制初始场和配置，网格 polyMesh 不复制。</p>
<h2>示例 2：给已有网格配新设置</h2>
<pre><code class="language-bash">foamCopySettings caseA caseB
</code></pre>
<p>caseB 的网格保留，同名配置可能被源文件覆盖。</p>
<h2>示例 3：从教程取得配置</h2>
<pre><code class="language-bash">mkdir -p cavity-input
foamCopySettings "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-input
</code></pre>
<p>获得方腔输入模板，随后在目标运行 blockMesh 生成网格。</p>
<h2>示例 4：建立多套参数起点</h2>
<pre><code class="language-bash">mkdir -p settingA settingB
for target in settingA settingB; do foamCopySettings caseA "$target"; done
</code></pre>
<p>为两组参数建立共同输入基础，原始源目录保持不变。</p>
<h2>示例 5：复制后比较系统设置</h2>
<pre><code class="language-bash">foamCopySettings caseA caseB
diff -ru caseA/system caseB/system
</code></pre>
<p>比较结果可定位保留或覆盖的差异；rsync 未使用 --delete，目标独有文件仍可能存在。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCopySettings">源码与说明</a> · <a href="/assets/command-help/foamcopysettings.txt">帮助文本</a></p>
