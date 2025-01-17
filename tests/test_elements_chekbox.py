from pages.element_page_checkbox import ElementsPageCheckbox


def test_elements_checkbox_expand_all(page):
    checkbox_page = ElementsPageCheckbox(page)
    checkbox_page.go_to_task_checkbox()
    checkbox_page.click_expand_all()
    checkbox_page.check_expand_all()


def test_elements_checkbox_collapse_all(page):
    checkbox_page = ElementsPageCheckbox(page)
    checkbox_page.go_to_task_checkbox()
    checkbox_page.click_expand_all()
    checkbox_page.click_collapse_all()
    checkbox_page.check_collapse_all()

def test_click_checkbox_home(page):
    checkbox_page = ElementsPageCheckbox(page)
    checkbox_page.go_to_task_checkbox()
    checkbox_page.click_home()
    checkbox_page.review_home_checkbox()

def test_click_checkbox_desktop(page):
    checkbox_page = ElementsPageCheckbox(page)
    checkbox_page.go_to_task_checkbox()
    checkbox_page.click_desktop()
    checkbox_page.review_desktop_checkbox()

def test_click_checkbox_documents(page):
    checkbox_page = ElementsPageCheckbox(page)
    checkbox_page.go_to_task_checkbox()
    checkbox_page.click_documents()
    checkbox_page.review_documents_checkbox()

def test_click_checkbox_downloads(page):
    checkbox_page = ElementsPageCheckbox(page)
    checkbox_page.go_to_task_checkbox()
    checkbox_page.click_downloads()
    checkbox_page.review_downloads_checkbox()


