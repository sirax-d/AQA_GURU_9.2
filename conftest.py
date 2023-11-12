import pytest
from selene.support.shared import browser, config

@pytest.fixture(scope="function")
def start_settings_google():
    config.window_width = 1600
    config.window_height = 1280
    browser.open('https://google.com')
    yield
    browser.clear_local_storage()
    browser.quit()