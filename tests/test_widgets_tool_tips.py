from pages.widgets_page_tool_tips import WidgetsPageToolTips

def test_check_tooltip_button(page):
    tooltip_page = WidgetsPageToolTips(page)
    tooltip_page.go_to_task_tooltips()
    tooltip_page.check_hover_on_button()


def test_check_tooltip_link(page):
    tooltip_page = WidgetsPageToolTips(page)
    tooltip_page.go_to_task_tooltips()
    tooltip_page.check_hover_on_one_link()


    page.wait_for_timeout(6000)