const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const {chromium} = require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const root = path.resolve(__dirname, '..');
const output = path.join(root, '.openfoam-work/refinements');
fs.mkdirSync(output, {recursive: true});
const assets = {
  'refinements.css': ['themes/foam-lab/source/assets/refinements.css', 'text/css'],
  'refinements.js': ['themes/foam-lab/source/assets/refinements.js', 'text/javascript'],
  'site-streamlines.svg': ['source-openfoam/assets/diagrams/site-streamlines.svg', 'image/svg+xml'],
};

(async () => {
  const browser = await chromium.launch({channel: 'msedge', headless: true});
  const results = [];
  for (const scenario of [
    {name: 'desktop-light', viewport: {width: 1440, height: 1000}, theme: 'light'},
    {name: 'desktop-dark', viewport: {width: 1440, height: 1000}, theme: 'dark'},
    {name: 'mobile-light', viewport: {width: 390, height: 844}, theme: 'light', isMobile: true, hasTouch: true},
    {name: 'mobile-dark', viewport: {width: 390, height: 844}, theme: 'dark', isMobile: true, hasTouch: true},
  ]) {
    const context = await browser.newContext({...scenario, reducedMotion: 'no-preference'});
    await context.addInitScript(theme => localStorage.setItem('foamlab.theme', theme), scenario.theme);
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.route('**/assets/**', async route => {
      const name = new URL(route.request().url()).pathname.split('/').pop();
      if (assets[name]) return route.fulfill({body: fs.readFileSync(path.join(root, assets[name][0])), contentType: assets[name][1]});
      return route.continue();
    });
    await page.goto('http://localhost:4173/', {waitUntil: 'networkidle'});
    const shapeBefore = await page.locator('.scientific-home').boundingBox();
    if (!(await page.locator('link[href*="refinements.css"]').count())) await page.addStyleTag({path: path.join(root, assets['refinements.css'][0])});
    await page.addScriptTag({path: path.join(root, assets['refinements.js'][0])});
    const shapeAfter = await page.locator('.scientific-home').boundingBox();
    assert.deepEqual(shapeAfter, shapeBefore, 'Decorative styles must not change the homepage geometry');
    const initial = await page.evaluate(() => ({
      overflow: document.documentElement.scrollWidth > innerWidth,
      theme: document.documentElement.dataset.theme,
      background: getComputedStyle(document.querySelector('.app-shell')).backgroundImage,
      panel: getComputedStyle(document.querySelector('.science-panel')).backgroundColor,
      selected: getComputedStyle(document.querySelector('.nav-item.active')).boxShadow,
    }));
    assert.equal(initial.overflow, false);
    assert.equal(initial.theme, scenario.theme);
    assert.match(initial.background, /linear-gradient/);
    assert.match(initial.selected, /inset/);
    await page.screenshot({path: path.join(output, `${scenario.name}.png`), fullPage: true});

    const heading = page.locator('.science-intro h1');
    await heading.click({position: {x: 40, y: 22}});
    assert.equal(await page.locator('.foam-ripple').count(), 1);
    assert.equal(await page.locator('.foam-ripple-layer').evaluate(node => getComputedStyle(node).pointerEvents), 'none');
    await page.waitForTimeout(110);
    await page.screenshot({path: path.join(output, `${scenario.name}-ripple.png`)});
    await page.waitForTimeout(700);
    assert.equal(await page.locator('.foam-ripple').count(), 0);

    await page.emulateMedia({reducedMotion: 'reduce'});
    await heading.click({position: {x: 40, y: 22}});
    assert.equal(await page.locator('.foam-ripple').count(), 0);
    await page.emulateMedia({reducedMotion: 'no-preference'});
    await page.keyboard.press('Tab');
    const focus = await page.evaluate(() => ({
      outline: getComputedStyle(document.activeElement).outlineStyle,
      width: getComputedStyle(document.activeElement).outlineWidth,
      tag: document.activeElement.tagName,
    }));
    assert.equal(focus.outline, 'solid');
    assert.equal(focus.width, '2px');

    if (scenario.isMobile) {
      await page.locator('.mobile-menu').click();
      assert.equal(await page.locator('body').evaluate(node => node.classList.contains('nav-open')), true);
      await page.locator('.nav-item[href="/commands/"]').click();
    } else {
      await page.locator('.nav-item[href="/commands/"]').click();
    }
    await page.waitForURL('**/commands/');
    await page.waitForSelector('.command-card');
    // Apply the same independent assets on this page if the parent has not included them yet.
    if (!(await page.locator('link[href*="refinements.css"]').count())) await page.addStyleTag({path: path.join(root, assets['refinements.css'][0])});
    await page.addScriptTag({path: path.join(root, assets['refinements.js'][0])});
    const filter = page.locator('[data-command-filter]').nth(1);
    await filter.click();
    assert.equal(await filter.getAttribute('aria-pressed'), 'true');
    assert.match(await filter.evaluate(node => getComputedStyle(node).boxShadow), /inset/);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
    await page.screenshot({path: path.join(output, `${scenario.name}-commands.png`)});
    results.push({name: scenario.name, initial, focus, errors, checks: ['unchanged-layout', 'no-horizontal-overflow', 'local-ripple', 'ripple-cleanup', 'reduced-motion', 'keyboard-focus', 'link-navigation', 'selected-filter']});
    assert.deepEqual(errors, []);
    await context.close();
  }
  await browser.close();
  fs.writeFileSync(path.join(output, 'verification.json'), JSON.stringify(results, null, 2));
  console.log(JSON.stringify({passed: results.length, screenshotFolder: output, results}, null, 2));
})().catch(error => {console.error(error); process.exit(1);});
