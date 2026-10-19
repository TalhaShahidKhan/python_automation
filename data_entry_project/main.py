import csv

from playwright.sync_api import sync_playwright

LOGIN_URL = "https://inventory.teamrabbil.com/userLogin"
CUSTOMER_PAGE_URL = "https://inventory.teamrabbil.com/customerPage"

EMAIL = "talha@gmail.com"
PASSWORD = "abc123@xyz  "
CSV_FILE = "customers.csv"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # ✅ Login
    page.goto(LOGIN_URL, wait_until="networkidle")
    page.locator("#email").fill(EMAIL)
    page.locator("#password").fill(PASSWORD)

    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_text("NEXT", exact=False).click()

    print("✅ Login Successful")

    # ✅ Go to Customer Page
    page.goto(CUSTOMER_PAGE_URL, wait_until="networkidle")

    # ✅ Read CSV
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["customerName"]
            email = row["customerEmail"]
            mobile = row["customerMobile"]

            print(f"➡ Adding Customer: {name}")

            # ✅ Open Create Modal
            page.locator('button[data-bs-target="#create-modal"]').click()
            page.wait_for_selector("#create-modal.show")

            # ✅ Fill Form
            page.locator("#customerName").fill(name)
            page.locator("#customerEmail").fill(email)
            page.locator("#customerMobile").fill(mobile)

            # ✅ Submit
            page.locator("#save-btn").click()

            # ✅ Wait for request & modal close
            page.wait_for_timeout(1500)

            print(f"✅ Saved: {name}")

    browser.close()
    print("🎉 All Customers Added Successfully!")
