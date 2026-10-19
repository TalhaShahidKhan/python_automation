import asyncio
from playwright.async_api import async_playwright

WINDOWS_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=WINDOWS_UA)
        page = await context.new_page()

        await page.goto("https://www.amazon.com")
        title = await page.title()
        print("Page Title:", title)

        await browser.close()

asyncio.run(run())

"""
Multiple Automation Tasks Run Together
- Async lets you open many pages, tabs, or browsers at the same time, making automation much faster.

Faster Web Scraping & Searching
- You can search 10 keywords or scrape 100 URLs in parallel instead of one by one.

Human-Like Behavior Runs Smoothly
- Scrolling, typing, waiting, loading — all can run together without blocking each other.

Perfect for Queue/Batch Jobs
- Bulk operations (product upload, form submission, CSV tasks) finish quickly because tasks work concurrently.

Proxy & User-Agent Rotation Becomes Easy
-Each async task can use a different proxy, user-agent, or profile — ideal for anti-bot automation.

"""