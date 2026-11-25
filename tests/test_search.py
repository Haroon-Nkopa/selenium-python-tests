#this is the test function that will tes search of the browser

#lets get the page object from pages 
from pages.search import HomePage
from pages.results import resultsPage

from selenium.webdriver.common.by import By

def test_search(browser):

    #lets create an instace of this page object
    HomePage_instance = HomePage(browser)
    resultsPage_instance = resultsPage(browser)
    Phrase = "python"

    #Given the home page is displayed, load method of the search Class.
    HomePage_instance.load()

    #When the user searches for "python"
    HomePage_instance.search(Phrase)

    #check weather the results page has successfully loaded before asseting. 
    wait = browser.execute_script("return document.readyState;")
    while wait != "complete":
        wait = browser.execute_script("return document.readyState;")


    #Then the search results title should contain "python", check the resultsPage object
    assert Phrase in resultsPage_instance.get_title()

    #and the search result query should be "python"
    assert Phrase == resultsPage_instance.get_query()

    #and the search results lins should pertain to "python"
    for title in resultsPage_instance.get_links():
        assert Phrase.lower() in title.lower()