import time

from selenium.webdriver.common.keys import Keys


def test_bc010_double_graph(dash_duo, run_bubble_app):
    """
    GIVEN that the dash app is running
    WHEN the user is on the bubble chart page and they select 'Women' in the gender checklist
    THEN only 'Women' should appear under the graph container
        AND there should be 'Men' under the graph container
        AND there should be a 'Time - Women (days)' header in the table
        AND there should be a 'Time - Men (days)' header in the table
    """
    dash_duo.wait_for_element("H5", timeout=4)
    dash_duo.driver.implicitly_wait(3)
    women_checkbox = dash_duo.find_element('#_dbcprivate_checklist_gender_input_1')
    women_checkbox.click()
    time.sleep(2)
    men_click = dash_duo.find_element('#_dbcprivate_checklist_gender_input_2')
    men_click.click()
    time.sleep(5)
    assert 'Women' in dash_duo.find_element('#bubble_chart_col').text, 'The Women chart has not been produced'
    assert 'Men' in dash_duo.find_element('#bubble_chart_col').text, 'The Men chart has not been produced'
    assert 'Men' in dash_duo.find_element('#values_table').text
    assert 'Women' in dash_duo.find_element('#values_table').text

