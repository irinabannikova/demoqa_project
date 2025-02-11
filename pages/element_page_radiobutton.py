from idlelib.searchengine import get_selection

from playwright.sync_api import Page, expect
import time

from pages.basepage import BasePage


class ElementsPageRadiobutton(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    #локаторы
    text_massage = ".mt-3"
    value = "#result > span:nth-child({point_num})"


    def go_to_task_radio_btn(self):
        self.goto('https://demoqa.com/radio-button')

    def click_yes(self):
        self.page.locator("text=Yes").check()

    def click_impressive(self):
        self.page.locator("text=Impressive").check()


    def review_click_yes(self):
        assert self.page.locator(self.text_massage).inner_text() == 'You have selected Yes'
        assert not self.page.locator("text=Impressive").is_checked()
        radio_btn_no = self.page.locator("#noRadio")
        expect(radio_btn_no).to_be_disabled()

    def review_click_impressive(self):
        assert self.page.locator(self.text_massage).inner_text() == 'You have selected Impressive'
        assert not self.page.locator("text=Yes").is_checked()
        radio_btn_no = self.page.locator("#noRadio")
        expect(radio_btn_no).to_be_disabled()