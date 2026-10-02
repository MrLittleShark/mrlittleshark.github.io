---
title: "foamPrintJobs · 与 foamCheckJobs 配合使用"
layout: reference
description: "与 foamCheckJobs 配合使用。"
cms_slug: "command-foamprintjobs"
---

<p>与 foamCheckJobs 配合使用。</p><h2>用法</h2><pre><code class="language-bash">foamPrintJobs jobState</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamPrintJobs [stateFile]

This program prints a table of all running and finished jobs.

It is normally used in conjunction with foamCheckJobs which outputs
a &quot;stateFile&quot; containing the actual process status of all jobs.

If stateFile is not supplied, the default is used:
    $DEFSTATEFILE</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamPrintJobs">源码与说明</a> · <a href="/assets/command-help/foamprintjobs.txt">帮助文本</a></p>
