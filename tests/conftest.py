import pytest
from playwright.sync_api import Page, Request, Response
from tests.pages.Login_Page import LoginPage
from tests.pages.HomePage import HomePage

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Reserved name in playwright that allows to pass additional parameters
    when creating new context"""
    return {
        **browser_context_args,
        "storage_state": "tests/storage_state.json",
    }


@pytest.fixture(scope="session")
def login(browser, base_url):
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce", base_url)
    context.storage_state(path="tests/storage_state.json")
    context.close()

def on_request(request: Request):
    print("Request:", request)

def on_response(response: Response):
    print("Response:",  response)



@pytest.fixture(scope="function", autouse=True)
def navigate(login, page: Page, base_url):
    """2 lines down are replaced by browser_context_args fixture"""
    # context = browser.new_context(storage_state="storage_state.json")
    # page = context.new_page()
    page.on("request", on_request)
    page.on("response", on_response)
    # page.route("**/*.js", on_route_js)
    page.goto("https://www.saucedemo.com/inventory.html")
    yield
    page.screenshot(path="..tests/screenshot.png", full_page=True)
    page.close()


@pytest.fixture(scope="function")
def home_page(page: Page):
    homepage = HomePage(page)
    yield homepage
