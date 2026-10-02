---
title: "createCode · 该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码"
layout: reference
description: "该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码。"
cms_slug: "command-createcode"
---

<p>该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 需要 Ragel。先 cp -a "$WM_PROJECT_DIR/wmake/src" scanner-demo；脚本会进入自身目录，固定为 wmkdepend.rl 生成扫描器。以下只处理 scanner-demo 副本。</p>
<h2>示例 1：生成依赖分析扫描器</h2>
<pre><code class="language-bash">bash scanner-demo/createCode
</code></pre>
<p>调用 makeParser -scanner=wmkdepend.rl，输出 scanner-demo/wmkdepend.cc。</p>
<h2>示例 2：省略源码行号映射</h2>
<pre><code class="language-bash">bash scanner-demo/createCode -no-lines
</code></pre>
<p>向 Ragel 传递不生成 #line 的选项，便于比较纯生成代码。</p>
<h2>示例 3：修改规则后再生成</h2>
<pre><code class="language-bash">${EDITOR:-vi} scanner-demo/wmkdepend.rl
bash scanner-demo/createCode
</code></pre>
<p>规则修改完成后刷新生成源码，供后续工具编译。</p>
<h2>示例 4：比较生成文件变化</h2>
<pre><code class="language-bash">cp scanner-demo/wmkdepend.cc scanner.before.cc
bash scanner-demo/createCode -no-lines
diff -u scanner.before.cc scanner-demo/wmkdepend.cc
</code></pre>
<p>把前后两份生成代码比较，定位行号或规则变化。</p>
<h2>示例 5：生成后构建工具</h2>
<pre><code class="language-bash">bash scanner-demo/createCode
WMAKE_BIN="$PWD/scanner-tools-bin" bash scanner-demo/Allmake
</code></pre>
<p>刷新扫描器后构建 wmake 工具，输出位于独立个人目录。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/src/createCode">源码与说明</a> · <a href="/assets/command-help/createcode.txt">帮助文本</a></p>
