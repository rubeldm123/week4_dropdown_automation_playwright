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