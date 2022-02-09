import time

from selenium.webdriver.common.keys import Keys
from dash.testing.application_runners import import_app
from selenium.webdriver.support.ui import WebDriverWait

def test_rere001_h1textequals(dash_duo, run_choropleth_app):
    dash_duo.wait_for_element("H5", timeout=4)
    h1_text = dash_duo.find_element("H5").text
    dash_duo.driver.implicitly_wait(3)
    assert h1_text.casefold() == 'Select Region'.casefold()
