from playwright.sync_api import sync_playwright

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_viewport_size({"width": 414, "height": 896})
    page.goto("https://talhashahidkhan.com", wait_until="networkidle")
    page.screenshot(path="screenshot.png", full_page=True)
    browser.close()
