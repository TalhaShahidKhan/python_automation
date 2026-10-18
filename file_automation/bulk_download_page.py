import os
import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://inventory.teamrabbil.com/DownloadPage", wait_until="networkidle")
    download_buttons = page.locator("a.btn.btn-success.btn-sm")
    total = download_buttons.count()
    img_dir = os.path.join(os.getcwd(), "images")
    for x in range(total):
        with page.expect_download() as d:
            download_buttons.nth(x).click()
        download = d.value
        file_name = download.suggested_filename
        save_path = os.path.join(img_dir, file_name)
        download.save_as(save_path)
        print(f"Saved {file_name}")
        time.sleep(2)
    browser.close()
