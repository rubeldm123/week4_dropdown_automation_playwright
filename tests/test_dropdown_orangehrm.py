def test_orangehrm_dropdown(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")
    page.wait_for_selector("h6:has-text('Dashboard')")

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

    # Interact with 'User Role' custom dropdown
    page.click("//label[text()='User Role']/../following-sibling::div")
    page.click("//div[@role='listbox']//span[text()='Admin']")

    # Interact with 'Status' custom dropdown
    page.click("//label[text()='Status']/../following-sibling::div")
    page.click("//div[@role='listbox']//span[text()='Enabled']")

    print("Dropdowns successfully selected in OrangeHRM.")