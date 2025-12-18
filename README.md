# Playwright with Python

This is an implementation of the Playwright with Python tutorial by Automation Step By Step, available in: https://youtube.com/playlist?list=PLhW3qG5bs-L8WcAa9cfXaqGe0-Cq85y4X&si=VaNlxENZPbpg8wOo

Notes and instructions are included below, for future reference creating projects with this stack.

Each lesson matches a commit.


## Install Playwright

1. Create a new project folder:

```bash
mkdir playwright_python_project
cd playwright_python_project
```

2. Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate # for Mac/Linux
venv/Scripts/activate # for Windows
```

To deactivate the venv type: `deactivate`

3. Install Playwright and verify version:

Use `python -m` before to run commands locally in the virtual environment instead of globally.

```bash
pip install playwright
python pip install pytest-playwright

playwright --version
pytest --version
````

## Project Structure

1. Check the required libraries are installed
```bash
pip list
````

2. Create subfolders from root
```bash
mkdir tests pages utils reports
````

3. Create test configuration file in root, to define browser and page fixtures
```bash
touch conftest.py
```

4. Create `pytest.ini` for test execution options to simplify terminal usage
```bash
touch pytest.ini
```

5. Create `requirements.txt` with the dependencies list
```bash
pip freeze > requirements.txt
```

The dependencies can be installed afterwards via:
```python
pip install -r requirements.txt
```

6. Run the tests
```bash
pytest
```

## Recording



1. Go to project root folder in terminal.

2. Run: 
```bash
playwright codegen <url>
```
This will open a browser and a Playwright inspector window, side by side.

3. Record actions and copy/paste generated script. Press `Ctrl + C`in terminal to stop, or close the browser.

4. To save code directly to a file:
```bash
playwright codegen <url> --target python -o test_recorded_script.py
```

## Page Object Model

Without POM:
- Objects are not reusable
- Maintenance is manual and time consuming
- Code is not clear or readable

POM separates WebElements + Methods from Test Methods.

POM is a design pattern.

Each webpage is a class which contains:
- Locators: how to find the elements.
- Actions: What can be done with the elements.

How it helps:
- Reusability
- Readability
- Maintainability
- Clean Code

How to:

1. Create a file per page in pages/ folder.
```bash
touch pages/orangehrm_login_page.py
```

2. The file must contain a page class with the constructor.

3. Add locators for all the objects tha will be used.

4. Add the action methods to perform actions on objects.

5. Use the classes in the tests and update scripts to use page class methods.

The test file should be in tests/ folder.
```bash
touch tests/test_login_orangehrm.py
```

## Trace Viewer

Is a GUI tool that records traces of the executed tests, able to replay and inspect visually every performed action, as a visual debugging tool.

Usage:

```bash
pytest --tracing=on
```

Possible values: `on`, `off`, `retain-on-failure`.

This will record the trace an place it in `test-results/trace-zip` as long as the default fixtures for `page`and `browser` are being used (and not overriden).

To open the trace:

```bash
playwright show-trace <path-to-trace.zip>
```

or open the zip file in `trace.playwright.dev`.
