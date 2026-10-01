from pathlib import Path
p=Path(__file__).resolve().parents[1]/'themes/foam-lab/source/assets/account.js'
s=p.read_text(encoding='utf-8')
s=s.replace('configured:false,dataError:false','configured:false,githubEnabled:false,dataError:false')
s=s.replace("$('#sign-in').disabled=!state.configured", "$('#sign-in').disabled=!state.githubEnabled")
s=s.replace("state.configured?'使用 GitHub 授权登录；本站不读取或保存 GitHub 密码。':'登录服务尚未启用。课程、资料与公开课堂仍可访问。'", "state.githubEnabled?'使用 GitHub 授权登录；本站不读取或保存 GitHub 密码。':state.configured?'GitHub 登录正在配置中。课程、资料与公开课堂仍可访问。':'登录服务尚未启用。课程、资料与公开课堂仍可访问。'")
s=s.replace('state.configured=true;await loadUser();', "state.configured=true;const settingsResponse=await fetch(cfg.supabaseUrl+'/auth/v1/settings',{headers:{apikey:cfg.publishableKey},signal:AbortSignal.timeout(10000)});if(!settingsResponse.ok)throw Error('无法检查登录服务，请稍后刷新。');const settings=await settingsResponse.json();state.githubEnabled=settings.external?.github===true;await loadUser();")
s=s.replace("if(!state.client)return;$('#sign-in')", "if(!state.client||!state.githubEnabled)return;$('#sign-in')")
p.write_text(s,encoding='utf-8')
