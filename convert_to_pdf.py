from playwright.sync_api import sync_playwright

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rabbil.com", wait_until="networkidle")
    page.pdf(path="page.pdf", format="A4", print_background=True)
    browser.close()
