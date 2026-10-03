---
title: "foamTestTutorial · 将指定教程复制到测试目录并运行，检查算例能否正常执行"
layout: reference
description: "将指定教程复制到测试目录并运行，检查算例能否正常执行。"
cms_slug: "command-foamtesttutorial"
---

<p>将指定教程复制到测试目录并运行，检查算例能否正常执行。</p><h2>开始前</h2>
<p>加载 v2512 环境。输入使用相对于 $FOAM_TUTORIALS 的教程路径，例如 incompressible/icoFoam/cavity/cavity。指定 -output 时须先建立该目录。工具将教程复制到独立目录后测试。</p>
<h2>示例 1：运行一步检查</h2>
<pre><code class="language-bash">foamTestTutorial incompressible/icoFoam/cavity/cavity
</code></pre>
<p>默认修改测试副本，仅运行一个时间步；结束后清理临时副本。</p>
<h2>示例 2：保留测试副本</h2>
<pre><code class="language-bash">mkdir -p tests-one-step
foamTestTutorial -output=tests-one-step incompressible/icoFoam/cavity/cavity
</code></pre>
<p>输出目录内按教程路径生成子目录，日志与结果保留。</p>
<h2>示例 3：完成整个算例</h2>
<pre><code class="language-bash">mkdir -p tests-full
foamTestTutorial -full -output=tests-full incompressible/icoFoam/cavity/cavity
</code></pre>
<p>-full 保留原 controlDict 的运行区间。</p>
<h2>示例 4：测试两个不同几何</h2>
<pre><code class="language-bash">mkdir -p tests-batch
foamTestTutorial -output=tests-batch incompressible/icoFoam/cavity/cavity incompressible/icoFoam/elbow
</code></pre>
<p>按列表分别测试方腔与弯管；elbow 的 Allrun 会从官方资源目录读取网格输入。</p>
<h2>示例 5：优先串行脚本</h2>
<pre><code class="language-bash">mkdir -p tests-serial
foamTestTutorial -serial -full -output=tests-serial incompressible/icoFoam/cavity/cavity
</code></pre>
<p>优先使用 Allrun-serial；不存在时回退到教程默认流程。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-1</code></td><td>修改 controlDict，使算例仅运行一个时间步；此项为默认行为。</td></tr><tr><td><code>-full</code></td><td>运行到计算结束，保持 controlDict 原有设置。</td></tr><tr><td><code>-force</code></td><td>覆盖已有输出目录。</td></tr><tr><td><code>-debian</code></td><td>采用适合 autopkgtest 的运行设置。</td></tr><tr><td><code>-serial</code></td><td>优先执行 Allrun-serial 脚本。</td></tr><tr><td><code>-parallel</code></td><td>优先执行 Allrun-parallel 脚本。</td></tr><tr><td><code>-output=DIR</code></td><td>指定输出目录，默认使用临时目录。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamTestTutorial">源码与说明</a> · <a href="/assets/command-help/foamtesttutorial.txt">帮助文本</a></p>
