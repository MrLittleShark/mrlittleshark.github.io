const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');

(async()=>{
  const origin='https://foamlabshark.github.io';
  const browser=await chromium.launch({channel:'msedge',headless:true});
  const checks=[];
  try {
    for(const entry of [
      {route:'/account/',button:'#sign-in',name:'account'},
      {route:'/admin/',button:'[data-lab-login]',name:'admin'}
    ]) {
      const context=await browser.newContext({viewport:{width:1440,height:1000}});
      try {
        const page=await context.newPage();
        const errors=[];
        let authorize;
        page.on('pageerror',e=>errors.push(e.message));
        page.on('request',r=>{
          const u=new URL(r.url());
          if(u.hostname.endsWith('.supabase.co')&&u.pathname==='/auth/v1/authorize') {
            // Do not log OAuth state, the PKCE challenge, or the full URL.
            authorize={provider:u.searchParams.get('provider'),redirectTo:u.searchParams.get('redirect_to'),pkce:u.searchParams.get('code_challenge_method')};
          }
        });
        const response=await page.goto(origin+entry.route,{waitUntil:'networkidle'});
        assert.equal(response.status(),200);
        await page.evaluate(()=>window.foamAuth.ready);
        assert.equal(await page.evaluate(()=>window.foamAuth.githubEnabled),true);
        const button=page.locator(entry.button).first();
        await button.waitFor({state:'visible'});
        assert(await button.isEnabled());
        await page.screenshot({path:path.join(__dirname,'../.openfoam-work/live-'+entry.name+'.png'),fullPage:true});
        await button.click();
        await page.waitForURL('https://github.com/**',{timeout:30000});
        await page.waitForLoadState('domcontentloaded');
        const check={route:entry.route,httpStatus:response.status(),providerEnabled:true,authorize,githubHost:new URL(page.url()).hostname,githubPageTitle:await page.title(),githubLoginVisible:await page.locator('input[name=login]').count()>0};
        assert.equal(authorize.provider,'github');
        assert.equal(authorize.redirectTo,origin+'/account/');
        assert.equal(authorize.pkce,'s256');
        assert.equal(check.githubLoginVisible,true);
        if(entry.name==='admin') {
          // Return anonymously in the same tab to inspect its saved destination.
          // This does not simulate or perform a successful user authorization.
          await page.goto(origin+'/account/',{waitUntil:'networkidle'});
          check.savedDestination=await page.evaluate(()=>sessionStorage.getItem('foamlab.afterLogin'));
          assert.equal(check.savedDestination,'/admin/');
        }
        check.browserErrors=errors;
        assert.deepEqual(errors,[]);
        checks.push(check);
      } finally { await context.close(); }
    }
    const report={checkedAt:new Date().toISOString(),checks,scope:'Both login launches, GitHub login pages, and saved admin destination verified; personal GitHub authorization not automated'};
    fs.writeFileSync(path.join(__dirname,'../.openfoam-work/live-auth-check.json'),JSON.stringify(report,null,2));
    console.log(JSON.stringify(report,null,2));
  } finally { await browser.close(); }
})().catch(e=>{console.error(e.message);process.exitCode=1;});
