from playwright.sync_api import sync_playwright

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://inventory.teamrabbil.com", wait_until="networkidle")
    element = page.locator("h2").nth(0)
    inner_text = element.inner_text()
    print(inner_text)
    browser.close()
