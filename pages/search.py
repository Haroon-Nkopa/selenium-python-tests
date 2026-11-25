#here we creating a page object that represent the chrome home page
#Page object is just a class with necesaary properties and methods to interact with the page

#class that help creating locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage:

    home_page_url = "https://duckduckgo.com"

    #lets create a locator for the input field
    input_field_locator = (By.NAME, "q")


    #contructor function for creating the page object
    def __init__(self, browser):
        self.browser = browser

    #method that responsabdle for loading the home page
    def load(self):
        #here we write logic to load the home page.
        #we going to using the webdriver.get method to load the homepage. 
        self.browser.get(self.home_page_url)


    def search(self, phrase):
        #here we write logic to perform search on the home pag
        #lets get the element uding the find_element method
        inputs_field = self.browser.find_element(*self.input_field_locator)
        #send the key stroke to the elemennt vaya the send_keys method
        inputs_field.send_keys(phrase+Keys.RETURN)


