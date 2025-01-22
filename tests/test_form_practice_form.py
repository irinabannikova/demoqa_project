from pages.form_page_practice_form import FormPagePracticeForm
import pytest



def test_add_student_valid(page):
    practice_form = FormPagePracticeForm(page)
    practice_form.go_to_practice_form()
    practice_form.fill_main_info('irina',
                                  'bannikova',
                                 'test@mail.ru',
                                 'Male',
                                 '9252336164',
                                 '26 Sep 1992',
                                 'English',
                                 'Sport',
                                 'st patrike 2',
                                 'NCR',
                                 'Delhi')
    practice_form.add_picture()
    practice_form.click_to_submit()
    practice_form.review_form_valid_result()

def test_add_student_required_fields(page):
    practice_form = FormPagePracticeForm(page)
    practice_form.go_to_practice_form()
    practice_form.fill_main_info('',
                                 '',
                                 'test@mail.ru',
                                 'Male',
                                 '',
                                 '26 Sep 1992',
                                 'English',
                                 'Sport',
                                 'st patrike 2',
                                 'NCR',
                                 'Delhi')
    practice_form.add_picture()
    practice_form.click_to_submit()
    practice_form.review_form_required_fields()

def test_date_of_birth(page):
    practice_form = FormPagePracticeForm(page)
    practice_form.go_to_practice_form()
    practice_form.select_date_of_birth('11', '2022', '29')





