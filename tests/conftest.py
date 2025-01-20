import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

DEFAULT_BROWSER_NAME = "chrome"
DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption("--browser_name")
    parser.addoption("--browser_version")


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def remote_run(request):
    browser_name = request.config.getoption('browser_name') or DEFAULT_BROWSER_NAME
    browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_host = os.getenv("SELENOID_HOST")
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_password = os.getenv("SELENOID_PASSWORD")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@{selenoid_host}/wd/hub",
        options=options
    )
    browser.config.driver = driver

    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://qa-scooter.praktikum-services.ru'

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def local_run(request):
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://qa-scooter.praktikum-services.ru'

    yield browser

    browser.quit()
