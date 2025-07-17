# 🧪 WEEK 4: Dropdown Automation Test Using Playwright & Pytest (Wikipedia + OrangeHRM)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-tested-green.svg)
![License](https://img.shields.io/badge/license-Educational-lightgrey.svg)

This project is part of a full QA Automation Engineer learning path using Playwright with Python.

In **Week 4**, you'll practice dropdown interaction automation on two real-world websites: [Wikipedia.org](https://www.wikipedia.org/) and the [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/). You'll extract dropdown attributes, count and list all options, and perform selection by value, label, and index—covering both **standard HTML `<select>` dropdowns** and **custom (non-`<select>`) dropdowns**.

---

## ✅ What You'll Learn

* How to locate and extract HTML attributes using Playwright
* How to interact with both standard `<select>` dropdowns and non-select (custom JS) dropdowns
* How to dynamically count and iterate over dropdown items
* How to use Playwright fixtures with Pytest

---

## 📁 Project Structure

```
week4_dropdown_automation_playwright/
├── tests/
│   ├── test_dropdown_wikipedia.py      # Dropdown test script for Wikipedia
│   └── test_dropdown_orangehrm.py      # Dropdown test script for OrangeHRM (non-<select>)
├── conftest.py                         # Browser and page fixture setup
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Files ignored by Git
└── README.md                           # Project documentation
```

---

## ⚙️ Setup Instructions

### 1⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/week4_dropdown_automation_playwright.git
cd week4_dropdown_automation_playwright
```

### 2⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3⃣ Install Dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 4⃣ Run the Tests
```bash
pytest -s -v
```

---

## 🧩 conftest.py Code (Browser & Page Fixture)
```python
import pytest
from playwright.sync_api import sync_playwright

# Replace this with your actual Chrome path
# CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        # Uncomment and set CHROME_PATH to use real Chrome instead of bundled Chromium
        # browser = p.chromium.launch(headless=False, executable_path=CHROME_PATH)
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
```

---

## ▶️ How the Tests Work

### Wikipedia Dropdown Test (`test_dropdown_wikipedia.py`)
```python
# tests/test_dropdown_wikipedia.py

def test_wikipedia_dropdown(page):
    page.goto("https://www.wikipedia.org/")
    dropdown = page.locator("select#searchLanguage")
    dropdown_handle = dropdown.element_handle()

    attributes = page.evaluate("""
        (element) => {
            const attrs = {};
            for (const attr of element.attributes) {
                attrs[attr.name] = attr.value;
            }
            return attrs;
        }
    """, dropdown_handle)

    print("Attributes of dropdown:")
    for attr, val in attributes.items():
        print(f"- {attr}: {val}")

    options = dropdown.locator("option")
    count = options.count()
    print(f"\nTotal options: {count}")

    for i in range(count):
        value = options.nth(i).get_attribute("value")
        text = options.nth(i).inner_text()
        print(f"{i+1}. Value: '{value}' | Text: '{text}'")

    dropdown.select_option("hi")
    dropdown.select_option(label="Deutsch")
    value_at_5 = options.nth(5).get_attribute("value")
    dropdown.select_option(value=value_at_5)
```

### OrangeHRM Dropdown Test (`test_dropdown_orangehrm.py`)
```python
# tests/test_dropdown_orangehrm.py

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
```

---

## 📤 Push to GitHub

### First Time Setup:
```bash
git init
git add .
git commit -m "Week 4: Wikipedia & OrangeHRM dropdown automation"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/week4_dropdown_automation_playwright.git
git push -u origin main
```
> 🔁 Replace `YOUR_USERNAME` with your GitHub username.

---

## 📄 License & Credit
This test uses [Wikipedia.org](https://www.wikipedia.org/) and the [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/) for educational purposes only. No changes are made to their servers or data.
