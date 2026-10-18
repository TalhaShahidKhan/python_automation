import os
import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        "https://inventory.teamrabbil.com/public/UploadPage", wait_until="networkidle"
    )
    for file_name in os.listdir("images"):
        file_path = os.path.join("images", file_name)
        page.set_input_files("input[name='file']", file_path)
        page.click("button[type='submit']")

        try:
            page.wait_for_selector(".alert-success", timeout=5000)
            print(f"{file_name} uploaded")
        except:
            print(f"{file_name} upload failed")

        time.sleep(5)
        page.reload(wait_until="networkidle")
    browser.close()
