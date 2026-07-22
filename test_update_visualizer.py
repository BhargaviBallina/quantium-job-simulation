from update_visualizer import dash_app
import dash
import pytest

def test_header_present(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element_by_id("header", timeout=10)
    assert "Welcome to Dash" in dash_duo.find_element("#header").text

def test_visualiser_present(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#visualiser",timeout=10)


def test_region_picker_present(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region-picker",timeout=10)
    radios = dash_duo.find_elements("input[type='radio']")
    radios[1].click()     
    assert radios[1].is_selected()