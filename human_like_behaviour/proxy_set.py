from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        proxy={
            "server": "http://gate.decodo.com:10003",
            "username": "sp8tcdlo12",
            "password": "ArC~9fMa8cj7vgdu6F",
        },
    )

    page = browser.new_page()
    page.goto("https://ifconfig.me")
    page.wait_for_timeout(10000)  # wait for 5 seconds to observe the IP
    browser.close()
