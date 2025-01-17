from idlelib.searchengine import get_selection

from playwright.sync_api import Page, expect
import time


class ElementsPageDynamicProperties:
    def __init__(self, page: Page):
        self.page = page
        self.toggles_list = ''

    def go_to_task_dynamic_properties(self):
        self.page.goto('https://demoqa.com/dynamic-properties')

    def check_dynamic_element_before_5_second(self):
        assert self.page.locator('#visibleAfter').is_hidden()
        assert self.page.locator('#colorChange').evaluate('(element) => window.getComputedStyle(element).color') == 'rgb(255, 255, 255)'

    def check_dynamic_element_after_5_second(self):
        self.page.wait_for_timeout(5000)
        assert self.page.locator('#visibleAfter').is_visible()
        assert self.page.locator('#colorChange').evaluate('(element) => window.getComputedStyle(element).color') == 'rgb(220, 53, 69)'