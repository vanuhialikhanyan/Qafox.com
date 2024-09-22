from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1018")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    driver.find_element(By.NAME, 'email').send_keys("vanuhi@mailinator.com")
    driver.find_element(By.NAME, 'password').send_keys("password321")
    driver.find_element(By.XPATH, '//input[@value="Login"]').click()

