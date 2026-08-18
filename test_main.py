import re
import pytest
from playwright.sync_api import (expect, Page)

from pages.Login_Page import LoginPage
from pages.HomePage import HomePage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Reserved name in playwright that allows to pass additional parameters
    when creating new context"""
    return {
        **browser_context_args,
        "storage_state": "storage_state.json",
    }


@pytest.fixture(scope="session")
def login(browser, base_url):
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce", base_url)
    context.storage_state(path="storage_state.json")
    context.close()


@pytest.fixture(scope="function", autouse=True)
def navigate(login, page: Page, base_url):
    """2 lines down are replaced by browser_context_args fixture"""
    # context = browser.new_context(storage_state="storage_state.json")
    # page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    yield
    page.screenshot(path="screenshot.png", full_page=True)
    page.close()

@pytest.fixture(scope="function")
def home_page(page: Page):
    homepage = HomePage(page)
    yield homepage

def test_add_to_cart(home_page: HomePage, page: Page):
    product: str = "Sauce Labs Backpack"
    home_page.buy_product_by_name(product)

    button = home_page._product_button(product)
    expect(button).to_have_text("Remove", timeout=10)
    button.screenshot(path='button.png')
    expect(button).to_have_id("remove-sauce-labs-backpack")
    expect(page).to_have_url(re.compile("demo"))
    expect(button).to_have_css("width", "160px")
    page.mouse.wheel(0, 100)
