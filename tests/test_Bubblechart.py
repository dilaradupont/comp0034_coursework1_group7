"""
This file is used to test the Bubble chart app page. It tests for titles, dropdown menus and finally simulates possible
interactions that a user could have with the app.
"""
import time
from selenium.webdriver.common.keys import Keys
import numpy as np


def test_bc002_h2_headers(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page
    THEN there should be exactly 2 H2 headers in the page and they should be:
            "Relationship between factors involved in starting a business",
            "Data for the chosen geographic area"
    """
    time.sleep(5)
    actual_list = dash_duo.find_elements("H2")
    expected_list = ["Relationship between factors involved in starting a business",
                     "Data for the chosen geographic area"]
    dash_duo.driver.implicitly_wait(3)
    if len(actual_list) == len(expected_list):
        for h_i in range(0, len(actual_list)):
            assert actual_list[h_i].text.casefold() == expected_list[h_i].casefold()
    else:
        raise AssertionError


def test_bc001_h1_headers(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page
    THEN there should be no H1 (html) headers in the page
    """
    time.sleep(5)
    actual_list = dash_duo.find_elements("H1")
    dash_duo.driver.implicitly_wait(3)
    assert not actual_list


def test_bc003_h3_headers(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page
    THEN there should be no H3 (html) headers in the page
    """
    dash_duo.wait_for_element("H5", timeout=10)
    actual_list = dash_duo.find_elements("H3")
    dash_duo.driver.implicitly_wait(3)
    assert not actual_list


def test_bc004_h4_headers(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page
    THEN there only be one H4 header and it should be "Calculated based on absolute score"
    """
    time.sleep(5)
    actual_list = dash_duo.find_elements("H4")
    expected_list = ["Calculated based on absolute score"]
    dash_duo.driver.implicitly_wait(3)
    if len(actual_list) == len(expected_list):
        for h_i in range(0, len(actual_list)):
            assert actual_list[h_i].text.casefold() == expected_list[h_i].casefold()
    else:
        raise AssertionError


def test_bc005_h5_headers(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page
    THEN there should be exactly 3 H5 headers and they should be 'Select Gender', 'Select Region', 'Select Year'
    """
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H5")
    expected_list = ['Select Gender', 'Select Region', 'Select Year']
    dash_duo.driver.implicitly_wait(3)
    if len(actual_list) == len(expected_list):
        for h_i in range(0, len(actual_list)):
            assert actual_list[h_i].text.casefold() == expected_list[h_i].casefold()
    else:
        raise AssertionError


def test_bc006_gender_selector(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page
    THEN the gender checklist should contain both 'Women' and 'Men'
    """
    time.sleep(5)
    dash_duo.driver.implicitly_wait(3)
    expected_options = ['Women', 'Men']
    for option in expected_options:
        assert option in dash_duo.find_element("#gender").text


def test_bc007_region_selector(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page
    THEN the region checklist should contain all the following:
        'East Asia & Pacific', 'Europe & Central Asia', 'Latin America & Caribbean',
        'Middle East & North Africa', 'South Asia', 'Sub-Saharan Africa'
    """
    dash_duo.wait_for_element("H5", timeout=4)
    dash_duo.driver.implicitly_wait(3)
    expected_options = ['East Asia & Pacific', 'Europe & Central Asia', 'Latin America & Caribbean',
                        'Middle East & North Africa', 'South Asia', 'Sub-Saharan Africa']
    for option in expected_options:
        assert option in dash_duo.find_element("#region").text


def test_bc008_year_selector(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page
    THEN the year dropdown menu should contain all years between 2006 and 2020
    """
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


def test_bc009_single_graph(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page and they select 'Women' in the gender checklist
    THEN only 'Women' should appear under the graph container
        AND there should be no 'Men' under the graph container
        AND there should be a 'Women' header in the table
        AND there should not be a 'Men' header in the table
    """
    dash_duo.wait_for_element("H5", timeout=4)
    dash_duo.driver.implicitly_wait(3)
    women_checkbox = dash_duo.find_element('#_dbcprivate_checklist_gender_input_1')
    women_checkbox.click()
    time.sleep(5)
    assert 'Women' in dash_duo.find_element('#bubble_chart_col').text, 'The Women chart has not been produced'
    assert ~('Men' in dash_duo.find_element('#bubble_chart_col').text), 'The Men chart has been produced'
    assert 'Women' in dash_duo.find_element('#values_table').text
    assert ~('Men' in dash_duo.find_element('#values_table').text)


def test_bc010_double_graph(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page and they select 'Women' in the gender checklist
    THEN only 'Women' should appear under the graph container
        AND there should be 'Men' under the graph container
        AND there should be a 'Women' header in the table
        AND there should be a 'Men' header in the table
    """
    dash_duo.wait_for_element("H5", timeout=4)
    dash_duo.driver.implicitly_wait(3)
    women_checkbox = dash_duo.find_element('#_dbcprivate_checklist_gender_input_1')
    women_checkbox.click()
    time.sleep(2)
    men_checkbox = dash_duo.find_element('#_dbcprivate_checklist_gender_input_2')
    men_checkbox.click()
    time.sleep(5)
    assert 'Women' in dash_duo.find_element('#bubble_chart_col').text, 'The Women chart has not been produced'
    assert 'Men' in dash_duo.find_element('#bubble_chart_col').text, 'The Men chart has not been produced'
    assert 'Women' in dash_duo.find_element('#values_table').text
    assert 'Men' in dash_duo.find_element('#values_table').text


def test_bc011_table_for_region(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page and they select 'Europe & Central Asia' in the region checklist
    THEN 'Spain' should be found among the countries in the table
    """
    dash_duo.wait_for_element("H5", timeout=4)
    dash_duo.driver.implicitly_wait(3)
    RegionClick = dash_duo.find_element('#_dbcprivate_checklist_region_input_Europe\ \&\ Central\ Asia')
    RegionClick.click()
    time.sleep(5)
    assert 'Spain' in dash_duo.find_element('#values_table').text


def test_bc012_slider(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page and they go through every year in the slider
    THEN the year selected in the slider should match that found under the graph
    """
    dash_duo.wait_for_element("H5", timeout=15)
    time.sleep(5)
    time_click = dash_duo.find_element('#bubble_chart > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.slider-container > g > rect.slider-rail-touch-rect')
    year = 2006
    for i, pos in enumerate(np.arange(0.03, 0.99, 1/15)):
        if i >= 8:
            pos = 0.56 + (i-8) * 0.067
        dash_duo.click_at_coord_fractions(time_click, pos, 0.5)
        time.sleep(0.5)
        assert ('Year='+str(year)) in dash_duo.find_element('#bubble_chart_col').text
        year += 1


