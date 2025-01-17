from idlelib.searchengine import get_selection

from playwright.sync_api import Page, expect
import time


class ElementsPageTextbox:
    def __init__(self, page: Page):
        self.page = page
        self.full_name = ""
        self.email = ""
        self.current_address = ""
        self.permanent_address = ""

    # text box
    def go_to_task_textbox(self):
        self.page.goto('https://demoqa.com/text-box')

    def submit_form(self, full_name: str, email: str, current_address: str, permanent_address: str):
        self.full_name = full_name
        self.email = email
        self.current_address = current_address
        self.permanent_address = permanent_address

        self.page.get_by_placeholder('Full Name').fill(full_name)
        self.page.get_by_placeholder('name@example.com').fill(email)
        self.page.get_by_placeholder('Current Address').fill(current_address)
        self.page.locator('#permanentAddress').fill(permanent_address)
        self.page.locator('#submit').click()

    def check_form_result(self):
        if self.page.locator('#name').is_visible():
            assert self.page.locator('#name').inner_text() == f'Name:{self.full_name}'

        if self.page.locator('#email').is_visible():
            assert self.page.locator('#email').inner_text() == f'Email:{self.email}'

        if self.page.locator('.mb-1#currentAddress').is_visible():
            assert self.page.locator('.mb-1#currentAddress').inner_text() == f'Current Address :{self.current_address}'

        if self.page.locator('.mb-1#permanentAddress').is_visible():
            assert self.page.locator('.mb-1#permanentAddress').inner_text() == f'Permananet Address :{self.permanent_address}'

    def check_form_result_with_invalid_email(self):
        assert self.page.locator('.border').is_hidden()
        assert self.page.locator('#email').is_hidden()































































