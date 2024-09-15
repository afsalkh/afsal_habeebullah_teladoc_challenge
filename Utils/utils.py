import configparser
import json
from Utils.chrome_driver_launcher import ChromeDriverLauncher
from Utils.edge_driver_launcher import EdgeDriverLauncher


class ConfigLaunch:
    testdatafilepath = "..\\TestData\\testdata.json"
    def __init__(self,browser_type, env):
        self.configfilepath="..\\Config\\config.ini"
        self.base_url=""
        self.driver=""
        self.set_config(browser_type, env)

    def set_config(self,browser_type, env):
        configvars=configparser.ConfigParser()
        configvars.read(self.configfilepath)
        driver_path=configvars['drivers'][browser_type]
        self.driver = self.get_driver(browser_type, driver_path)
        self.base_url=configvars[env]['base_url']

    def get_driver(self,browser_type, driver_path):
        if browser_type =="chrome":
            return ChromeDriverLauncher.make_driver(driver_path)
        elif browser_type == "edge":
            return EdgeDriverLauncher.make_driver(driver_path)

    @classmethod
    def get_test_data(cls,env):
        with open(cls.testdatafilepath,"r") as f:
            bulk=json.load(f)
            return bulk[env]





