from tkinter import dialog

from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright, Playwright



class AlertsPageAlerts:
    def __init__(self, page: Page):
        self.page = page
        self.message = ""

    def go_to_alerts(self):
        self.page.goto('https://demoqa.com/alerts')

    # def accept_dialog(self, dialog):
    #     self.message = dialog.message
    #     dialog.accept()


    def test_click_one_button_and_accept(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.click('#alertButton')
        assert self.page.locator('dialog').is_hidden()

    def test_click_two_button_and_accept(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.click('#timerAlertButton')
        assert self.page.locator('dialog').is_hidden()

    def click_tree_button_and_accept(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.click('#confirmButton')
        assert self.page.locator('dialog').is_hidden()
        assert self.page.locator('#confirmResult').inner_text() == 'You selected Ok'

    def click_tree_button_and_dismiss(self):
        self.page.on("dialog", lambda dialog: dialog.dismiss())
        self.page.click('#confirmButton')
        assert self.page.locator('dialog').is_hidden()
        assert self.page.locator('#confirmResult').inner_text() == 'You selected Cancel'

    def click_four_button_and_accept(self, name):
        self.page.on("dialog", lambda dialog: dialog.accept(name))
        self.page.click('#promtButton')
        assert self.page.locator('dialog').is_hidden()
        assert self.page.locator('#promptResult').inner_text() == f'You entered {name}'

    def click_four_button_and_dismiss(self):
        self.page.on("dialog", lambda dialog: dialog.dismiss())
        self.page.click('#promtButton')
        assert self.page.locator('dialog').is_hidden()


















