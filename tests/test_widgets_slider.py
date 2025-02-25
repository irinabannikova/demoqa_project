from pages.widgets_page_slider_progress_bar import WidgetsPageSliderProgress
import pytest

@pytest.mark.parametrize('amount',['0','100','67'])
def test_check_slider(page, amount):
    slider_page = WidgetsPageSliderProgress(page)
    slider_page.go_to_task_slider()
    slider_page.move_slider(amount)
@pytest.mark.parametrize('percent',[3, 15, 50, 90])
def test_check_stop_at_percentage(page,percent):
    progress_page = WidgetsPageSliderProgress(page)
    progress_page.go_to_task_progress()
    progress_page.click_progress_start()
    progress_page.click_progress_stop_after_num(percent)

def test_check_stop_at_max_percentage(page):
    progress_page = WidgetsPageSliderProgress(page)
    progress_page.go_to_task_progress()
    progress_page.click_progress_start()
    progress_page.check_max_value_progress()

def test_check_progress_increases_value(page):
    progress_page = WidgetsPageSliderProgress(page)
    progress_page.go_to_task_progress()
    progress_page.click_progress_start()
    progress_page.check_progress_increases_after_start_click()







    # page.wait_for_timeout(10000)