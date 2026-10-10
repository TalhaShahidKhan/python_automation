from playwright.sync_api import sync_playwright

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://talhashahidkhan.com", wait_until="networkidle")
    html = page.content()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("done")
    browser.close()
