import pytest
from playwright.sync_api import sync_playwright

# Replace this with your actual Chrome path
#CHROME_PATH = CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
@pytest.fixture(scope="function")
def browser():
	with sync_playwright() as p:
		#browser=p.chromium.launch(headless=False, executable_path=CHROME_PATH)
		browser=p.chromium.launch(headless=False)
		yield browser
		browser.close()

@pytest.fixture(scope="function")
def page(browser):
	context=browser.new_context()
	page=context.new_page()
	page.set_viewport_size({"width":1920,"height":1080})
	yield page