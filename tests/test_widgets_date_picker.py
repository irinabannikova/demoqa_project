from pages.widgets_page_date_picker import WidgetsPageDatePicker


def test_select_date_in_picker(page):
    date_picker_page = WidgetsPageDatePicker(page)
    date_picker_page.go_to_task_date_picker()
    date_picker_page.check_add_date_with_picker()


def test_select_date_add_manual(page):
    date_picker_page = WidgetsPageDatePicker(page)
    date_picker_page.go_to_task_date_picker()
    date_picker_page.check_add_date_manual()

def test_add_date_and_time(page):
    date_picker_page = WidgetsPageDatePicker(page)
    date_picker_page.go_to_task_date_picker()
    date_picker_page.check_add_date_and_time_picker('September',
                                                    '1992',
                                                    '26',
                                                    '11:30')

    page.wait_for_timeout(10000)