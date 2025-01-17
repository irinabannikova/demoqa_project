from pages.element_page_links import ElementsPageLinks


def test_link_open_new_tab(page):
    page_links = ElementsPageLinks(page)
    page_links.go_to_task_links()
    page_links.review_click_home_link()

def test_link_send_an_api_created(page):
    page_links = ElementsPageLinks(page)
    page_links.go_to_task_links()
    page_links.check_get_request_after_click('#created', 'https://demoqa.com/created')

def test_link_send_an_api_no_content(page):
    page_links = ElementsPageLinks(page)
    page_links.go_to_task_links()
    page_links.check_get_request_after_click('#no-content', 'https://demoqa.com/no-content')

