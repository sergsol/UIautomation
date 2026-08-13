from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False ,slow_mo=500)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    context.storage_state(path="storage_state.json")

    context.close()

    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(storage_state="storage_state.json")
    page = context.new_page()

    page.goto("https://www.saucedemo.com/inventory.html")


