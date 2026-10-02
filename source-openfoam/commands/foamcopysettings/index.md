---
title: "foamCopySettings · 采用 rsync，按 foamCopySettings.rc 定义的规则复制，不包含网格和计算结"
layout: reference
description: "采用 rsync，按 foamCopySettings.rc 定义的规则复制，不包含网格和计算结果。"
cms_slug: "command-foamcopysettings"
---

<p>采用 rsync，按 foamCopySettings.rc 定义的规则复制，不包含网格和计算结果。</p><h2>用法</h2><pre><code class="language-bash">foamCopySettings ../baseCase ./</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCopySettings srcDir dstDir

    Copy OpenFOAM settings from one case to another, without copying
    the mesh or results.
    - requires rsync

Note
    The foamCopySettings.rc (found via foamEtcFile) can be used to add any
    custom rsync options.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCopySettings">源码与说明</a> · <a href="/assets/command-help/foamcopysettings.txt">帮助文本</a></p>
