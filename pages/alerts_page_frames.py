from playwright.sync_api import Page, expect
import re



class AlertsPageFrames:
    def __init__(self, page: Page):
        self.page = page

    def go_to_frame(self):
        self.page.goto('https://demoqa.com/frames')


    def check_big_frame(self):
        frame = self.page.frame_locator('#frame1')
        get_frame_text = frame.locator('#sampleHeading').inner_text()
        assert get_frame_text == 'This is a sample page'

        frame_bounding_box = self.page.locator("#frame1").bounding_box()
        iframe_width = round(frame_bounding_box['width'])
        iframe_height = round(frame_bounding_box['height'])
        assert round(iframe_width) == 500
        assert round(iframe_height) == 350

    def check_small_frame(self):
        frame = self.page.frame_locator('#frame2')
        get_frame_text = frame.locator('#sampleHeading').inner_text()
        assert get_frame_text == 'This is a sample page'

        frame_bounding_box = self.page.locator("#frame2").bounding_box()
        iframe_width = round(frame_bounding_box['width'])
        iframe_height = round(frame_bounding_box['height'])
        assert round(iframe_width) == 100
        assert round(iframe_height) == 100


















