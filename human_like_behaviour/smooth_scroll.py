import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://inventory.teamrabbil.com", wait_until="networkidle")

    # ✅ Scroll Down Slowly
    for _ in range(50):  # repeat scrolling
        page.mouse.wheel(0, 50)  # 50 px down
        time.sleep(1)  # small delay = smooth

    time.sleep(1)

    # ✅ Scroll Up Slowly
    for _ in range(50):
        page.mouse.wheel(0, -50)  # 50 px up
        time.sleep(1)

    browser.close()
