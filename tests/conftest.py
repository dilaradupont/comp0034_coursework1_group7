import pytest
from dash.testing.application_runners import import_app
from selenium.webdriver.chrome.options import Options


def pytest_setup_options():
    options = Options()
    # Uncomment the following if testing on GitHub actions, the browser needs to run in headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')  # this is commented out to automatically open the test in a new chrome window
    # options.add_argument('--start-maximized')
    return options


@pytest.fixture(scope='function')
def start_main_app(dash_duo):
    app = import_app("Multi_Page.index")
    yield dash_duo.start_server(app)


@pytest.fixture(scope='function')
def run_bubble_app(dash_duo, start_main_app):
    app = import_app("Multi_Page.apps.Bubble_Chart.Bubble_Chart_app")
    yield dash_duo.start_server(app)


@pytest.fixture(scope='function')
def run_choropleth_app(dash_duo, start_main_app):
    app = import_app("Multi_Page.apps.Choropleth_Map.Choropleth_app")
    yield dash_duo.start_server(app)


@pytest.fixture(scope='function')
def run_radar_app(dash_duo, start_main_app):
    app = import_app("Multi_Page.apps.Radar_Chart.Radar_Chart_app")
    yield dash_duo.start_server(app)

"""
# Tried to use fixture with navigation but problems with dash testing for timeout exceptions. The issue is not with the
# app but with how dash testing for multi page apps work. However these can be used to run single tests.

@pytest.fixture(scope='function')
def run_bubble_app(dash_duo, start_main_app):
    yield dash_duo.driver.get('http://127.0.0.1:8050/bubble-chart')

 
@pytest.fixture(scope='function')
def run_choropleth_app(dash_duo, start_main_app):
    yield dash_duo.driver.get('http://127.0.0.1:8050/choropleth-map')


@pytest.fixture(scope='function')
def run_radar_app(dash_duo, start_main_app):
    yield dash_duo.driver.get('http://127.0.0.1:8050/radar-chart')
"""