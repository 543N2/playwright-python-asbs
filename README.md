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


## API Testing

The function that contains the test, must include `(playwright)` as argument.


1. Create a request context

An HTTP client is created using `APIRequestContext`:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request_context = p.request.new_context()
```
Or if `pytest-playwright` is used this version can be used:
```python
def test_api_get_request(playwright):
    request = playwright.request.new_context()
```
The HTTP client may take headers:
```python
request = playwright.request.new_context(
    extra_http_headers={
        "Accept": "application/json",
        "Authorization": "Bearer <access_token>",
        "X-Api-Key": "reqres-free-v1"
    }
)
```

2. Make an API call using HTTP methods of `APIRequestContext`:

`APIRequestContext` class provides methods to send HTTP requests including: 
- .get() 
- .post()
- .put()
- .delete()

It's used for:
- Sending direct requests to API endpoints.
- Avoid loading the whole browser.
- Test APIs quickly and easily.
- Can be used standalone or along with UI tests

A GET request:
```python
response = request_context.get(<URL>)
```

It may have included headers:
```python
response = request.get(<URL>, headers={<required_headers>})
``` 

A POST HTTP request method:
```python
response = request_context.post(
    <URL>,
    data={
        "<key1>": "<value1>",
        "<key2>": "<value2>",
    })
```


3. Use the response

To convert the data to json:
```python
json_data = response.json()
```

To evaluate conditions and assert responses:
```python
assert response.status == 200
``` 

JSON path finder can be used to assert specific response items:
```python
assert json_data[<key-1>][<key2>][<key-3>] == <value>
```

Return types:
- `response.status`: Status code
- `response.ok`: True if status is 2xx
- `response.json()`: Parse response body to Python dictionary 
- `response.text()`: Get raw response as text
- `response.body()`: Get response as bytes

```python
print(response.status)
print(response.json())
assert response.ok
```

4. Dispose context
```python
request_context.dispose()
```


## Data Driven Testing

1. Create a simple test that uses some data.

2. Parametrize the test, passing values to the variables using `@pytest.mark.parametrize()` fixture.

A CSV file can be used:

1. Create and fill a test data file in csv format
```bash
mkdir test_data
touch data.csv
```

2. Create a function to read data from cvs file

```python
def get_csv_data():
    data = []
    with open("test_data/data.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data
```

A JSON file can be used as well:

1. Create and fill the JSON file.
```bash
touch test_data/data.json
```

2. Create a function to read data from json file.
```python
def get_json_data() -> list:
    import json
    with open("./test_data/data.json", "r") as jsonfile:
       data = json.load(jsonfile)
    return [(item["username"], item["password"]) for item in data]
```

3. Run the tests. All data should be added up automatically.