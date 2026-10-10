from playwright.sync_api import sync_playwright

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://inventory.teamrabbil.com", wait_until="networkidle")
    nameInputElement = page.locator("input[placeholder='Name']")
    nameInputElement.fill("Talha Khan")
    page.wait_for_timeout(2000)
    browser.close()
