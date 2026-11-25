# Selenium WebDriver UI Test Automation Suite

An automated UI testing project utilizing Python, Selenium WebDriver, and the Page Object Model (POM) pattern to test search functionality.

## Test Overview (`tests/test_search.py`)
* Navigates to the search home page (`HomePage.load()`).
* Executes a search for `"python"` (`HomePage.search("python")`).
* Waits for the page to finish loading (`document.readyState == "complete"`).
* Verifies that the results page title, query, and links correspond to `"python"`.

## Project Structure
```text
├── pages/                  # Page Object Model classes
│   ├── search.py           # HomePage class
│   └── results.py          # resultsPage class
├── tests/                  # Pytest test suite
│   └── test_search.py      # Search functionality test
├── config.json             # Configuration settings
├── Pipfile                 # Dependency definitions
└── README.md
```

## Quick Start
```bash
git clone https://github.com
cd selenium-python-tests
pipenv install && pipenv shell
pytest -v
```
