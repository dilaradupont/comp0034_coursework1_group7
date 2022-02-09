import pytest
from dash.testing.application_runners import import_app
from selenium.webdriver.chrome.options import Options


def pytest_setup_options():
    options = Options()
    # Uncomment the following if testing on GitHub actions, the browser needs to run in headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    # options.add_argument('--start-maximized')
    return options


@pytest.fixture(scope='function')
def run_bubble_app(dash_duo):
    app = import_app("Multi_Page.index")
    yield dash_duo.start_server(app)