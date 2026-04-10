from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
def pytest_setup_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # optional but recommended
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return options