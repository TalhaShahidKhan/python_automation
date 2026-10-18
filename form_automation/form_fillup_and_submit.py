from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        "https://inventory.teamrabbil.com/userRegistration", wait_until="networkidle"
    )
    page.locator("#email").fill("talha@gmail.com")
    page.wait_for_timeout(2000)
    page.locator("#firstName").fill("Fname1")
    page.wait_for_timeout(2000)
    page.locator("#lastName").fill("Lname1")
    page.wait_for_timeout(2000)
    page.locator("#mobile").fill("01722233343")
    page.wait_for_timeout(2000)
    page.locator("#password").fill("abc123@xyz")
    page.wait_for_timeout(2000)
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_text("Complete").click()
    print("Signup Successfull")
    print(page.url)

    browser.close()
