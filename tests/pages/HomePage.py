
from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
        self.page = page


    def buy_product_by_name(self, product_name: str):
        item = self.page.locator('[data-test="inventory-item-description"]')
        item.filter(has_text=product_name).get_by_role('button').click()


    def _product_button(self, product_name: str):
        return self.page.locator('[data-test="inventory-item-description"]') \
            .filter(has_text=product_name).get_by_role('button')