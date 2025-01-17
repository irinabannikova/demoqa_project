from pages.element_page_radiobutton import ElementsPageRadiobutton


def test_check_radio_btn(page):
    radio_btn_page = ElementsPageRadiobutton(page)
    radio_btn_page.go_to_task_radio_btn()
    radio_btn_page.click_yes()
    radio_btn_page.review_click_yes()
    radio_btn_page.click_impressive()
    radio_btn_page.review_click_impressive()

