from playwright.sync_api import Page, expect

from pages.basepage import BasePage


class WidgetsPageAccordian(BasePage):
    # cоздаём новый объект который ссылается на текущий объект page c Типом Page
    def __init__(self, page: Page):
        # вызываем метод инициализации родительского класса для текущего объекта
        super().__init__(page)
        # каждый объект класса WidgetsPageAccordian будет иметь свой собственный атрибут page
        self.page = page

    def go_to_task_accordian(self):
        self.goto('https://demoqa.com/accordian')

    def click_to_accordian(self, text):
        self.page.get_by_text(text).click()

    def check_open_section_one(self):
        assert self.page.locator('div.card-header > div.show')
        text = self.page.inner_text('#section1Content > p')
        assert text, "Текст отсутствует в первой секции"

    def check_close_section_one(self):
        assert self.page.locator('div.card-header > div.show').is_hidden()

    def check_close_section_two(self):
        assert self.page.locator('#accordianContainer > div >div:nth-child(2) > div.show').is_hidden()

    def check_open_section_two(self):
        assert self.page.locator('#accordianContainer > div >div:nth-child(2) > div.show')
        text = self.page.inner_text('#section2Content > p')
        assert text, "Текст отсутствует в первой секции"

    def check_close_section_tree(self):
        assert self.page.locator('#accordianContainer > div > div:nth-child(3) > div.show').is_hidden()

    def check_open_section_tree(self):
        assert self.page.locator('#accordianContainer > div > div:nth-child(3) > div.show')
        text = self.page.inner_text('#section3Content > p')
        assert text, "Текст отсутствует в первой секции"




