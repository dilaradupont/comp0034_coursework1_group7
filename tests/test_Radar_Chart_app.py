"""
This file is used to test the radar chart app page. It tests for titles, dropdown menus and finally simulates a possible
interaction that a user could have with the app.

The same file can be used to run multiple test on the app when is running singularly or run a single test (example:
Run Test: test_bc001_h1_headers) when using a multi page layout. When performing the latter is important to change the
conftest.py file as outlined in the README and in teh file itself.
"""
from selenium.webdriver.common.keys import Keys


def test_rd001_h1_headers(dash_duo, run_radar_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the radar chart page
    THEN there should be no H1 (html) headers in the page
    """
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H1")
    dash_duo.driver.implicitly_wait(3)
    assert not actual_list


def test_rd002_h2_headers(dash_duo, run_radar_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the radar chart page
    THEN there should be no H2 (html) headers in the page
    """
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H2")
    dash_duo.driver.implicitly_wait(3)
    assert not actual_list


def test_rd003_h3_headers(dash_duo, run_radar_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the radar chart page
    THEN there should be no H3 (html) headers in the page
    """
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H3")
    dash_duo.driver.implicitly_wait(3)
    assert not actual_list


def test_rd004_h4_headers(dash_duo, run_radar_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the radar chart page
    THEN there should be no H4 (html) headers in the page
    """
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H4")
    assert not actual_list


def test_rd005_h5_header(dash_duo, run_radar_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the radar chart page
    THEN there should be exactly 4 H5 headers and they should be: 'Select Country', 'Select Year',
            'Select Country', 'Select Year'
    """
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H5")
    expected_list = ['Select Country', 'Select Year', 'Select Country', 'Select Year']
    dash_duo.driver.implicitly_wait(3)
    if len(actual_list) == len(expected_list):
        for h_i in range(0, len(actual_list)):
            assert actual_list[h_i].text.casefold() == expected_list[h_i].casefold()
    else:
        raise AssertionError


def test_rd006_select_country(dash_duo, run_radar_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the radar chart page and they select 'Italy' in the country selector
    THEN 'Italy' should appear in the column containing the graph
    """
    dash_duo.wait_for_element("H5", timeout=4)
    country_dropdown = dash_duo.find_element('#country input')
    country_dropdown.send_keys('Italy')
    country_dropdown.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(10)
    assert 'Italy' in dash_duo.find_element('#radar_chart > div.js-plotly-plot > div > div').text


def test_rd007_select_year(dash_duo, run_radar_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the radar chart page and they select '2016' in the year selector
    THEN '2016' should appear in the column containing the graph
    """
    dash_duo.wait_for_element("H5", timeout=4)
    country_dropdown = dash_duo.find_element('#year input')
    country_dropdown.send_keys('2016')
    country_dropdown.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(10)
    assert '2016' in dash_duo.find_element('#radar_chart > div.js-plotly-plot > div > div').text