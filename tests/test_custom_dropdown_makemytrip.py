from playwright.sync_api import sync_playwright

def test_dismiss_modal_with_xpath():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.makemytrip.global/?cc=am&redirectedBy=gl")

        page.wait_for_timeout(3000)

        # Try to click close button on modal
        try:
            page.wait_for_selector("//section[contains(@class,'modal')]/span", timeout=5000)
            page.click("//section[contains(@class,'modal')]/span")
            print("✅ Modal closed via close button.")
        except Exception as e:
            print(f"⚠️ Modal close failed: {e}")

        # Proceed with dropdown interaction
        page.click("//label[@for='fromCity']")
        page.fill("//input[@placeholder='From']", "New York")
        page.click("//p[contains(text(), 'New York')]")

        page.wait_for_timeout(5000)
        browser.close()
