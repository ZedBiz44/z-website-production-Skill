const fs=require('fs'),assert=require('assert'),path=require('path');
const {chromium}=require('/app/node_modules/playwright-core');
(async()=>{
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
const page=await browser.newPage();await page.route('**/*',r=>r.abort());
const result=[];
for(const width of [1280,390]){
 await page.setViewportSize({width,height:900});await page.setContent(fs.readFileSync(path.join(__dirname,'preview.html'),'utf8'));
 assert(await page.locator('nav').isVisible());
 for(const target of ['services','process','contact']){await page.locator('nav a[href="#'+target+'"]').click();assert(await page.locator('#'+target).isVisible());}
 await page.getByRole('link',{name:'Ask about garden care',exact:true}).click();
 assert.equal(await page.evaluate(()=>document.activeElement.name),'name');
 await page.waitForFunction(()=>{const r=document.querySelector('input[name="name"]').getBoundingClientRect();return r.y>=0&&r.bottom<=innerHeight});
 await page.locator('form button').click();assert.equal((await page.locator('[role="status"]').textContent()).trim(),'');
 await page.locator('input[name="name"]').fill('Synthetic Demo');await page.locator('input[name="email"]').fill('demo@example.invalid');await page.locator('form button').click();
 assert((await page.locator('[role="status"]').textContent()).includes('no message was sent'));
 assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
 const text=await page.locator('body').textContent();for(const keep of ['Prairie Bench','Seasonal cleanup, recurring garden care, and planting support.','Tell us about your garden. We discuss your needs and provide a written scope before work begins.','Canmore','Demo form: no messages are delivered.'])assert(text.includes(keep));
 result.push({width,navigation:'pass',heroFocus:'pass',invalidForm:'pass',validDemoForm:'pass',overflow:'none',protectedContent:'pass'});
}
await browser.close();console.log(JSON.stringify(result,null,2));
})().catch(e=>{console.error(e);process.exit(1)});
