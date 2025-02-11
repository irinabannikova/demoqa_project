from pages.widgets_page_accordian import WidgetsPageAccordian

def test_section_one(page):
    accordian_page = WidgetsPageAccordian(page)
    accordian_page.go_to_task_accordian()
    accordian_page.check_open_section_one()
    accordian_page.click_to_accordian('What is Lorem Ipsum?')
    accordian_page.check_open_section_one()

def test_section_two(page):
    accordian_page = WidgetsPageAccordian(page)
    accordian_page.go_to_task_accordian()
    accordian_page.check_close_section_two()
    accordian_page.click_to_accordian('Where does it come from?')
    accordian_page.check_open_section_two()

def test_section_tree(page):
    accordian_page = WidgetsPageAccordian(page)
    accordian_page.go_to_task_accordian()
    accordian_page.check_close_section_tree()
    accordian_page.click_to_accordian('Why do we use it?')
    accordian_page.check_open_section_tree()



    page.wait_for_timeout(6000)
