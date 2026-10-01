from pathlib import Path
r=Path(__file__).resolve().parents[1]
p=r/'themes/foam-lab/source/assets/account.js'
s=p.read_text(encoding='utf-8').replace("if(!state.user)throw Error('请先登录。');", "if(!state.user)throw Error('请先登录。');if(state.dataError)throw Error('账号记录暂时不可用，请刷新后重试。');")
s=s.replace("if(!state.user)return;const form=", "if(!state.user||state.dataError)return;const form=").replace("if(!state.user)return;let local", "if(!state.user||state.dataError)return;let local")
p.write_text(s,encoding='utf-8')
p=r/'themes/foam-lab/source/assets/site.js';s=p.read_text(encoding='utf-8')
s=s.replace("'已完成 '+n+' 讲。学习记录保存在当前浏览器。'", "'已完成 '+n+' 讲。'+(window.foamAuth?.user?'学习记录保存在当前账号。':'学习记录保存在当前浏览器。')")
s=s.replace("const id=Number(complete.dataset.id),done=!completed.includes(id);complete.disabled=true;try{await window.foamAuth?.ready;", "const id=Number(complete.dataset.id);complete.disabled=true;try{await window.foamAuth?.ready;if(window.foamAuth?.user)completed=window.foamAuth.progress;const done=!completed.includes(id);")
p.write_text(s,encoding='utf-8')
p=r/'README.md';s=p.read_text(encoding='utf-8').replace('202 条命令','242 条命令')
s=s.replace('学习进度是当前浏览器的本机记录，不是跨设备账号成绩。','访客进度保存在当前浏览器；启用认证服务后，登录账号的进度保存在数据库并支持跨设备同步。学习进度不是作业成绩。')
s=s.replace('## 内容维护','## 个人中心与认证\n\n个人中心使用 Supabase Auth 的 GitHub OAuth，资料与学习进度存储于启用行级访问控制的数据库。认证尚未配置时，页面明确显示服务未启用，不提供模拟登录。配置步骤见 [认证服务配置](supabase/SETUP.md)，数据库结构与策略见 `supabase/schema.sql`。\n\n## 内容维护')
s=s.replace('| `source-openfoam/downloads`', '| `source-openfoam/assets/dictionaries.json` | 53 项配置文件、关键字和关联命令 |\n| `source-openfoam/dictionaries` | 配置文件独立说明页 |\n| `source-openfoam/account` | 个人中心入口 |\n| `source-openfoam/downloads`')
p.write_text(s,encoding='utf-8')
