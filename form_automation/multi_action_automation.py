from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://inventory.teamrabbil.com/userLogin", wait_until="networkidle")
    page.locator("#email").fill("talha@gmail.com")
    page.locator("#password").fill("abc123@xyz")
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_text("Next", exact=False).click()

    page.goto("https://inventory.teamrabbil.com/userProfile", wait_until="networkidle")
    page.locator("#firstName").fill("")
    page.locator("#lastName").fill("")
    page.locator("#firstName").fill("Talha")
    page.locator("#lastName").fill("Khan")
    page.get_by_text("Update", exact=False).click()

    page.wait_for_timeout(3000)
    page.goto("https://inventory.teamrabbil.com/dashboard", wait_until="networkidle")
    page.wait_for_timeout(3000)
    page.goto("https://inventory.teamrabbil.com/logout", wait_until="networkidle")
    page.wait_for_timeout(3000)
    print("done")
    print(page.url)
    browser.close()
