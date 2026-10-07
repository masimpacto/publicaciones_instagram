"""Renderiza placas.html a placa1..6.jpg (1080x1350). Uso: python3 placas/render.py"""
import os
from playwright.sync_api import sync_playwright
here = os.path.dirname(os.path.abspath(__file__))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium") if os.path.exists("/opt/pw-browsers/chromium") else p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto("file://" + os.path.join(here, "placas.html"))
    pg.evaluate("document.fonts.ready")
    for i in range(1, 7):
        pg.locator(f"#p{i}").screenshot(path=os.path.join(here, "..", f"placa{i}.jpg"), type="jpeg", quality=95)
    b.close()
