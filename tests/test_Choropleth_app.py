"""
This file is used to test the choropleth app page. It tests for titles, dropdown menus and finally simulates a possible
interaction that a user could have with the app.
"""
import time
import numpy as np
from selenium.webdriver.common.keys import Keys


def test_ch001_h5_text_list_equals(dash_duo, run_choropleth_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the choropleth map page
    THEN there should be only certain H5 (html) headers in the page
    """
    ref_list_h5 = ['Select Region', 'Select Income Group', 'Select Bar Chart Year', 'Select Indicator']
    dash_duo.wait_for_element("h5", timeout=4)
    h5_list = dash_duo.find_elements('h5')
    h5_text_list = [h5_element.text for h5_element in h5_list]
    dash_duo.driver.implicitly_wait(3)
    assert set(ref_list_h5) == set(h5_text_list)


def test_ch002_h4_text_equals(dash_duo, run_choropleth_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the choropleth map page
    THEN there should be only certain H4 (html) headers in the page
    """
    dash_duo.wait_for_element("h4", timeout=4)
    h4_text = dash_duo.find_element('h4').text
    dash_duo.driver.implicitly_wait(3)
    assert h4_text.casefold() == 'Top 10 charts'.casefold()


def test_ch003_h1_headers(dash_duo, run_choropleth_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the choropleth map page
    THEN there should be no H1 (html) headers in the page
    """
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H1")
    dash_duo.driver.implicitly_wait(3)
    assert not actual_list


def test_ch004_h2_headers(dash_duo, run_choropleth_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the choropleth map page
    THEN there should be no H2 (html) headers in the page
    """
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H2")
    dash_duo.driver.implicitly_wait(3)
    assert not actual_list


def test_ch005_h3_headers(dash_duo, run_choropleth_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the choropleth map page
    THEN there should be no H3 (html) headers in the page
    """
    dash_duo.wait_for_element("H5", timeout=4)
    actual_list = dash_duo.find_elements("H3")
    dash_duo.driver.implicitly_wait(3)
    assert not actual_list


def test_ch006_dropdown_defaults(dash_duo, run_choropleth_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the choropleth chart page
    THEN there should be certain default values for the dropdown menus
    """
    ref_dropdown_def_list = ['Starting a business - Score', '2006']
    dropdowns_id = ['#year', '#indicator']
    dropdown_def_list = []
    dash_duo.wait_for_element_by_id('indicator', timeout=4)
    for id_name in dropdowns_id:
        dropdown_def_list.append(dash_duo.find_element(id_name).text)
    dash_duo.driver.implicitly_wait(3)
    assert set(ref_dropdown_def_list) == set(dropdown_def_list)


def test_ch007_year_selector(dash_duo, run_choropleth_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the choropleth chart page
    THEN the year dropdown menu should contain all years between 2006 and 2020
    """
    dash_duo.wait_for_element("H5", timeout=4)
    dash_duo.driver.implicitly_wait(5)
    elements = []

    for year in range(2006, 2020):
        select_input = dash_duo.find_element("#year input")
        select_input.send_keys(year)
        select_input.send_keys(Keys.RETURN)
        dash_duo.driver.implicitly_wait(5)
        elements.append(dash_duo.find_element("#year").text)
        assert str(year) in elements, f'{str(year)} is not in the dropdown menu'


def test_ch008_slider(dash_duo, run_choropleth_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the choropleth chart page and they go through every year in the slider
    THEN the year selected in the slider should match that found under the graph
    """
    dash_duo.wait_for_element("H5", timeout=4)
    time.sleep(3)
    time_click = dash_duo.find_element('#choropleth > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.slider-container > g > rect.slider-rail-touch-rect')
    year = 2006
    for i, pos in enumerate(np.arange(0.03, 0.99, 1/15)):
        # Solving bug when sliding with selenium after 2014
        if i >= 8:
            pos = 0.56 + (i-8) * 0.067
        dash_duo.click_at_coord_fractions(time_click, pos, 0.5)
        time.sleep(0.5)
        assert ('Year='+str(year)) in dash_duo.find_element('#choropleth').text
        year += 1


def test_ch009_overall_interactivity(dash_duo, run_choropleth_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the choropleth chart page and they filter the map using a specific region, indicator and income
         group ('Europe & Central Asia', 'Starting a business: Time - Average (days) - Score' and 'Low income'), and
         moves both the choropleth and bar chart to 2020
    THEN the values should match and be equal to the one taken from the dataframe (93.46734)
    """
    dash_duo.wait_for_element("H5", timeout=4)
    time.sleep(3)
    # Choose the indicator and check it is selected and displayed in the title of the choropleth map
    indicator_input = dash_duo.find_element('#indicator input')
    indicator_input.send_keys('Starting a business: Time - Average (days) - Score')
    indicator_input.send_keys(Keys.RETURN)
    time.sleep(2)
    indicator_dropdown_content = dash_duo.find_element('#indicator').text
    choropleth_title = dash_duo.find_element('#choropleth').text
    assert 'Starting a business: Time - Average (days) - Score' in indicator_dropdown_content, "'Starting a business: Time - Average (days) - Score' should appear in the Select Indicator dropdown menu"
    assert 'Starting a business: Time - Average (days) - Score' in choropleth_title, "'Starting a business: Time - Average (days) - Score' should appear in the title"
    # Choose the region and check it is selected in the dropdown menu
    region_input = dash_duo.find_element('#region input')
    region_input.send_keys('Europe & Central Asia')
    region_input.send_keys(Keys.RETURN)
    time.sleep(2)
    region_dropdown_content = dash_duo.find_element('#region').text
    assert 'Europe & Central Asia' in region_dropdown_content, "'Europe & Central Asia' should appear in the Select " \
                                                               "Region dropdown menu"
    # Choose the income group and check it is selected in the dropdown menu
    income_input = dash_duo.find_element('#income input')
    income_input.send_keys('Low income')
    income_input.send_keys(Keys.RETURN)
    time.sleep(2)
    income_dropdown_content = dash_duo.find_element('#income').text
    assert 'Low income' in income_dropdown_content, "'Low income' should appear in the Select Income dropdown menu"
    # Choose the year for barchart and check it is selected in the dropdown menu
    year_bar_input = dash_duo.find_element('#year input')
    year_bar_input.send_keys('2020')
    year_bar_input.send_keys(Keys.RETURN)
    time.sleep(2)
    year_dropdown_content = dash_duo.find_element('#year').text
    assert '2020' in year_dropdown_content, "'2020' should appear in the Select Year dropdown menu"
    # Choose the year from the choropleth animation and check map is updated
    year_click = dash_duo.find_element(
        '#choropleth > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.slider-container > g > rect.slider-rail-touch-rect')
    dash_duo.click_at_coord_fractions(year_click, 0.99, 0.5)
    time.sleep(2)
    assert 'Year=2020' in dash_duo.find_element('#choropleth').text
    # Check value for score is the right one and displayed when hovering
    hover_choropleth = dash_duo.find_element('#choropleth')
    dash_duo.click_at_coord_fractions(hover_choropleth, 0.5, 0.5)
    assert '93.46734' in dash_duo.find_element('#choropleth').text, "The value of the score when hovering over the " \
                                                                    "choropleth map should be of 93.46734"
    # Check value for score is the right one and displayed when hovering
    hover_barchart = dash_duo.find_element('#barchart')
    dash_duo.click_at_coord_fractions(hover_barchart, 0.5, 0.5)
    assert '93.46734' in dash_duo.find_element('#barchart').text, "The value of the score when hovering over the " \
                                                                  "bar chart should be of 93.46734"
