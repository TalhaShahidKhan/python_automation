from playwright.sync_api import sync_playwright

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://rabbil.com", wait_until="networkidle")

    title = page.locator("title").first.inner_text()
    desc = page.locator("meta[name='description']").get_attribute("content")
    print(desc)
    browser.close()
