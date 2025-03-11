from playwright.sync_api import Page, expect

from pages.basepage import BasePage

from datetime import datetime

class WidgetsPageMenu(BasePage):
    # cоздаём новый объект который ссылается на текущий объект page c Типом Page
    def __init__(self, page: Page):
        # вызываем метод инициализации родительского класса для текущего объекта
        super().__init__(page)
        # каждый объект класса WidgetsPageAccordian будет иметь свой собственный атрибут page
        self.page = page


    def go_to_task_menu(self):
        url = 'https://demoqa.com/menu'
        self.page.goto(url, timeout=60000)

    def open_main_item_2(self):
        item_2_color_before_pick = self.page.locator('#nav > li:nth-child(2)').evaluate('(element) => window.getComputedStyle(element).getPropertyValue("background-color")')
        assert item_2_color_before_pick == 'rgb(36, 175, 21)', f'{item_2_color_before_pick} should be rgb(36, 175, 21)'

        self.page.locator("//*[contains(text(), 'Main Item 2')]").hover()

        item_2_color_after_pick = self.page.locator('#nav > li:nth-child(2)').evaluate('(element) => window.getComputedStyle(element).getPropertyValue("background-color")')
        assert item_2_color_after_pick == 'rgb(0, 63, 32)', f'{item_2_color_after_pick} should be rgb(0, 63, 32)'

    def check_count_item(self):
        list_item = self.page.locator('#nav > li:nth-child(2) >ul > li > a')
        assert list_item.count() == 3

    def check_name_item(self):
        list_item = self.page.locator('#nav > li:nth-child(2) >ul > li > a').all_inner_texts()
        assert list_item[0] == 'Sub Item'
        assert list_item[1] == 'Sub Item'
        assert list_item[2] == 'SUB SUB LIST »'

    def hover_item(self):
        self.page.get_by_text('Sub Item').first.hover()
        self.page.locator('li:nth-child(2) > ul > li:nth-child(2) > a').hover()
        self.page.locator('li:nth-child(2) > ul > li:nth-child(3) > a').hover()






    # def check_item(self):
    #     list_item = self.page.locator('#nav > li:nth-child(2) >ul > li > a').all_inner_texts()
    #     assert list_item[0] == 'Sub Item'






