import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from IPython.display import display

# IS THIS POOR PRACTICE????
def test_all_h5_headers(dash_duo, run_bubble_app):
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H5")
    expected_list = ['Select Gender', 'Select Region', 'Select Year']
    dash_duo.driver.implicitly_wait(3)
    if len(actual_list) == len(expected_list):
        for h_i in range(0, len(actual_list)):
            assert actual_list[h_i].text.casefold() == expected_list[h_i].casefold()
    else:
        raise AssertionError


def test_all_h4_headers(dash_duo, run_bubble_app):
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H4")
    expected_list = ["Calculated based on absolute score"]
    dash_duo.driver.implicitly_wait(3)
    if len(actual_list) == len(expected_list):
        for h_i in range(0, len(actual_list)):
            assert actual_list[h_i].text.casefold() == expected_list[h_i].casefold()
    else:
        raise AssertionError


def test_all_h3_headers(dash_duo, run_bubble_app):
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H3")
    expected_list = []
    dash_duo.driver.implicitly_wait(3)
    if len(actual_list) == len(expected_list):
        for h_i in range(0, len(actual_list)):
            assert actual_list[h_i].text.casefold() == expected_list[h_i].casefold()
    else:
        raise AssertionError


def test_all_h2_headers(dash_duo, run_bubble_app):
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H2")
    expected_list = ["Relationship between factors involved in starting a business",
                     "Data for the chosen geographic area"]
    dash_duo.driver.implicitly_wait(3)
    if len(actual_list) == len(expected_list):
        for h_i in range(0, len(actual_list)):
            assert actual_list[h_i].text.casefold() == expected_list[h_i].casefold()
    else:
        raise AssertionError


def test_all_h1_headers(dash_duo, run_bubble_app):
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H1")
    expected_list = []
    dash_duo.driver.implicitly_wait(3)
    if len(actual_list) == len(expected_list):
        for h_i in range(0, len(actual_list)):
            assert actual_list[h_i].text.casefold() == expected_list[h_i].casefold()
    else:
        raise AssertionError


def test_gender_selector(dash_duo, run_bubble_app):
    dash_duo.wait_for_element("H5", timeout=4)
    dash_duo.driver.implicitly_wait(3)
    expected_options = ['Women', 'Men']
    for option in expected_options:
        assert option in dash_duo.find_element("#gender").text


def test_region_selector(dash_duo, run_bubble_app):
    dash_duo.wait_for_element("H5", timeout=4)
    dash_duo.driver.implicitly_wait(3)
    expected_options = ['East Asia & Pacific', 'Europe & Central Asia', 'Latin America & Caribbean',
                        'Middle East & North Africa', 'South Asia', 'Sub-Saharan Africa']
    for option in expected_options:
        assert option in dash_duo.find_element("#region").text


def test_year_selector(dash_duo, run_bubble_app):
    dash_duo.wait_for_element("H5", timeout=4)
    dash_duo.driver.implicitly_wait(10)
    elements = []

    for year in range(2006, 2020):
        select_input = dash_duo.find_element("#year input")
        select_input.send_keys(year)
        select_input.send_keys(Keys.RETURN)
        dash_duo.driver.implicitly_wait(10)
        elements.append(dash_duo.find_element("#year").text)
        assert str(year) in elements, f'{str(year)} is not in the dropdown menu'


def test_double_graph(dash_duo, run_bubble_app):
    dash_duo.wait_for_element("H5", timeout=4)
    dash_duo.driver.implicitly_wait(3)
    WomenClick = dash_duo.find_element('#_dbcprivate_checklist_gender_input_1')
    WomenClick.click()
    time.sleep(2)
    MenClick = dash_duo.find_element('#_dbcprivate_checklist_gender_input_2')
    MenClick.click()
    time.sleep(5)
    print(dash_duo.find_element('#bubble_chart_col').text)
    assert 'Women' in dash_duo.find_element('#bubble_chart_col').text, 'The Women chart has not been produced'
    assert 'Men' in dash_duo.find_element('#bubble_chart_col').text, 'The Men chart has not been produced'

