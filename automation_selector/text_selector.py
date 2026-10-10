from playwright.sync_api import sync_playwright

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://inventory.teamrabbil.com", wait_until="networkidle")

    # Text Selector
    element = page.get_by_text("Login")
    element.click()
    print(page.url)
    page.wait_for_timeout(5000)
    browser.close()
