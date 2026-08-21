# from playwright.sync_api import Page
#
# def test_task(page: Page):
#     page.goto("https://the-internet.herokuapp.com/tables")
#     page.get_by_text("Last Name").first.click()
#     # forpage.locator("//table[@id='table1']//tr/th[2]/../../../tbody/tr/td[2]").text_content()
#     table = page.locator("//table[@id='table1']")
#     headers = table.locator("thead th")
#     count = headers.count()




    # self.headers.count()


# Last_name | Sting | AllCaps
# Monet | Decimal | removedolar



""" 
Task: Check that dynamic table sorting returns valid results using pytest+PLaywright

Target: https://the-internet.herokuapp.com/tables (Table 1) DONE

User Story:
As an end-user, I want to sort the web table by clicking column headers so I can easily analyze table data.
Acceptance Criteria:
Clicking the 'Last Name' header DONE 
sorts the table rows alphabetically.
Clicking the 'Due' header sorts the table rows numerically by monetary value.
"""

#
# //table[@id='table1']//tr/th[2]/../../../tbody/tr/td[2]