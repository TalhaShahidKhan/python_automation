from playwright.sync_api import sync_playwright

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://inventory.teamrabbil.com", wait_until="networkidle")
    element = page.locator("form").nth(0)
    inner_html = element.inner_html()
    print(inner_html)
    browser.close()
