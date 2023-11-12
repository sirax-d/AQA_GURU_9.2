import pytest
from selene.support.shared import browser, config

@pytest.fixture(scope="module")
def start_settings_google():
    browser.open('https://google.com')
    config.window_width = 800
    config.window_height = 1200
    browser.open('https://google.com')
    yield
    browser.clear_local_storage()
    browser.quit()