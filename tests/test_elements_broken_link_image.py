from pages.element_page_webtables import ElementsPageWebTables
import pytest
from pages.element_page_broken_link_image import ElementsPageBrokenLinkImage


def test_check_img(page):
    broken_page = ElementsPageBrokenLinkImage(page)
    broken_page.go_to_task_broken_link_img()
    broken_page.check_page_broken_img()

# проверка перехода через получение адреса новой страницы
def test_check_valid_link(page):
    broken_page = ElementsPageBrokenLinkImage(page)
    broken_page.go_to_task_broken_link_img()
    broken_page.go_to_valid_link()
    broken_page.review_navigation()

# проверка перехода через получение адреса новой страницы
def test_check_broken_link(page):
    broken_page = ElementsPageBrokenLinkImage(page)
    broken_page.go_to_task_broken_link_img()
    broken_page.go_to_broken_link()
    broken_page.review_navigation()

# проверка перехода через получение статус кода
def test_broken_link(page):
    broken_page = ElementsPageBrokenLinkImage(page)
    broken_page.go_to_task_broken_link_img()
    broken_page.check_page_broken_link()
    broken_page.review_navigation()


# проверка перехода через получение статус кода
def test_valid_link(page):
    broken_page = ElementsPageBrokenLinkImage(page)
    broken_page.go_to_task_broken_link_img()
    broken_page.check_page_valid_link()





