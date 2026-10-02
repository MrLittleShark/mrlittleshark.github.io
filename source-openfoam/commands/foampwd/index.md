---
title: "foamPwd · 用 OpenFOAM 环境变量缩写显示当前路径"
layout: reference
description: "用 OpenFOAM 环境变量缩写显示当前路径。"
cms_slug: "command-foampwd"
---

<p>用 OpenFOAM 环境变量缩写显示当前路径。</p><h2>开始前</h2>
<p>先加载环境；路径替换依赖 WM_PROJECT_DIR、WM_PROJECT_USER_DIR、FOAM_RUN。</p>
<h2>示例 1：缩写源码路径</h2>
<pre><code class="language-bash">cd "$WM_PROJECT_DIR/src/finiteVolume"
foamPwd
</code></pre>
<p>输出以 $WM_PROJECT_DIR 开头的可读路径。</p>
<h2>示例 2：缩写个人算例路径</h2>
<pre><code class="language-bash">mkdir -p "$FOAM_RUN/caseA"
cd "$FOAM_RUN/caseA"
foamPwd
</code></pre>
<p>个人运行目录优先显示为 $FOAM_RUN。</p>
<h2>示例 3：缩写个人项目路径</h2>
<pre><code class="language-bash">mkdir -p "$WM_PROJECT_USER_DIR/notes"
cd "$WM_PROJECT_USER_DIR/notes"
foamPwd
</code></pre>
<p>在个人目录而非 run 下，显示 $WM_PROJECT_USER_DIR 前缀。</p>
<h2>示例 4：在笔记中记录当前位置</h2>
<pre><code class="language-bash">foamPwd &gt; case-location.txt
</code></pre>
<p>得到一行带变量名的展示路径。文件内容适合阅读记录，重新用作路径时需按 shell 规则展开变量。</p>
<h2>示例 5：比较显示路径和真实路径</h2>
<pre><code class="language-bash">pwd -P
foamPwd
</code></pre>
<p>前者解析符号链接为真实路径，后者按当前逻辑工作目录生成简写。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
