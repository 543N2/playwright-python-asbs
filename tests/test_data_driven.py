import pytest
from playwright.sync_api import Page, expect


# auxiliary function for json parametrization
def get_json_data() -> list:
    import json
    with open("./test_data/data.json", "r") as jsonfile:
       data = json.load(jsonfile)
    return [(item["username"], item["password"]) for item in data]


# auxiliary function for csv parametrization
def get_csv_data() -> list:
    import csv
    data = []
    with open("./test_data/data.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


# test using a json file and csv auxiliary function
@pytest.mark.parametrize("username, password", get_json_data())
def test_data_driven_example_parametrized_json(page: Page, username, password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()


# test using a csv file and json auxiliary function
@pytest.mark.parametrize("username, password", get_csv_data())
def test_data_driven_example_parametrized_csv(page: Page, username, password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()


# test using list parametrization
@pytest.mark.parametrize(
        "username, password",
        [
            ("Admin", "admin123"),
            ("user1", "password1"),
            ("user2", "password2"),
        ]
)
def test_data_driven_example_parametrized(page: Page, username, password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()


