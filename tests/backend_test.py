#
# from playwright.sync_api import *
#
# def on_api_route(route:Route):
#     response = route.fetch()
#     user_age = response.json()
#     user_age['title'] = 'Serge'
#     route.fulfill(response=response, json=user_age)
#
# def test_login(page:Page, playwright:Playwright):
#     response = playwright.request.new_context(base_url="https://dummyjson.com",
#                                               extra_http_headers={"accept-language": "en-US,en;q=0.9"})
#     response = page.request.get("https://dummyjson.com/products/1")
#     data = response.json()
#     print(data)
#     assert "brand" in data
#     assert data['reviews'][0]['rating'] == 3
#
#     api_context = playwright.request.new_context(
#         base_url="https://dummyjson.com",
#     )
#     page.route("**/products/1", on_api_route)
#     response = page.request.get("https://dummyjson.com/products/1")
#     print(response.json())
#
#
