"""
This file is used to test the main page, checking the browser (title, url) and navigation characteristics. The main page
content is also tested to check that is the pre-set content.
"""
import time


def test_in001_title(dash_duo, start_main_app):
    """
    GIVEN that the app is loaded correctly
    WHEN the page is opened on the browser
    THEN check that the page title is correct and set to 'Business'
    """
    dash_duo.wait_for_element("h3", timeout=4)
    app_title = dash_duo.driver.title
    time.sleep(2)
    assert 'Business' == app_title, "The app title should be 'Business'"


def test_in002_app_url(dash_duo, start_main_app):
    """
    GIVEN that the app is loaded correctly
    WHEN the page is opened on the browser
    THEN check that the page url is correct and ends with 8050
    """
    dash_duo.wait_for_element("h3", timeout=4)
    app_url = dash_duo.driver.current_url
    time.sleep(2)
    assert '8050' in app_url, "The app url should finish in 8050"


def test_in003_nav(dash_duo, start_main_app):
    """
    GIVEN that the app is loaded correctly
    WHEN the page is opened on the browser and the user navigates to another page (choropleth map) and goes back
         and forward on the browser
    THEN check that the page url is correct and changes every time
    """
    dash_duo.wait_for_element("h3", timeout=4)
    # Navigate to the choropleth map page
    dash_duo.driver.get('http://127.0.0.1:8050/choropleth-map')
    time.sleep(2)
    current_app_url = dash_duo.driver.current_url
    assert 'http://127.0.0.1:8050/choropleth-map' == current_app_url, 'The app should be on the Choropleth page'
    # Pressing the browser back button and checking url is different
    dash_duo.driver.back()
    back_app_url = dash_duo.driver.current_url
    assert back_app_url != current_app_url, 'The app should go back to the main page'
    # Pressing the browser forward button and checking url is the same as the first open page
    dash_duo.driver.forward()
    forward_app_url = dash_duo.driver.current_url
    assert forward_app_url == current_app_url, 'The app should go forward to the Choropleth page'

