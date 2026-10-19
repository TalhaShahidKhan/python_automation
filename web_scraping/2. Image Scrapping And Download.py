import os
import asyncio
import requests
from playwright.async_api import async_playwright

URL="https://www.amazon.com"
FOLDER="images"

os.makedirs(FOLDER, exist_ok=True)

async def main():
    image_urls = []

    # Using Playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = browser.new_context()
        page = await context.new_page()

        def save_img_urls(res):
            if res.request.resource_type == "image":
                image_urls.append(res.url)

        page.on(event="response", save_img_urls)
        await page.goto(URL)
        await page.wait_for_timeout(3000)
        await browser.close()

    # Download
    image_urls = list(set(image_urls))

    for index, url in enumerate(image_urls):
        try:
            img_response = requests.get(url)
            img_path = os.path.join(FOLDER, f"image_{index}.jpg")
            with open(img_path, "wb") as file:
                file.write(img_response.content)
            print("Downloaded:", img_path)
        except Exception as e:
            print("Failed:", img_path, "Error:", e)

    print("Done")

asyncio.run(main())
