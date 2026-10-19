import asyncio
from playwright.async_api import async_playwright

WINDOWS_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=WINDOWS_UA)
        urls=[
            "https://google.com",
            "https://www.youtube.com",
            "https://www.amazon.com",
            "https://www.bing.com",
            "https://www.github.com",
        ]

        pages = []
        for _ in range(5):
            EachPage = await context.new_page()
            pages.append(EachPage)

        tasks= []
        for i in range(5):
            EachTask= pages[i].goto(urls[i])
            tasks.append(EachTask)

        await asyncio.gather(*tasks)

        print("Done")

        await asyncio.sleep(15)
        await browser.close()



asyncio.run(main())

