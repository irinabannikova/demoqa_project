from pydoc import visiblename

from playwright.sync_api import Page, expect

from pages.basepage import BasePage

from datetime import datetime

class WidgetsPageToolTips(BasePage):
    # cоздаём новый объект который ссылается на текущий объект page c Типом Page
    def __init__(self, page: Page):
        # вызываем метод инициализации родительского класса для текущего объекта
        super().__init__(page)
        # каждый объект класса WidgetsPageAccordian будет иметь свой собственный атрибут page
        self.page = page


    def go_to_task_tooltips(self):
        url = 'https://demoqa.com/tool-tips'
        self.page.goto(url, timeout=60000)

    def check_hover_on_button(self):
        self.page.hover('#toolTipButton')
        hover_text = self.page.locator('.tooltip-inner').inner_text()
        assert hover_text == 'You hovered over the Button', f'{hover_text} неверный'
        assert self.page.locator('[role="tooltip"]').is_visible()
    def check_hover_on_one_link(self):
        self.page.hover('#texToolTopContainer > a:nth-child(1)')
        hover_text = self.page.locator('.tooltip-inner').inner_text()
        assert hover_text == 'You hovered over the Contrary', f'{hover_text} неверный'
        assert self.page.locator('[role="tooltip"]').is_visible()









