import time
from asyncio import wait_for

from playwright.sync_api import Page, expect

from pages.basepage import BasePage
from datetime import datetime

class WidgetsPageSliderProgress(BasePage):
    # cоздаём новый объект который ссылается на текущий объект page c Типом Page
    def __init__(self, page: Page):
        # вызываем метод инициализации родительского класса для текущего объекта
        super().__init__(page)
        # каждый объект класса WidgetsPageAccordian будет иметь свой собственный атрибут page
        self.page = page


    def go_to_task_slider(self):
        url = 'https://demoqa.com/slider'
        self.page.goto(url, timeout=60000)
    def go_to_task_progress(self):
        url = 'https://demoqa.com/progress-bar'
        self.page.goto(url, timeout=60000)

    def move_slider(self, move_amount):
        self.page.get_by_role("slider").fill(move_amount)
        expect(self.page.locator("#sliderValue")).to_have_value(move_amount)

    def click_progress_start(self):
        self.page.get_by_text('Start').click()

    #остановить прогресс бар после конкретной цифры
    def click_progress_stop_after_num(self, num:int):
        while True:
            progress_num = int(self.page.locator('.bg-info').get_attribute('aria-valuenow'))
            if progress_num == num:
                self.page.get_by_text('Stop').click()
                break
        assert progress_num in range(num, num + 3)

    def check_max_value_progress(self):
        max_value = self.page.wait_for_selector('.bg-success')
        assert max_value.inner_text() == '100%'
        self.page.get_by_text('Reset').click()
        assert self.page.get_by_text('Start')
        assert self.page.locator('.bg-info[aria-valuenow="0"]')

    #проверяем, что значение в прогресс баре именно увеличивается каждый раз
    def check_progress_increases_after_start_click(self):
        previous_value = 0
        work_till = time.time() + 5
        while time.time() < work_till:
            progress_num = int(self.page.locator('.bg-info').get_attribute('aria-valuenow'))
            assert progress_num >= previous_value
            print(progress_num, previous_value )
            previous_value = progress_num











        # previous = 01
        # workTill = time.time() + 3s
        # while time.time() < workTill:
        #     progress_num = int(self.page.locator('.bg-info').get_attribute('aria-valuenow'))
        #     assert progress_num >= previous
        #     previous = progress_num
        #     print(previous)









        # while self.page.get_by_role('progressbar').inner_text() != '50%':
        #     pass
        # self.page.get_by_text('Stop').click()
        # assert self.page.get_by_role('progressbar').inner_text() == '50%'














    # def click_progress_stop(self):
    #     progress_num = self.page.get_by_role('progressbar').inner_text()
    #     if progress_num == '53':
    #         self.page.get_by_text('Stop').click()






