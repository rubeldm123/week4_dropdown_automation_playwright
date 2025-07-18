from playwright.sync_api import sync_playwright

def test_dropdown_with_loop_and_condition():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.makemytrip.global/?cc=am&redirectedBy=gl")

        page.wait_for_timeout(3000)

        # Close modal popup
        try:
            page.wait_for_selector("//section[contains(@class,'modal')]/span", timeout=5000)
            page.click("//section[contains(@class,'modal')]/span")
            print("✅ Modal closed via close button.")
        except Exception as e:
            print(f"⚠️ Modal close failed: {e}")

        # Click on "From" field
        page.click("//label[@for='fromCity']")
        page.fill("//input[@placeholder='From']", "New York")
        page.wait_for_timeout(2000)

        # Get all city options
        options = page.locator("//ul[@role='listbox']//p")
        count = options.count()
        print(f"🔍 Found {count} city suggestions.")

        # Loop through options and select the exact match
        for i in range(count):
            option_text = options.nth(i).inner_text().strip()
            print(f"➡️ Option {i+1}: {option_text}")
            if "New York" in option_text:
                options.nth(i).click()
                print(f"✅ Selected city: {option_text}")
                break
        else:
            print("❌ Desired city not found in dropdown.")

        page.wait_for_timeout(5000)
        browser.close()
