import time
from calendar import month

from playwright.sync_api import Page, expect

from pages.basepage import BasePage
from datetime import datetime

class WidgetsPageDatePicker(BasePage):
    # cоздаём новый объект который ссылается на текущий объект page c Типом Page
    def __init__(self, page: Page):
        # вызываем метод инициализации родительского класса для текущего объекта
        super().__init__(page)
        # каждый объект класса WidgetsPageAccordian будет иметь свой собственный атрибут page
        self.page = page

    def go_to_task_date_picker(self):
        url = 'https://demoqa.com/date-picker'
        self.page.goto(url, timeout=60000)

    def check_add_date_manual(self):
        input_select_date = self.page.locator('#datePickerMonthYearInput')
        input_select_date.clear()
        input_select_date.fill('26/09/1992')
        self.page.locator('#datePickerContainer h1').click()
        expect(input_select_date).to_be_empty()

    def check_add_date_with_picker(self):
        input_select_date = self.page.locator('#datePickerMonthYearInput')
        input_select_date.click()
        select_month = self.page.select_option('.react-datepicker__month-select', value='8')
        select_year = self.page.select_option('.react-datepicker__year-select', value='1992')
        self.page.locator('[aria-label*="September 1st, 1992"]').click()
        input_date = input_select_date.input_value()
        assert input_date == '09/01/1992'

    def check_add_date_and_time_picker(self, month, year, date, times):
        #локаторы
        picker_input = self.page.locator('#dateAndTimePickerInput')
        month_drop_down = self.page.locator("#dateAndTimePicker span").first
        year_drop_down = self.page.locator("#dateAndTimePicker span").nth(2)
        year_down_arrow = self.page.locator("a.react-datepicker__navigation--years-previous").first
        year_up_arrow = self.page.locator("a.react-datepicker__navigation--years-upcoming").first

        #клик на главное поле
        picker_input.click()

        #выбор месяца из дропдауна
        month_drop_down.click()
        self.page.get_by_text(month).click()

        #выбор года из дропдауна
        year_drop_down.click()
        if year > '2030':
            arrow = year_up_arrow
        else:
            arrow = year_down_arrow
        while True:
            year_locator = self.page.locator('.react-datepicker__year-option').get_by_text(year)
            if year_locator.count() > 0:
                year_locator.click()
                break

            for _ in range(7):
                arrow.click()
        #выбор даты
        self.page.locator(f'.react-datepicker__day.react-datepicker__day--0{date}:not(.react-datepicker__day--outside-month)').click()

        # Клик по времени '14:30'
        self.page.locator('.react-datepicker__time-list-item').get_by_text(times).click()


        # Конвертируем время из формата в формат '0:00 PM/AM'
        time_obj = datetime.strptime(times, '%H:%M')
        converted_time_str = time_obj.strftime('%I:%M %p')
        if converted_time_str[0] == '0':
            converted_time_str = converted_time_str[1:]

        # Получаем финальное значение времени
        final_date = self.page.locator('#dateAndTimePickerInput').input_value()

        assert final_date == f'{month} {date}, {year} {converted_time_str}'