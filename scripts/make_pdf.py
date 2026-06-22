from playwright.sync_api import sync_playwright
from PIL import Image
import io, os
EXE="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
HTML="file:///home/user/example-of-report/slides/督导系统建设成果汇报.html"
imgs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=EXE,args=["--no-sandbox","--disable-gpu","--force-color-profile=srgb"])
    pg=b.new_page(viewport={"width":1280,"height":720},device_scale_factor=2)
    pg.goto(HTML); pg.wait_for_timeout(700)
    # hide on-screen controls for clean export
    pg.add_style_tag(content=".nav,.counter,.hint{display:none!important}")
    n=pg.evaluate("N")
    for i in range(n):
        pg.evaluate(f"show({i})"); pg.wait_for_timeout(260)
        png=pg.screenshot(); im=Image.open(io.BytesIO(png)).convert("RGB")
        im=im.resize((1920,1080))
        imgs.append(im)
    b.close()
out="/home/user/example-of-report/slides/督导系统建设成果汇报.pdf"
imgs[0].save(out,save_all=True,append_images=imgs[1:],resolution=144.0)
print("PDF pages:",len(imgs),"->",out, round(os.path.getsize(out)/1024),"KB")
