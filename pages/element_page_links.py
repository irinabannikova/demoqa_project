from playwright.sync_api import Page
import requests

from pages.basepage import BasePage


class ElementsPageLinks(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def go_to_task_links(self):
        self.goto('https://demoqa.com/links')

    def review_click_home_link(self):
        with self.page.context.expect_page() as tab:
            self.page.locator('#simpleLink').click()
        new_tab = tab.value
        assert new_tab.url == "https://demoqa.com/"

    def check_get_request_after_click(self, locator, endpoint):
        # Переменная для хранения флага об отправке GET-запроса на нужный URL
        get_request_sent = False

        # Функция для обработки запросов
        def on_request(route, request):
            if request.method == "GET" and request.url == endpoint:
                nonlocal get_request_sent
                get_request_sent = True
            route.continue_()

        # Назначаем функцию обработки запросов на все запросы

        self.page.route("**", on_request)


        # Находим и кликаем на ссылку, которая должна отправить GET-запрос
        link = self.page.locator(locator)
        link.click()

        response = requests.get(endpoint)
        x = response.status_code

        # Проверяем, был ли отправлен GET-запрос на нужный URL с кодом 200
        assert get_request_sent, f"GET-запрос на {endpoint} с кодом 200 не был отправлен"
        print(f'статус код {x}')

