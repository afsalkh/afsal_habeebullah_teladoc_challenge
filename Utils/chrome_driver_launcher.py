from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class ChromeDriverLauncher:
    @staticmethod
    def make_driver(driver_path):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver=webdriver.Chrome(service=Service(driver_path),options=options)
        return driver


