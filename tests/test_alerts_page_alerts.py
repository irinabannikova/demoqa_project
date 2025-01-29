from pages.alerts_page_alerts import AlertsPageAlerts

def test_click_button_see_alert(page):
    alert_page = AlertsPageAlerts(page)
    alert_page.go_to_alerts()
    alert_page.test_click_one_button_and_accept()

def test_click_button_see_alert_after_5_sec(page):
    alert_page = AlertsPageAlerts(page)
    alert_page.go_to_alerts()
    alert_page.test_click_two_button_and_accept()

def test_click_button_with_option_accept(page):
     alert_page = AlertsPageAlerts(page)
     alert_page.go_to_alerts()
     alert_page.click_tree_button_and_accept()

def test_click_button_with_option_dismiss(page):
     alert_page = AlertsPageAlerts(page)
     alert_page.go_to_alerts()
     alert_page.click_tree_button_and_dismiss()

def test_click_button_with_prompt_accept(page):
    alert_page = AlertsPageAlerts(page)
    alert_page.go_to_alerts()
    alert_page.click_four_button_and_accept('Irina')

def test_click_button_with_prompt_dismiss(page):
    alert_page = AlertsPageAlerts(page)
    alert_page.go_to_alerts()
    alert_page.click_four_button_and_dismiss()

    page.wait_for_timeout(10000)














