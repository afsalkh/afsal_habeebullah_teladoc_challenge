from selenium import webdriver
from selenium.webdriver.edge.service import Service


class EdgeDriverLauncher:
    @staticmethod
    def make_driver(driver_path):
        options=webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver=webdriver.Edge(service=Service(driver_path),options=options)
        return driver

