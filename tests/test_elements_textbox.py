from pages.element_page_textbox import ElementsPageTextbox
import pytest

@pytest.mark.parametrize("full_name, email, current_address, permanent_address", [
    ("irina", "test@mail.com", "test1@mail.com", "test"),
    ("", "142632HG@gmail.com", "982176353rt)(*&^%$# ----++++===\||||", "982176353rt)(*&^%$# ----++++===\||||"),
    ("irina", "", "test1@mail.com", "test"),
    ("irina", "test@mail.com", "", "test"),
    ("irina", "test@mail.com", "test1@mail.com", "")
])
def test_elements_text_box(page, full_name, email, current_address, permanent_address):
    textbox_page = ElementsPageTextbox(page)
    textbox_page.go_to_task_textbox()
    textbox_page.submit_form(full_name, email, current_address, permanent_address)
    textbox_page.check_form_result()

def test_elements_text_box_fill_email(page):
    textbox_page = ElementsPageTextbox(page)
    textbox_page.go_to_task_textbox()
    textbox_page.submit_form("irina", "asdgmail.com", "test1mailcom", "testmail")
    textbox_page.check_form_result_with_invalid_email()














