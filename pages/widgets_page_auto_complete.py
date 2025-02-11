from asyncio import wait_for

from playwright.sync_api import Page, expect

from pages.basepage import BasePage

class WidgetsPageAutoComplete(BasePage):
    # cоздаём новый объект который ссылается на текущий объект page c Типом Page
    def __init__(self, page: Page):
        # вызываем метод инициализации родительского класса для текущего объекта
        super().__init__(page)
        # каждый объект класса WidgetsPageAccordian будет иметь свой собственный атрибут page
        self.page = page

    def go_to_task_auto_complete(self):
        url = 'https://demoqa.com/auto-complete'
        self.page.goto(url, timeout=60000)

    def input_valid_colors(self):
        self.page.locator("#autoCompleteMultipleInput").fill("bl")
        assert self.page.locator('.auto-complete__menu').is_visible()
        self.page.get_by_text("Blue", exact=True).click()
        self.page.locator("#autoCompleteMultipleInput").fill("bl")
        assert self.page.locator('.auto-complete__menu').is_visible()
        self.page.get_by_text("Black", exact=True).click()
        self.page.locator("#autoCompleteMultipleInput").fill("r")
        assert self.page.locator('.auto-complete__menu').is_visible()
        self.page.get_by_text("Red", exact=True).click()
        self.page.locator("#autoCompleteMultipleInput").fill("r")
        assert self.page.locator('.auto-complete__menu').is_visible()
        self.page.get_by_text("Green", exact=True).click()

    def review_valid_colors(self):
        input_colors = self.page.locator("#autoCompleteMultipleContainer .css-1hwfws3").all_inner_texts()
        assert input_colors == ['Blue\nBlack\nRed\nGreen']

    def remove_all_colors(self):
        self.page.locator('.auto-complete__clear-indicator').click()
        locator_input = self.page.locator("#autoCompleteMultipleInput")
        expect(locator_input).to_be_empty()

    def input_invalid_colors(self):
        locator_input = self.page.locator("#autoCompleteMultipleInput")
        locator_input.fill("jo")
        assert self.page.locator('.auto-complete__menu').is_hidden()
        locator_input.fill("щз")
        assert self.page.locator('.auto-complete__menu').is_hidden()
        self.page.locator('#autoCompleteContainer h1').click(button='left')
        expect(locator_input).to_be_empty()

    def review_invalid_colors(self):
        locator_input = self.page.locator("#autoCompleteMultipleInput")
        expect(locator_input).to_be_empty()

    def input_color(self):
        self.page.locator("#autoCompleteMultipleInput").fill("vo")
        self.page.keyboard.press("Enter")

    def remove_color(self):
        self.page.locator('.auto-complete__multi-value__remove').click()
        locator_input = self.page.locator("#autoCompleteMultipleInput")
        expect(locator_input).to_be_empty()

    def input_single_colors(self):
        single_color = self.page.locator('#autoCompleteSingleInput')
        single_color.click()
        single_color.fill('blue')
        self.page.get_by_text("Blue", exact=True).click()
        select_color = self.page.locator('.auto-complete__single-value').inner_text()
        assert select_color == 'Blue'
        single_color.fill('black')
        self.page.get_by_text("Black", exact=True).click()
        select_color = self.page.locator('.auto-complete__single-value').inner_text()
        assert select_color == 'Black'




