from pages.element_page_dynamic_properties import ElementsPageDynamicProperties


def test_dynamic_property(page):
    dynamic_page = ElementsPageDynamicProperties(page)
    dynamic_page.go_to_task_dynamic_properties()
    dynamic_page.check_dynamic_element_before_5_second()
    dynamic_page.check_dynamic_element_after_5_second()

