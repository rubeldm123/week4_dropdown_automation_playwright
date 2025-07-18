"""
Test Script for Interacting with Standard <select> Dropdown on Wikipedia.

This script contains three tests demonstrating how to select dropdown options
by index, value, and visible text using Playwright and Pytest.

Target URL: https://www.wikipedia.org/
"""

import pytest

@pytest.mark.dropdown
def test_select_by_index(page):
    """
    Selects an option from the language dropdown by index.
    Index is 0-based. This test selects the 6th item (index=5).
    """
    print("\n🔹 Start Test: test_select_by_index")
    
    page.goto("https://www.wikipedia.org/")
    
    # Count all dropdown options
    total_options = page.locator("select#searchLanguage option")
    print("🔢 Total options in dropdown:", total_options.count())

    # Select the 6th option using index
    dropdown = page.locator("select#searchLanguage")
    dropdown.select_option(index=5)
    
    # Wait for observation (not needed in real automation)
    page.wait_for_timeout(5000)
    
    print("✅ End Test: test_select_by_index")


@pytest.mark.dropdown
def test_select_by_value(page):
    """
    Selects the French language ('fr') using the 'value' attribute of the option.
    """
    print("\n🔹 Start Test: test_select_by_value")
    
    page.goto("https://www.wikipedia.org/")
    
    # Select French using value="fr"
    dropdown = page.locator("select#searchLanguage")
    dropdown.select_option(value="fr")
    
    page.wait_for_timeout(5000)
    
    print("✅ End Test: test_select_by_value")


@pytest.mark.dropdown
def test_select_by_label(page):
    """
    Selects the Slovak language by its visible label "Slovenčina".
    """
    print("\n🔹 Start Test: test_select_by_label")
    
    page.goto("https://www.wikipedia.org/")
    
    # Select using visible text/label
    dropdown = page.locator("select#searchLanguage")
    dropdown.select_option(label="Slovenčina")
    
    page.wait_for_timeout(5000)
    
    print("✅ End Test: test_select_by_label")
