"""
The following file was originally created to test the app by using teh multi page app and index. This means that the
server was started through the main page (index) and then the different pages were called by navigating using the url.
However, after multiple tests and trials, it was found that the testing of multi page is not supported as the multi page
app is loaded once, and then the server only runs the index without calling the other pages. For this reason, the app
were copied and modified in a 'individual_app_test' folder to allow individual app testing. The copied folders and file
finish in '_ind' to indicate that it is the modified version for an individual app rather than multi page.
"""
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


# The following fixtures were created to test the app when running singularly rather than in a multi page layout. This
# is because running multiple tests on multi page app through index is not supported


@pytest.fixture(scope='function')
def run_bubble_app(dash_duo):
    app = import_app("Individual_app_test.Bubble_Chart_ind.Bubble_Chart_app_ind")
    yield dash_duo.start_server(app)


@pytest.fixture(scope='function')
def run_choropleth_app(dash_duo):
    app = import_app("Individual_app_test.Choropleth_Map_ind.Choropleth_app_ind")
    yield dash_duo.start_server(app)


@pytest.fixture(scope='function')
def run_radar_app(dash_duo):
    app = import_app("Individual_app_test.Radar_Chart.Radar_Chart_app_ind")
    yield dash_duo.start_server(app)


"""
# Tried to use fixture with navigation but problems with dash testing for timeout exceptions. The issue is not with the
# app but with how dash testing for multi page apps work. However these fixtures can be used to run single tests. Please
# refer to README file for more info


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
