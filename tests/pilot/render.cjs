// Disposable local-only test harness. No website navigation or network requests.
const fs=require('fs');
const path=require('path');
const {chromium}=require('/app/node_modules/playwright-core');
(async()=>{
 const root=__dirname; const input=path.resolve(root,process.argv[2]||'index.html');
 if(path.dirname(input)!==root || !['index.html','preview.html'].includes(path.basename(input))) throw Error('Fixture only');
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const page=await browser.newPage();
 await page.route('**/*',r=>r.abort());
 const out=[];
 for(const width of [1280,390]){
  await page.setViewportSize({width,height:900});
  await page.setContent(fs.readFileSync(input,'utf8'));
  const info=await page.evaluate(()=>({title:document.title,h1:document.querySelector('h1')?.textContent,navVisible:[...document.querySelectorAll('nav')].some(e=>e.getBoundingClientRect().height>0),brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(e=>!document.getElementById(e.getAttribute('href').slice(1))).map(e=>({label:e.textContent,href:e.getAttribute('href')})),overflow:document.documentElement.scrollWidth>innerWidth}));
  await page.screenshot({path:path.join(root,path.basename(input,'.html')+'-'+width+'.png'),fullPage:true});
  const form=page.locator('form');
  if(await form.count()){
   for(const [name,value] of [['name','Synthetic Demo'],['email','test@example.invalid']]) { const el=page.locator('input[name="'+name+'"]');if(await el.count()) await el.fill(value); }
   const btn=form.locator('button'); if(await btn.count()&&await btn.first().isEnabled()) await btn.first().click();
   info.formStatus=await page.locator('[role="status"]').allTextContents();
  }
  out.push({width,...info});
 }
 await browser.close(); console.log(JSON.stringify(out,null,2));
})().catch(e=>{console.error(e);process.exit(1)});
