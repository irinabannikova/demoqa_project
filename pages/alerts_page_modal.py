from playwright.sync_api import Page, expect



class ModalPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_modal(self):
        self.page.goto('https://demoqa.com/modal-dialogs')

    def click_small_modal(self):
        small_button = self.page.locator('#showSmallModal')
        small_button.click()
    def check_small_modal_open(self):
        assert self.page.wait_for_selector('.modal-open')
        assert self.page.locator('#example-modal-sizes-title-sm').inner_text() == 'Small Modal'
        assert self.page.locator('.modal-body').inner_text() == 'This is a small modal. It has very less content'

    def close_small_modal_open(self):
        self.page.locator('#closeSmallModal').click()
        self.page.wait_for_timeout(1000)
        assert not self.page.locator('.modal-open').is_visible()











