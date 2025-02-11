from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def is_element_hidden(self, selector: str) -> bool:
        element = self.page.locator(selector)
        return element.is_hidden()
    def is_element_visible(self, selector: str) -> bool:
        element = self.page.locator(selector)
        return element.is_visible()
