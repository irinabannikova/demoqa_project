from idlelib.searchengine import get_selection

from playwright.sync_api import Page, expect
import time

from pages.basepage import BasePage


class ElementsPageBrokenLinkImage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.toggles_list = ''

    def go_to_task_broken_link_img(self):
        self.goto('https://demoqa.com/broken')

    def check_page_broken_img(self):
        image_elements = self.page.query_selector_all("img")
        for image in image_elements:
            width = self.page.evaluate('(element) => element.width', image)
            height = self.page.evaluate('(element) => element.height', image)
            if width == 16 and height == 16:
                raise AssertionError(f"Изображение {image.get_attribute('src')} имеет размеры 16x16")
            else:
                print(f"Изображение {image.get_attribute('src')} имеет размеры {width}x{height}")

    def go_to_valid_link(self):
        self.page.locator('div:nth-child(2) > a:nth-child(11)').click()

    def go_to_broken_link(self):
        self.page.locator('div:nth-child(2) > a:nth-child(15)').click()


    def review_navigation(self):
        new_page = self.page.url
        assert new_page == 'https://demoqa.com/', 'переход по ссылке не корректный'








    def check_page_broken_link(self):
        link = self.page.get_attribute(' div:nth-child(2) > a:nth-child(15)', 'href')
        response = self.page.goto(link)
        status_code = response.status
        if status_code == 500:
            raise AssertionError(f"статус код {status_code} по ссылке {link}")
        else:
            print(f"ссылка отрывается корректно")
    def check_page_valid_link(self):
        link = self.page.get_attribute('div:nth-child(2) > a:nth-child(11)', 'href')
        response = self.page.goto(link)
        status_code = response.status
        if status_code == 500:
            raise AssertionError(f"статус код {status_code} по ссылке {link}")
        else:
            print(f"ссылка отрывается корректно")




