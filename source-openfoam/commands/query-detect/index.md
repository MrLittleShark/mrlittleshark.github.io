---
title: "query-detect · 调用依赖检测脚本，列出发现的软件位置"
layout: reference
description: "调用依赖检测脚本，列出发现的软件位置。"
cms_slug: "command-query-detect"
---

<p>调用依赖检测脚本，列出发现的软件位置。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 名称对应 wmake/scripts/have_&lt;名称&gt; 检测脚本，结果是实际探测到的依赖位置。</p>
<h2>示例 1：检查全部依赖</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/query-detect" -all
</code></pre>
<p>遍历安装中所有 have_* 脚本，各自运行 -test。</p>
<h2>示例 2：检查图划分依赖</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/query-detect" scotch
</code></pre>
<p>查看 Scotch 头文件、库或安装路径的检测信息。</p>
<h2>示例 3：检查两个可选依赖</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/query-detect" scotch metis
</code></pre>
<p>对并行分区相关依赖分别输出结果。</p>
<h2>示例 4：只使用安装级配置</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/query-detect" -mode=o scotch
</code></pre>
<p>通过 FOAM_CONFIG_MODE 限制配置来源，排查个人覆盖设置。</p>
<h2>示例 5：比较配置搜索范围</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/query-detect" -mode=ugo scotch &gt; detection-all.txt
"$WM_PROJECT_DIR/bin/tools/query-detect" -mode=o scotch &gt; detection-install.txt
diff -u detection-install.txt detection-all.txt
</code></pre>
<p>对比用户/站点覆盖是否改变依赖检测结果。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-all</code></td><td>运行全部检测。</td></tr><tr><td><code>-mode=MODE</code></td><td>将此选项传给 foamEtcFile。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/query-detect">源码与说明</a> · <a href="/assets/command-help/query-detect.txt">帮助文本</a></p>
