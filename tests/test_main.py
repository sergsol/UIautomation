import re
from playwright.sync_api import (expect, Page, Route)

from tests.pages.HomePage import HomePage


# def on_route(route: Route):
#     if route.request.resource_type == "image":
#         route.abort()
#     else:
#         route.continue_()

# def on_route(route: Route):
#     route.fulfill(body="Hello world!")

# def on_route(route: Route):
#     response = route.fetch()
#     body = response.text().replace("Swag LabsSwag Labs", "Serge Automation")
#     route.fulfill(response=response
#                   , body=body)


def on_route_js(route: Route):
    response = route.fetch()
    body = response.text().replace("Swag Labs", "Serge Automation")
    route.fulfill(status=response.status, headers=response.headers, body=body)


def test_add_to_cart(home_page: HomePage, page: Page):
    product: str = "Sauce Labs Backpack"
    home_page.buy_product_by_name(product)
    button = home_page._product_button(product)
    expect(button).to_have_text("Remove", timeout=10)
    expect(button).to_have_id("remove-sauce-labs-backpack")
    expect(page).to_have_url(re.compile("demo"))
    expect(button).to_have_css("width", "160px")
    page.mouse.wheel(0, 100)
    # breakpoint()
