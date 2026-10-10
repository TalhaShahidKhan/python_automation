from playwright.sync_api import sync_playwright

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://google.com")
    page.wait_for_timeout(3000)

    page.goto("https://github.com")
    page.wait_for_timeout(3000)

    page.goto("https://rabbil.com")
    page.wait_for_timeout(3000)

    page.reload()
    page.wait_for_timeout(3000)

    page.go_back()
    page.wait_for_timeout(3000)

    page.go_back()
    page.wait_for_timeout(3000)

    page.go_forward()
    page.wait_for_timeout(3000)

    page.go_forward()
    page.wait_for_timeout(3000)

    browser.close()
