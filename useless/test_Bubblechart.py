import time

from selenium.webdriver.common.keys import Keys


def test_rere001_h1textequals(dash_duo, run_bubble_app):
    dash_duo.wait_for_element("H5", timeout=4)
    h1_text = dash_duo.find_element("H5").text
    dash_duo.driver.implicitly_wait(3)
    assert h1_text.casefold() == "Select Gender".casefold()
