from pages.widgets_page_menu import WidgetsPageMenu


def test_check_down_menu(page):
    page_down_menu = WidgetsPageMenu(page)
    page_down_menu.go_to_task_menu()
    page_down_menu.open_main_item_2()
    page_down_menu.check_count_item()
    page_down_menu.check_name_item()
    page_down_menu.hover_item()












