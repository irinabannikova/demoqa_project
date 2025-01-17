from idlelib.searchengine import get_selection

from playwright.sync_api import Page, expect
import time


class ElementsPageWebTables:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = ""
        self.last_name = ""
        self.age = ""
        self.salary = ""
        self.departament = ""
        self.before_search = ""
        self.value = ""
        self.num = ""

    #локаторы
    input_first_name = 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)'
    input_departament = 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(6)'
    input_last_name = 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(2)'
    input_age = 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(3)'
    input_salary = 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(5)'

    old_first_name = 'div.rt-table > div.rt-tbody > div:nth-child(3) > div > div:nth-child(1)'
    old_departament = 'div.rt-table > div.rt-tbody > div:nth-child(3) > div > div:nth-child(6)'
    old_last_name = 'div.rt-table > div.rt-tbody > div:nth-child(3) > div > div:nth-child(2)'
    old_age = 'div.rt-table > div.rt-tbody > div:nth-child(3) > div > div:nth-child(3)'
    old_salary = 'div.rt-table > div.rt-tbody > div:nth-child(3) > div > div:nth-child(5)'


    def go_to_task_web_tabel(self):
        self.page.goto('https://demoqa.com/webtables')

    #add
    def add_new_record(self, first_name, last_name, email, age, salary, departament):
        self.first_name = first_name
        self.departament = departament
        self.page.get_by_role("button", name="Add").click()
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("name@example.com").fill(email)
        self.page.get_by_placeholder("Age").fill(age)
        self.page.get_by_placeholder("Salary").fill(salary)
        self.page.get_by_placeholder("Department").fill(departament)
        self.page.get_by_role("button", name="Submit").click()

    def review_add_valid_new_record(self):
        input_first_name = self.page.locator(self.input_first_name).inner_text()
        assert input_first_name == self.first_name
        input_departament = self.page.locator(self.input_departament).inner_text()
        assert input_departament == self.departament

    def review_add_max_value(self):
       length_first_name = len(self.page.locator(self.input_first_name).inner_text())
       length_last_name = len(self.page.locator(self.input_last_name).inner_text())
       length_age = len(self.page.locator(self.input_age).inner_text())
       length_salary = len(self.page.locator(self.input_salary).inner_text())
       length_department = len(self.page.locator(self.input_departament).inner_text())
       assert length_first_name == 25
       assert length_last_name == 25
       assert length_age == 2
       assert length_salary == 10
       assert length_department == 25

    #edit
    def edit_old_record(self, input_first_name, last_name, email, age, salary, input_departament):
        self.first_name = input_first_name
        self.departament = input_departament
        self.page.locator("#edit-record-3").get_by_role("img").click()
        self.page.get_by_placeholder("First Name").fill(input_first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("name@example.com").fill(email)
        self.page.get_by_placeholder("Age").fill(age)
        self.page.get_by_placeholder("Salary").fill(salary)
        self.page.get_by_placeholder("Department").fill(input_departament)
        self.page.get_by_role("button", name="Submit").click()

    def review_edit_old_record(self):
        new_first_name = self.page.locator(self.old_first_name).inner_text()
        assert new_first_name == self.first_name

        new_departament = self.page.locator(self.old_departament).inner_text()
        assert new_departament == self.departament


    def review_add_invalid_record(self):
        assert self.page.locator("text=Registration Form")

    #delete
    def delete_record(self):
        self.page.locator("#delete-record-3").get_by_role("img").click()
        assert self.page.locator("#delete-record-3").is_hidden(), 'record not delete'

    #search
    def count_fill_cell(self):
        cells = self.page.locator(".rt-td").all()
        fill_cell_count = 0
        for cell in cells:
            if cell.inner_text().strip():
                fill_cell_count += 1
        return fill_cell_count

    def input_to_search(self,  input_value):
        self.value = input_value
        self.before_search = self.count_fill_cell()
        self.page.get_by_placeholder("Type to search").fill(input_value)


    def review_result_to_search(self):
        after_search = self.count_fill_cell()
        assert after_search < self.before_search
        if self.value == " ":
            assert self.page.get_by_text('No rows found')
        else:
            x = self.page.locator('div.rt-table > div.rt-tbody > div:nth-child(1) > div').inner_text()
            assert self.value in x

    #настройка отображения кол-ва строк

    def select_num_rows(self, input_num):
        self.num = int(input_num)
        self.page.get_by_label("rows per page").select_option(input_num)

        count_row_all = len(self.page.get_by_role('rowgroup').all())

        assert count_row_all == self.num, f'{count_row_all} ne ravno {input_num}'

    def add_many_record(self, first_name, last_name, email, age, salary, departament):
        next_button = self.page.locator("div.-next > button")
        next_button_enabled = next_button.is_enabled()

        while not next_button_enabled:
            self.page.get_by_role("button", name="Add").click()
            self.page.get_by_placeholder("First Name").fill(first_name)
            self.page.get_by_placeholder("Last Name").fill(last_name)
            self.page.get_by_placeholder("name@example.com").fill(email)
            self.page.get_by_placeholder("Age").fill(age)
            self.page.get_by_placeholder("Salary").fill(salary)
            self.page.get_by_placeholder("Department").fill(departament)
            self.page.get_by_role("button", name="Submit").click()

            next_button = self.page.locator("div.-next > button")
            next_button_enabled = next_button.is_enabled()

    def review_next_button(self):
        start_page = self.page.locator('span.-pageInfo > div > input[type=number]').input_value()
        self.page.locator("div.-next > button").click()
        next_page = self.page.locator('span.-pageInfo > div > input[type=number]').input_value()
        assert int(next_page) == int(start_page) + 1


