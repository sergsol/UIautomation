import pytest
from playwright.sync_api import sync_playwright, expect, Page

""""""
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Reserved name in playwright that allows to pass additional parameters
    when creating new context"""
    return {
        **browser_context_args,
        "storage_state": "storage_state.json",
    }

@pytest.fixture(scope="session")
def login():
    with sync_playwright() as p:
        br = p.chromium.launch(headless=True, slow_mo=1000)
        context = br.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
        context.storage_state(path="storage_state.json")
        context.close()
        br.close()


@pytest.fixture(scope="function", autouse=True)
def navigate(login, page: Page):
    """2 lines down are replaced by browser_context_args fixture"""
    # context = browser.new_context(storage_state="storage_state.json")
    # page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    yield
    page.screenshot(path="screenshot.png",full_page=True)
    page.close()


def test_add_to_cart(page: Page):
    item = page.locator('[data-test="inventory-item-description"]')
    button = item.filter(has_text="Sauce Labs Backpack").get_by_role('button')
    button.click()
    expect(button).to_have_text("Remove", timeout=10)
    button.screenshot(path='button.png')
