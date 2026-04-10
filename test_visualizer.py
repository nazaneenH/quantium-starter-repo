from visualizer import dash_app

def test_header(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header")

def test_visuals(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#visual")

def test_radio(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#radio")