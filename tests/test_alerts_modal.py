from pages.alerts_page_modal import ModalPage


def test_check_small_modal(page):
    modal_page = ModalPage(page)
    modal_page.go_to_modal()
    modal_page.click_small_modal()
    modal_page.check_small_modal_open()
    modal_page.close_small_modal_open()

    page.wait_for_timeout(5000)
