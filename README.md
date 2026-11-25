# selenium-python-tests
Automated end-to-end web UI test suite built with Python, Selenium WebDriver, and Pytest using the Page Object Model (POM) design pattern.



# Selenium WebDriver UI Test Automation Suite

An automated end-to-end UI testing framework built with **Python**, **Selenium WebDriver**, and **Pytest**, structured using the **Page Object Model (POM)** design pattern for maintainability and reusability.

## Key Features
* **Page Object Model (POM):** Separates page locators and user interactions (e.g., `HomePage`, `ResultsPage`) from test logic.
* **Pytest Fixtures:** Manages browser lifecycle setup and teardown (`conftest.py`) cleanly across test runs.
* **Explicit Waits:** Uses Selenium `WebDriverWait` and `expected_conditions` to handle dynamic web elements and reduce test flakiness.
* **Isolated Dependency Management:** Configured for reproducible test environments using `pipenv` / `venv`.

## Tech Stack
* **Language:** Python 3.x
* **Automation Tool:** Selenium WebDriver
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM)

## Project Structure
```text
├── pages/                  # Page Object classes (locators & page actions)
│   ├── __init__.py
│   ├── home.py             # Home page interactions
│   └── results.py          # Search results page assertions & actions
├── tests/                  # Pytest test suites
│   ├── conftest.py         # WebDriver setup/teardown fixtures
│   └── test_search.py      # End-to-end UI test scenarios
├── .gitignore              # Excludes virtual environments and cache files
├── Pipfile                 # Project dependencies (or requirements.txt)
└── README.md
```

## Getting Started

### Prerequisites
* Python 3.10+ installed
* Google Chrome (or configured WebDriver browser)
* `pipenv` or `pip`

### Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd your-repo-name
   ```

2. **Install dependencies:**
   If using `pipenv`:
   ```bash
   pipenv install
   pipenv shell
   ```
   *(Or using standard `venv` and `requirements.txt`:)*
   ```bash
   python -m venv .venv
   # Activate on Windows PowerShell: .venv\Scripts\Activate.ps1
   # Activate on Linux/macOS: source .venv/bin/activate
   pip install -r requirements.txt
   ```

### Running the Tests
Execute the full test suite with verbose output:
```bash
pytest -v
```

## What This Project Demonstrates
* Translating manual test scenarios into maintainable automated UI checks.
* Applying software engineering principles (encapsulation, DRY, separation of concerns) to QA automation.
* Handling cross-platform WebDriver execution and dynamic DOM elements.
