#here we define a fixture that is responsable for creating and destroying
#the webdriver instance for each test.

import pytest
import selenium.webdriver as webdriver
import json


#creatcing a fixture responsable for reading the configuration file, validating it, passing to python dictionary and returning it. 
@pytest.fixture
def config(scope="session"):
    #scope="session", we want fixture to run once per test suite, and be reused on every tast case on that suite. 

    #now let's read the configuration file and passing it textual content to a python dictionary. 
    with open("config.json") as config_file:
        config = json.load(config_file)

    #validate if the content of the config file is what we expect. 
    #1. browser is one of the supported browsers.
    assert config["browser"] in ["chrome","firefox", "headless chrome"]
    
    #2. implicit_wait is an integer
    assert isinstance(config["implicit_wait"], int)

    #3. implicit_wait is a positive number
    assert config["implicit_wait"] > 0

    return config

#browser fixture depends on config fixture
@pytest.fixture
def browser(config):
    #get the browser type
    conf_browser = config["browser"]

    match conf_browser:
        case "chrome":
            webdriver_instance = webdriver.Chrome()
        case "firefox":
            webdriver_instance = webdriver.Firefox()
        case "headless chrome":
            opts = webdriver.ChromeOptions()
            opts.add_argument("headless")
            webdriver_instance = webdriver.Chrome(options=opts)
        case _:
            raise Exception(f"Browser type {conf_browser} is not supported")
        
    #wait for 10sec tiil the test gives up
    webdriver_instance.implicitly_wait(config["implicit_wait"]) # teh wait will be taken from the config file not hard coded.

    #rerurn thr instance to the set for killing it after the test is done
    yield webdriver_instance

    #destroy the webdriver instance after the test is done
    webdriver_instance.quit()