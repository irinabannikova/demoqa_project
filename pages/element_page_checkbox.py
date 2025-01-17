from idlelib.searchengine import get_selection

from playwright.sync_api import Page, expect
import time

class ElementsPageCheckbox:
    def __init__(self, page: Page):
        self.page = page
        self.toggles_list = ''

    #локаторы
    home_toggle = '#tree-node > ol > li > span > button > svg'
    desktop_toggle = '#tree-node > ol > li > ol > li:nth-child(1) > span > button > svg'
    documents_toggle = '#tree-node > ol > li > ol > li:nth-child(2) > span > button > svg'
    download_toggle = '#tree-node > ol > li > ol > li:nth-child(3) > span > button > svg'
    workspace_toggle = 'li >ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > button > svg'
    office_toggle = 'li >ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(2) > span > button > svg'
   #чек боксы
    home_checkbox = '#tree-node > ol > li > span > label > span.rct-checkbox > svg'
    desktop_checkbox = '#tree-node > ol > li > ol > li:nth-child(1) > span > label > span.rct-checkbox'
    documents_checkbox = '#tree-node > ol > li > ol > li:nth-child(2) > span > label > span.rct-checkbox'
    download_checkbox = '#tree-node > ol > li > ol > li:nth-child(3) > span > label > span.rct-checkbox'
   #итоговые сообщение
    text_massage = "#result > span:nth-child(1)"
    instrument = "#result > span:nth-child({point_num})"
    def go_to_task_checkbox(self):
        self.page.goto('https://demoqa.com/checkbox')

    def click_expand_all(self):
        self.page.get_by_title('Expand all').click()

    def click_collapse_all(self):
        self.page.get_by_title('Collapse all').click()

    def check_expand_all(self):
        self.toggles_list = [
            self.home_toggle,
            self.desktop_toggle,
            self.documents_toggle,
            self.download_toggle,
            self.workspace_toggle,
            self.office_toggle
        ]
        for toggle in self.toggles_list:
            expand_value = self.page.get_attribute(toggle, 'class')
            assert 'rct-icon-expand-open' in expand_value, f'{toggle} not "expand-open" class'

    def check_collapse_all(self):
        collapse_value = self.page.get_attribute(self.home_toggle, 'class')
        assert 'rct-icon-expand-close' in collapse_value
        self.toggles_list = [
            self.desktop_toggle,
            self.documents_toggle,
            self.download_toggle,
            self.workspace_toggle,
            self.office_toggle
        ]
        for toggle in self.toggles_list:
            toggle_element = self.page.locator(toggle)
            assert not toggle_element.is_visible(), f'{toggle} is visible on the page'

    def click_home(self):
        self.page.locator(self.home_toggle).click()
        self.page.locator(self.home_checkbox).check()

    def review_home_checkbox(self):
        assert self.page.locator(self.text_massage).inner_text() == 'You have selected :'
        elements = {
             2: "home",
             3: "desktop",
             4: "notes",
             5: "commands",
             6: "documents",
             7: "workspace",
             8: "react",
             9: "angular",
             10: "veu",
             11: "office",
             12: "public",
             13: "private",
             14: "classified",
             15: "general",
             16: "downloads",
             17: "wordFile",
             18: "excelFile"
         }
        for point_num, text in elements.items():
            element = self.page.locator(self.instrument.format(point_num=point_num))
            actual_text = element.inner_text()
            assert actual_text == text, f"Expected text '{text}', but found '{actual_text}'"

    def click_desktop(self):
        self.page.locator(self.home_toggle).click()
        self.page.locator(self.desktop_toggle).click()
        self.page.locator(self.desktop_checkbox).check()

    def review_desktop_checkbox(self):
        home_checkbox = self.page.get_attribute(self.home_checkbox, 'class')
        assert 'rct-icon-half-check' in home_checkbox, f'not "half-check" class'
        assert self.page.locator(self.text_massage).inner_text() == 'You have selected :'
        elements = {
             2: "desktop",
             3: "notes",
             4: "commands"
          }
        for point_num, text in elements.items():
             element = self.page.locator(self.instrument.format(point_num=point_num))
             actual_text = element.inner_text()
             assert actual_text == text, f"Expected text '{text}', but found '{actual_text}'"

    def click_documents(self):
        self.page.locator(self.home_toggle).click()
        self.page.locator(self.documents_toggle).click()
        self.page.locator(self.documents_checkbox).check()

    def review_documents_checkbox(self):
        home_checkbox = self.page.get_attribute(self.home_checkbox, 'class')
        assert 'rct-icon-half-check' in home_checkbox, f'not "half-check" class'
        assert self.page.locator(self.text_massage).inner_text() == 'You have selected :'
        elements = {
            2: "documents",
            3: "workspace",
            4: "react",
            5: "angular",
            6: "veu",
            7: "office",
            8: "public",
            9: "private",
            10: "classified",
            11: "general"
          }
        for point_num, text in elements.items():
             element = self.page.locator(self.instrument.format(point_num=point_num))
             actual_text = element.inner_text()
             assert actual_text == text, f"Expected text '{text}', but found '{actual_text}'"

    def click_downloads(self):
        self.page.locator(self.home_toggle).click()
        self.page.locator(self.download_toggle).click()
        self.page.locator(self.download_checkbox).check()

    def review_downloads_checkbox(self):
        home_checkbox = self.page.get_attribute(self.home_checkbox, 'class')
        assert 'rct-icon-half-check' in home_checkbox, f'not "half-check" class'
        assert self.page.locator(self.text_massage).inner_text() == 'You have selected :'
        elements = {
            2: "downloads",
            3: "wordFile",
            4: "excelFile"
          }
        for point_num, text in elements.items():
             element = self.page.locator(self.instrument.format(point_num=point_num))
             actual_text = element.inner_text()
             assert actual_text == text, f"Expected text '{text}', but found '{actual_text}'"