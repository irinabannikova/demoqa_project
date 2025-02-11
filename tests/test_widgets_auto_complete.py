from pages.widgets_page_auto_complete import WidgetsPageAutoComplete

def test_check_multiple_valid_colors(page):
    auto_complete_page = WidgetsPageAutoComplete(page)
    auto_complete_page.go_to_task_auto_complete()
    auto_complete_page.input_valid_colors()
    auto_complete_page.review_valid_colors()
    auto_complete_page.remove_all_colors()

def test_check_multiple_invalid_colors(page):
    auto_complete_page = WidgetsPageAutoComplete(page)
    auto_complete_page.go_to_task_auto_complete()
    auto_complete_page.input_invalid_colors()
    auto_complete_page.review_invalid_colors()

def test_check_multiple_delete_color(page):
    auto_complete_page = WidgetsPageAutoComplete(page)
    auto_complete_page.go_to_task_auto_complete()
    auto_complete_page.input_color()
    auto_complete_page.remove_color()

def test_add_single_color(page):
    auto_complete_page = WidgetsPageAutoComplete(page)
    auto_complete_page.go_to_task_auto_complete()
    auto_complete_page.input_single_colors()


    page.wait_for_timeout(9000)


