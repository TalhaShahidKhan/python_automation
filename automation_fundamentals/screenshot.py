from playwright.sync_api import sync_playwright

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com", wait_until="networkidle")
    page.screenshot(path="screenshot.png", full_page=True)
    browser.close()
