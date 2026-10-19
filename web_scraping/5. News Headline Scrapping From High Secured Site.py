import asyncio
import random
import pandas as pd
from playwright.async_api import async_playwright


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent=random.choice(USER_AGENTS),
            viewport={"width": 1280, "height": 800},
            locale="en_US",
        )

        page = await context.new_page()

        await page.goto("https://www.bbc.com")
        await page.wait_for_selector('h2[data-testid="card-headline"]', timeout=30000)

        items = await page.query_selector_all('h2[data-testid="card-headline"]')

        data = []
        for i, item in enumerate(items[:10]):
            title = (await item.text_content()).strip()
            data.append({"id": i, "title": title})

        dataframe = pd.DataFrame(data)
        dataframe.to_csv("bbc.csv", index=False, encoding="utf-8")

        await browser.close()


asyncio.run(main())
