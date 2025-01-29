from pages.alerts_page_frames import AlertsPageFrames
from playwright.sync_api import Page, expect

def test_big_frames(page):
    alert_page = AlertsPageFrames(page)
    alert_page.go_to_frame()
    alert_page.check_big_frame()

def test_small_frames(page):
    alert_page = AlertsPageFrames(page)
    alert_page.go_to_frame()
    alert_page.check_small_frame()





