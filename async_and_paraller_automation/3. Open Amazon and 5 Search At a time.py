import  asyncio
import random
from playwright.async_api import async_playwright
import time
KEYWORDS = ["laptop", "keyboard", "router", "monitor", "ssd"]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
]

async def search_amazon(page,keyword):
    await page.goto("https://www.amazon.com",wait_until="domcontentloaded")

    box = page.locator("#twotabsearchtextbox")

    if not await box.is_visible():
        box = page.locator("#nav-bb-search")

    if not await box.is_visible():
        print("Search Box Not Visible")
        return

    await box.click()
    await box.fill(keyword)
    await box.press("Enter")
    time.sleep(3)
    print("Search Result Found")


async def main():
    async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(user_agent=random.choice(USER_AGENTS))

            pages=[]
            for i in range(5):
                EachPage = await context.new_page()
                pages.append(EachPage)

            tasks = []
            for i in range(5):
                EachTask =  search_amazon(pages[i],KEYWORDS[i])
                tasks.append(EachTask)

            await asyncio.gather(*tasks)

            await asyncio.sleep(20)
            await browser.close()
            print("done...")
            return


asyncio.run(main())




