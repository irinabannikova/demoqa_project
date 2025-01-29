from pages.alerts_page_browser_windows import AlertsPageBrowser


def test_new_tab(page):
    browser_page = AlertsPageBrowser(page)
    browser_page.go_to_browser_windows()
    browser_page.click_new_tab()

def test_new_window(page):
    browser_page = AlertsPageBrowser(page)
    browser_page.go_to_browser_windows()
    browser_page.click_new_window()

def test_new_window_message(page):
    browser_page = AlertsPageBrowser(page)
    browser_page.go_to_browser_windows()
    browser_page.click_new_window_massage()


