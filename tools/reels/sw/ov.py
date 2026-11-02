from playwright.sync_api import sync_playwright
F="file:///tmp/claude-0/fonts/node_modules/@fontsource/"
CSS=f"""<style>@font-face{{font-family:Cap;src:url({F}caprasimo/files/caprasimo-latin-400-normal.woff2)}}
@font-face{{font-family:Fig;font-weight:700;src:url({F}figtree/files/figtree-latin-700-normal.woff2)}}
@font-face{{font-family:Fig;font-weight:800;src:url({F}figtree/files/figtree-latin-800-normal.woff2)}}
*{{margin:0;box-sizing:border-box}}html,body{{background:transparent}}body{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:Fig,'Noto Color Emoji'}}
.h{{position:absolute;left:40px;right:40px;top:210px;text-align:center;color:#fff;font:400 80px/1.1 Cap,'Noto Color Emoji'}}
.h b{{color:#FFC857;font-weight:400}}
.l{{position:absolute;top:470px;width:500px;text-align:center;font:800 40px Fig,'Noto Color Emoji';color:#FDEFF4}}
.p{{position:absolute;top:1460px;width:500px;text-align:center;font:400 64px Cap;color:#fff}}
.dim{{position:absolute;inset:0;background:rgba(26,21,56,.78)}}
.q{{position:absolute;left:70px;right:70px;top:640px;text-align:center;color:#fff;font:400 104px/1.08 Cap,'Noto Color Emoji'}}
.s{{position:absolute;left:70px;right:70px;top:1010px;text-align:center;color:#FFC857;font:800 50px Fig}}
.logo{{position:absolute;left:480px;top:1110px;width:120px;height:120px;border-radius:26px}}
</style>"""
P={"h1":'<div class="h">Same words.</div>',
"h2":'<div class="h">Same words.<br><b>Two ways to send them.</b></div>',
"lab":'<div class="l" style="left:27px">As a text 💬</div><div class="l" style="left:553px">As a Little Gasp 💌</div>',
"pay":'<div class="p" style="left:27px">Read once.</div><div class="p" style="left:553px;color:#FFC857">Replayed.</div>',
"end":'<div class="dim"></div><img class="logo" src="/tmp/claude-0/newreels/sw/logo.png"><div class="q">Which one would you replay? 💌</div><div class="s">Sealed with Love · Try it free · link in bio</div>'}
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
  for k,v in P.items():
    open("/tmp/claude-0/newreels/sw/t.html","w").write(CSS+v.replace('src="/tmp','src="file:///tmp'))
    pg.goto("file:///tmp/claude-0/newreels/sw/t.html"); pg.wait_for_timeout(300)
    pg.screenshot(path=f"/tmp/claude-0/newreels/sw/o_{k}.png",omit_background=True)
  b.close()
