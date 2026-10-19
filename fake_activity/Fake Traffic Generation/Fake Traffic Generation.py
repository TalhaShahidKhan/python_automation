import random
from playwright.sync_api import sync_playwright
import time
PROXY = [
    {"server": "http://gate.decodo.com:10001","username": "user-sp8tcdlo12-asn-23688","password": "a3+yfO2WjCesfh5O7l"},
    {"server": "http://gate.decodo.com:10002", "username": "user-sp8tcdlo12-asn-23688", "password": "a3+yfO2WjCesfh5O7l"},
    {"server": "http://gate.decodo.com:10003", "username": "user-sp8tcdlo12-asn-23688", "password": "a3+yfO2WjCesfh5O7l"}
]
USER_AGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 Chrome/121 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 Version/16.4 Safari/605.1.15"
]

SESSION = 10
TARGET= "https://inventory.teamrabbil.com"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    for  _ in range(SESSION):
        context = browser.new_context( user_agent=random.choice(USER_AGENT), proxy=random.choice(PROXY))
        page= context.new_page()
        page.goto(TARGET,wait_until="networkidle")

        time.sleep(random.uniform(3,7))

        # Scroll like a human
        for _ in range(3):
            page.evaluate("window.scrollBy(0, 500)")
            time.sleep(random.uniform(0.5,1.2))

        time.sleep(random.uniform(2, 4))


        context.close()
        browser.close()

        time.sleep(random.uniform(2, 4))



