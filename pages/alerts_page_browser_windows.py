from lib2to3.fixes.fix_input import context

from playwright.sync_api import Page, expect



class AlertsPageBrowser:
    def __init__(self, page: Page):
        self.page = page

    def go_to_browser_windows(self):
        self.page.goto('https://demoqa.com/browser-windows')

    def click_new_tab(self):
        with self.page.context.expect_page() as new_tab_event:
             self.page.locator('#tabButton').click()
             new_tab = new_tab_event.value
        assert new_tab.url == "https://demoqa.com/sample"

    def click_new_window(self):
        #ожидаем появления нового окна (popup) и сохраняем информацию в popup_info
        with self.page.expect_popup() as popup_info:
             self.page.click('#windowButton')
        #получаем новую страницу
        new_page = popup_info.value
        # Проверка, что новое окно открылось
        assert new_page is not None
        # Проверка текста на новом окне
        new_page_text = new_page.locator('h1').inner_text()
        assert new_page_text == 'This is a sample page'
        # Получаем список всех открытых страниц в браузере и сохраняем в переменную all_pages
        all_pages = self.page.context.pages
        # Проверяем, что наша новая страница есть среди всех открытых
        assert new_page in all_pages
        new_page.close()

    def click_new_window_massage(self):
        with self.page.expect_popup() as popup_massage:
             self.page.click('#messageWindowButton')
        massage_window = popup_massage.value

        assert massage_window is not None
        text = massage_window.locator('body').inner_text()
        assert text == "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization."










