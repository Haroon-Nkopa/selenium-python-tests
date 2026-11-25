#this page is responsible for representing the search results page and its elements

from selenium.webdriver.common.by import By 

class resultsPage:
    #constructor function for creating a resultssPage 

    #create locators for search field in the results page and links to the search results
    search_field_locator = (By.NAME, "q")
    links_locator = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")

    def __init__(self, browser):
        self.browser = browser

    def get_title(self):
        #check the title of the search results page
        return self.browser.title

    def get_query(self): 
        #check the search query in the search results page
        search_field = self.browser.find_element(*self.search_field_locator)
        value = search_field.get_attribute("value")
        return value

    def get_links(self):
        #check the search results links
        links = self.browser.find_elements(*self.links_locator)
        links_text = [link.text for link in links]
        return links_text
    