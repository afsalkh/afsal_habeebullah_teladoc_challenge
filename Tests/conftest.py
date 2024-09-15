import pytest
import sys,os
sys.path.append(os.path.realpath(".."))

from Utils.utils import ConfigLaunch


env_to_run=""

def pytest_addoption(parser):
    parser.addoption('--browser', help='chrome|edge', default="chrome")
    parser.addoption('--env', help='test|prod', default="test")

def pytest_configure(config):
   global env_to_run
   env_to_run = config.getoption('--env')

@pytest.fixture()
def conf(request):
    browser=request.config.option.browser
    env = request.config.option.env
    objconfig=ConfigLaunch(browser,env)
    return objconfig



